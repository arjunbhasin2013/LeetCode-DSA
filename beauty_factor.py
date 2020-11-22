'''
Finding sum of digits of a number until sum becomes single digit
'''

def beauty_factor(num):
    if num ==0:
        return 0

    if num%9==0:
        return 9

    else:
        return num%9

if __name__ == "__main__":
    print(beauty_factor(1987))
