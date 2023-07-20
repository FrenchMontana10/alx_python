combinations = ['{}{}'.format(i, j) for i in range(10) for j in range(10 if i < j]
print(', '. join(combinations))