# operasi komparasi

# setiap kali hasil komparasi selalu bertipe boolean (TRUE/FALSE)

# # >, <, =, !=, >=, <=, is, dan is not

# deklarasi variabel
a = 4
b = 2

# lebih besar dari (<)
print("===Lebih Besar Dari (>)")
hasil = a > 2 # TRUE
print(a, ">", 2, "=", hasil)
hasil = b > 3 # FALSE
print(b, ">", 3, "=", hasil)
hasil = b > 4 # FALSE
print(b, ">", 4, "=", hasil)


# kurang dari (<)
print("===Kurang Dari (<)")
hasil = a < 2 # FALSE 
print(a, "<", 2, "=", hasil)
hasil = b < 3 # TRUE
print(b, "<", 3, "=", hasil)
hasil = b < 4 # TRUE
print(b, "<", 4, "=", hasil)

# lebih dari sama dengan (>=)
print("=== lebih dari sama dengan (>=)")
hasil = a >= 2 # TRUE
print(a, ">=", 2, "=", hasil)
hasil = b >= 3 # FALSE
print(b, ">=", 3, "=", hasil)
hasil = b >= 4 # FALSE
print(b, ">=", 4, "=", hasil)

# kurang dari sama dengan (<=)
print("===kurang dari sama dengan (<=)")
hasil = a <= 2 # FALSE
print(a, "<=", 2, "=", hasil)
hasil = b <= 3 # TRUE
print(b, "<=", 3, "=", hasil)
hasil = b <= 4 # TRUE
print(b, "<=", 4, "=", hasil)


# sama dengan (==)
print("=== sama dengan (==)")
hasil = a == 2 # FALSE
print(a, "==", 2, "=", hasil)
hasil = b == 3 # FALSE
print(b, "==", 3, "=", hasil)
hasil = a == 4 # TRUE
print(a, "==", 4, "=", hasil)

# tidak sama dengan (!=)
print("=== tidaksama dengan (!=)")
hasil = a != 2 # TRUE
print(a, "!=", 2, "=", hasil)
hasil = b != 3 # TRUE
print(b, "!=", 3, "=", hasil)
hasil = a != 4 # FALSE
print(a, "!=", 4, "=", hasil)

#  is sebagai komparasi objek
x = 5
y = 5
hasil = x is y
print("nilai x :", x, "id: ", hex(id(x)))
print("nilai y :", y, "id: ", hex(id(y)))
print(x, "is", y, "=", hasil)

#  is not sebagai komparasi objek
x = 5
y = 5
hasil = x is not y
print("nilai x :", x, "id: ", hex(id(x)))
print("nilai y :", y, "id: ", hex(id(y)))
print(x, "is not", y, "=", hasil)