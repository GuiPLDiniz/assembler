from pathlib import Path

from parser import Parser
from code import Code


input_file = Path("tests/test.asm")
output_file = input_file.with_suffix(".hack")

parser = Parser(input_file)

with open(output_file, "w") as output:

    while parser.has_more_commands():

        parser.advance()

        if parser.command_type() == Parser.A_COMMAND:

            symbol = parser.symbol()

            if symbol.isdigit():

                output.write(
                    Code.a_instruction(symbol) + "\n"
                )

print("Arquivo gerado:", output_file)