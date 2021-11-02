def socc():
	n = abs(int(input("\nEnter number of digits: ")))
	l = []
	print("\nEnter the digits:\n\n")
	for i in range(0, n):
		l.append(abs(int(input())))
	x = abs(int(input("\nEnter x: ")))
	a = b = c = 0
	for i in range(0, n):
		if x == l[i]:
			if a == b:
				a = i
				c += 1
			elif (b == 0) and (a > 0):
				b = i
			else:
				if b-a > i-b:
					b = i
					a = b
	if b == 0:
		print("\nShrtest distance:", -1)
	else:
		print("\nShrtest distance:", b-a)

socc()