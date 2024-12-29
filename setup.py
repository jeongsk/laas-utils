from setuptools import setup, find_packages

setup(
    name='laas-utils',
    description="LaaS Helper Library",
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'langchain',
    ],
    python_requires=">=3.11.0",
    author='jeongsk',
    zip_safe=False,
    author_email='jeongseok@wantedlab.com',
    url="https://github.com/jeongsk/laas-utils",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
