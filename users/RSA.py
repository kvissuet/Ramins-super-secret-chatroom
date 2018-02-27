def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def decoder(n):
  alph="abcdefghijklmnopqrstuvwxyz"
  n=str(n)
  word=""
  for i in range(len(n)//2):
    word+=alph[int(n[2*i:2*(i+1)])-1]
  return(word)
  
def RSA_encryption(private_key,n):
	n=712446816787
	p1=740513
	p2=962099
	lamb=(p1-1)*(p2-1)

	e=6551
	d=modinv(e,lamb)
	
	s=273095689186
