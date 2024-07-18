import unittest
import yaml

class TestOpcodes(unittest.TestCase):
    def setUp(self):
        with open('data/rv_i_opcodes.yaml', 'r') as file:
            self.opcodes = yaml.safe_load(file)['opcodes']

    def test_opcode_name(self):
        for opcode in self.opcodes:
            self.assertIn('name', opcode, "Opcode must have a name")

    def test_opcode_value(self):
        for opcode in self.opcodes:
            self.assertIn('opcode', opcode, f"Opcode {opcode.get('name', 'unknown')} must have an opcode value")

    def test_funct_value(self):
        for opcode in self.opcodes:
            self.assertIn('funct', opcode, f"Opcode {opcode.get('name', 'unknown')} must have a funct value")

    def test_operands(self):
        for opcode in self.opcodes:
            self.assertIn('operands', opcode, f"Opcode {opcode.get('name', 'unknown')} must have operands")

    def test_description(self):
        for opcode in self.opcodes:
            self.assertIn('description', opcode, f"Opcode {opcode.get('name', 'unknown')} must have a description")

if __name__ == '__main__':
    unittest.main()
