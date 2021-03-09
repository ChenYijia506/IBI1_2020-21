X = 1
print("第1项是"， X）
Y = 1
print("第2项是", Y)
for i in range(3,14):
Z = X + Y
X = Y
Y = Z
print("第", i, "项是", Z)
