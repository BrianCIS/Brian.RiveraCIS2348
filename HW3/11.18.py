#Brian Rivera
# 1922712
intergers = input().split()
result = []

for num in intergers:
    num = int(num)
    if num >= 0:
        result.append(num)

result.sort()
for num in result:
    print(num, end=' ')
