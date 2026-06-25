a = input("Enter value for a: ")
b = input("Enter value for b: ")
c = input("Enter value for c: ")
print(f"Before swap: a={a}, b={b}, c={c}")
a, b, c = b, c, a
print(f"After swap:  a={a}, b={b}, c={c}")