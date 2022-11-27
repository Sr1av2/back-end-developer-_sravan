import re
phone = input("Enter Contact Number: ").strip()
valid_phone = "([\+1]|\+1)?[\s\-\.]?\(?[1-9][0-9]{2}\)?[\s\-\.]?[0-9]{3}[\s\-\.]?[0-9]{4}"
if re.match(valid_phone,phone):
	print("Valid")
else:
	print("Invalid")
