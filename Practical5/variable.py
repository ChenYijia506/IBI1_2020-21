a = 120502
b = 190784
c = 100321
d = abs(a-c)
e = abs(a-b)
if d == e:
  print("d quals to e")
elif d > e:
  print("d is bigger than e")
else:
  print("d is smaller than e")

X = True
Y = False
Z = (X and not Y)or(Y and not X)
W = X!=Y
if Z==W:
    print("Z and W are the same.")

X = False
Y = True
Z = (X and not Y)or(Y and not X)
W = X!=Y
if Z==W:
    print("Z and W are the same.")


X = True
Y = True
Z = (X and not Y)or(Y and not X)
W = X!=Y
if Z==W:
    print("Z and W are the same.")


X = False
Y = False
Z = (X and not Y)or(Y and not X)
W = X!=Y
if Z==W:
    print("Z and W are the same.")
