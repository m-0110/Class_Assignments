'''
PROGRAM DESCRIPTION:
Send request to api  using requests module and get response search for name- Afghan Hound and if exists print details
'''


#PROGRAMMED BY: Modika Ishwarya
#DATE:20-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None



import requests
import json


class test:
    
    #check the url exists or not
    def check_url(self, url):
        try:
            url = requests.get(url)
            return True
        except:
            return False

    def read_url(self, url):
        response = requests.get(url)
        return response.text

    # returning the json response for the request sent to api
    def return_json(self,url):

        response = requests.get(url)

        #checking response is successful or not
        if(response.status_code==200):
            print('request is successful')
        return response.json()


url = "https://api.thedogapi.com/v1/breeds"

s = test()

#print(s.read_url(url))

#check url exists or not
if(s.check_url(url)):

    #get json response
    json_response = s.return_json(url)
    for i in json_response:
        if(i['name']=='Afghan Hound'):
            print('name exists')
            print('--details of {} --'.format(i['name']))
            print()
            for details in i:
                print("{}:{}".format(details,i[details]))
            break
else:
    print('not present')

#output on execution

'''

request is successful
name exists
--details of Afghan Hound --

weight:{'imperial': '50 - 60', 'metric': '23 - 27'}
height:{'imperial': '25 - 27', 'metric': '64 - 69'}
id:2
name:Afghan Hound
country_code:AG
bred_for:Coursing and hunting
breed_group:Hound
life_span:10 - 13 years
temperament:Aloof, Clownish, Dignified, Independent, Happy
origin:Afghanistan, Iran, Pakistan
reference_image_id:hMyT4CDXR
image:{'id': 'hMyT4CDXR', 'width': 606, 'height': 380, 'url': 'https://cdn2.thedogapi.com/images/hMyT4CDXR.jpg'}



'''

