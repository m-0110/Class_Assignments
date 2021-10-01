'''
PROGRAM DESCRIPTION:
Send request to api  using requests module and get response
and get breed_group and their image urls
'''


#PROGRAMMED BY: Modika Ishwarya
#DATE:21-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None


import requests
import json


class test:

    def check_url(self, url):
        try:
            response = requests.get(url)
            return True
        except:
            return False

    def read_url(self, url):
        url = requests.get(url)
        return url.text

    def return_json(self, url):

        response = requests.get(url)
        if(response.status_code==200):

            print(' request is successful\n ')
            # response.json() method to see the data we received back from the API in json format
            return response.json()
        else:
            return -1


url = "https://api.thedogapi.com/v1/breeds"

s = test()

if(s.check_url(url)):
    json_response= s.return_json(url) # get response as json

    if(json_response!=-1):# if request is successful

        breed_image={}#dictionary with breed_group as key and image_urls as values

        for i in json_response:
            if('breed_group' in i):
                if(i['breed_group'] not in breed_image ): # if key not exists before create empty add key with empty list
                    breed_image[i['breed_group']] = []

                #if image and url exists for breed_group append it to corresponding list
                if('image' in i and 'url' in i['image']):
                    breed_image[i['breed_group']].append(i['image']['url'])

        #Now print breed_group with its image urls
        print('----breed_group with its image urls----')
        for i in breed_image:
            print("breed_group:",i)# print the breed_group name

            print("image urls of '{}' : ".format(i))
            print()
            #print image urls
            k=1
            for j in breed_image[i]:
                print("{}. {}".format(k,j))
                k+=1# for numbering image url
            print('____________________________________')


#on execution output will be

'''
 request is successful
 
----breed_group with its image urls----
breed_group: Toy
image urls of 'Toy' : 

1. https://cdn2.thedogapi.com/images/BJa4kxc4X.jpg
2. https://cdn2.thedogapi.com/images/HJRBbe94Q.jpg
3. https://cdn2.thedogapi.com/images/B1pDZx9Nm.jpg
4. https://cdn2.thedogapi.com/images/SkIgzxqNQ.jpg
5. https://cdn2.thedogapi.com/images/rkXiGl9V7.jpg
6. https://cdn2.thedogapi.com/images/SJAnzg9NX.jpg
7. https://cdn2.thedogapi.com/images/r1H6feqEm.jpg
8. https://cdn2.thedogapi.com/images/B1SV7gqN7.jpg
9. https://cdn2.thedogapi.com/images/Hy3H7g94X.jpg
10. https://cdn2.thedogapi.com/images/SkJj7e547.jpg
11. https://cdn2.thedogapi.com/images/ByIiml9Nm.jpg
12. https://cdn2.thedogapi.com/images/HJd0XecNX.jpg
13. https://cdn2.thedogapi.com/images/HyJvcl9N7.jpg
14. https://cdn2.thedogapi.com/images/HkP7Vxc4Q.jpg
15. https://cdn2.thedogapi.com/images/BkrJjgcV7.jpg
16. https://cdn2.thedogapi.com/images/ByzGsl5Nm.jpg
17. https://cdn2.thedogapi.com/images/B17ase9V7.jpg
18. https://cdn2.thedogapi.com/images/B12BnxcVQ.jpg
____________________________________
breed_group: Hound
image urls of 'Hound' : 

1. https://cdn2.thedogapi.com/images/hMyT4CDXR.jpg
2. https://cdn2.thedogapi.com/images/S14n1x9NQ.jpg
3. https://cdn2.thedogapi.com/images/SkvZgx94m.jpg
4. https://cdn2.thedogapi.com/images/H1dGlxqNQ.jpg
5. https://cdn2.thedogapi.com/images/BkMQll94X.jpg
6. https://cdn2.thedogapi.com/images/Sy57xx9EX.jpg
7. https://cdn2.thedogapi.com/images/Syd4xxqEm.jpg
8. https://cdn2.thedogapi.com/images/HJAFgxcNQ.jpg
9. https://cdn2.thedogapi.com/images/Skdcgx9VX.jpg
10. https://cdn2.thedogapi.com/images/rJxieg9VQ.jpg
11. https://cdn2.thedogapi.com/images/ryNYMx94X.jpg
12. https://cdn2.thedogapi.com/images/B1IcfgqE7.jpg
13. https://cdn2.thedogapi.com/images/Hyd2zgcEX.jpg
14. https://cdn2.thedogapi.com/images/Byz6mgqEQ.jpg
15. https://cdn2.thedogapi.com/images/B1i67l5VQ.jpg
16. https://cdn2.thedogapi.com/images/HJMzEl5N7.jpg
17. https://cdn2.thedogapi.com/images/By9zNgqE7.jpg
18. https://cdn2.thedogapi.com/images/fjFIuehNo.jpg
19. https://cdn2.thedogapi.com/images/SkNjqx9NQ.jpg
20. https://cdn2.thedogapi.com/images/zv89hR-O8.jpg
21. https://cdn2.thedogapi.com/images/SkRpsgc47.jpg
22. https://cdn2.thedogapi.com/images/Hyv-ne94m.jpg
____________________________________

.
.
.
.
.
'''


