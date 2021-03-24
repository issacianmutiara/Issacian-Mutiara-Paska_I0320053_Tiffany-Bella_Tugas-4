a = 4       # 4 = 100
b = 11      # 11= 1011

print("------------------------------------")
#a
c = 4 | 11
print("nilai:" ,a,"binary" ,format(a, '03b'))
print("nilai:" ,b, "binary",format(b, '04b'))
print("nilai:" ,c, "binary",format(c, '05b'))

print("-------------------------------------")
#b
c = 4 >> 11
print("nilai:" ,a,"binary" ,format(a, '03b'))
print("nilai:" ,b, "binary",format(b, '04b'))
print("nilai:" ,c, "binary",format(c, '05b'))

print("-------------------------------------")
#c
c = 4 ^ 11
print("nilai:" ,a,"binary" ,format(a, '03b'))
print("nilai:" ,b, "binary",format(b, '04b'))
print("nilai:" ,c, "binary",format(c, '05b'))

print("--------------------------------------")
#d
c = ~4
print("nilai:" ,a,"binary" ,format(a, '03b'))
print("nilai:" ,b, "binary",format(b, '04b'))
print("nilai:" ,c, "binary",format(c, '05b'))

print("--------------------------------------")
#e
c = 11 & 4
print("nilai:" ,a,"binary" ,format(a, '03b'))
print("nilai:" ,b, "binary",format(b, '04b'))
print("nilai:" ,c, "binary",format(c, '05b'))
