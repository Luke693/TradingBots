import time

risk = 0.02
portfolio_value = 5000
max_risk = portfolio_value * risk

TICKER = input("Please Enter Ticker")
OTE = float(input("What is the OTE for this position?  "))
SL = float(input("What is the Stop-Loss for this position?  "))
T1 = float(input("Please enter 1st target:  "))
T2 = float(input("Please enter 2nd target:  "))
T3 = float(input("Please enter 3rd target:  "))

#calculate risk per unit
cents_at_risk = (OTE-SL)

#calculate ideal position size and risk for trade in USD & % terms
ideal_position_size = (max_risk/cents_at_risk)-1
usd_risk = (float(OTE-SL)*ideal_position_size)
trade_risk = str(round(usd_risk/portfolio_value*100, 2))

#specifies volumes for trade 1, 2 and 3
v1 = round(ideal_position_size*0.2)
v2 = round(ideal_position_size*0.4)
v3 = round(ideal_position_size*0.4)

#Tells me how position should be divided & risk levels
print("\n\nIdeal position size is: " + str(round(ideal_position_size)))
time.sleep(1)

if (v1 + v2 + v3) > ideal_position_size:
    v3 = v3-1
    print("Position should be split: " + str(v1) + ", " + str(v2) + ", " + str(v3) + " "),
else:
    print("Position should be split: " + str(v1) + ", " + str(v2) + ", " + str(v3) + " ")

time.sleep(1)
print("Risk to portfolio from this trade would be: " + trade_risk + "%")
time.sleep(1)
print("Risk in USD is: " + "$" + str(round(usd_risk, 2)))


#Calculate Risk Reward
time.sleep(1)
total_risk = usd_risk
total_reward = ((T1-OTE)*v1) + ((T2-OTE)*v2) + ((T3-OTE)*v3)
risk_reward = str(round(total_reward/total_risk, 2))
print("Risk Reward Ratio is:  " + "1:" + risk_reward)
