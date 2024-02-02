'''
@author: Ciaran Burr
12-3
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    content = []
    import os.path
    file = os.path.join("data", "books.txt")
    f = open(file)
    #taken from past codes, how to access the data file
    ratings = {}
    items = []
    for each in f:
        each = each.strip()
        each = each.split(',')
        content.append(each)
    #splits everything and makes into content so you can iterate through
    for tlst in content:
        ratings[tlst[0]] = []
    for tlst in content:
        for i in range(1, len(tlst), 2):
            if tlst[i] not in items:
                items.append(tlst[i])
            #count by 2 since every 2nd
            ratings[tlst[0]].append(tlst[i+1])
    for each in ratings:
        ratings[each] = ([int(x) for x in ratings[each]])
    #ensures they are ints for each student
    end = (items, ratings)
    return end

if __name__ == '__main__':
    print(getdata())
    pass