'''
@author: Ciaran Burr
12/3
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    content = []
    import os.path
    file = os.path.join("data", "movies.txt")
    f = open(file)
    #taken from past
    ratings = {}
    items = []
    for each in f:
        each = each.strip()
        each = each.split(',')
        content.append(each)
    content = sorted(content, key=lambda x : x[1])
    #sorted it by movies
    for tlst in content:
        ratings[tlst[0]] = []
        if tlst[1] not in items:
            items.append(tlst[1]) #creates list for every item
    movie = content[0][1]
    x=0 #initializes first movie, the iterate through and tells if movie changes
    for tlst in content:
        if tlst[1] == movie:
            ratings[tlst[0]].append(int(tlst[2]))
        elif tlst[1] != movie:
            #if movie changes, adds zeros for everything w/o movie
            x += 1
            for each in ratings:
                if len(ratings[each]) < x:
                    ratings[each].append(0)
            ratings[tlst[0]].append(int(tlst[2]))
        movie = tlst[1]
    x += 1
    for each in ratings:
        if len(ratings[each]) < x:
            ratings[each].append(0)
    #adds the final 0 since the movie does not change for the last part of list
    for each in ratings:
        ratings[each] = ([int(x) for x in ratings[each]])
    #ensures everything is a int (since debugging)
    tup = (sorted(items),ratings)
    #sorted it, makes it tuple
    return tup

if __name__ == '__main__':
    print(getdata())
    pass