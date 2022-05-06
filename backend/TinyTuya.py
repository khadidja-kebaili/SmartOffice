# Zum Ausprobieren:

import tinytuya
d = tinytuya.OutletDevice('bf1562e54d66eccf59oq7t',
                          '192.168.2.106', '1877eea950b2d4ff')

d.set_version(3.3)
'''d_status = d.status()
print(d_status)'''

#d.set_value(2, 90)
d.set_value(1,'open')
