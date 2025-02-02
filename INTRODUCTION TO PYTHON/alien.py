# DICTIONARIES
# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can 
# use a key to access the value associated with that key. A key's value can be a number, string, a list or 
# even another dictionary. In fact you can use any object that you can create in Python as a value in a
# dictionary.

# In Python a dictionary is wrapped in braces ,{}, with a series of key value pairs inside the braces,
# as shown in the earlier example:


alien_0 = {'color':'green', 'points': 5}

# A key-value pai is a set of values associated with each other. When you provide a key, Python returns
# the value associated with that key. Every key is connected to its value by a colon, and individual
# key-value pairs are separated by commas. You can store as many key-value pairs as you want in a dictionary.


# ACCESSING VALUES IN A DICTIONARY

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# ADDING NEW KEY-VALUE PAIRS

# To add a new key-value pair, you would give the name of the dictionary followed by the new key in 
# square brackets along with the new value.

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# As of Python 3.7 dictionaries retain the order in which they were defined.

# STARTING WITH AN EMPTY DICTIONARY
# Typically, you'll use empty dictionaries when storing user-supplied data in a dictionary or when you write
# code that generates a large number of key-value pairs automatically.

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# MODIFYING VALUES IN A DICTIONARY
# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and 
# then the new value you want associated with that key.

alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

# Track the position of an alien that can move at different speeds. We'll store a value representing the 
# alien's current speed and then use it to determine how far to the right the alien should move:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x position: {alien_0['x_position']}.")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  # This must be a fast alien.
  x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x position: {alien_0['x_position']}")

# REMOVING KEY-VALE PAIRS
# When you don't longer need information that's stored in a dictionary, you can use the del statement to 
# COMPLETELY REMOVE a key-value pair. All del needs is the name of the dictionary and the key that you want 
# to remove.

alien_0 = {'color': 'green', 'point': 5}
print(alien_0)

del alien_0['color']
print(alien_0)

