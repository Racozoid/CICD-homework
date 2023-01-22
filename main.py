import prettytable

# Very simple script
table = prettytable.PrettyTable()

table.field_names = ["Column 1", "Column 2", "Column 3"]
table.add_row([0, 1, 2])
table.add_row([3, 4, 5])
table.add_row([6, 7, 8])

print(table)
