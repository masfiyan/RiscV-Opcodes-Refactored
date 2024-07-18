## Tests

### `__init__.py`

This file marks the `tests` directory as a Python package. It can be empty.

### `test_opcodes.py`

**Purpose:**  
Contains unit tests for validating individual opcode definitions.

**Tests Included:**
- `test_opcode_name`: Ensures every opcode has a name.
- `test_opcode_value`: Ensures every opcode has a defined opcode value.
- `test_funct_value`: Ensures every opcode has a `funct` value.
- `test_operands`: Ensures every opcode lists its operands.
- `test_description`: Ensures every opcode has a description.

**Usage:**  
To run the tests, use the command:
```sh
python3 tests/test_opcodes.py
```

### `test_validation.py`

**Purpose:**  
Tests the validation script used to check the correctness of opcode definitions in the YAML file.

**Tests Included:**
test_validation_script: Executes the validation script and checks for successful completion

**Usage:**  
To run the tests, use the command:
```sh
python3 tests/test_validation.py
```

### `test_integration.py`

**Purpose:**  
Contains integration tests for validating the integration and consistency of opcode values.

**Tests Included:**
test_integration: Checks that all opcode values in the YAML file match expected values.

**Usage:**  
To run the tests, use the command:
```sh
python3 tests/test_integration.py
```

### Running All Tests

To run all tests in the tests directory, navigate to the root of the repository and use the following command:

```sh
python3 -m unittest discover tests/
```

