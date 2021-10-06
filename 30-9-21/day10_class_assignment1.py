'''
PROGRAM DESCRIPTION:
FIND
GEOMETRIC MEAN
HARMONIC MEAN

'''


#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:30-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None



class Progression:
    #finding geometric mean
    def geometric_mean(self,data):
        n=len(data)#number of elements
        product=1
        for i in data:
            #multiply all elements
            product=i*product

        # round to two decimal places
        return round((product)**(1/n),2)

    def harmonic_mean(self,data):
        n=len(data)
        sum=0
        for i in data:
            #sum reciprocals of elements
            sum=sum+(1/i)

        # round to two decimal places
        return round(n/sum,2)


p=Progression()
data=[1,2,3,4,5]
print("geometric mean ",p.geometric_mean(data))
print("harmonic mean",p.harmonic_mean(data))
