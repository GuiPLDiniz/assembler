from parser import Parser

parser = Parser("tests/test.asm")

while parser.has_more_commands():

    parser.advance()

    print(
        parser.command_type(),
        parser.current_command,
        parser.symbol() if parser.command_type() != "C_COMMAND" else "",
        parser.dest(),
        parser.comp(),
        parser.jump()
    )