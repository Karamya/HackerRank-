line1 = input()
line2 = input()
line3 = input()
line4 =  input()

n = int(str.split(line1)[0])
k = int(str.split(line1)[1])

line2 = [float(x) for x in line2.split()]
line3 = [float(x) for x in line3.split()]
line4 = [float(x) for x in line4.split()]

expected_money = []
for i in range(n):
    expected_money.append(line2[i]*line3[i] - (1 - line2[i])*line4[i])

expected_money = sorted(expected_money, reverse = True)
max_profit = 0
for j in range(k):
    if expected_money[j] > 0:
        max_profit = max_profit + expected_money[j]
    else:
        break
    
print(format((max_profit), '.2f'))
