def xo(str):
    x, o = 0, 0

    for s in str:
        if s.lower() == 'o':
            o += 1
        if s.lower() == 'x':
            x += 1
    return o == x

