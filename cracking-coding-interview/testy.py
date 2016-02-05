def test(val, exp):
    if (exp == val):
        print("OK. expected %r got %r" % (exp, val))
        return True
    else:
        print("********** False ********")
        print("Expected %r Got %r" % (exp, val))
        return False


