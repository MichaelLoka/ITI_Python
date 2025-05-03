def mult_table (t_size):
    for i in range(1, t_size+1):
        for j in range(1, i+1):
            print(i , " x ", j, " = ", i*j)
        print("===================================")


def mult__table_list(number):
    mult_table = []

    for i in range(1, number+1):
        row = []
        for j in range(1, i+1):
            row.append(i*j)
        mult_table.append(row)
    print(f"Multiplication Table: {mult_table}")