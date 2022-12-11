a1 = "sample text"              # 1

a2 = "sample text"

a3 = "sample text"

print(a1 == a2 == a3)

print(a1 is a2 is a3)

a3 = set(a1)

a4 = set(a2)

a5 = set(a3)

print(a3 == a4 == a5)

print(a3 is a4 is a5)

b1 = {1, 2, 3}                      # 2

b2 = {1, 2, 3}

print(b1 == b2)

print(b1 is b2)

b3 = bool(b1)

b4 = bool(b2)

print(b3 == b4)

print(b3 is b4)
