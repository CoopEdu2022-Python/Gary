travel_list = ['china', 'USA', 'UK', 'Japan', 'Newzeland']
travel_list1 = travel_list.copy()
print(travel_list)
for i in travel_list:
    print(i)
travel_list.reverse()
for i in travel_list:
    print(i)

print(travel_list)
for i in travel_list:
    if i == travel_list1[travel_list1.index(i)]:
        print('变了')
    else:
        print('没变')
travel_list.reverse()
print(travel_list)
travel_list.sort(reverse=True)

print(travel_list)
for i in travel_list:
    if i == travel_list1[travel_list1.index(i)]:
        print('变了')
    else:
        print('没变')
travel_list.sort()
for i in travel_list:
    if i == travel_list1[travel_list1.index(i)]:
        print('变了')
    else:
        print('没变')