def pattern(n):
    if n < 1:
        return ''
    if n == 1:
        return '1'
    final = ''
    for i in range(1,n+1,1):
       line = ''
       for j in range(n,i-1,-1):
          line = line + str(j)
       final = final + line + '\n'
    return final.rstrip()
