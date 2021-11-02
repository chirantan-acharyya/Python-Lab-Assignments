def dif(n):
	a = int(n % 10)
	n = int(n/10)
	b = int(n % 10)
	n = int(n/10)
	if abs(a-b) == 1:
		while n != 0:
			a = b
			b = int(n % 10)
			if abs(a-b) != 1:
				return 0
			n = int(n/10)
		return 1
	else:
		return 0



n = abs(int(input("\nEnter n: ")))
l = []
if n-9 <= 0:
	l.append(-1)
for i in range(10, n+1):
	if dif(i):
		l.append(i)
print("\nOutput:", l)
