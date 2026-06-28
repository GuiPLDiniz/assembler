from pathlib import Path

from parser import Parser
from code import Code
from symbol_table import SymbolTable


input_file = Path("tests/test.asm")
output_file = input_file.with_suffix(".hack")

symbol_table = SymbolTable()

# ---------- PRIMEIRA PASSAGEM ----------

parser = Parser(input_file)

rom_address = 0

while parser.has_more_commands():

    parser.advance()

    if parser.command_type() == Parser.L_COMMAND:

        label = parser.symbol()

        if not symbol_table.contains(label):
            symbol_table.add_entry(label, rom_address)

    else:

        rom_address += 1


# ---------- SEGUNDA PASSAGEM ----------

parser = Parser(input_file)

next_variable = 16

with open(output_file, "w", encoding="utf-8") as output:

    while parser.has_more_commands():

        parser.advance()

        command = parser.command_type()

        if command == Parser.L_COMMAND:
            continue

        if command == Parser.A_COMMAND:

            symbol = parser.symbol()

            if symbol.isdigit():

                address = int(symbol)

            else:

                if not symbol_table.contains(symbol):

                    symbol_table.add_entry(symbol, next_variable)
                    next_variable += 1

                address = symbol_table.get_address(symbol)

            output.write(
                Code.a_instruction(address) + "\n"
            )

        else:

            output.write(
                Code.c_instruction(
                    parser.dest(),
                    parser.comp(),
                    parser.jump()
                ) + "\n"
            )

print("Arquivo gerado:", output_file)