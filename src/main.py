from pathlib import Path

from parser import Parser
from symbol_table import SymbolTable


input_file = Path("tests/test.asm")

symbol_table = SymbolTable()
parser = Parser(input_file)

rom_address = 0

while parser.has_more_commands():

    parser.advance()

    command_type = parser.command_type()

    if command_type == Parser.L_COMMAND:

        label = parser.symbol()

        if not symbol_table.contains(label):
            symbol_table.add_entry(label, rom_address)

    else:
        rom_address += 1


print("LOOP:", symbol_table.get_address("LOOP"))