from Samples.mapapi_PG import show_map
import sys

lon, lat, spn = input().split(' ')
param1 = f'{lon},{lat}'
param2 = f"&spn={spn},{spn}"
show_map(f'll={param1}{param2}')
#  45.997943 51.538328 0.005
