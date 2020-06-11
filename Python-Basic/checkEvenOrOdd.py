import argparse
#import numberHalfUtility as nhfu
from Utilities import numberHalfUtility as nhfu
# from numberHalfUtility import numberHalf

def getArgs():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i','--integer',help='Please enter an integer :',default=1, type=int)
    args=parser.parse_args()
    return args.integer
    

def isEven(number):
    if number%2==0:
        print('{} is Even'.format(number))
    else:
        print('{} is Odd'.format(number))
        
def numberHalf(number):
    print('My numberHalf is called')
    return(number**2)
        
def main():
    isEven(getArgs())
    print ('Calling numberHalfUtility')
    isEven(nhfu.numberHalf(getArgs()))    
        
if __name__=='__main__':
    main()
    
