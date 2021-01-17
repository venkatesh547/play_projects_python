# % of gain calculator in Stocks 

import math

f_num = int(input('Enter Current Price: '))
s_num = int(input('Enter Target Price: '))

res = ((f_num-s_num)/f_num)*100

print('It\'s '+"{}" '% gain'.format(math.fabs(res)) if res < 0 else "{}".format(res))

