n,k = list(map(int,input().rstrip().split(" ")))
vals = []
answers = [0]*n
for i in range(n):
    vals.append(int(input().rstrip()))
for position in range(n):
    if position == 0:
        answers[position] = vals[position]
    elif position >= k+1:
        answers[position] = max(vals[position] + answers[position-k-1], answers[position-1])
    else:
        answers[position] = max(vals[position], answers[position-1])
print(max(answers))