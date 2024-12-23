from icecream import ic

if __name__ == "__main__":
	ar=[4,35,8,9,2,6,2,15,4,3]
	for i in ar:
		if i % 3 == 0:
			ic(i)
			print("fizz")
			if i % 5 == 0:
				print("buzz")
				if i % 3 == 0 and i % 5 == 0:
					ic(i)