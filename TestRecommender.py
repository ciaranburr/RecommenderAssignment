'''
@author: Ciaran Burr
12/3
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    """
    using this driver function to test all other function
    """
    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)

    
    avg = RecommenderEngine.averages(items,ratings)
    print("average",avg)
     
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
        print(key,slist)
        r3 = RecommenderEngine.recommendations(key,items,ratings,3)
        print("top",r3)
    answer=""
    if avg==[('DivinityCafe', 4.0), ('TheCommons', 3.0),
 ('Tandoor', 2.4285714285714284), ('IlForno', 1.8),
 ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0),
 ('TheSkillet', 0.0), ('PandaExpress', -0.2),
 ('McDonalds', -0.3333333333333333)]:
        answer += ("\nYour average worked!")
    else:
        answer += ("\nYour average failed!")
    if (RecommenderEngine.similarities('Sung-Hoon', ratings)) == [('Wei', 1),
        ('Sly one', -1), ('Melanie', -2), ('Sarah Lee', -6),
        ('J J', -14), ('Harry', -24), ('Nana Grace', -29)]:
        answer += ("\nYour similarities worked!")
    else:
        answer += ("\nYour similarities failed!")
    if RecommenderEngine.recommendations('Sarah Lee', items,
            ratings, 3)==[('Tandoor', 149.5), ('TheCommons', 128.0),
 ('DivinityCafe', 123.33333333333333), ('FarmStead', 69.5),
 ('TheSkillet', 66.0), ('LoopPizzaGrill', 62.0),
 ('IlForno', 33.0), ('McDonalds', -69.5),
 ('PandaExpress', -165.0)]:
        answer += ("\nYour recommendations worked!")
    else:
        answer += ("\nYour recommendations failed!")
    return answer
#multiple ifs, test all three and changes depending on results
        
        
if __name__ == '__main__':
    print(driver())