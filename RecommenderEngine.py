'''
@author: Ciaran Burr
12/3
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second
    element is a float.
    '''
    dic = {}
    i = 0
    for place in items:
        z = 0
        for name in ratings:
            if place not in dic:
                dic[place] = float(0)#initializes as float
            if ratings[name][i] == 0:
                pass
            else:
                dic[place] += ratings[name][i]#changes the ratings
                z += 1
        if dic[place] != 0:
            dic[place] = dic[place]/z
        i += 1
    templst = []
    for each in dic:
        tup = (each, dic[each])
        templst.append(tup)
        #puts it into tuples, then sorts it
    templst = sorted(templst, key=lambda x : x[0])
    templst = sorted(templst, key=lambda x : x[1], reverse=True)
    return templst


def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    i = 0
    ratingslst = ratings[name]
    tupslst = []
    for names in ratings:
        z = 0
        templst = []
        if name == names:
            i += 1
            pass
        else:
            for item in ratings[names]:
                templst.append(item*ratingslst[z])
                z += 1
            tup = names, sum(templst)
            tupslst.append(tup)
    tupslst = sorted(tupslst, key=lambda x: x[0])
    tupslst = sorted(tupslst, key=lambda x: x[1], reverse=True)
    return tupslst
 
def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    templst = similarities(name, ratings)
    templst = templst[0:numUsers]
    newratings = {}
    for name in templst:
        newratings[name[0]] = [name[1]*x for x in ratings[name[0]]]
    return averages(items, newratings)


if __name__ == '__main__':
    print(averages(['Cat', 'Dog'],{'Liam': [10, 1], 'Man-Lin': [1,
                                                                        3],
                                   'Max': [5, 6]}))
    pass