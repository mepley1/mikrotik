#!/usr/bin/python3
# https://docs.python.org/3/library/ipaddress.html
# ^^ pip3 install ipaddress
# -----------------------------
# Convert IPv6 address to hex format used in older RouterOS versions
# In newer versions you can use standard IPv6 syntax and don't need to do this

import ipaddress
ip = input('Enter IPv6: ')
ip = ipaddress.IPv6Address(ip).exploded
print(ip)
iphex = ip.replace(':', '')
print('0x'+iphex)
