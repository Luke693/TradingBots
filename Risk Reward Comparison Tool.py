"""
programme will read price data of top 5 stocks for that week from screenshots of website
It will then calculate the risk reward ratio for given portfolio value and optimal trade size for each
Returning the top 3 stocks
"""

from pandas.core.arrays import ExtensionArray
from positionsizer import max_risk
import cv2
import pytesseract
from pytesseract import Output
import csv


#First Choice
#reading image using opencv at same time as converting to greyscale

ticker = "btc"
image = cv2.imread('/Users/lukeashton/Desktop/Screenshot 2020-09-17 at 15.49.49.png', cv2.COLOR_BGR2BGRA)

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
#cv2.imshow('captures text', threshold_img)

# maintain output window until user presses a key
#cv2.waitKey(0)

# Destroying present windows on screen
#cv2.destroyAllWindows()

details = [string for string in details['text'] if string !='']

list = details

t3 = float(list[0].strip("()"))
t2 = float(list[1].strip("()"))
t1 = float(list[2].strip("()"))
ote = float(list[3].strip("()"))
sl = float(list[4].strip("{)"))


#section calculates reward per unit of risk for each of the top 5, creating a list
#It will need to have the ticker next to return as well

cents_at_risk = round((ote - sl), 2)

# calculate ideal position size and risk for trade in USD &
ideal_position_size = (max_risk / cents_at_risk) - 1
usd_risk = (ote - sl) * ideal_position_size

# specifies volumes for trade 1, 2 and 3
v1 = ideal_position_size * 0.2
v2 = ideal_position_size * 0.4
v3 = ideal_position_size * 0.4

if ideal_position_size < (v1 + v2 + v3):
    v3 = v3 - 1

total_reward = ((t1 - ote) * v1) + ((t2 - ote) * v2) + ((t3 - ote) * v3)

reward_for_risk = (round(total_reward / usd_risk, 2))

#Second choice
#reading image using opencv at same time as converting to greyscale

ticker2 = "tdoc"
image2 = cv2.imread('/Users/lukeashton/Desktop/Screenshot 2020-09-18 at 18.37.30.png', cv2.COLOR_BGR2BGRA)

"""""
Converting it to binary image by thresholding 
This step is required if you have a coloured image because if you skip this part
then tesseract wont be able to detect text correctly and this will give incorrect result 
"""

