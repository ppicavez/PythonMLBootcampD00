from vector import Vector

print("INITIALISATION TESTS")
print(Vector(1))
print("----------------------------------------------------------------------")
print(Vector("Other"))
print("----------------------------------------------------------------------")
print(Vector("2"))
print("----------------------------------------------------------------------")
print(Vector(3, 4))
print("----------------------------------------------------------------------")
print(Vector(["10"]))
print("----------------------------------------------------------------------")
print(Vector([]))
print("----------------------------------------------------------------------")
print(Vector([3]))
print("----------------------------------------------------------------------")
print(Vector([4, 5]))
print("----------------------------------------------------------------------")

# operations testing
print("OPERATION TESTS")
vector1 = Vector(5)
print("----------------------------------------------------------------------")
vector2 = Vector(5, 10)
print("----------------------------------------------------------------------")
vector3 = Vector([1, 3, 0])
print("----------------------------------------------------------------------")
print(repr(vector1))
print("----------------------------------------------------------------------")
print(repr(vector2))
print("----------------------------------------------------------------------")
print("TEST ADD")
print("----------------------------------------------------------------------")
print(vector1 + vector2)
print("----------------------------------------------------------------------")
print(vector2 + vector1)
print("----------------------------------------------------------------------")
print(vector1 + vector3)
print("----------------------------------------------------------------------")
print(vector1 + 13)
print("----------------------------------------------------------------------")
print(vector1 + "9")
print("----------------------------------------------------------------------")
print(vector1 + [0, 1, 2, 3, 4])
print("----------------------------------------------------------------------")
print(13 + vector1)
print("----------------------------------------------------------------------")
print("TEST SUB")
print("----------------------------------------------------------------------")
print(vector1 - vector2)
print("----------------------------------------------------------------------")
print(vector2 - vector1)
print("----------------------------------------------------------------------")
print(vector1 - 4)
print("----------------------------------------------------------------------")
print(4 - vector1)
print("----------------------------------------------------------------------")
print(vector1 - "100")
print("----------------------------------------------------------------------")
print("TEST MUL")
print("----------------------------------------------------------------------")
print(vector1 * vector2)
print("----------------------------------------------------------------------")
print(vector2 * vector1)
print("----------------------------------------------------------------------")
print(vector1 * vector3)
print("----------------------------------------------------------------------")
print(vector1 * 9)
print("----------------------------------------------------------------------")
print(vector1 * -10)
print("----------------------------------------------------------------------")
print(-1 * vector1)
print("----------------------------------------------------------------------")
print(vector1 * "9")
print("----------------------------------------------------------------------")
print(vector1 * [4])
print("----------------------------------------------------------------------")
print("TEST TRUEDIV")
print("----------------------------------------------------------------------")
print(vector1 / vector2)
print("----------------------------------------------------------------------")
print(vector1 / vector3)
print("----------------------------------------------------------------------")
print(vector1 / 2)
print("----------------------------------------------------------------------")
print(2 / vector1)
print("----------------------------------------------------------------------")
print(vector1 / "9")
print("----------------------------------------------------------------------")
print(vector1 / [2])
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")