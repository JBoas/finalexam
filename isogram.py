input = input("Enter number ")

if input.isdigit():
	c1 = 0
	c2 = 0
	c3 = 0
	c4 = 0
	c5 = 0
	c6 = 0
	c7 = 0
	c8 = 0
	c9 = 0
	for x in input:
		if x == "1":
			c1 = c1 + 1
			if c1 > 1:
				print("false")
		if x == "2":
			c2 = c2 + 1
			if c2 > 1:
				print("false")
		if x == "3":
                	c3 = c3 + 1
                	if c3 > 1:
                		print("false")
		if x == "4":
			c4 = c4 + 1
			if c4 > 1:
				print("false")
		if x == "5":
			c5 = c5 + 1
			if c5 > 1:
				print("false")
		if x == "6":
			c6 = c6 + 1
			if c6 > 1:
				print("false")
		if x == "7":
			c7 = c7 + 1
			if c7 > 1:
				print("false")
		if x == "8":
			c8 = c8 + 1
			if c8 > 1:
				print("false")
		if x == "9":
			c9 = c9 + 1
			if c9 > 1:
				print("false")

	if c9<=1 and c8<=1 and c7<=1 and c6<=1 and c5<=1 and c4<=1 and c3<=1 and c2<=1 and c1<=1:
			print("true")
else:
	print("false")
