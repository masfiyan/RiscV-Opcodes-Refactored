import yaml
import re


def validate_opcode(yaml_file):
    with open(yaml_file, 'r') as file:
        opcodes = yaml.safe_load(file)

    for opcode in opcodes['rv_i']:
        encoding = ['-'] * 32
        for entry in opcodes['rv_i'][opcode]:
            match = re.match(r'(\d+)\.\.(\d+)=(\w+)', entry)
            if match:
                msb, lsb, value = int(match.group(1)), int(match.group(2)), match.group(3)
                if msb < lsb:
                    print(f"Invalid encoding in {opcode}: {entry}")
                    return False
                if value.isdigit():
                    value = int(value)
                    if value >= (1 << (msb - lsb + 1)):
                        print(f"Value out of range in {opcode}: {entry}")
                        return False
                    for ind in range(lsb, msb + 1):
                        if encoding[31 - ind] != '-':
                            print(f"Overlapping bits in {opcode}: {entry}")
                            return False
                        encoding[31 - ind] = str((value >> (ind - lsb)) & 1)
                else:
                    # Handle symbolic values
                    for ind in range(lsb, msb + 1):
                        if encoding[31 - ind] != '-':
                            print(f"Overlapping bits in {opcode}: {entry}")
                            return False
                        encoding[31 - ind] = 'X'
            else:
                print(f"Invalid format in {opcode}: {entry}")
                return False
    print("All opcodes are valid")
    return True


validate_opcode('tools/opcodes.yaml')
