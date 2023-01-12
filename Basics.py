##  USEFUL FUNCTIONS -----------------------------------------------------------
type() # check data type (boolean, integer, floating, string)

print('x = ', y + 1) # same as print in R. Another complicated example: print("x and its type:  ", x, type(x))

len() # like length in R e.g., number of chars in a word; number of items in list

sum([1,2,3])


## LOGICAL OPPERATORS ----------------------------------------------------------
drink = "Coffee"                                # one example
if (drink == "Coffee") or (drink == "Tea"):
    print("you drink:", drink)

quit = False                                    # another example
if quit == True:
    print("\t block True")
else:
    print("\t block False")
    print("\t end ")
    print("----------")


## OTHER TIPS ------------------------------------------------------------------
x, y = y, x # swap the values of two variables

name = 'president'
print(name[0]) # just the first letter, p. Could also do [-1] for last letter, or [0:5] for first five letters

item_one = 1; item_two = 2; item_three = 3 # using "," for multiple items on one line 
total = item_one + \                       # using "\" for having one statment across multiple lines
        item_two + \
        item_three
total 


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



