## RSA Algorithm for Ecrytpion and Decryption

def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)
gcd(2,5)

def get_primes_from(x,y):
    primes = []
    for i in range(x,y):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            primes.append(i)
    return primes


print("RSA Algorithm Considers Two Prime Numbers For Encryption and Decryption")

print("Enter Range to consider prime numbers ")
print("Primes -> ",get_primes_from(int(input("Enter x-> ")),int(input("Enter y-> "))))

x = int(input("Enter Fisrt Prime Number : "))
y = int(input("Enter Second Prime Number : "))
n = x*y
phi = (x-1)*(y-1)
print("phi = ",phi)
print("n = ",n)

e = 2    ## 1<e<phi
while e < phi:
    if(gcd(e,phi)==1):
        break
    else:
       e = e+1


def gcdExtended(a,b):
    if a == 0:
        return b,0,1
    gcd,x1,y1 = gcdExtended(b%a,a)
    x = y1-(b//a)*x1
    y = x1
    return gcd,x,y

def get_multiplicative_inverse(gt,phi):
    gcd,t1 = gt[0],gt[1]
    if gcd == 1:
        if t1 < 0:
            return t1+phi
        else:
            return t1


d = get_multiplicative_inverse(gcdExtended(e,phi),phi)


## Now Encryption and Decryption

message = int(input("Enter Message -> "))
encrypted_msg = (message**e) % n
print("Encrypted Text = ",encrypted_msg)
decrypted_msg = (encrypted_msg**d) % n
print("Decrytped Text = ",decrypted_msg)


