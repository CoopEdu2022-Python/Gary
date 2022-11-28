def capitalize_title(title: str) -> str:
    v=title.split(' ')
    New_tiltle = []
    for i in v:
        if len(i) <=2:
            a = i.lower()
            New_tiltle.append(a+' ')
        else:
            a = i.lower()
            b=a[0:1].upper()
            c=a[1:]
            a=b+c
            New_tiltle.append(a+' ')
    return ''.join(New_tiltle)
print(capitalize_title("First leTTeR of EACH Word"))