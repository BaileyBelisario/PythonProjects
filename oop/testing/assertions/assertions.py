#def add_positive_number(x,y):
    #assert x > 0 and y > 0, "Both numbers must be positive"
    #return x + y
#
#print(add_positive_number(1,1))
#print(add_positive_number(1,-1))

def eat_junk(food):
    assert food in ['pizza','icecream','candy','fried butter'], "Food must be a junk food"
    return f"Nom nom nom i am eating {food}"

print(eat_junk('pizza'))
print(eat_junk('hdhd'))
