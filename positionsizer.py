import time
from TradeManagementSystem import getSL

risk = 0.0087
portfolio_value = 6450
max_risk = portfolio_value * risk


class Trade:
    def __init__(self, tick, t3, t2, t1, ote, sl):
        self.tick = tick
        self.ote = ote
        self.sl = sl
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3


    def get_trade_info(self):
        # calculate risk per unit
        cents_at_risk = (float(self.ote) - float(self.sl))

        # calculate ideal position size and risk for trade in USD & % terms
        ideal_position_size = round(max_risk / cents_at_risk)
        usd_risk = (float(self.ote) - float(self.sl)) * ideal_position_size
        trade_risk = round(usd_risk / portfolio_value * 100, 2)

        # specifies volumes for trade 1, 2 and 3
        v1 = round(ideal_position_size * 0.2)
        v2 = round(ideal_position_size * 0.4)
        v3 = round(ideal_position_size * 0.4)

# Tells me how position should be divided & risk levels
        if (ideal_position_size*float(self.ote)) < portfolio_value:
            print("\nIdeal Position Size: " + str(round(ideal_position_size, 2)))
            time.sleep(1)

            if (v1 + v2 + v3) > ideal_position_size:
                v3 = v3
                print("Position should be split: " + str(v1) + ", " + str(v2) + ", " + str(v3) + " ")

            else:
                print("Position should be split: " + str(v1) + ", " + str(v2) + ", " + str(v3) + " ")


            time.sleep(1)
            print("\nPortfolio Risk from Trade: " + str(trade_risk) + "%")
            time.sleep(1)
            print("Risk in USD: " + "$" + str(round(usd_risk, 2)))

# Calculate Risk Reward
            time.sleep(1)
            total_risk = usd_risk
            total_reward = ((float(self.t1) - float(self.ote)) * v1) + ((float(self.t2) - float(self.ote)) * v2) + ((
                        float(self.t3) - float(self.ote)) * v3)
            risk_reward = (round(total_reward / total_risk, 2))
            print("\nRisk Reward Ratio:  " + "1:" + str(risk_reward))
            print("Return: " + "$" + str(round(total_reward, 2)))

        else:
            print("\nInsufficient funds to open trade")


getSL()

