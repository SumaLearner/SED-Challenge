from itertools import groupby
import re

pattern1 = r'([456]\d{3}(-?\d{4}){3}$|\d{16}'
card_num = '5644-5567-7878-1121'

#def repetition(card_num):
#    return max(len(list(g)) for _, g in groupby(card_num)

if re.match( pattern1, card_num):
    print("hyphen and string length are correct")
    num = card_num.replace('-', '')
    if max(len(list(g)) for _, g in groupby(num)) >= 4:
       print('more than 4 repetiotions... number Invalid')
    else:
       print('Valid')
else:
    print("Invalid. Pattern matching failed")
