def isPhoneNumber(text): # xxx-xxx-xxxx
    if len(text) != 12:
        return False  # not a phone number sized string
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False #missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no first three digits
    if text[7] != '-':
        return False #missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # missing last four digits
    return True

message = 'Call me at 578-415-9612 tomorrow, or at 425-874-3678'

# Extract the phone numbers from the message string
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers in the input message.')
