
import sys
import operator

def main(fname):

	#forming a path to the file.
	data_path = "data/"+fname

	# try statement
	try:

		# Open the file in the file path in read only mode
		read_file = open(data_path, 'r')

		# Read and ignore header lines
		header = read_file.readline()
		separator_line = read_file.readline()

		# The dictionary to be used to store the calculated data
		data_dict = {}

		# Read the content in the file line by line
		for line in read_file:
			# Strip the characters of the string read
		    line = line.strip()
		    # Separate the stripped line string on all whitespaces
		    columns = line.split()

		    # Get the value of the day of the read line
		    day = columns[0]

		    # Maximum temperature value for the read line
		    # Split on * to remain with the real number value, this is mainly for the numbers with the *
		    max_temp = float(columns[1].split('*')[0])

		    # Minimum temperature value for the read line
		    # Split on * to remain with the real number value, this is mainly for the numbers with the *
		    min_temp = float(columns[2].split('*')[0])

		    # Check if we have reached the last line
		    if(day != 'mo'):
		    	# Calculate the spread as the difference between maximum and minimum temperature values on each day
		    	spread = float(max_temp - min_temp)

		    	# Update the results in the data_dict
		    	data_dict.update({day: spread})

		# Close file
		read_file.close()

		# sort the data in the dictionary in descending order
		#The day with the highest spread is at the top of the dictionary
		sorted_data_dict = sorted(data_dict.items(), key=operator.itemgetter(1),reverse=True)

		# Print out the item at position 0 in the dictionary in standard display
		print "Day" +"\t" +"Spread"
		print str(sorted_data_dict[0][0]) +"\t" + str(sorted_data_dict[0][1])

	# Handle exceptions
	except Exception:
		print "Could not proceed because of:"
		print "~ The file "+fname+" does not exist"
		print "Please supply the correct file name and run again"

if __name__ == "__main__":

	try:
		sys.exit(main(sys.argv[1]))

	except Exception:
		print "An error has occured"
		print "To run this program, the name of the file to be read should be passed"
		print "For instance, python weather.py weather.dat"
