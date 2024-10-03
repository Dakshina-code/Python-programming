area = 0;
height = 10;
width = 20;

#calculate the area of a triangle
area = width * height /2;

# printing formatted float value with 2 decimal places
print("the area of the the triangle would be %.2f" % area);

#printing the formatted decimal number with right justified to take up 6 space with leading zeros
print("My favorite number is %06d !" % 42);

#Do the same thing with the .formate syntax to include numbers our output
print("the are of thea triangle would be {0:f} ".format(area))
print("my favorite number is {0:d} ".format(42));

# this is an example with multiple numbers
# I have used the  \ to indicate command continues on next line
print("Here are three numbers! " +\
      "the first is {0:d} the second is {1:4d} and {2:d}".format(7,8,9));