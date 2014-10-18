__author__ = 'risinsun'

def find_details(id2find):
    s = {}
    list_file = open("list.txt")
    for line in list_file:
        (s['id'], s['name'], s['country'], s['average'], s['board_type'], s['age']) = line.split(";")
        if int(s['id']) == id2find:
            return(s)
    return({})

identifier = int(input("Enter id to find: "))
result = find_details(identifier)
if result:
    print("id:         " + result['id'])
    print("name:       " + result['name'])
    print("country:    " + result['country'])
    print("average:    " + result['average'])
    print("board type: " + result['board_type'])
    print("age:        " + result['age'])
