# Python Code Examples

## While Loop

The following Python script demonstrates the use of a `while` loop. It repeatedly prompts the user to enter a number until the entered number is greater than 50.

```python
i = int(input('Enter the Number: '))
while i <= 50:
    i = int(input('Enter the Number: '))
    print(i)
print("Done with the loop")
``` 
### How to Use:

- Run the script.
- Enter a number.
- The script will prompt you to enter a number until the entered number is greater than 50.
- The loop will terminate, and "Done with the loop" will be printed.
#



## If Else

The following Python script demonstrates the use of _if_, _elif_, and _else_ statements. It checks the value of a number and prints a corresponding message. If the enterd number is less than or equal to 100 then they print "This is "IF" statement". Also the number is equal to 150 then, print "This is "ELIF" statement". If the both of conditions false, print "This is "ELSE" statement"

```python
a = int(input('Enter the number: '))
if a <= 100:
    print('This is "IF" statement')
elif a == 150:
    print('This is "ELIF" statement')
else:
    print('This is "ELSE" statement')
print(a)
```

### How to Use:

- Run the script.
- Enter a number.
- The script will evaluate the entered number and print the corresponding message.
#


## Try Except

The following Python script demonstrates the use of try and except blocks. It generates the multiplication table for a given number.

``` python
a = int(input('Enter the number: '))
print(f'Multiplication table of {a} is:')

try:
    for i in range(1, 11):
        print(f'{int(a)} X {i} = {int(a*i)}')
except:
    print('An error occurred')
print('This text is for testing purposes')
```

### How to Use:

- Run the script.
- Enter a number.
- The script will display the multiplication table for the entered number.
- If an error occurs, the script will print an error message.
- The final line is a test message.


