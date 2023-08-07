# Syntax-Validation
Syntax validation of a programming language by writing the Context Free Grammar for the specific construct of a particular language and a program for the same.

Language: Python

Construct: if else

Syntax:
if (condition) : 
   statements
else : 
   statements

Context Free Grammar:
statement :   if expression : statement 
			    |   if expression : statement else : statement
			    |   id assignment_op expression
			    |   statement
expression:   expression logical_op expression
			    |   expression arithmetic_op expression
			    |   expression
			    |   id
			    |   value
logical_op		:   >   |   <   |    >=   |   <=   |   ==   |   !=   |   or   |   and
assignment_op	:   =   |   +=   |   -=   |   *=   |   /=   |   
arithmetic_op	:   +   |   -   |   *   |   /
