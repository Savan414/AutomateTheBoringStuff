import re

message = 'Call me at 578-415-9612 tomorrow, or at 425-874-3678'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message) #This returns a list of all matching items
print(mo)
