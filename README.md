# laas-utils

**L**LM for **A**s **A** **S**ervice (LAAS) provides a collection of utility functions for simplifying common tasks in robotic automation and control.  This library aims to streamline development by offering pre-built functions for tasks such as trajectory generation, sensor data processing, and communication with robotic hardware.

## Features

* Trajectory generation (linear, circular, etc.)
* Sensor data filtering and processing
* Communication interfaces for common robotic hardware (e.g., ROS)
* ...

## Installation

```bash
pip install git+https://github.com/jeongsk/laas-utils.git
```

## Dependencies

* langchain>=0.3.3

## Usage

```python
from laas_utils.langchain_laas.chat_models import ChatLaaS

# Example
llm = ChatLaaS(
    api_key=os.environ["LAAS_API_KEY"],
    laas_project=os.environ["LAAS_PROJECT"],
    laas_hash=os.environ["LAAS_HASH"],
)
print(llm.invoke("hello"))
```

## Contributing

Contributions are welcome!  Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
