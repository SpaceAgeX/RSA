import os
import math
import random
import datetime


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(min_val, max_val):
    prime = random.randint(min_val, max_val)
    while not is_prime(prime):
        prime = random.randint(min_val, max_val)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse doesn't exist")

def get_phi(P, Q):
    return (P-1)*(Q-1)

def encrypt(data, e, n):
    data  = [ord(ch) for ch in data]
    return [pow(ch, e, n) for ch in data]

def decrypt(c, d, n):
    c  = [pow(ch, d, n) for ch in c]
    return "".join(chr(ch) for ch in c)

def generate_key():
    P, Q = generate_prime(1000, 5000), generate_prime(1000, 5000)
    while P == Q:
        Q = generate_prime(1000, 5000)

    n = P  *Q
    phi = get_phi(P, Q)

    e = random.randint(3, phi-1)
    while math.gcd(e, phi) != 1:
        e = random.randint(3, phi-1)

    d = mod_inverse(e, phi)

    return (P, Q, n, phi, e, d)
def main():
    os.system('cls')

    #Encryption Var

    P, Q, n, phi, e, d = generate_key() 
    

    while True:

        os.system('cls')
        print("--Encryption Variables--")
        print("P: " + str(P) + "\nQ: " + str(Q) +"\ne: " + str(e) + "\nn: " + str(n) + "\nphi: " + str(phi) +"\nd: " + str(d))
        

        Edata = encrypt(input("Data: "), e, n)


        print("Encryption: " + str(Edata))
        print("Decryption: " + str(decrypt(Edata, d, n)))

       
        if input("Press Enter To Continue>") == "q":
            break

    print("--End Program--")





if __name__ == "__main__":
    main()