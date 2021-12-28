# Shin Language
> A basic programming language written in python and inspired by python and basic.

## Downloading

### Pre requisite:
  You need python3 and git installed on your system.

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
```

  Now, for script you can use the extension ".shin" for saving files and run with below command

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
  Alright now you've the shin lang installed, Now its time for using it.
  
___

# Documentation (still working)

> Below is the official documentation of the language, feel free to check it :>

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
# Its simlar to python 
```

## Printing

```shin
PRINT("Hello World!")
PRINT("Its similar to python but just a capitalised version.")

```

## Variables

```shin
VAR myVariable = "Hello World"
VAR myInteger = 0123
```

For making or setting a value to a variable you've to use the `VAR` keyword.

The data is mutuable also i.e you can change the value of Variables anytime.

Suported Data types -> Strings and Integers.
___
## Comparisons and Logical operator 

### Comparison operator: 

1. == : Checks if the value of variable is satisfied or not. If yes then it will do the <expression> if not it'll be `False` or will continue to next <condition>

2. != : Checks if the value of variable is satisfied or not. If no then it will do the <expression> if not it'll be `False` or will continue to next <condition>

3. \>= : Checks if the variables are equal or its greater than the other one.

4. <= : Checks if the variables are equal or its lesser than the other one.

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
___
## Conditions

**Conditions supoorted: ** -> IF, ELIF(ELSE IF) AND ELSE

### IF statement

```shin
IF <condition> THEN <expression>
```

**For example: **

Below is the program that checks if the number is 69.

```shin
VAR num = 69
IF NUM == 69 THEN PRINT("yes")
```

### IF/ELSE statement

```shin
IF <condition> THEN <expression> ELSE <expression>
```

**For example: **

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

### While statement

```shin
WHILE <condition> THEN
    <statement>
END 
```

**For example: **

```shin
WHILE 1 + 1 == 2 THEN
    PRINT("Yes")
END
```
> The above program will keep printing "Yes" because 1+1 is always equal to 2.

### Other stuff
i was tired so ill do it later 
thanks




