import random

race_breakdown = random.randint(1,2)
winning_horse = random.randint(1,5)
horse_chosen = random.randint(1,5)
money_bet = random.randint(1,20)
money = 100


print(f"money bet : {money_bet}")
print(f"horse chosen : {horse_chosen}")

if race_breakdown < 2 and race_breakdown > 0:
    print(f"its a really close race, but horse number {winning_horse} wins!")

if race_breakdown < 3 and race_breakdown > 1:
    print(f"its a no brainer as all the other horses are smoked and horse number {winning_horse} wins!")

print(f"winning horse : {winning_horse}")

if horse_chosen == winning_horse:
    if winning_horse is money_bet:
            Double_money = money_bet + money_bet
            print(f"double double! you win {Double_money}")
            money_made = Double_money
    else:
        print(f"you won ${money_bet}")
        money_made = money + money_bet
    
    
else:
    if money_bet == winning_horse:
        Double_lost = money_bet + money_bet
        print(f"Double double! you lost ${Double_lost}")
        money_lost = money - Double_lost
    else:
        print(f"sorry, but you lost ${money_bet}")
        money_lost = money - money_bet
    print("press run to lose more money")
    print(f"you now have ${money_lost}")


