### fibonacci series using iteration

#[0,1,1,2,3,5,8,13]

def fibo(n):
    n1,n2 = 0,1
    count = 1

    while count<=n:
        print(n1)
        n_sum = n1+n2
        n1 = n2
        n2 = n_sum
        count+=1

if __name__ == "__main__":
    print(fibo(5))




