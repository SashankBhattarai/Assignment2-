import random as r

n=[]
for i in range(15):
    n.append(r.randint(1, 30))

player1 = n[0:5]
player2 = n[5:10]
player3 = n[10:15]

sum1 = 0
sum2 = 0
sum3 = 0

for num in player1:
    sum1 += num

for num in player2:
    sum2 += num
 
for num in player3:
    sum3 += num

if sum1 > sum2 and sum1 > sum3:
    print(f"Player 1 wins!{sum1}")
elif sum2 > sum1 and sum2 > sum3:
    print(f"Player 2 wins!{sum2}")
elif sum3 > sum1 and sum3 > sum2:
    print(f"Player 3 wins!{sum3}")
else:
    print("It's a tie!")
