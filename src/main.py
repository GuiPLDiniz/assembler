from pathlib import Path

from parser import Parser
from code import Code


input_file = Path("tests/test.asm")
output_file = input_file.with_suffix(".hack")

parser = Parser(input_file)

with open(output_file, "w", encoding="utf-8") as output:

    while parser.has_more_commands():

        parser.advance()
        command_type = parser.command_type()

        if command_type == Parser.A_COMMAND:

            symbol = parser.symbol()

            if symbol.isdigit():

                output.write(Code.a_instruction(symbol) + "\n")

        elif command_type == Parser.C_COMMAND:

            output.write(
                Code.c_instruction(
                    parser.dest(),
                    parser.comp(),
                    parser.jump()
                ) + "\n"
            )

print("Arquivo gerado:", output_file)