def describe_city(city, country='China'):
    if city == 'Hainan' and country == 'China':
        return 'Yes'
    elif city == 'Shanghai' and country == 'China':
        return 'Yes'
    elif city == 'Tianjin' and country == 'China':
        return 'Yes'
    elif city == 'London' and country == 'England':
        return 'Yes'
    else:
        return 'No'


a = describe_city('Hainan', 'China')
print(a)
print(describe_city('Shanghai'))
print(describe_city('Tianjin'))
print(describe_city('London', 'England'))
