from code import Code

print(Code.c_instruction("D", "A", None))
print(Code.c_instruction(None, "0", "JMP"))
print(Code.c_instruction("M", "D+1", None))