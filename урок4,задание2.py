a = float(int(input()))
b = a % 100 // 10   
c = a % 10
d = a % 1000 // 100
e = a % 10000 // 1000
f = a % 100000 // 10000
print(b ** c * d / (f - e))


 