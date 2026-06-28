class Parser:

    A_COMMAND = "A_COMMAND"
    C_COMMAND = "C_COMMAND"
    L_COMMAND = "L_COMMAND"

    def __init__(self, filename):

        self.commands = []

        with open(filename, "r", encoding="utf-8") as file:

            for line in file:

                # Remove comentários
                line = line.split("//")[0].strip()

                # Ignora linhas vazias
                if line:
                    self.commands.append(line)

        self.current_index = -1
        self.current_command = None

    def has_more_commands(self):

        return self.current_index + 1 < len(self.commands)

    def advance(self):

        self.current_index += 1
        self.current_command = self.commands[self.current_index]

    def command_type(self):

        if self.current_command.startswith("@"):
            return self.A_COMMAND

        if (
            self.current_command.startswith("(")
            and self.current_command.endswith(")")
        ):
            return self.L_COMMAND

        return self.C_COMMAND

    def symbol(self):

        if self.command_type() == self.A_COMMAND:
            return self.current_command[1:]

        if self.command_type() == self.L_COMMAND:
            return self.current_command[1:-1]

        raise ValueError("Comando não possui símbolo.")

    def dest(self):

        if "=" in self.current_command:
            return self.current_command.split("=")[0]

        return None

    def comp(self):

        command = self.current_command

        if "=" in command:
            command = command.split("=")[1]

        if ";" in command:
            command = command.split(";")[0]

        return command

    def jump(self):

        if ";" in self.current_command:
            return self.current_command.split(";")[1]

        return None