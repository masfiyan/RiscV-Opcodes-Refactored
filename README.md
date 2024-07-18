# RiscV-Opcodes-Refactored

Refactored RISC-V Opcodes: Maintainable opcode definitions with enhanced documentation and automated tools for integration and checks.

## Overview

This repository contains refactored definitions of RISC-V opcodes. The goal is to provide a clean, maintainable, and well-documented set of opcode definitions. Additionally, tools for automating integration and consistency checks are included.

## Basic Opcode Definitions

### RV32I Base Integer Instruction Set

- **LUI**: Load Upper Immediate
  - Format: `lui rd, imm20`
  - Binary: `imm[31:12] rd[11:7] 0x0D`
  - Description: Loads a 20-bit immediate value into the upper 20 bits of the destination register, filling the lower 12 bits with zeros.

- **AUIPC**: Add Upper Immediate to PC
  - Format: `auipc rd, imm20`
  - Binary: `imm[31:12] rd[11:7] 0x05`
  - Description: Adds a 20-bit immediate value to the program counter and stores the result in the destination register.

- **JAL**: Jump and Link
  - Format: `jal rd, offset`
  - Binary: `offset[20|10:1|11|19:12] rd[11:7] 0x1B`
  - Description: Jumps to the address pc + offset and stores the return address in rd.

- **JALR**: Jump and Link Register
  - Format: `jalr rd, rs1, offset`
  - Binary: `offset[11:0] rs1[19:15] 0x0 rd[11:7] 0x19`
  - Description: Computes the target address by adding an immediate to a register, saves the return address, and jumps to the target.

- **BEQ**: Branch if Equal
  - Format: `beq rs1, rs2, offset`
  - Binary: `offset[12|10:5] rs2[24:20] rs1[19:15] 0x0 0x18`
  - Description: Branches to the target address if rs1 is equal to rs2.

- **BNE**: Branch if Not Equal
  - Format: `bne rs1, rs2, offset`
  - Binary: `offset[12|10:5] rs2[24:20] rs1[19:15] 0x1 0x18`
  - Description: Branches to the target address if rs1 is not equal to rs2.

- **LB**: Load Byte
  - Format: `lb rd, offset(rs1)`
  - Binary: `offset[11:0] rs1[19:15] 0x0 rd[11:7] 0x00`
  - Description: Loads a byte from memory into the destination register.

- **LW**: Load Word
  - Format: `lw rd, offset(rs1)`
  - Binary: `offset[11:0] rs1[19:15] 0x2 rd[11:7] 0x00`
  - Description: Loads a word from memory into the destination register.

- **SB**: Store Byte
  - Format: `sb rs2, offset(rs1)`
  - Binary: `offset[11:5] rs2[24:20] rs1[19:15] 0x0 0x08`
  - Description: Stores a byte from the source register into memory.

- **SW**: Store Word
  - Format: `sw rs2, offset(rs1)`
  - Binary: `offset[11:5] rs2[24:20] rs1[19:15] 0x2 0x08`
  - Description: Stores a word from the source register into memory.

- **ADDI**: Add Immediate
  - Format: `addi rd, rs1, imm`
  - Binary: `imm[11:0] rs1[19:15] 0x0 rd[11:7] 0x04`
  - Description: Adds an immediate value to a register and stores the result in the destination register.

- **ANDI**: AND Immediate
  - Format: `andi rd, rs1, imm`
  - Binary: `imm[11:0] rs1[19:15] 0x7 rd[11:7] 0x04`
  - Description: Performs a bitwise AND between a register and an immediate value, storing the result in the destination register.

## Tools

- **Validation Script**: Ensures opcode definitions meet the required format and criteria.
- **Automation Tools**: Scripts for automating opcode integration and consistency checks.

## Documentation

Detailed documentation. Usage guidelines, contribution guidelines, and maintenance instructions are also included.

## Contribution

Contributions are welcome! Please refer to the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.
