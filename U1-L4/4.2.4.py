def describe_city(city, country='China'):
    return '%s is in %s.'%(city,country)

print(describe_city('Hainan'))
print(describe_city('Shanghai'))
print(describe_city('Tianjin'))
print(describe_city('London','England'))
