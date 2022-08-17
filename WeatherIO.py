import requests
import json
import pandas as pd

#handles get request calls to RestAPI
def get_BuildA(url, auth):
  r = requests.get(url, headers={'Token': auth})
  print('Request Code: ' + str(r.status_code) + '\n\n')
  q = r.json()
  
  records = (q['results'])
  
  print('Record count: ' + str(len(records)) + '\n\n')
  
  for i in range(len(records)):
    print('Elevation: ', records[i]['elevation'],'\n',
    'Latitude: ', records[i]['latitude'], '\n',
    'Longitude: ', records[i]['longitude'], '\n',
    'Name: ', records[i]['name'], '\n')
    
#handles user input, defined parameters, and Oauth2 token
auth = str(input('Enter your NOAA auth token: '))


while True:
  zp_code = input('Enter Zip Code: ')
  url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=ZIP:' + zp_code
  print(url)
  get_BuildA(url, auth)
