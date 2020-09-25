n= int(input())
i = 1

while i <= n:
		left = ''.join(map(str, range(1,i)))
		spaces = ' ' * (n-i)
		print(f'{spaces}{left}{i}{left[::-1]}')
		i= i+1