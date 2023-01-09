def is_armstrong_number(number):
    while number>=0:
        n = [int(a) for a in str(number)]
        length = len(n)
        s=0
        for i in n:
            s+=i**length
        break

    if number==s:
        return True
    else:
        return False