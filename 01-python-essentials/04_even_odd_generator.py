
def even_odd():
    flag = True
    while True:
        if flag == True:
            flag = False
            yield 'Even'
        else:
            flag = True
            yield 'Odd'

generate_even_odd = even_odd()
print(next(generate_even_odd))
print(next(generate_even_odd))
print(next(generate_even_odd))
print(next(generate_even_odd))
