import pyperclip, re

# Phone regex
phone_re = re.compile(r'''(
    (\d{3}|(\d{3}\))? # Area code
    (\s |-|\.)? # Separator
    (\d{3}) # First 3 digits
    (\s | - | \.) # Separator
    (\d{4}) # Last 4 digits
    (\s*ext|x|ext\.)\s*(\d{2,5}))? # Extension
    )''', re.VERBOSE)

# email regex
email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # Username (one of more of uppercase or lowercase letter, digit, or special character)
    @ # @ symbol
    [a-zA-Z0-9.-]+ # Domain name (matches one or more of letters, digits, dots, or hyphens)
    (\.[a-zA-Z]{2,4}) # Dot-something (group 2, literal dot followed by 2 to 4 letters)                 
    )''', re.VERBOSE)

# Find all matches in the clipboard text (pyperclip.paste() function will get a string value of the text on the clipboard, and the findall() regex method will return a list of tuples)
text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]]) # area code, first 3 digits, last 4 digits, extension. phone number is a string with unique format for all.
    if groups[6] != '':
        phone_num += ' x' + groups[6] # extension added if existing
    matches.append(groups)
for groups in email_re.findall(text):
    matches.append(groups[0]) # append group 0 of each match (entire regular expression)

# Join matches into a string (pyperclip.copy() function takes only a single string value, not a list of strings => we must call the join() method on matches)
# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")