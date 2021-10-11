w3 = "anca" 
w1 = "ioana" 
w2 = "Constantin" 
temp = None

print(w2)
if w2 < w1:
    temp = w1
    w1 = w2
    w2 = temp

print(w2)

print(w3)

if w2 < w3:
    temp = w2
    w2 = w3
    w3 = temp
print(w3)

print (w1,w2,w3)
