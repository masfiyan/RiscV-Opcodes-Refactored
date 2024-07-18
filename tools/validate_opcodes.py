import yaml

def validate_opcodes(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        assert 'opcodes' in data, "The YAML file must contain 'opcodes' as the root key"
        opcodes = data['opcodes']
        
        for opcode in opcodes:
            assert 'name' in opcode, "Opcode must have a name"
            assert 'opcode' in opcode, f"Opcode {opcode.get('name', 'unknown')} must have an opcode value"
            assert 'funct' in opcode, f"Opcode {opcode.get('name', 'unknown')} must have a funct value"
            assert 'operands' in opcode, f"Opcode {opcode.get('name', 'unknown')} must have operands"
            assert 'description' in opcode, f"Opcode {opcode.get('name', 'unknown')} must have a description"

if __name__ == "__main__":
    validate_opcodes('data/rv_i_opcodes.yaml')
    print("Validation completed successfully.")
