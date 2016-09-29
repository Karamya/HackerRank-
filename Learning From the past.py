n = input()
try: 
    n = int(n)
except:
    print('Please enter a number')
largest = 0
for i in range(int(n)):
    xyz = str.split(input())
    try: 
        for number in xyz:
            int(number)
    except:
        print('Please enter a number')
    max_profit = int(sorted(xyz, reverse = True)[0]) + int(sorted(xyz, reverse = True)[1] )
    if (max_profit > largest):
        largest = max_profit
print(largest)
