# Input code

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# The comma after the end of each above print statement
# allows the print to not end the line with a newline char
# and go to the next line

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)