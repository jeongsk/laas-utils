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
import laas_utils

# Example: Generate a linear trajectory
trajectory = laas_utils.generate_linear_trajectory(start_point=[0, 0, 0], end_point=[1, 1, 1], duration=5)
print(trajectory)
```

## Contributing

Contributions are welcome!  Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
