# Shin Language
> A basic programming language written in python and inspired by python and BASIC.

## Downloading

### Pre requisite:
  You need `python3` and `git` installed on your system.

```bash
git clone https://github.com/Sarthak2143/shin
cd shin/
python3 shell.py 
```

## Initialising
  You've shin shell already by using above commands. Now you have shell mode so you can do arithmetic calculations in the shell itself.
  
**For example: **

```shin
shin > 2 + 2 
Output: 4 

shin > 75 - 6
Output: 69

shin > 33*3 
Output: 99

shin > 100/10 
Output: 10

shin > 2^3
Output: 8
```

  Now, for script you can use the extension `.shin` for saving files and run with below command.

```
shin > RUN("file_name.shin")
# Run the example file 
shin > RUN("example.shin")

```

*The example code:*
```
# This is a comment :)

FUN oopify(prefix) -> prefix + "oop"

FUN join(elements, separator)
	VAR result = ""
	VAR len = LEN(elements)

	FOR i = 0 TO len THEN
		VAR result = result + elements/i
		IF i != len - 1 THEN VAR result = result + separator
	END

	RETURN result
END

FUN map(elements, func)
	VAR new_elements = []

	FOR i = 0 TO LEN(elements) THEN
		APPEND(new_elements, func(elements/i))
	END

	RETURN new_elements
END

PRINT("Greetings universe!")

FOR i = 0 TO 5 THEN
	PRINT(join(map(["l", "sp"], oopify), ", "))
END


```
  Alright, now you've the shin lang installed. Now its time for using it.
  
___

# Documentation (still working)

> Below is the official documentation of the language, feel free to check it :D

**Note :**
You can run single line code in shell mode too.

## Arithmetic Operators:

1. `+` : It'll add the variable or integer.
2. `-` : It'll subtract the integers.
3. `*` : It'll multiply the integers
4. `/` : It'll divide the integer(s).
5. `^` : It's for power function. Eg: 2^3 = 8

## Comments

```shin
# This is a comment.
# It's simlar to python 
```

> Shin lang only supports Single line comments.

## Printing

```shin
PRINT("Hello World!")

PRINT("Its similar to python but just a capitalised version.")

VAR myVar = "Variable"

PRINT(myVar)

PRINT(2+3)

```

## Variables

```shin
VAR myVariable = "Hello World"
VAR myInteger = 0123
VAR myBool = TRUE # It'll take TRUE as 1
```

For making or setting a value to a variable you've to use the `VAR` keyword.

The data is mutuable also i.e you can change the value of Variables anytime.

```shin
shin > VAR Str = "Hey"
shin > Str
shin > Hey
shin > VAR Str = "It's mutuable"
shin > Str
shin > It's mutuable
```

Suported Data types -> Strings, Integers and Boolean.

## Data types

Shin lang supports Strings, Integers, Flloats and Boolean as data.

### Strings

String is a “string of characters” or in programming terms, an array of characters. A string is generally not a single object, but rather an array of characters that make a whole.

#### Escape character

`\\` -> This is a backslash and it's called escape as it escape some character specified.

Supported:

1. Quotes -> \"
2. Backlash -> \\\
3. New line -> \n 

```shin 
"Text with \"quotes\""
"Text with backslash \\"
"Text \n new \lin"
```


### Integers

An integer, in the context of computer programming, is a data type used to represent real numbers that do not have fractional values. ... For example, a short integer in many common programming languages is limited to a range of between 32,767 and -32,768.

### Floating

In programming, a floating-point or float is a variable type that is used to store floating-point number values. A floating-point number is one where the position of the decimal point can "float" rather than being in a fixed position within a number. Examples of floating-point numbers are 1.23, 87.425, and 9039454.2.

### Boolean

In computer science, a boolean or bool is a data type with two possible values: true or false. ... When referring to the data type in computer programming, the word "boolean" is properly spelled with a lowercase b.

In shin, `TRUE` is simplified as `1` and `FALSE` is simplified as `0`, That's how it's in low level languages.

___
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

___
## Functions

> Functions are "self contained" modules of code that accomplish a specific task. Functions usually "take in" data, process it, and "return" a result. Once a function is written, it can be used over and over and over again.

_Types of functions supported:_
**1. Short hand functions**
**2. Traditional functions**
**3. Anonymous functions**

*Short hand functions* 
```shin
FUN <func_name>(arguments) -> statement(s)
```

*Traditional functions*

```shin
FUN function_name(arguments)
    statement(s)
END # For ending the function 
```

An example of using functions:

