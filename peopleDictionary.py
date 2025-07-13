people = [
   {"name": "Alice", "age": 30},
   {"name": "Bob", "age": 17},
   {"name": "Charlie", "age": 25},
   {"name": "David", "age": 15}
]
#check list of people function
def checkList(people):
    #empty list
    list = []
    #run for each item in people
    for item in people:
        #retrieve age
        age = item.get("age")
        #if under 18
        if age < 18:
            #store name in list
            list.append(item.get("name"))
    #return list
    return list

#print list
print(checkList(people))