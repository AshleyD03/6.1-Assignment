# Food Past-Expiration Recommender
# v1.0.0
# author : Ashley Doel

# Take User Info
food = input('What food is it?')
expiry = int(input('How many days has it been since experation'))

# Preset Data
bad_foods = ['milk', 'cream', 'dairy', 'yogurt']

# Choose Recomendation(s)
if expiry < 5 : 
    print('\n'+food,'should still be good')
else : 
    print('\nI personally wouldn\'t')
    if str(food.lower()) in bad_foods : 
        print('\nI Really wouldn\'t, that\'s dairy')

        