```shin
FUN myFunc(name)
    VAR new_name = "Mr./Ms./Mrs." + name
    RETURN new_name
myFunc(John)
```

The `RETURN` keyword is used for returning the value of a variable.

```
Output: Mr./Ms./Mrs. John
```

*Anonymous functions*
>  An anonymous function is a function that is not stored in a program file, but is associated with a variable whose data type is function_handle. Anonymous functions can accept multiple inputs and return one output.

Syntax:
```shin
FUN(params) -> <expression>
```

**For example**

```shin 
VAR func_name = FUN(a) -> a + 6 
func_name(3)

```

`Output: 9`

### Note
> You can assign a function to variable too.

For example

```shin 
FUN oop(str) -> str + "oop"
VAR myFunc = oop
myFunc("P")
```

```
Output: Poop 
```


___
## Conditions

**Conditions supoorted: ** -> IF, ELIF(ELSE IF) AND ELSE

### IF statement

```shin
IF <condition> THEN <expression>
```

__For example:__

Below is the program that checks if the number is 69.

```shin
VAR num = 69
IF NUM == 69 THEN PRINT("yes")
```

### IF/ELSE statement

```shin
IF <condition> THEN <expression> ELSE <expression>
```

_For example:_

Below is a program that checks if a number is 2 or not.

```shin
VAR num = 2
IF NUM == THEN PRINT("Yes it's 2") ELSE PRINT("No it's not 2")
VAR num1 = 3 
IF NUM == THEN PRINT("Yes it's 2") ELSE PRINT("No it's not 2")
```

```
Output: 
Yes it's two 

No it's not 2 
```

### IF/ELIF/ELSE statement

```
IF <condition> THEN <expression> ELIF <condition> THEN <expression> ELSE <expression>
```

## While statement

_Types of WHILE statement:_

**1. Short Hand WHILE statement**
**2. Traditional WHILE statement**

_Short Hand WHILE statement_

```shin
WHILE <condition> THEN <expression>
```

_Traditional WHILE statement_

```shin
WHILE <condition> THEN
    <statement>
END 
```

_For example:_

```shin
WHILE TRUE THEN
    PRINT("Yes")
END
```
> The above program will keep printing "Yes" because 1+1 is always equal to 2.

## FOR statement

_Short Hand FOR statement_

```shin
FOR <var_name> = <start_value> TO <end_value> THEN <expression>
```

__For example:__

```shin
VAR result = 1
FOR i = 1 TO 6 THEN VAR result = result*i
PRINT(result)
```

```
Output: 120
```

*Normal FOR statement*

```shin
FOR <condition> or <increment> THEN
    <statement(s)>
END
```


```
<increment> = <var_name> = <start_value> TO <end_value>
```

### STEP in FOR statement

`STEP` keyword is for changing the increment value.

__For example:__

```shin
FOR i = 0 TO 11 STEP 2 THEN ....
```

> The above block of code will take numbers from 0 to 11 with a increment value of 2, so the numbers should be 0,2,4,6,8,10.

`STEP` values can be negative too i.e STEP -n 

## Lists

List is the most versatile data type available in functional programming languages used to store a collection of similar data items. The concept is similar to arrays in object-oriented programming. List items can be written in a square bracket separated by commas.

**Creating a empty list**

```
[]
```
It'll create a empty list, you can assign a name to a list.

```
VAR myList = []
```

**Creating a list with elements**

```
shin > VAR myList = [1,2,3]
shin > [1,2,3]
```

**Adding elements in a list**

Element can be added by `+` operator.

```
shin > VAR myList = [1,2,3]
shin > [1,2,3]
shin > myList + 4
shin > [1,2,3,4]
```

A list can be added as an element too.

```
shin > VAR myList = [1,2,3]
shin > [1,2,3]
shin > VAR newList = [4,5,6]
shin > [1,2,3,[4,5,6]]
```

**Combining two lists**

Two lists can be combined by `*` operator.

```
shin > VAR myList = [1,2,3]
shin > [1,2,3]
shin > VAR newList = [4,5,6]
shin > [4,5,6]
shin > myList * newList
shin > [1,2,3,4,5,6]
```

**Removing elements**

Elements can be removed by their index number.
Elements can be removed by `<list_name> - <index>`.

Index number starts from 0.
Negative index number starts from -1.

```
shin > VAR myList = [1,2,3,4]
shin > [1,2,3,4]
shin > myList - 0
shin > [2,3,4]
shin > myList - 1 
shin > [2,4]
shin > myList - -1
shin > [2]
```

In the above block of code, first `1` is removed as it's index number is 0. Then, `3` is removed as it's index number is 1. Then, `4` is removed as it's index number is -1.

