'''
@author: Ciaran Burr
12/3
'''


import RecommenderEngine


def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple
    consisting of two lists. The first list is the top items rated by the rater
    called name (string).The second list is the top items not seen/rated by name
    (string)
    '''
    answer = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    namelst = (ratings[name])
    ownlst = []
    i = 0
    for each in items:
        tup = (each, namelst[i])
        i += 1
        ownlst.append(tup)
    ownlst = sorted(ownlst, key=lambda x: x[1], reverse=True)
    #ownlst of rankings, answer stores the weighted averages
    finallst1=[]
    finallst2=[]
    for x in answer:
        for y in [z for z in ownlst if z[1]!=0][:]:
            if x[0]==y[0]:
                finallst1.append(x)
    for x in answer:
        for y in [z for z in ownlst if z[1]==0][:]:
            if x[0]==y[0]:
                finallst2.append(x)
    #creates two different lists of where they ranked 0 and didnt, then 0:top
    # to take 'top' amount
    tupfin = (finallst1[0:top], finallst2[0:top]) #allows tuple
    return tupfin


if __name__ == '__main__':
    print(makerecs('student1367',['127 Hours', 'The Godfather', '50 First '
                                                                 'Dates', 'A Beautiful Mind', 'A Nightmare on Elm Street', 'Alice in Wonderland', 'Anchorman: The Legend of Ron Burgundy', 'Austin Powers in Goldmember', 'Avatar', 'Black Swan']
,{'student1367': [ 0, 3,-5, 0, 0, 1, 5, 1, 3, 0],
'student1046': [ 0, 0, 0, 3, 0, 0, 0, 0, 3, 5],
'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0],
'student1103': [-3, 3,-3, 5, 0, 0, 5, 3, 5, 5]},  2,3))
    pass
             



