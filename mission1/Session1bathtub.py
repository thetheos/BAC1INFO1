import math

volume_leak = 1 #liter per minute
volume_add = 12 #liter per minute
filled_time = 80/11 #time in minute
water_vol = 0

for i in range(0, math.ceil(filled_time)):
    water_vol += volume_add
    water_vol -= volume_leak


print(water_vol, "\t", math.ceil(filled_time) , "\t", filled_time)