**Printing elements**

Elements can be printed by their index number.

`<list_name>/index`

```
shin > VAR myList = [1,2,3,4,5,6]
shin > [1,2,3,4,5,6]
shin > myList/0 
shin > 1 
shin myList/3 
shin > 4 
shin > myList/-2 
shin > 5
```

### APPEND function

It'll add elements in a pre-defined list.

```shin
shin > VAR <list_name> = []
shin > APPEND(<list_name, <element>)
```

For example: 

```
shin > VAR myList = [1,2,3]
shin > [1,2,3]
shin > APPEND(myList, 4)
shin > [1,2,3,4]
```

You can add lists as an element too.

```
shin > VAR myList = [1,2,3]
shin > [1,2,3]
shin > APPEND(myList, [4,5,6])
shin > [1,2,3,[4,5,6]]
```

### POP function 

It removes an element from a list by it's index number.

```
shin > VAR <list_name> = []
shin > POP(<list_name>, <index>)
```

For example: 
```
shin > VAR list = [1,2,3,4]
shin > POP(list, 3)
shin > list
shin > [1,2,3]
```

It removed 4 as it's index number is 3.
> Negative indexing can be also used.

### EXTEND() function

In shin lang, EXTEND is the operation for concatenating linked lists.

Basically elements of 2nd list is joint in 1st list

```
shin > VAR <list1> = []
shin > VAR <list2> = []
shin > EXTEND(<list1>, <list2>)
```

For example:

```
shin > VAR list1 = [2,4,89]
shin > VAR list2 = [23,78,99]
shin > EXTEND(list1, list2)
shin > list1
shin > [2,4,89,23,78]
```

### LEN() function 

It prints the length of a list.

Usage: 
```
shin > VAR <list_name> = []
shin > LEN(<list_name>)
```

For example: 

```
shin > VAR myList = [1,2,3,3,5]
shin > LEN(myList)
shin > 5
```

___

## Built in functions

A function that is built into an application and can be accessed by end-users. For example, most spreadsheet applications support a built-in SUM function that adds up all cells in a row or column.

### MATH_PI

Prints the value of Pi/π.

```
shin > MATH_PI
shin > 3.141592653589793
```

### INPUT statement

An input/output statement or I/O statement is a portion of a program that instructs a computer how to read and process information. It pertains to gather information from an input device, or sending information to an output device.

> It only supports Strings, For integer see INPUT_INT

```
shin > VAR <var_name> = INPUT()
```

The above block of code will assign a value to the variable that is entered by user.

```
shin > VAR name = INPUT()
John Doe
shin > "John Doe"
```

### INPUT_INT statement

It's basically the same keyword as above but it's for integers.

```
shin > VAR <var_name> = INPUT_INT()
```

The above block of code will assign an integer to the variable that is entered by user.

```
shin > VAR myAge = INPUT_INT()
69
shin > 69
```

Erorr if the taken input isn't an integer.

```
shin > VAR <var_name> = INPUT_INT()
Bruh
"Bruh" must be an integer, Try again!
69
shin > 69 
```

### CLEAR() and CLS()

It'll clear the screen

```
shin > CLS()
shin >CLEAR()
```

### IS_NUM()

It'll check if the given data is an integer or not.

```
shin > IS_NUM(69)
shin > 1 
shin > IS_NUM("String")
shin > 0 
shin > IS_NUM([])
shin > 0 
```

As specified earlier, 1 is TRUE and 0 is FALSE.

### IS_STR()

It'll check if the given data is a string or not.

```
shin > IS_STR("HEY")
shin > 1 
shin > IS_STR(69) 
shin > 0 
shin > IS_STR([])
shin > 0 
```

### IS_LIST()

It'll check if the given data is a list or not.

```
shin > IS_LIST([])
shin > 1 
shin > VAR myList = [1,2,3]
shin > [1,2,3]
shin > IS_LIST(myList)
shin > 1 
shin > IS_LIST(23)
shin > 0 
```

### IS_FUN()

It'll check if the given data is a function or not, it works on built in function and defined function both.

```
shin > IS_FUN(PRINT)
shin > 1 
shin > FUN oop() -> PRINT("oop")
shin > IS_FUN(oop)
shin > 1 
shin > IS_FUN(23)
shin > 0
```

> Thanks, for coming till here. 

# To-Do 

- [x] Make a language
- [x] Upload on GitHub 
- [x] Make documentation
- [] Brushing the language
- [] Adding more built-in functions
- [] Make a website
- [] Make a support server
- [] Make a package manager(maybe not)




