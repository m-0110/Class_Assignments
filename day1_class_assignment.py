'''
PROGRAM DESCRIPTION:
Given a 4 -digit number
return True if it gives 6174(kaprekar constant) else False

PROGRAMMED BY: Modika Ishwarya
DATE:17-09-2021
PYTHON VERSION:3.8
CAVEATS:None
LICENSE:None
'''


def kaprekar_constant(a):
    if(a==6174):
        return True
    else:
        #get the greatest and smallest number formed  from given number

        num=str(a)
        num=list(num)
        num.sort()
        l1=int(''.join(num))
        l2=int(''.join(num[::-1]))

        #if greatest and smallest are equal l1-l2 will be 0 and they do not give 6174 at all
        if(l1==l2):
            return False

        #else call the function again with difference of both l1 and l2
        else:
            return kaprekar_constant(abs(l1 - l2))

l=int(input("enter number:"))
print(kaprekar_constant(l))


# if input is 1111 ,2222 ,3333 output is False(if all digits are same  ,then the number wont give 6174)
# if input is 5234 output is True