# original
q = 8666-7777
w = 4
print("original = " + str (q),(w))

# 1 ver
e = q
q = w
w = e
print("1 ver = " + str (q),(w))

# 2 ver
q, w = w, q
print("2 ver = " + str (q),(w))

# 3 ver
q = w + q
w = q - w
q = q - w
print("3 ver = " + str (q),(w))


