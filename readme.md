# Code Question

The accompanying file `weather.dat` contains weather data for a single month as space-separated values. The first column (Dy) contains the day of the month; the second (MxT) contains the maximum temperature for that day, while the third (MnT) contains the minimum temperature.

The final row contains aggregate values for the entire month.

Write a program to find the row with the **maximum** spread in the weather.dat file, where spread is defined as the difference between MxT and MnT. For example, the spread for day 2 was (79 - 63) = 16. 

Your program should print the day of the month and spread to standard output.

Assuming that your program is called weather.py, then a sample run will look like:

    $ python weather.py
    2 16

… where 2 is the day of the month with the maximum spread, and the actual spread is 16. (The actual day and spread will depend on the contents of the file.)

# Expectations

* You may code your solution in **any** language (if you are comfortable with Python, that's a good way to go) 
* You are **not** allowed to edit the weather.dat file before running your program on it. 
* Include a readme.txt file explaining how to run your code, and detailing any assumptions you have made.
* Focus on producing a **correct** and **efficient** solution with well-organized, readable code. 
