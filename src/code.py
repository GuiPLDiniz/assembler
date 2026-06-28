def decimal_to_binary(value):
    return format(int(value), "016b")


class Code:

    @staticmethod
    def a_instruction(symbol):

        return decimal_to_binary(symbol)