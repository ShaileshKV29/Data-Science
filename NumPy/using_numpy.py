import numpy as np
hp = [61,62,65,63,67]
wp = [100, 200, 160, 180, 123]
array_hp = np.array(hp)
array_wp = np.array(wp)
hp_m = array_hp*0.0254
wp_m = array_wp*0.4535
bmi = hp_m/wp_m
print(bmi)