threshold_img2 = cv2.threshold(image2, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# configuring parameters for tesseract
custom_config2 = r'--oem 3 --psm 6'

# now feeding image to tesseract
details2 = pytesseract.image_to_data(threshold_img2, output_type=Output.DICT, lang='eng')

total_boxes2 = len(details2['text'])
for sequence_number in range(total_boxes2):
    if int(details2['conf'][sequence_number]) > 30:
        (x, y, w, h) = (details2['left'][sequence_number], details2['top'][sequence_number], details2['width'][sequence_number], details2['height'][sequence_number])
        threshold_img2 = cv2.rectangle(threshold_img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

# display image
#cv2.imshow('captures text', threshold_img2)

# maintain output window until user presses a key
#cv2.waitKey(0)

# Destroying present windows on screen
#cv2.destroyAllWindows()

#print(details2["text"])

details2 = [string for string in details2['text'] if string !='']

list2 = details2

t3_2= float(list2[0].strip("()"))
t2_2 = float(list2[1].strip("()"))
t1_2 = float(list2[2].strip("()"))
ote_2 = float(list2[3].strip("()"))
sl_2 = float(list2[4].strip("()"))


#section calculates reward per unit of risk for each of the top 5, creating a list
#It will need to have the ticker next to return as well

cents_at_risk2 = round((ote_2 - sl_2), 2)

# calculate ideal position size and risk for trade in USD &
ideal_position_size2 = (max_risk / cents_at_risk2) - 1
usd_risk2 = (ote_2 - sl_2) * ideal_position_size2

# specifies volumes for trade 1, 2 and 3
v1_2 = ideal_position_size2 * 0.2
v2_2 = ideal_position_size2 * 0.4
v3_2 = ideal_position_size2 * 0.4

if ideal_position_size2 < (v1_2 + v2_2 + v3_2):
    v3_2 = v3_2 - 1

total_reward2 = ((t1_2 - ote_2) * v1_2) + ((t2_2 - ote_2) * v2_2) + ((t3_2 - ote_2) * v3_2)

reward_for_risk2 = (round(total_reward2 / usd_risk2, 2))


#Third choice
#reading image using opencv at same time as converting to greyscale

ticker3 = "amzn"
image3 = cv2.imread('/Users/lukeashton/Desktop/Screenshot 2020-09-19 at 15.11.24.png', cv2.COLOR_BGR2BGRA)

"""""
Converting it to binary image by thresholding 
This step is required if you have a coloured image because if you skip this part
then tesseract wont be able to detect text correctly and this will give incorrect result 
"""

threshold_img3 = cv2.threshold(image3, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# configuring parameters for tesseract
custom_config3 = r'--oem 3 --psm 6'

# now feeding image to tesseract
details3 = pytesseract.image_to_data(threshold_img3, output_type=Output.DICT, lang='eng')

total_boxes3 = len(details3['text'])
for sequence_number in range(total_boxes3):
    if int(details3['conf'][sequence_number]) > 30:
        (x, y, w, h) = (details3['left'][sequence_number], details3['top'][sequence_number], details3['width'][sequence_number], details3['height'][sequence_number])
        threshold_img3 = cv2.rectangle(threshold_img3, (x, y), (x + w, y + h), (0, 255, 0), 2)

# display image
#cv2.imshow('captures text', threshold_img3)

# maintain output window until user presses a key
#cv2.waitKey(0)

# Destroying present windows on screen
#cv2.destroyAllWindows()

#print(details3["text"])

details3 = [string for string in details3['text'] if string !='']

list3 = details3


t3_3= float(list3[0].strip("()"))
t2_3 = float(list3[1].strip("()"))
t1_3 = float(list3[2].strip("()"))
ote_3 = float(list3[3].strip("()"))
sl_3 = float(list3[4].strip("()"))


#section calculates reward per unit of risk for each of the top 5, creating a list
#It will need to have the ticker next to return as well

cents_at_risk3 = round((ote_3 - sl_3), 2)

# calculate ideal position size and risk for trade in USD &
ideal_position_size3 = (max_risk / cents_at_risk3) - 1
usd_risk3 = (ote_3 - sl_3) * ideal_position_size3

# specifies volumes for trade 1, 2 and 3
v1_3 = ideal_position_size3 * 0.2
v2_3 = ideal_position_size3 * 0.4
v3_3 = ideal_position_size3 * 0.4

if ideal_position_size3 < (v1_3 + v2_3 + v3_3):
    v3_3 = v3_3 - 1

total_reward3 = ((t1_3 - ote_3) * v1_3) + ((t2_3 - ote_3) * v2_3) + ((t3_3 - ote_3) * v3_3)

reward_for_risk3 = round(total_reward3 / usd_risk3, 2)



#Fourth choice
#reading image using opencv at same time as converting to greyscale

ticker4 = "docu"
image4 = cv2.imread('/Users/lukeashton/Desktop/Screenshot 2020-09-19 at 17.19.31.png', cv2.COLOR_BGR2BGRA)

"""""
Converting it to binary image by thresholding 
This step is required if you have a coloured image because if you skip this part
then tesseract wont be able to detect text correctly and this will give incorrect result 
"""

threshold_img4 = cv2.threshold(image4, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# configuring parameters for tesseract
custom_config4 = r'--oem 3 --psm 6'

# now feeding image to tesseract
details4 = pytesseract.image_to_data(threshold_img4, output_type=Output.DICT, lang='eng')

total_boxes4 = len(details4['text'])
for sequence_number in range(total_boxes4):
    if int(details4['conf'][sequence_number]) > 30:
        (x, y, w, h) = (details4['left'][sequence_number], details4['top'][sequence_number], details4['width'][sequence_number], details4['height'][sequence_number])
        threshold_img4 = cv2.rectangle(threshold_img4, (x, y), (x + w, y + h), (0, 255, 0), 2)

# display image
#cv2.imshow('captures text', threshold_img4)

# maintain output window until user presses a key
#cv2.waitKey(0)

# Destroying present windows on screen
#cv2.destroyAllWindows()

#print(details4["text"])

details4 = [string for string in details4['text'] if string !='']

list4 = details4


t3_4= float(list4[0].strip("()"))
t2_4 = float(list4[1].strip("()"))
t1_4 = float(list4[2].strip("()"))
ote_4 = float(list4[3].strip("()"))
sl_4 = float(list4[4].strip("()"))


#section calculates reward per unit of risk for each of the top 5, creating a list
#It will need to have the ticker next to return as well

cents_at_risk4 = round((ote_4 - sl_4), 2)

# calculate ideal position size and risk for trade in USD &
ideal_position_size4 = (max_risk / cents_at_risk4) - 1
usd_risk4 = (ote_4 - sl_4) * ideal_position_size4

# specifies volumes for trade 1, 2 and 3
v1_4 = ideal_position_size4 * 0.2
v2_4 = ideal_position_size4 * 0.4
v3_4 = ideal_position_size4 * 0.4

if ideal_position_size4 < (v1_4 + v2_4 + v3_4):
    v3_4 = v3_4 - 1

total_reward4 = ((t1_4 - ote_4) * v1_4) + ((t2_4 - ote_4) * v2_4) + ((t3_4 - ote_4) * v3_4)

reward_for_risk4 = round(total_reward4 / usd_risk4, 2)


#Fifth choice
#reading image using opencv at same time as converting to greyscale

ticker5 = "xrp"
image5 = cv2.imread('/Users/lukeashton/Desktop/Screenshot 2020-09-19 at 18.23.54.png', cv2.COLOR_BGR2BGRA)

"""""
Converting it to binary image by thresholding 
This step is required if you have a coloured image because if you skip this part
then tesseract wont be able to detect text correctly and this will give incorrect result 
"""

threshold_img5 = cv2.threshold(image5, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# configuring parameters for tesseract
custom_config5 = r'--oem 3 --psm 6'

# now feeding image to tesseract
details5 = pytesseract.image_to_data(threshold_img5, output_type=Output.DICT, lang='eng')

total_boxes5 = len(details5['text'])
for sequence_number in range(total_boxes5):
    if int(details5['conf'][sequence_number]) > 30:
        (x, y, w, h) = (details5['left'][sequence_number], details5['top'][sequence_number], details5['width'][sequence_number], details5['height'][sequence_number])
        threshold_img5 = cv2.rectangle(threshold_img5, (x, y), (x + w, y + h), (0, 255, 0), 2)

# display image
#cv2.imshow('captures text', threshold_img5)

# maintain output window until user presses a key
#cv2.waitKey(0)

# Destroying present windows on screen
#cv2.destroyAllWindows()

#print(details5["text"])

details5 = [string for string in details5['text'] if string !='']

list5 = details5


t3_5= float(list5[0].strip("()"))
t2_5 = float(list5[1].strip("()"))
t1_5 = float(list5[2].strip("()"))
ote_5 = float(list5[3].strip("()"))
sl_5 = float(list5[4].strip("()"))


#section calculates reward per unit of risk for each of the top 5, creating a list
#It will need to have the ticker next to return as well

cents_at_risk5 = round((ote_5 - sl_5), 2)

# calculate ideal position size and risk for trade in USD &
ideal_position_size5 = (max_risk / cents_at_risk5) - 1
usd_risk5 = (ote_5 - sl_5) * ideal_position_size5

# specifies volumes for trade 1, 2 and 3
v1_5 = ideal_position_size5 * 0.2
v2_5 = ideal_position_size5 * 0.4
v3_5 = ideal_position_size5 * 0.4

if ideal_position_size5 < (v1_5 + v2_5 + v3_5):
    v3_5 = v3_5 - 1


total_reward5 = ((t1_5 - ote_5) * v1_5) + ((t2_5 - ote_5) * v2_5) + ((t3_5 - ote_5) * v3_5)

reward_for_risk5 = round(total_reward5 / usd_risk5, 2)


# Collates risk reward ratios
risk_rewards = [reward_for_risk, reward_for_risk2, reward_for_risk3, reward_for_risk4, reward_for_risk5]

sys.stdin.readline()


result = ticker + ": " + str((risk_rewards[0]))
result2 = ticker2 + ": " + str((risk_rewards[1]))
result3 = ticker3 + ": " + str((risk_rewards[2]))
result4 = ticker4 + ": " + str((risk_rewards[3]))
result5 = ticker5 + ": " + str((risk_rewards[4]))

results = [result, result2, result3, result4, result5]

print(results)


