# I will input order price and SL price, system will pull my portfolio balance, and, keeping risk per position to under
# 2% will return the necessary volumes of my 3 sub positions, and place these into the corresponding individual order
# Functions with the only work then needing to be done being entering target levels
# Programme will then place orders with corresponding order prices, stop losses and target prices for each sub position
# Once the market is closed.

#Position Divider will take inputs and spit corresponding position volumes, as well as OTE, SL, and targets for each
#into the programme

import positionsizer
from positionsizer import max_risk
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from pandas.core.arrays import ExtensionArray
import cv2
import pytesseract
from pytesseract import Output
import csv
import sys
import threading
import time
from TradeManagementSystem import MarketOpen, ordersOnMarket, dailyHigh, getSecondLastSL
# I will manually enter ticker and past

ticker = "atvi"
image = cv2.imread('/Users/lukeashton/Desktop/Screenshot 2020-09-19 at 17.19.31.png', cv2.COLOR_BGR2BGRA)

"""
Converting it to binary image by thresholding 
This step is required if you have a coloured image because if you skip this part
then tesseract won't be able to detect text correctly and this will give incorrect result 
"""

threshold_img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) [1]

# configuring parameters for tesseract
custom_config = r'--oem 3 --psm 6'

# now feeding image to tesseract
details = pytesseract.image_to_data(threshold_img, output_type=Output.DICT, lang='eng')

total_boxes = len(details['text'])
for sequence_number in range(total_boxes):
    if int(details['conf'][sequence_number]) > 30:
        (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number], details['height'][sequence_number])
        threshold_img = cv2.rectangle(threshold_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# display image
#cv2.imShow('captures text', threshold_img)

# maintain output window until user presses a key
#cv2.waitKey(0)

# Destroying present windows on screen
#cv2.destroyAllWindows()

#2 variables below refer to the printed list derived from the jpeg
details = [string for string in details['text'] if string !='']

list = details



# arranges list to match with corresponding price point
t3 = float(list[0].strip("()"))
t2 = float(list[1].strip("()"))
t1 = float(list[2].strip("()"))
ote = float(list[3].strip("()"))
sl = float(list[4].strip("()"))


#Returns trade information from trade class in positionsizer
trade1 = positionsizer.Trade(ticker, t3, t2, t1, ote, sl)
trade1.get_trade_info()

print("Check Order Levels: ", str(sl),  str(ote), str(t1), str(t2), str(t3))

#requires user to hit enter before continuing to place orders
print("Press Enter to Check Connection")
sys.stdin.readline()



cents_at_risk = ote - sl


# calculate ideal position size and risk for trade in USD & % terms
ideal_position_size = (max_risk / cents_at_risk) - 1

# specifies volumes for trade 1, 2 and 3
v1 = round(ideal_position_size * 0.2)
v2 = round(ideal_position_size * 0.4)
v3 = round(ideal_position_size * 0.4)

if ideal_position_size < (v1 + v2 + v3):
    v3 = v3 - 1

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextorderId = orderId
        print("The next valid order ID is: ", self.nextorderId)

    def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print('orderStatus - orderId:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining,
              'lastFillPrice', lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)


def run_loop():
    app.run()


# Function to create Stocks Order contract
def stk_order(symbol):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = "USD"
    return contract


app = IBapi()
app.connect('127.0.0.1', 7497, 123)

app.nextorderId = None

# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

# Check if the API is connected via orderId
while True:
    if isinstance(app.nextorderId, int):
        print('connected')
        break
    else:
        print('waiting for connection')
        time.sleep(1)

#requires user to hit enter before continuing to place order
print("Press Enter to Place Orders")
sys.stdin.readline()

#create object for order
parent = Order()
parent.orderId = app.nextorderId
parent.action = 'BUY'
parent.totalQuantity = ideal_position_size
parent.orderType = 'LMT'
parent.lmtPrice = ote
parent.transmit = False

# Create stop loss order object
stop_order = Order()
stop_order.orderId = app.nextorderId + 1
stop_order.action = 'SELL'
stop_order.totalQuantity = ideal_position_size
stop_order.orderType = 'STP'
stop_order.auxPrice = sl
stop_order.ParentId = parent.orderId
stop_order.transmit = False

# Create take profit order object
tp_order = Order()
tp_order.orderId = app.nextorderId + 2
tp_order.action = 'SELL'
tp_order.totalQuantity = v1
tp_order.orderType = 'LMT'
tp_order.lmtPrice = t1
tp_order.ParentId = parent.orderId
tp_order.transmit = False

# Create take profit order object 2
tp_order1 = Order()
tp_order1.orderId = app.nextorderId + 3
tp_order1.action = 'SELL'
tp_order1.totalQuantity = v2
tp_order1.orderType = 'LMT'
tp_order1.lmtPrice = t2
tp_order1.ParentId = parent.orderId
tp_order1.transmit = False

# Create take profit order object 3
tp_order2 = Order()
tp_order2.orderId = app.nextorderId + 4
tp_order2.action = 'SELL'
tp_order2.totalQuantity = v3
tp_order2.orderType = 'LMT'
tp_order2.lmtPrice = t3
tp_order2.ParentId = parent.orderId
tp_order2.transmit = False

# Place orders
app.placeOrder(parent.orderId, stk_order(ticker), parent)
app.placeOrder(stop_order.orderId, stk_order(ticker), stop_order)
app.placeOrder(tp_order.orderId, stk_order(ticker), tp_order)
app.placeOrder(tp_order1.orderId, stk_order(ticker), tp_order1)
app.placeOrder(tp_order2.orderId, stk_order(ticker), tp_order2)

#Cancel order
#print('cancelling order')
#app.cancelOrder(app.nextOrderId)

time.sleep(3)
app.disconnect()


datafile = open("t1.txt", "w+")
datafile.write(t1)
datafile.close()

datafile = open("ticker.txt", "w+")
datafile.write(ticker)
datafile.close()

datafile = open("IPS.txt", "w+")
datafile.write(ideal_position_size)
datafile.close()
