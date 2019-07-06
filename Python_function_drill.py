

mySentence = 'loves the color'

color_list = ['blue','green','red','yellow','black','purple','teal','magenta']



def color_function(name):
    lst = []
    for i in color_list:
       msg = "{} {} {}".format(name,mySentence,i)
       lst.append(msg)
    return lst
    
        


lst = color_function('Matt')

for i in lst:
    print(i)

    
