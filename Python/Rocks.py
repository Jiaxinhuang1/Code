#  File: Rocks.py

#  Description: Program that returns a list representing rocks after all meetings have occurred

#  Student Name: Jiaxin Huang

'''
John has a row of rocks, represented by an array of nonzero integers.
Each rock moves to the right if its integer is positive, and left otherwise.
The power of each rock is its integer squared. Assuming that each rock moves
at the same speed, some rocks will meet. If two rocks meet, the one with less
power disappears. If both rocks have the same power, both rocks disappear.
Return the arary after all such meetings have occurred. Two rocks moving in the
same direction will not meet.
'''

import sys

# Input:  rocks is a list of nonzero integers
# Output: return a list representing rocks after all meetings have occurred
def get_rock_list(rocks):
	if len(rocks) == 2:
		if not isNeg(rocks[0]) and isNeg(rocks[1]):
			if rocks[0] ** 2 < rocks[1] ** 2:
				del rocks[0]
			elif rocks[0] ** 2 > rocks[1] ** 2:
				del rocks[1]
			else:
				rocks.clear()
	else:
		for i in range(len(rocks) - 1):
			if not isNeg(rocks[i]) and isNeg(rocks[i + 1]):
				if rocks[i] ** 2 < rocks[i + 1] ** 2:
					del rocks[i]
				elif rocks[i] ** 2 > rocks[i + 1] ** 2:
					del rocks[i + 1]
				else:
					del rocks[i]
					del rocks[i + 1]
			else:
				continue
		for i in range(len(rocks) - 1):
			if not isNeg(rocks[i]) and isNeg(rocks[i + 1]):
				if rocks[i] ** 2 < rocks[i + 1] ** 2:
					del rocks[i]
				elif rocks[i] ** 2 > rocks[i + 1] ** 2:
					del rocks[i + 1]
				else:
					del rocks[i]
					del rocks[i + 1]
			else:
				continue	
	return rocks

	
def isNeg(num):
	if num < 0:
		return True
	else:
		return False
# ***There is no reason to change anything below this line***

def main():
	rocks = [int(r) for r in sys.stdin.readline().strip().split(" ")]
	result = get_rock_list(rocks)
	print(result)

if __name__ == "__main__":
	main()
