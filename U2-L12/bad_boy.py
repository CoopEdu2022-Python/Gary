a = 1
for i in range(10):
   a += 1
   print(a)
for i in range(10):
    a -= 1
    print(a)
    if a == 5:
      print(a)
      break
    else:
        if a == 7:
            print(a)
            break
print(a)