
'''
PROGRAM DESCRIPTION :
FIND VARIANCE  OF A POPULATION

'''

#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:21-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None

class stat:
    #finding mean
    def dsmean(self, data):
        res_list = []
        sum = 0
        n = len(data)
        #the elements must be of type int or float
        if (all([True if (isinstance(i, int) or isinstance(i, float)) else (False) for i in data])):

            for i in range(0, len(data)):

                sum = sum + data[i]

            # round to two decimal places
            return round(sum/n,2)

    #finding variance
    def variance(self,data):
        #find mean
        mean=self.dsmean(data)
        square_diff_sum=0
        n=len(data)
        for x in data:
            #find x-mean and add up and find avg
            square_diff_sum= square_diff_sum + (x - mean) * (x - mean)

        #round to two decimal places
        return round(square_diff_sum / n, 2)


p=stat()
#find variance
print('variance is ',p.variance([1,2,3,4]))

