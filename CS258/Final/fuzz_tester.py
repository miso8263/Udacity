"""


"""


# Fuzz Testing
# ------------
# Write a random fuzzer, based on Charlie Miller's example
# from Problem Set 4, for a text viewer application.
#
# For multiple iterations, the procedure, fuzzit, should take in the content
# of a text file, pass the content into a byte array, randomly modify bytes
# of the "file", and add the resulting byte array (as a String) to a list. 
# The return value of the fuzzit procedure should be a list of 
# byte-modified strings.


import random
import math

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""


def fuzzit(content):
	# Write a random fuzzer for a simulated text viewer application
	# Pass the content into a byte array
	buf = bytearray(content)
	FuzzFactor = len(content)
	NumTests = 100
	strlist = []
	# start Charlie Miller code
	numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1
	for i in range(NumTests):
		for j in range(numwrites):
			# randomly modify bytes of the "file" 
			rbyte = random.randrange(256) 
			rn = random.randrange(len(buf)) 
			buf[rn] = "%c"%(rbyte)
			# end Charlie Miller code
			# Add the resulting byte array (as a String) to a list. 
			strlist.append(str(buf))
		
	# The return value should be a list of byte-modified strings.
	return strlist