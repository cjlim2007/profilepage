import math
def non_origin_rotation(x, y, angle, b = 0, c = 0):
	newx = (b - x) * math.cos(math.radians(angle)) - (c - y) * math.sin(math.radians(angle)) + x
	newy = (b - x) * math.sin(math.radians(angle)) + (c - y) * math.cos(math.radians(angle)) + y
	print (newx, newy)
	return (newx, newy)
def rotation(x, y, angle = 120):
	newx = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
	newy = y * math.cos(math.radians(angle)) + x * math.sin(math.radians(angle))
	print (newx, newy)
	return (newx, newy)
rotation(7,11)
rotation(7,9)
rotation(7,6)
rotation(4,8)
rotation(10,8)
rotation(5,4)
rotation(9,4)
rotation(10,10)

