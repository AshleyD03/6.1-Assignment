# I 
a = float(input('a ?')); b = float(input('b ?'))

# Repeating code way
answer_1 = str(a / b)
print(answer_1)
answer_2 = str(b / a)
print(answer_2)

# Function way
def div(c, d):
    return str(c / d)

# We now can just call a function, 
# instead of having to repeat the calculation code
print(div(a, b))
print(div(b, a))


