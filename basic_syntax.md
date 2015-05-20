# Basic Syntax

![Monty Python and Holy Grail](http://sellingout.com/wp-content/uploads/2014/04/monty_python_and_the_holy_grail_59205-1600x1200.jpg)

## Simple Exercises

monty_films = ["And Now For Something Completly Different",
				"Monty Python and the Holy Grail",
				"Monty Python's Life of Brain",
				"Monty Python live at the Hollywood Bowl",
				"Monty Python's the meaning of life"]
    

Length:
```
>>> len(monty_films)
5
``` 

Uppercase:
```
>>> monty_films[0].upper()
'AND NOW FOR SOMETHING COMPLETLY DIFFERENT'
```
Count:
```
>>> monty_films[1].count("Monty")
1
```
Lowercase:
```
>>> monty_films[0].lower()
'and now for something completly different'
```
Index:
```
>>> monty_films[2].index("Monty")
0
```
Reverse:
```
>>> print monty_films.reverse()

["Monty Python's the meaning of life", 
'Monty Python live at the Hollywood Bowl', 
"Monty Python's Life of Brain", 
'Monty Python and the Holy Grail', 
'And Now For Something Completly Different']
```
Split:
```
>>> monty_films[0].split()
['Monty', "Python's", 'the', 'meaning', 'of', 'life']
```
Startswith:
```
>>> [i for i in range(len(monty_films)) if monty_films[i].startswith('M')]
 [0, 1, 2, 3] / the array is in reversed order now.
```


monty_films[0][0:10]
monty_films[0:]
monty_films[:10]
copy_array = Monty_films[:]
arr = Monty_films






