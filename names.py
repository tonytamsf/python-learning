def count_arara(n):
    names = ['anane', 'adak']
    name = ''

    if n == 1:
        return names[0]
    if n == 2:
        return names[1]
    if n % 2 == 0:
        for i in range(1,n,2):
            name = name + ' ' + names[1]
    else:
        name = count_arara(n - 1) + ' ' + names[0]
    return name.lstrip()

print count_arara(9)
