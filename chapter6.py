l = []
def inp(rows, cols):
    for i in range(rows):
        row_vals = []
        for j in range(cols):
            row_vals.append(int(input(f"Enter value at {i}th row and {j}th column: ")))
        l.append(row_vals)
    return l

def out():
    print(l)
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j] + " ", end="")
            
rows = int(input("Enter row: "))
cols = int(input("Enter col:"))

inp(rows, cols)
out()
        