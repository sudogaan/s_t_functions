def cm(feet=0, inches=0):
	"""Converts a length from feet and inches to centrimeters."""
	inches_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	return inches_to_cm + feet_to_cm

print(cm(feet=5))
print(cm(inches=70))
print(cm(feet=5, inches=8))
print(cm(inches=8, feet=5))
