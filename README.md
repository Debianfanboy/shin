# Shin Language

> A basic toy programming language written in python and inspired by python and BASIC.

[![forthebadgemade-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Installing

### Pre-requisites:
  You need `python3` and `git` installed on your system.

```bash
git clone https://github.com/Sarthak2143/shin
cd shin/
python3 -m shin
```

## Initialising
  You've installed shin shell already by using the commands above. Now you have shell mode so you can do arithmetic calculations in the shell itself.

**For example:**

```py
shin >>> 2 + 2
Output: 4

shin >>> 75 - 6
Output: 69

shin >>> 33*3
Output: 99

shin >>> 100/10
Output: 10

shin >>> 2^3
Output: 8
```

> `**` is replaced by `^` for power.

  Now, for script you can use the extension `.shin` for saving files and run with below command.

```
shin >>> run("<file_name>.shin")
```

---

# Documentation

> Below is the official documentation of the language.

**Note:**
You can run single line code in shell mode too.

## Arithmetic Operators:

1. `+` : It'll add the variable or integer.
2. `-` : It'll subtract the integers.
3. `*` : It'll multiply the integers
4. `/` : It'll divide the integer(s).
5. `^` : It's for power function. Eg: 2^3 = 8

## Comments

```py
# This is a comment.
# It's simlar to python
```

> Shin lang only supports **single line comments** as of now.

## Printing

```py
print("Hello World!")

print("Its similar to python but just a capitalised version.")

let myVar = "Variable"

print(myVar)

print(2+3)

```

> Only double quotes e.g `""` are supported.


## Variables

```py
let myVariable = "Hello World"
let myInteger = 0123
let myBool = TRUE # It'll take TRUE as 1
```

For making or setting a value to a variable you've to use the `let` keyword.

The data is mutuable also i.e you can change the value of variables anytime.

```py
shin >>> let Str = "Data"
shin >>> Str
shin >>> "Data"
shin >>> let Str = "It's mutuable"
shin >>> Str
shin >>> "It's mutuable"
```

Suported Data types -> Strings, Integers and Boolean.

## Data types

Shin lang supports Strings, Integers, Flloats and Boolean as data.

### Strings

String is a “string of characters” or in programming terms, an array of characters. A string is generally not a single object, but rather an array of characters that make up the text.

#### Escape character

`\\` -> This is a backslash and it's called escape as it escape some character specified.

Supported:

1. Quotes -> `\"`
2. Backlash -> `\\`
3. New line -> `\n`

```shin
"Text with \"quotes\""
"Text with backslash \\"
"Text \n in new \line."
```


### Integers

An integer, in the context of computer programming, is a data type used to represent real numbers that do not have fractional values. ... For example, a short integer in many common programming languages is limited to a range of between 32,767 and -32,768.

### Floating

In programming, a floating-point or float is a variable type that is used to store floating-point number values. A floating-point number is one where the position of the decimal point can "float" rather than being in a fixed position within a number. Examples of floating-point numbers are 1.23, 87.425, and 9039454.2.

### Boolean

In computer science, a boolean or bool is a data type with two possible values: true or false. ... When referring to the data type in computer programming, the word "boolean" is properly spelled with a lowercase b.

In shin, `TRUE` is simplified as `1` and `FALSE` is simplified as `0`, That's how it's in low level languages.

---

## Comparisons and Logical operator

### Comparison operator:

1. `==` : Checks if the value of variable is satisfied or not. If yes then it will do the <expression> if not it'll be `False` or will continue to next <condition>

2. `!=` : Checks if the value of variable is satisfied or not. If no then it will do the <expression> if not it'll be `False` or will continue to next <condition>

3. `>=` : Checks if the variables are equal or its greater than the other one.

4. `<=` : Checks if the variables are equal or its lesser than the other one.

### Logical operators:

1. `and` : It'll print True if both condition are True and False if one of them is False.

2. `or` : It'll print True if one of the conditions is correct.

3. `not` : It'll print `True` incase of False condition and `False` incase of True condition.

---
## Functions

> Functions are "self contained" modules of code that accomplish a specific task. Functions usually "take in" data, process it, and "return" a result. Once a function is written, it can be used over and over and over again.

_Types of functions supported:_
**1. Short hand functions**
**2. Traditional functions**
**3. Anonymous functions**

*Short hand functions*
```shin
func <func_name>(arguments) -> statement(s)
```

*Traditional functions*

```py
func function_name(arguments)
    statement(s)
end # For ending the function
```

An example of using functions:

```py
func myFunc(name)
    let new_name = "Mr./Ms./Mrs." + name
    return new_name
myFunc(John)
```

The `return` keyword is used for returning the value of a variable.

```
Output: Mr./Ms./Mrs. John
```

*Anonymous functions*

An anonymous function is a function that is not stored in a program file, but is associated with a variable whose data type is function_handle. Anonymous functions can accept multiple inputs and return one output.

Syntax:
```shin
func(params) -> <expression>
```

**For example:**

```py
let func_name = func(a) -> a + 6
func_name(3)

```

`Output: 9`

### Note
> You can assign a function to variable too.

**For example**

```py
func oop(str) -> str + "oop"
var myFunc = oop
myFunc("P")
```

```
Output: "Poop"
```


---
## Conditions

**Conditions supoorted: ** -> IF, ELIF(ELSE IF) AND ELSE

### IF statement

```py
if<condition> then <expression>
```

**For example:**

Below is the program that checks if the number is 69.

```py
let num = 69
if num == 69 then print("yes")
```

### IF/ELSE statement

```py
if <condition> then <expression> else <expression>
```

**For example:**

Below is a program that checks if a number is 2 or not.

```py
let num = 2
if num == then print("Yes it's 2") else print("No it's not 2")
let num1 = 3
if num1 == 2 then print("Yes it's 2") else print("No it's not 2")
```

```
Output:
"Yes it's two"
"No it's not 2"
```

### if/elif/else statement

```py
if <condition> then <expression> elif <condition> then <expression> else <expression>
```

## While statement

_Types of WHILE statement:_

**1. Short Hand WHILE statement**
**2. Traditional WHILE statement**

_Short Hand WHILE statement_

```py
while <condition> then <expression>
```

_Traditional WHILE statement_

```py
while <condition> then
    <statement>
end
```

**For example:**

```py
while 1 then
    print("Yes")
end
```
The above program will keep printing "Yes" because it's **TRUE**.

## for statement

**Short Hand `for` statement**

```py
for <var_name> = <start_value> to <end_value> then <expression>
```

__For example:__

```py
let result = 1
for i = 1 to 6 then let result = result*i
print(result)
```

```
Output: 120
```

**Normal `for` statement**

```py
for <condition> or <increment> then
    <statement(s)>
end
```


```
<increment> = <var_name> = <start_value> to <end_value>
```

### STEP in FOR statement

`step` keyword is for changing the increment value.

**For example:**

```py
for i = 0 to 11 step 2 then ....
```

The above block of code will take numbers from 0 to 11 with a increment value of 2, so the numbers should be 0,2,4,6,8,10.

`step` values can be negative too i.e STEP -n

## Lists

List is the most versatile data type available in functional programming languages used to store a collection of similar data items. The concept is similar to arrays in object-oriented programming. List items can be written in a square bracket separated by commas.

**Creating a empty list**

```py
[]
```
It'll create a empty list, you can assign a name to a list.

```py
let myList = []
```

**Creating a list with elements**

```py
shin >>> let myList = [1,2,3]
shin >>> [1,2,3]
```

**Adding elements in a list**

Element can be added by `+` operator.

```py
shin >>> let myList = [1,2,3]
shin >>> [1,2,3]
shin >>> myList + 4
shin >>> [1,2,3,4]
```

A list can be added as an element too aka **list concatenation.**

```py
shin >>> let myList = [1,2,3]
shin >>> [1,2,3]
shin >>> let newList = [4,5,6]
shin > [1,2,3,[4,5,6]]
```

**Combining two lists**

Two lists can be combined by `*` operator.

```py
shin >>> let myList = [1,2,3]
shin >>> [1,2,3]
shin >>> let newList = [4,5,6]
shin >>> [4,5,6]
shin >>> myList * newList
shin >>> [1,2,3,4,5,6]
```

**Removing elements**

Elements can be removed by their index number.
Elements can be removed by `<list_name> - <index>`.

Index number starts from 0.
Negative index number starts from -1.

```py
shin >>> let myList = [1,2,3,4]
shin >>> [1,2,3,4]
shin >>> myList - 0
shin >>> [2,3,4]
shin >>> myList - 1
shin >>> [2,4]
shin >>> myList - -1
shin >>> [2]
```

In the above block of code, first `1` is removed as it's index number is 0. Then, `3` is removed as it's index number is 1. Then, `4` is removed as it's index number is -1.

**Printing elements**

Elements can be printed by their index number.

`<list_name>/index`

```py
shin >>> let myList = [1,2,3,4,5,6]
shin >>> [1,2,3,4,5,6]
shin >>> myList/0
shin >>> 1
shin >>>  myList/3
shin >>> 4
shin >>> myList/-2
shin >>> 5
```

### APPEND function

It'll add elements in a pre-defined list.

```py
shin >>> let <list_name> = []
shin >>> append(<list_name, <element>)
```

**For example:**

```py
shin >>> let myList = [1,2,3]
shin >>> [1,2,3]
shin >>> append(myList, 4)
shin >>> [1,2,3,4]
```

You can add lists as an element too.

```py
shin >>> let myList = [1,2,3]
shin >>> [1,2,3]
shin >>> append(myList, [4,5,6])
shin >>> [1,2,3,[4,5,6]]
```

### POP function

It removes an element from a list by it's index number.

```py
shin >>> let <list_name> = []
shin >>> pop(<list_name>, <index>)
```

**For example:**
```py
shin >>> let list = [1,2,3,4]
shin >>> pop(list, 3)
shin >>> list
shin >>> [1,2,3]
```

It removed 4 as it's index number is 3.

Negative indexing can be also used.

### EXTEND() function

In shin lang, EXTEND is the operation for concatenating linked lists.

Basically elements of 2nd list is joint in 1st list

```py
shin >>> let <list1> = []
shin >>> let <list2> = []
shin >>> extend(<list1>, <list2>)
```

**For example:**

```py
shin >>> let list1 = [2,4,89]
shin >>> let list2 = [23,78,99]
shin >>> extend(list1, list2)
shin >>> list1
shin >>> [2,4,89,23,78]
```

### LEN() function

It prints the length of a list.

Usage:
```py
shin >>> let <list_name> = []
shin >>> let(<list_name>)
```

**For example:**

```py
shin >>> let myList = [1,2,3,3,5]
shin >>> len(myList)
shin >>> 5
```

__

## Built in functions

A function that is built into an application and can be accessed by end-users. For example, most spreadsheet applications support a built-in SUM function that adds up all cells in a row or column.

### math_pi

Prints the value of Pi/π.

```py
shin >>> math_pi
shin >>> 3.141592653589793
```

### input statement

An input/output statement or I/O statement is a portion of a program that instructs a computer how to read and process information. It pertains to gather information from an input device, or sending information to an output device.

> It only supports Strings, For integer see INPUT_INT

```py
shin >>> let <var_name> = input()
```

The above block of code will assign a value to the variable that is entered by user.

```py
shin >>> let name = input()
John Doe
shin >>> "John Doe"
```

### input_int statement

It's pyally the same keyword as above but it's for integers.

```py
shin >>> let <var_name> = input_int()
```

The above block of code will assign an integer to the variable that is entered by user.

```py
shin >>> var myAge = input_int()
69
shin >>> 69
```

Erorr if the taken input isn't an integer.

```py
shin >>> let <var_name> = input_int()
Text
"Text" must be an integer, Try again!
69
shin >>> 69
```

### clear() and cls()

It'll clear the screen.

```py
shin >>> cls() #for windows nt
shin >>> clear() # for mac and linux
```

### is_num()

It'll check if the given data is an integer or not.

```py
shin >>> is_num(69)
shin >>> 1
shin >>> is_num("String")
shin >>> 0
shin >>> is_num([])
shin >>> 0
```

As specified earlier, 1 is TRUE and 0 is FALSE.

### is_str()

It'll check if the given data is a string or not.

```py
shin >>> is_str("HEY")
shin >>> 1
shin >>> is_str(69)
shin >>> 0
shin >>> is_str([])
shin >>> 0
```

### is_list()

It'll check if the given data is a list or not.

```py
shin >>> is_list([])
shin >>> 1
shin >>> let myList = [1,2,3]
shin >>> [1,2,3]
shin >>> is_list(myList)
shin >>> 1
shin >>> is_list(23)
shin >>> 0
```

### is_func()

It'll check if the given data is a function or not, it works on built in function and defined function both.

```py
shin >>> is_func(print)
shin >>> 1
shin >>> func oop() -> print("oop")
shin >>> is_func(oop)
shin >>> 1
shin >>> is_func(23)
shin >>> 0
```

> Thanks, for coming till here.

# To-Do

- [x] Make a language
- [x] Upload on GitHub
- [x] Make documentation
- [x] Brushing the language
- [x] Adding examples for programs
- [ ] Adding more built-in functions
- [ ] Make a website
- [ ] Make a package manager(maybe not)
