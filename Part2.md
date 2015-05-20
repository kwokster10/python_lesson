# PART 2:

![Burn](http://imoviequotes.com/wp-content/uploads/2014/10/3-Monty-Python-and-the-Holy-Grail-quotes.gif)

## Objects:

Everything in Python is object-oriented just like in Ruby. You can define custom classes like so. 

```
class Python:
    age = 12
    color = "blue"
    length = "6 ft"
    name = ""
    
    def speak(self):
        talk = "%s hisssssed!" % self.name
        return (talk)

slytherin = Python()
print (slytherin.age)
slytherin.color = "yellow"
print (slytherin.color)
slytherin.name = "Snape"
print (slytherin.speak())
```

## Let's look at how functions are defined
```
def introduction():
    print "Hello everybody!"

introduction()
```
   A few important things to note:
   	1. The colon
   	2. The 4 spaces indentation
   	3. The parentheses: needed to declare and call the function
   	4. No termination but you do need to hit return in 'python' from the terminal to end the block 
   	5. If you are using repl.it, you will need parens around the print string


## Interesting things to note about functions: scope
```
 number = 3.14159
    def scope():
        number = 5
        print number
    scope()
    print number
```
    1. Inside the function, it would read the local variable and outside it would read the global. Since Python does not compile everything on load, it doesn't hit the number = 5 until the scope function is called.
    2. Similarly, if we had number = number + 5 in the function, we would get an error b/c it's trying to find a local variable number. You would need to make a new variable like number2 = number before you can add a value to number to itself.
    3. Using _ and //

## An fascinating function 

- if you are in the python interpreter, it will look like this with ... to remind you are in a block and >>> when you are not. 

```
def operate(num1, num2, num3, **operation):
...     if operation.get("addition") == "add":
...         print "The sum is: %d" % (num1 + num2 + num3)
...     if operation.get("subraction") == "subtract":
...         print "The difference is: %d" % (num1 - num2 - num3)
...     if operation.get("multiplication") == "multiply":
...         print "The * is: %d" % (num1 * num2 * num3)
...     if operation.get("division") == "divide":
...         print "The / is: %d" % (num1 / (num2 + num3))
...     if operation.get("exponent") == "power":
...         print "The ** is: %d" % ((num1 + num2) ** num3)
... 
>>> print operate(1, 2, 3, addition = "add", subraction = "subtract", multiplication = "multiply", division = "divide", exponent = "power")
```
   1. Obviously if you used 0 in num2 and num3 here, it would break at some of the operators but you get the idea. You can pass in more params too if you'd like.
   2. There is also a function with just one * that takes a variable number of arguments

![Run Away](http://toolbox.klasresearch.com/Content/Images/Research/BlogPostImages/RunAway3.jpg)

Mini Exercise: 
** Can't be done in repl.it
- touch a file called mini_ex.py 
- first line 'import sys' - like require for Ruby / JS
- Create a command line app that will take a string and returns it printed in all caps and in pig latin if the word starts with the letter 'p'. If the word is "Crawford", print "Hey , hey, hey!". Otherwise print it in reverse one letter at a time. Hint, Python's equivalent of process.argv[2] is sys.argv[1]. 