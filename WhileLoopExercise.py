# printing descending numbers from the input number to the 1
# without the number 6 if encluded
# not also icluding the zero and the starting number
# zero input must not be taken
num = int(input("please enter a number bigger than 0 ").strip())

pac = num

listt = []
# condition to refuse zero as input
if num == 0:
 print("Number 0 Is Not Larger Than 0")
# adding the descended numbers to a list
else:

 while pac > 1:

  listt.append(pac - 1)

  pac = pac - 1

 # condition  if the number 6 is in the descended numbers
 bigl = [1, 2, 3, 4, 5]

 if len(listt) not in bigl:

  listt.pop(listt.index(6))

 # loop for printing list elements
 index = 0
 while index < len(listt):
     element = listt[index]
     print(element)

     index += 1

 print(f"{len(listt)} Numbers Printed Successfully ")
