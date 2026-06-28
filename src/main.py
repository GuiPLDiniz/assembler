from symbol_table import SymbolTable

table = SymbolTable()

print(table.get_address("SP"))
print(table.get_address("LCL"))
print(table.get_address("R0"))
print(table.get_address("R15"))
print(table.get_address("SCREEN"))
print(table.get_address("KBD"))

table.add_entry("LOOP", 10)
print(table.contains("LOOP"))
print(table.get_address("LOOP"))