def is_multiple(n: int, of: int) -> bool:
	if n % of == 0:
		return True

	return False

s = 0

for i in range(1000):
	if(is_multiple(i, 3) or is_multiple(i, 5)):
		s += i

print(s)