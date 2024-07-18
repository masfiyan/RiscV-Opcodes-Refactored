
import unittest
import yaml

class TestIntegration(unittest.TestCase):
    def setUp(self):
        with open('data/rv_i_opcodes.yaml', 'r') as file:
            self.opcodes = yaml.safe_load(file)['opcodes']

    def test_integration(self):
        valid_opcodes = {opcode['opcode'] for opcode in self.opcodes}
        
        for opcode in self.opcodes:
            self.assertIn(opcode['opcode'], valid_opcodes, f"Opcode {opcode.get('name', 'unknown')} has an unexpected value")

if __name__ == '__main__':
    unittest.main()
