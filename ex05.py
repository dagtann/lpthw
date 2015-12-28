# exercise formally introduces format strings
# -> used for shorthand referencing variables in strings

name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy" % weight
print "Actually that's not too heavy."
# variables are called in order of reference
print "He's got %s eyes and %s hair." % (hair, eyes)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
  age, height, weight, age + height + weight
)

# study drills
import math
print "Come to the Darkside. We got %r." % math.pi

# convert cm to inches
length_metric = 10 # cm
inch_mult = 0.39370
print "%d cm in the metric system are equivalent to %d inches in the imperial system" % (
  length_metric, length_metric * inch_mult)

