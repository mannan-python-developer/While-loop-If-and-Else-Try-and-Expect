###############################  While loop  ############################

i = int(input('Enter the Number: '))
while(i <= 50):
    i = int(input('Enter the Number: '))
    print(i)
print("Done with the loop")



###############################  If Else  ################################

a = int(input('Enter the number: '))
if(a <= 100):
    print('This is "IF" statment')
elif(a == 150):
    print('This is "ELIF" statment')
else:
    print('This is "ELSE" statment')

print(a)



##############################  Try Expect  ###############################

a = int(input('Enter the number: '))
print(f'Multipicaton table of {a} is:')

try:
  for i in range(1,11):
     print(f'{int(a)} X {i} = {int(a*i)}')
except:
   print('error occer')

print('This text for test')

