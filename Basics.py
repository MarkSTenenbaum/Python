##  USEFUL FUNCTIONS -----------------------------------------------------------
type() # check data type (boolean, integer, floating, string)

print('x = ', y + 1) # same as print in R. Another complicated example: print("x and its type:  ", x, type(x))

len() # like length in R e.g., number of chars in a word; number of items in list

sum([1,2,3])

str(); int; float() # changing type of variable

input() # function to prompt user to type something

## STATEMENTS ------------------------------------------------------------------
x%2 # gives remainder, e.g if x = 10, remainder is 0; if x%4, remainder 2
7//3 # gives number of times 3 goes into 7, e.g., in this case 3
2**6 # same as ^ in R. expenential power

## LOGICAL OPPERATORS ----------------------------------------------------------
drink = "Coffee"                                # one example
if (drink == "Coffee") or (drink == "Tea"):
    print("you drink:", drink)
    
x = -5                                           # another example
if x > 0: 
    print("positive") 
elif x==0: 
    print("zero")
else:
    print("negative")

x = 3                                            # nested if statement
if x > 0:
    if (x%2 == 0): #
        print("   positive even ")
    else:
      print('   positive odd')
else:
    print(" not positive")

## LOOPS ----------------------------------------------------------------------
# While loop
while True:
    a = int(input('type an integer')).    # asking respondnets to give dimensions for triange, and saying whether it is valid triange
    b = int(input('type an integer'))
    c = int(input('type an integer'))

    if (a+b > c) and (c + a > b) and (b + c > a):
        print('Valid triange')
    else:
        print('Not valid triange')
        
    play = input('Play again (y/n)')
    if play == 'n':
            break

print('good bye.')

# For loop
count = 0 

for year in range(1900, 2021, 4): 
    if (year%4 == 0 and year%100 != 0 ) or (year%400 == 0):
        count +=1 
print(count)   

# Big loop creating Feb calendar
daysOfTheWeek = 'Sun  Mon  Tue  Wed  Thu  Fri  Sat'

print('          February 2023')
print('Sun  Mon  Tue  Wed  Thu  Fri  Sat')

for d in range(1, 29):
    if (d == 1):                              # getting the "1" correct"
        for x in range(0, len(daysOfTheWeek)):
            if (daysOfTheWeek[x] == 'd'):
                print(d, end = '')
                break
            else:
                print(' ', end = '')
    elif (d < 5):                            # 2-4
        print(f'{d:5}', end = '')
    else:                                    # one digit numbers
        if (len(str(d)) == 1):
            print(' ', d, end = '  ')
        else:                               # two-digit numbers
            print('', d, end = '  ')
    if ((d-4) % 7) == 0:                    # move net line
            print()


## OTHER TIPS ------------------------------------------------------------------
x, y = y, x # swap the values of two variables

name = 'president'
print(name[0]) # just the first letter, p. Could also do [-1] for last letter, or [0:5] for first five letters

item_one = 1; item_two = 2; item_three = 3 # using "," for multiple items on one line 
total = item_one + \                       # using "\" for having one statment across multiple lines
        item_two + \
        item_three
total 

for row in range (1,11): # creating 10x10 multiplication table
    for col in range (1,11):
        print(f'{row*col:3}', end =' ') # custom string fields
    print() # separate rows

## KEYBORD SHORTCUTS
# CTRL + /  comment
# CTRL + "]" one-tab right
# CTRL + "[" one-tab right

## ESSENTIAL LIBRARIES ---------------------------------------------------------
# NumPy: It provides the data structures, algorithms, and library glue needed for most scientific applications involving numerical data in Python
# pandas: provides high-level data structures and functions designed to make working with structured or tabular data fast, easy, and expressive. Uses dataframe and arrays. 
# matplotlib: most popular library for producing 2D data vizualizations. 

## INSTALLING PACKAGES ---------------------------------------------------------
pip install package_name # installing package
pip install --upgrade package_name # upgrading packages



