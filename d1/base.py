f = input('What food is it?')
e = int(input('How many days has it been since experation'))

bad_foods_list_recomendation = ['milk', 'cream', 'dairy', 'yogurt']

if e < 5 : {
print('\n'+f,'should still be good')
}
else : 
    print('\nI personally wouldn\'t')
    if str(f.lower()) in bad_foods_list_recomendation : {
    print('\nI Really wouldn\'t, that\'s dairy')
    }