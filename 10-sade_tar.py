from math import prod

l = [float(input()) for i in range(4)]

print(f'Sum : {sum(l):.6f}')
print(f'Average : {sum(l)/len(l):.6f}')
print(f'Product : {prod(l):.6f}')
print(f'Max : {max(l):.6f}')
print(f'Min  : {min(l):.6f}')