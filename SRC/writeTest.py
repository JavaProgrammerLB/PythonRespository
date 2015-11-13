#!/usr/bin/env python

# create and open file
f = open("test.txt","a")

# write data to file
f.write("\n")
f.write("Hello World, \n")
f.write("  This data will be written to the file.")

# close file
f.close()
