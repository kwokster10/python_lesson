# PART 1

![Flesh Wound](http://images6.fanpop.com/image/photos/35300000/Monty-Python-and-the-Holy-Grail-Inspired-Quote-Poster-monty-python-and-the-holy-grail-35315673-551-849.jpg)

## String Formatting - a cool way to concat strings
So we've strings being concated with simply '+'' or '#{}'. 
We can still add in Python or with string literals, you do just have a space. But check this out:
We can add with arugment specifiers listed below:

	1. %s - string or something you want to turn to string
	2. %d - integers
	3. %f - floats
	4. %.#f - where # is the number of decimals you want

AND - "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list)
	- A tuple is another special data format stored in parens that is immutable. Meaning it's contents cannot be changed, unlike lists or dictionaries.

Mini Exercise:
Let's think back to the bank homework. If we wanted to print "You made a deposit / payment of $20.25.", how would we write it with these variables:
```
credit = "deposit" 
deduction = "payment" 
amount  = 20.2555555

print "You made a %s / %s of %.2f." % (credit, deduction, amount)
```

## Conditional

The most well-known statement type is the if statement.

1. Python does not use { } to enclose blocks of code for if statements like javascript etc.. Instead, Python uses the colon (:) and indentation/whitespace to group statements. 
2. The boolean test for an if does not need to be in parenthesis (big difference from Ruby/Java), and it can have *elif* and *else* clauses (mnemonic: the word "elif" is the same length as the word "else").
 
The "zero" values all count as False: None, 0, empty string, empty list, empty dictionary

```
# Example 1: 'if' statement

food = 'ice cream'
if food == 'ice cream':
    print('Ummmm, my favorite!')

# Example 2: 'if else' statement

 if food == 'ice cream':
    print('Ummmm, my favorite!')
else:
    print("No, I won't have it. I want ice cream!")   
```
```
# Example 3: 'chained' conditional

if x < y:
    STATEMENTS_A
elif x > y:
    STATEMENTS_B
else:
    STATEMENTS_C

# Example 4: Nested conditional

if x < y:
    STATEMENTS_A
else:
    if x > y:
        STATEMENTS_B
    else:
        STATEMENTS_C
```






