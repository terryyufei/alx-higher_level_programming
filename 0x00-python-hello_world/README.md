## 0x00. Python - Hello, World

## 0. Run Python file
     * A Shell script that runs a Python script. 
     * The Python file will be saved in the environment variable $PYFILE

## 1. Run inline
     * A shell script that runs Python code
     * The Python code will be saved in the environment variable $PYCODE

## 2. Hello, print
     * A python script that prints exactly ”Programming is like building a multilingual puzzle
     * followed by a new line
     * use the function print

## 3. Print interger
      * Complete the given source code in order to print the interger stored in the variable number
      * followed by Battery street followed by a new line
      * output of the program should be:
          * the number, followed by Battery street followed by a newline
      * you are not allowed to cast the variable number into a string
      * code must be 3 lines long
      * you have to use f-strings

## 4. Print float
      * Complete the given source code in order to print the float stored in the variable number
      * with a precison of 2 digits
      * output of the program should be:
          * Float:,  followed by  the float with only 2 digits, followed by a new line
      * you are not allowed to cast the variable number into a string
      * you have to use f-strings

## 5. Print string
      * Complete the given source code in order to print  3 times a string stored in the variable str
      * followed by its first 9 characters
      * output of the program should be:
           * 3 times the value of str
           * followed by a new line
           * followed by the first 9 characters of str
           * followed by a new line
      * you are not allowed to use any loops or conditional statements
      * your program should be maximum 5 lines long

## 6. Play with strings
     * Complete the given source code in order to print  Welcome to Holberton School!  
     * you are not allowed to use any loops or conditional statements
     * You have to use the variables str1 and str2 in your new line of code
     * your program should be exactly 5 lines long

## 7. Copy-Cut-Paste
     * Complete the given source code 
     *Your program should be exactly 8 lines long
     * word_first_3 should contain the first 3 letters of the variable word
     * word_last_2 should contain the last 2 letters of the variable word
     * middle_word should contain the value of the variable word without the first and last letters

## 8. Create a new sentence
     * Complete the given source code in order to print object-oriented programming with Python, followed by a new line.
     * You are not allowed to use any loops or conditional statements
     * Your program should be exactly 5 lines long
     * You are not allowed to create new variables
     * You are not allowed to use string literals

## 9. Easter Egg
    *A Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
    *Your script should be maximum 98 characters long  

## 10. Linked list cycle
     * A function in C that checks if a singly linked list has a cycle in it
     * Requirements: 
     * Only these functions are allowed: write, printf, putchar, puts, malloc, free
> The code;
     * The function check_cycle takes a pointer to the head of a linked list (listint_t *list) as its input parameter 
     * and returns an integer value of either 1 or 0.
     * The function uses the "slow and fast pointers" approach to detect cycles in the linked list.
     * It initializes two pointers, slow and fast, both pointing to the head of the list.
     * The function then enters a loop that continues as long as slow, fast, and fast->next (the next node after fast) are all non-null. 
     * In each iteration, slow moves one node forward (slow = slow->next), and fast moves two nodes forward (fast = fast->next->next).
     * If at any point slow and fast become equal (slow == fast), it means that the pointers have met, indicating the presence of a cycle 
     * in the linked list. In this case, the function returns 1 to indicate the existence of a cycle.
     * If the loop completes without detecting a cycle, it means that the end of the linked list has been reached, and there are no cycles. 
     * In this case, the function returns 0 to indicate the absence of a cycle.
     * Overall, the check_cycle function uses the "slow and fast pointers" technique to efficiently determine if a linked list contains a cycle. 
     * It achieves this by moving two pointers through the list at different speeds and checking if they eventually meet.

## 100. Hello, write
     * a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
     * Use the function write from the sys module
     * You are not allowed to use print
     * Your script should print to stderr
     * Your script should exit with the status code 1

## 101. Compile
     * A script that compiles a Python script file.
     * The Python file name will be stored in the environment variable $PYFILE
     * The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

## 102. ByteCode-> Python #1
     * Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
		 3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE

