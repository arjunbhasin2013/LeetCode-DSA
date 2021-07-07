'''
implementing iterative string reversal
'''

def reverser_string(s):
    return ''.join(s[i] for i in range(len(s)-1, -1, -1))

print(reverser_string('hello'))