#exclusive mode
# Exclusive mode (x) creates a file only if it does not exist and raises an error if it already exists, preventing accidental overwriting.

with open("exclusivemode.txt", "x") as fp:
    fp.write("this is demo for exclusive mode x")
    fp.seek(0)
    data = fp.read()
    print(data)