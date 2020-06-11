def numberHalf(number):
    print('numberHalf called')
    print(__name__)
    return (number/2)


if __name__=='__main__':
    print(__name__)
    numberHalf(1)