#Author: Beyonce Radcliffe
#Date Created: May 3, 2022
#Course:ITT103
#Purpose: Calculate Sales Commission of a person. 

print('Calculate Sales  Commission')
print('Please Enter Sales')
Sales=int(input(''))
print('Please Enter SalesID')
SalesID=int(input(''))
print('Please Enter Class')
Class1=int(input('')) 
if Class1 ==1:
 if Sales <=1000:
  print(0.06 * Sales)
elif 1000<Sales<=2000:
 print (0.07 * Sales)
elif Class1==2:
 if Sales <=1000:
  print(0.04 * Sales)
else:
 print (0.06 *Sales)
 if Class1 ==3:
  print(0.045 * Sales)
 else:
  print('ERROR')
    
