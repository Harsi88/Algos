def gcd(m,n):
	if m%n==0:
		return n
	else:
		return gcd(n,m%n)

m = int(raw_input())
n = int(raw_input())
print gcd(m,n)
