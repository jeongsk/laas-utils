import logging
from typing import Any, Dict, List, Optional, Self

import openai
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import BaseMessage
from langchain_core.outputs import ChatResult
from langchain_core.utils.utils import from_env, secret_from_env
from langchain_openai.chat_models.base import BaseChatOpenAI, _convert_message_to_dict
from pydantic import Field, SecretStr, model_validator

logger = logging.getLogger(__name__)


class ChatLaaS(BaseChatOpenAI):
    laas_api_key: Optional[SecretStr] = Field(
        alias="api_key", default_factory=secret_from_env("LAAS_API_KEY", default=None)
    )
    laas_project: Optional[str] = Field(
        alias="project", default_factory=from_env("LAAS_PROJECT", default=None)
    )
    laas_hash: Optional[str] = Field(default=None, alias="hash")
    # model_name: str = Field(default="gpt-4o-mini", alias="model")
    temperature: Optional[float] = Field(default=None)
    params: Optional[Dict[str, Any]] = Field(default=None)
    timeout: Optional[float] = Field(default=60.0)
    max_retries: Optional[int] = Field(default=3)

    @model_validator(mode="after")
    def validate_environment(self) -> Self:
        """Validate that api key and python package exists in environment."""
        if self.laas_api_key is None:
            raise ValueError("laas_api_key environment variable not found.")
        if self.laas_project is None:
            raise ValueError("laas_project environment variable not found.")
        if self.laas_hash is None:
            raise ValueError("laas_hash environment variable not found.")

        self.client = openai.OpenAI(
            api_key=self.laas_api_key.get_secret_value(),
            base_url="https://api-laas.wanted.co.kr/api/preset/v2",
            max_retries=self.max_retries,
            timeout=self.timeout,
            default_headers={
                "Content-Type": "application/json",
                "apiKey": self.laas_api_key.get_secret_value(),
                "project": self.laas_project,
            },
        ).chat.completions

        return self

    @property
    def _llm_type(self) -> str:
        """Return type of chat model."""
        return "laas-chat"

    @classmethod
    def is_lc_serializable(cls) -> bool:
        """Return whether this model can be serialized by Langchain."""
        return False

    @property
    def lc_secrets(self) -> Dict[str, str]:
        return {"laas_api_key": "LAAS_API_KEY"}

    @classmethod
    def get_lc_namespace(cls) -> List[str]:
        """Get the namespace of the langchain object."""
        return ["langchain", "chat_models", "laas"]

    def _get_request_payload(
        self,
        input_: LanguageModelInput,
        *,
        stop: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> dict:
        messages = self._convert_input(input_).to_messages()
        if stop is not None:
            kwargs["stop"] = stop
        return {
            "messages": [_convert_message_to_dict(m) for m in messages],
            **self._default_params,
            **kwargs,
        }

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        payload = self._get_request_payload(
            messages,
            # model=self.model_name,
            stop=stop,
            extra_body={
                "hash": self.laas_hash,
                "params": self.params,
            },
            **kwargs,
        )
        response = self.client.create(**payload)
        return self._create_chat_result(response)
