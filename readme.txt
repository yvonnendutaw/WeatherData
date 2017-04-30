Yvonne Nduta
Software Engineer
yvonnendutaw@gmail.com
---------------------------------------------------------------
Code Challenge - Maximum Spread in Weather Data
---------------------------------------------------------------
Problem Description

The question to be solved expected me to write a program to find the row with the maximum spread in the weather.dat file, where spread is defined as the difference between MxT and MnT. The file weather.dat (data/weather.dat) provided contains weather data for a single month as space-separated values. The first column (Dy) contains the day of the month; the second (MxT) contains the maximum temperature for that day, while the third (MnT) contains the minimum temperature.

RESOURCES USED
    Programming Language - Python 2.7.12
    OS - Ubuntu 16.04

STEPS TAKEN
    * The program should read the data file line by line
    * Since the first two lines in the files are not values going to be used they are ignored.
		* Each line read represents weather reading - including maximum temperature on the second column
		  and minimum temperature on the third column on each day on the first column.
		* The read line input is then stripped and separated on white spaces to obtain
		  the Day, MaxT and MinT values, which are needed for the calculations
		* Spread for each day is calculated as the difference between the extracted MaxT and
		  MinT values and stored in a dictionary whose key is the day and value is the spread
		* The last line of the file which contains monthly averages is not considered while
		  tabulating spread.
		* Once spread for all the days has been calculated and stored in the dictionary, the
		  dictionary is sorted by value in descending order such that the highest spread is
		  at position 0 of the dictionary.
		* The item at position 0 in the dictionary is then printed in standard display as the
		  maximum spread

ASSUMPTIONS MADE

    * The asterisk on some of the values was assumed to mean an approximation hence ignored. The number on the left side of the asterisk was taken to be the value for that day.

CODE FOLDER STRUCTURE

	The program is in a folder titled WeatherData which contains:

	|...WeatherData
			|...data/ 			// Contains the data file weather.dat
			    |...weather.dat // Weather.dat file containing weather data for a single month
			...readme.txt 		// The read me file containing instructions on running the program
      ...readme.md 		// This read me file contains the code challenge
			...weather.py   	// The Python script containing the program code

SETTING UP & RUNNING THE APPLICATION

  Prerequisites

		- Before running the program, ensure that Python (preferably version 2.7.12 or a later version)
		  is installed

  Running the program

	After downloading and extracting the code to a destination location, execute it as follows:

		- Navigate to the folder containing the file to execute.

		  	$ cd ../WeatherData

		- Once on the root of the folder containing the source code, execute the file weather.py which
		  bears the main method. The name of the data file (weather.dat) to be read should be passed as
		  a command line argument as follows:

		  	$ python weather.py weather.dat


		- If there are no errors, the program will compile and output will be displayed as follows:

			Day	Spread
			9	  54.0
