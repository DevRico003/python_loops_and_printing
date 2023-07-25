# Range-Functions

This Python module provides various range functions, including functionality to define start, end, and step values, print values from one to ten, print even values up to twenty, and define steps from one value to another.

## Installation

No special installation instructions required. Simply clone the repository and run `functions.py`.

## Functions

1. `from_to_by(start, end, step)`: This function accepts three parameters - start, end, and step. It will print a sequence of numbers starting from the "start" number to the "end" number in steps of "step". Throws a ValueError if step is zero, or if the end is less than the start for a positive step, or if the end is greater than the start for a negative step.

2. `one_to_ten()`: This function prints numbers from one to ten.

3. `evens_to_twenty()`: This function prints even numbers up to twenty.

4. `from_to(start, end)`: This function accepts two parameters - start and end. It will print a sequence of numbers from "start" to "end". The step is automatically determined based on whether start is less than or greater than end.

## Usage

```python
python3 range_functions.py
```

When run directly, this script will perform various tests of the functions. The output for each test will be printed to the console.

## Contribute

If you want to contribute, feel free to open an issue or submit a pull request.

## License

MIT License

## Contact

If you have questions or issues about this script, please open an issue on this repository.
