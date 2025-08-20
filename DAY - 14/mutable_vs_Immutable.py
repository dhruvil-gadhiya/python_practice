# Identify which Python data types are mutable (can be changed in place) and which are immutable...

# Immutable example: string
s = "hello"
print("String before:", s, "| id:", id(s))
s = s + " world"   # creates a NEW string
print("String after:", s, "| id:", id(s))

print("-" * 40)

# Mutable example: list
lst = [1, 2, 3]
print("List before:", lst, "| id:", id(lst))
lst.append(4)       # modifies the SAME list
print("List after:", lst, "| id:", id(lst))

print("-" * 40)

# Immutable example: tuple
t = (1, 2, 3)
print("Tuple:", t, "| id:", id(t))
# t[0] = 10  #This will raise TypeError

print("-" * 40)

# Mutable example: dict
d = {"a": 1, "b": 2}
print("Dict before:", d, "| id:", id(d))
d["c"] = 3         # modifies in place
print("Dict after:", d, "| id:", id(d))


