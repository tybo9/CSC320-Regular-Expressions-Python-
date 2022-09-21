# CSC320-Regular-Expressions-Python-
Overview
In this programming assignment, you shall prepare a Python 3 script which reads input from the user, parses it using a regular expression to see if it meets valid criteria, and produces output to the screen. You shall submit the python script you developed here by uploading the .py file you create.  

Details
In rhetoric and writing, certain special words allow us to combine together shorter sentences. The set of these words includes: for, and, nor, but, or, yet, so. We use the mnemonic FANBOYS to easily remember them, and a comma precedes their appearance in a sentence (like this one!). Thus, using FANBOYS, we may transform the following three sentences into a single sentence with two of these key words:

"I ate a brownie for breakfast. I also ate a cookie. I am in quarantine."

This becomes: "I ate a brownie for breakfast, and I ate a cookie, for I am in quarantine."

The above sentences are for illustration purposes only, and they are not based on personal experience. A brownie and cookie represent terrible breakfast choices, and I would never subject myself to that kind of slack. Instead, as an over-achiever, I consumed three brownies, but I call them bouchon, so it feels much healthier. 

You shall create a Python script that reads in a single sentence from the user. You may either accept this input through the keyboard or use a text file as input. That is, the program may pause and wait for the user to type a sentence or it may open an existing file with the sentence inside. The choice is left to the student (I prefer reading files when developing because I don't need to keep typing in text). 

The script shall then parse the input string using a regular expression (import re) and detect the FANBOYS present. These words may all appear naturally in a sentence by themselves, so to count as a FANBOYS, a comma must immediately precede the conjunction. After locating each of the FANBOYS, the program shall display the separate thoughts these words link together and display the result to the screen. It shall number each thought sequentially. Using the previous example as the input string, the program would then output:

1: I ate a brownie for breakfast

2: I ate a cookie

3: I am in quarantine. 
 

Useful References:
Python 3 documentation on the re module: https://docs.python.org/3/library/re.html (Links to an external site.) 

Python 3 HOWTO on regular expressions: https://docs.python.org/3.3/howto/regex.html (Links to an external site.) 
