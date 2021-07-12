'''
Find the count of total prime numbers for N numbers in array
'''

def sieve_prime(num):
    sieve = [0 for i in range(0, num+1)]
    sieve[0] = 1
    sieve[1] = 1
    
    #labeling all odd numbers as prime
    for i in range(3,num+1, 2):
        sieve[i-1] = 1
        
    for i in range(3, num, 2):
        if sieve[i-1] == 1:
            for j in range(i*i,num,i):
                sieve[j-1] = 0
    
    primes = [i for i in range(0, num+1) if sieve[i-1] ==1]
    return primes

if __name__ == "__main__":
    print(sieve_prime(20))
    
    