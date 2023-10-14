x = 5
y = 20
h = x // 2
full_stack_size = h * (h + 1)

if h != x / 2:
    full_stack_size += x // 2

full_stacks = y // full_stack_size
left = y - full_stacks * full_stack_size
step = x
res = [0] * x

while left != 0:
    stack = 0
    if left > step:
        stack = step
        left -= step
    else:
        stack = left
        left = 0
    
    stack_left = (x - stack) // 2
    stack_right = stack_left + stack
    
    for idx in range(stack_left, stack_right):
        res[idx] += 1
    
    step -= 2

left = y
l = []
for i in range(h):
    r = full_stacks * (i + 1) + res[i]
    left -= r
    l.append(r)

if h != x / 2:
    h = (x // 2) + 1
    r = full_stacks * h + res[h - 1]
    left -= r
    l.append(r)

for i in range(h, x):
    r = full_stacks * (x - i) + res[i]
    if r > left:
        r = left
    left -= r
    l.append(r)

print(l)