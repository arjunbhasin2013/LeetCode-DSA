'''
Closes special number

1. Every digit i present in X, occurs in i number of times in X

2. The count of even digits is equal to the count of odd digits. 
Same digits are considered just once. 
For ex- 12112, has 1 odd digit '1' and 1 even digit '2'

'''

def create_map(num):
    map_counter = {}

    for i in str(num):
        if i in map_counter:
            map_counter[i]+=1
        else:
            map_counter[i] = 1
    return map_counter

def check_special(mp_obj):
    cnter=0,odd = 0,even = 0
    for key, value in mp_obj.items():
        if int(key) == int(value):
            cnter+=1
    for key, value in mp_obj.items():
        if int(key)%2==0:
            even+=1
        else:
            odd+=1
    if(int(cnter)==len(mp_obj)) and (even==odd):
        return True
    else:
        return False

def solve (N):
    for i in range(N, N*1000):
        mp = create_map(i)
        main_out = check_special(mp)
        if main_out == True:
            return i

T = int(input())
res = []
for _ in range(T):
    N = int(input())
    out_ = solve(N)
    res.append(out_)
for i in res:print(i)