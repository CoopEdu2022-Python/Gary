intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print(trantab)
str = "this is string example....wow!!!"
print (str.translate(trantab))