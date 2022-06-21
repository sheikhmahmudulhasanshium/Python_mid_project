#all the key info is collected from https://realpython.com/python-keywords/

keyword_list=[
{"name":"and", "details":"The Python keyword and is used to determine if both the left and right operands are truthy or falsy. If both operands are truthy, then the result will be truthy. If one is falsy, then the result will be falsy","sample_code":"x = y and z"}
,{"name":"or", "details":"Python’s or keyword is used to determine if at least one of the operands is truthy. An or statement returns the first operand if it is truthy and otherwise returns the second operand","sample_code":"x = y or z"}
,{"name":"not","details":"Python’s not keyword is used to get the opposite Boolean value of a variable","sample_code":'>>> val = ""  # Truthiness value is `False` \n >>> not val \n True \n >>> val = 5  # Truthiness value is `True`\n >>> not val\n False"'}
,{"name":"in","details":"Python’s in keyword is a powerful containment check, or membership operator. Given an element to find and a container or sequence to search, in will return True or False indicating whether the element was found in the container","sample_code":">>> name = 'Chad'\n>>> 'c' in name\nFalse\n>>> 'C' in name\nTrue"}
,{"name":"is","details":"Python’s is keyword is an identity check. This is different from the == operator, which checks for equality. Sometimes two things can be considered equal but not be the exact same object in memory. The is keyword determines whether two objects are exactly the same object:","sample_code":"<obj1> is <obj2>"}
,{"name":"if","details":"The if keyword is used to start a conditional statement. An if statement allows you to write a block of code that gets executed only if the expression after if is truthy.The syntax for an if statement starts with the keyword if at the beginning of the line, followed by a valid expression that will be evaluated for its truthiness value","sample_code":"if <expr>:\n\t<statements>"}
,{"name":"elif","details":"The elif statement looks and functions like the if statement, with two major differences:Using elif is only valid after an if statement or another elif.You can use as many elif statements as you need.In other programming languages, elif is either else if (two separate words) or elseif (both words mashed together). When you see elif in Python, think else if","sample_code":"if <expr1>:\n\t<statements>\nelif <expr2>:\n\t<statements>\nelif <expr3>:\n\t<statements>"}
,{"name":"else","details":"The else statement, in conjunction with the Python keywords if and elif, denotes a block of code that should be executed only if the other conditional blocks, if and elif, are all falsy","sample_code":"if <expr>:\n\t<statements>\nelse:\n\t<statements>"}
,{"name":"for","details":"The most common loop in Python is the for loop. It’s constructed by combining the Python keywords for and in explained earlier. The basic syntax for a for loop is as follows","sample_code":'>>> people = ["Kevin", "Creed", "Jim"]\n>>> for person in people:\n\tprint(f"{person} was in The Office.")\nKevin was in The Office.\nCreed was in The Office.\nJim was in The Office.'}
,{"name":"while","details":"Python’s while loop uses the keyword while and works like a while loop in other programming languages. As long as the condition that follows the while keyword is truthy, the block following the while statement will continue to be executed over and over again","sample_code":'>>> while True:\n\tprint("working...")'}
,{"name":"break","details":"If you need to exit a loop early, then you can use the break keyword. This keyword will work in both for and while loops","sample_code":'>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n>>> sum = 0\n>>> for num in nums:\n\t sum += num\n\t if sum > 10:\n\t break\n sum\n 15'}
,{"name":"continue","details":"Python also has a continue keyword for when you want to skip to the next loop iteration. Like in most other programming languages, the continue keyword allows you to stop executing the current loop iteration and move on to the next iteration","sample_code":'for <element> in <container>:\n\tif <expr>:\n\t\tcontinue'}
,{"name":"def","details":"Python’s keyword def is used to define a function or method of a class. This is equivalent to function in JavaScript and PHP. The basic syntax for defining a function with def looks like this","sample_code":'def <function>(<params>):\n\t<body>'}
,{"name":"class","details":"To define a class in Python, you use the class keyword. The general syntax for defining a class with class is as follows:","sample_code":'class MyClass(<extends>):\t\n<body>'}
,{"name":"with","details":"Context managers are a really helpful structure in Python. Each context manager executes specific code before and after the statements you specify. To use one, you use the with keyword","sample_code":'with <context manager> as <var>:\n\t<statements>'}
,{"name":"as","details":"If you want access to the results of the expression or context manager passed to with, you’ll need to alias it using as. You may have also seen as used to alias imports and exceptions, and this is no different. The alias is available in the with block","sample_code":'with <expr> as <alias>:\n\t<statements>'}
,{"name":"pass","details":"Since Python doesn’t have block indicators to specify the end of a block, the pass keyword is used to specify that the block is intentionally left blank. It’s the equivalent of a no-op, or no operation. Here are a few examples of using pass to specify that the block is blank","sample_code":'def my_function():\n\tpass\nclass MyClass:\n\tpass\nif True:\n\tpass'}
,{"name":"lamda","details":"The lambda keyword is used to define a function that doesn’t have a name and has only one statement, the results of which are returned. Functions defined with lambda are referred to as lambda functions","sample_code":'>>> ids = ["id1", "id2", "id30", "id3", "id20", "id10"]\n>>> sorted(ids)\n["id1", "id10", "id2", "id20", "id3", "id30"]\n>>> sorted(ids, key=lambda x: int(x[2:]))\n["id1", "id2", "id3", "id10", "id20", "id30"]'}
,{"name":"return","details":"Python’s return keyword is valid only as part of a function defined with def. When Python encounters this keyword, it will exit the function at that point and return the results of whatever comes after the return keyword","sample_code":'>>> def return_none():\n\treturn\n>>> return_none()\n>>> r = return_none()\n>>> print(r)None'}
,{"name":"yield","details":"Python’s yield keyword is kind of like the return keyword in that it specifies what gets returned from a function. However, when a function has a yield statement, what gets returned is a generator. The generator can then be passed to Python’s built-in next() to get the next value returned from the function.When you call a function with yield statements, Python executes the function until it reaches the first yield keyword and then returns a generator. These are known as generator functions:","sample_code":'def <function>():\n\tyield <expr>'}
,{"name":"import","details":"Python’s import keyword is used to import, or include, a module for use in your Python program. Basic usage syntax looks like this","sample_code":'import <module>'}
,{"name":"from","details":"The from keyword is used together with import to import something specific from a module","sample_code":'>>> from collections import Counter\n>>> Counter()\nCounter()'}
,{"name":"try","details":"Any exception-handling block begins with Python’s try keyword. This is the same in most other programming languages that have exception handling.The code in the try block is code that might raise an exception. Several other Python keywords are associated with try and are used to define what should be done if different exceptions are raised or in different situations. These are except, else, and finally:","sample_code":'def mpg(miles, gallons):\n\t try:\n\t\t mpg = miles / gallons\n\t except ZeroDivisionError:\n\t\t mpg = None\n\treturn mpg'}
,{"name":"except","details":"Python’s except keyword is used with try to define what to do when specific exceptions are raised. You can have one or more except blocks with a single try. The basic usage looks like this","sample_code":'try:\n\t <statements>\n except <exception>:\n\t <statements>'}
,{"name":"raise","details":"The raise keyword raises an exception. If you find you need to raise an exception, then you can use raise followed by the exception to be raised","sample_code":'raise <exception>'}
,{"name":"finally","details":"Python’s finally keyword is helpful for specifying code that should be run no matter what happens in the try, except, or else blocks. To use finally, use it as part of a try block and specify the statements that should be run no matter what:","sample_code":'try:\n\t <statements>\nfinally:\n\t <statements>'}
,{"name":"assert","details":"The assert keyword in Python is used to specify an assert statement, or an assertion about an expression. An assert statement will result in a no-op if the expression (<expr>) is truthy, and it will raise an AssertionError if the expression is falsy. To define an assertion, use assert followed by an expression:","sample_code":'assert <expr>'}
,{"name":"del","details":"del is used in Python to unset a variable or name. You can use it on variable names, but a more common use is to remove indexes from a list or dictionary. To unset a variable, use del followed by the variable you want to unset:","sample_code":'del <variable>'}
,{"name":"global","details":"If you need to modify a variable that isn’t defined in a function but is defined in the global scope, then you’ll need to use the global keyword. This works by specifying in the function which variables need to be pulled into the function from the global scope:","sample_code":'global <variable>'}
,{"name":"print","details":"When print was a keyword, the syntax to print something to the screen looked like this:","sample_code":'print "Hello, World"'}
,{"name":"exec","details":"In Python 2.7, the exec keyword took Python code as a string and executed it. This was done with the following syntax:","sample_code":'exec "<statements>"'}]

