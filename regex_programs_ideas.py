'''
1/ Find website URLs that begin with http:// or https://.
2/ Clean up dates in different date formats (such as 3/14/2030, 03-14-2030, and
2030/3/14) by replacing them with dates in a single, standard format.
3/ Remove sensitive information such as Social Security numbers or credit card
numbers.
4/ Find common typos, such as multiple spaces between words, accidentally
accidentally repeated words, or multiple exclamation marks at the ends of
sentences. Those are annoying!!
'''


# Practice 1: websites searching
import re

text = "Last night I was curious about that story I read about wild animals. So I visited https://www.nationalgeo.org and also http://wildanimals.org "

website_finder = re.compile(r'https?://[^\s]+')
# [^\s]+ is the same as \S+
# [...] is a character class: match one character from this set
# ^ inside a character class, at the very start -> negation: match anything not in the set
# \s -> any whitespace character (in Python Regex, this includes spaces, tabs, newlines, and most Unicode spaces)
# + -> one or more of the preceding token, and it's greedy (it will take the longest run it can, then backtrack if needed)

# Possessive: Match zero or one non-space character — but don’t backtrack.
web_search = re.compile(r'https?://\S?+')
find_web = web_search.findall(text)
print(find_web) # ['https://w', 'http://w']

# Lazy: match as few as possible but expand if needed
web_search = re.compile(r'https?://\S+?')
find_web = web_search.findall(text)
print(find_web) # ['https://w', 'http://w']

# Greedy search 
web_search = re.compile(r'https?://\S+')
find_web = web_search.findall(text)
print(find_web) # ['https://www.nationalgeo.org', 'http://wildanimals.org']

'''
https? → matches http or https (s is optional).
:// → literal ://.
[^\s]+ → one or more characters that are not whitespace (so the URL stops at a space). It matches the longest contiguous run of characters that are not whitespace. It grabs “one or more non-whitespace characters,” greedily.
'''

# website_finder2 = re.match(r'^https', text)
# print(website_finder2.group())

find_those = website_finder.findall(text)
print(find_those)


# Practice 2: Dates formatting

'''
3/14/2030
03-14-2030
2030/3/14


dates_pattern = re.compile(
    r'(?:\d{1,2}/\d{1,2}/\d{2,4})'
    r'|(?:\d{1,2}-\d{1,2}-\d{2,4})'
    r'|(?:\d{2,4}/\d{1,2}/\d{1,2})'
                        )
find_dates = dates_pattern.findall("I was born on 3/14/2000 and became IM on 2-3-1996, and GMI on 02/12/23")
find_dates2 = dates_pattern.findall("I was born last month and became GMI yesterday")

if find_dates2:
    print(find_dates2)
else:
    print("no dates found")


try - except AttributeError useful with .search(), since returning None if nothing is found. Not useful with .findall() since it returns an empty list when nothing is found.
.findall() with capturing groups returns a list of tuples, and a list with non-capturing groups.
Possible to flatten the result tuples if sticking with capturung groups:
dates = [d1 or d2 for d1, d2 in find_dates]
print(dates)
'''


import re
import datetime

dates_pattern = re.compile(
    r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})'   # mm/dd/yyyy or mm-dd-yyyy
    r'|(\d{2,4})[/-](\d{1,2})[/-](\d{1,2})' # yyyy/mm/dd or yyyy-mm-dd
)
# Need to use capturing groups to handle the 2 possible formats (year first or at the end).
# We must group the digits to actually extract month, day, year separately:
# Group 1: month 
# Group 2: day
# Group 3: year
# Group 4: year
# Group 5: month
# Group 6: day

text = "I was born on 3/14/2000 and became IM on 2-3-1996, and GMI on 02/12/23, and will retire on 2030/3/14"

matches = dates_pattern.findall(text)

'''
[('3', '14', '2000', '', '', ''), 
 ('2', '3', '1996', '', '', ''), 
 ('02', '12', '23', '', '', ''), 
 ('', '', '', '2030', '3', '14')]
'''

parsed_dates = []
for m, d, y, Y, M, D in matches:
    if m:  # mm/dd/yyyy
        month, day, year = int(m), int(d), int(y)
    else:  # yyyy/mm/dd
        year, month, day = int(Y), int(M), int(D)

    # Normalize year to 4 digits
    if year < 100:
        if year < 50:
            year += 2000
        else:
            year += 1900

    parsed_dates.append((month, day, year))

print(parsed_dates)

# [(3, 14, 2000), (2, 3, 1996), (2, 12, 2023), (3, 14, 2030)]

for month, day, year in parsed_dates:   # unpack the tuple
    g = datetime.datetime(year, month, day)  # use the unpacked values
    print(g)



# Practice #3: Hide sensitive data

import re

text = "I was trying to buy some cool stuff and eventually found my credit card mumber 1234-4568-7894-4564 and also my SSN 123-45-4545. I also have the other card 4567456891234578 and 4568 1234 8945 6458 but I barely use it."

'''
ssn_pattern = re.compile(r'\d{3}-\d{2}-\d{4}')

card_number_pattern = re.compile(r'\d{16}|\d{4}\s\d{4}\s\d{4}\s\d{4}|\d{4}-\d{4}-\d{4}-\d{4}')

find_cards = card_number_pattern.findall(text)
find_ssn = ssn_pattern.search(text)


print(find_cards)
print(card_number_pattern.sub(r'****************', text))

print(find_ssn.group())

print(ssn_pattern.sub(r'***-**-****', text))
print(ssn_pattern.sub(lambda m: re.sub(r'\d', '*', m.group()), text)) # if search

if findall

matches = ssn_pattern.findall(text)

masked = []
for ssn in matches:
    masked_ssn = re.sub(r'\d', '*', ssn)  # replace digits with *
    masked.append(masked_ssn)

print("Matches:", matches)
print("Masked :", masked)
'''

# The (?: … ) is a non-capturing group so you don’t accidentally mess up group numbering when you use .sub().

sensitive_pattern = re.compile(
    r'(?:\d{3}-\d{2}-\d{4})'
    r'|(?:\d{16})'
    r'|(?:\d{4}-\d{4}-\d{4}-\d{4})'
    r'|(?:\d{4}\s\d{4}\s\d{4}\s\d{4})'
)

# Option 1: If I want to mask all SSN and credit card info

matches = sensitive_pattern.findall(text)
print("Matches:", matches)

masked = sensitive_pattern.sub(lambda m: '*' * len(m.group()), text)
print("Masked :", masked)

# card_number_pattern = re.compile(r'(\d{12})(\d{4})')
# print(card_number_pattern.sub(r'************\2', "1234567812345678"))

# Option 2: If I want to mask all SSN and keep last 4 digits of credit card

def mask_sensitive(m: re.Match) -> str:
    s = m.group(0)
    digits = re.sub(r'\D', '', s)   # strip out non-digits
    if len(digits) == 16:  # credit card
        # mask all but last 4, preserve separators
        result = []
        digit_index = 0
        for ch in s:
            if ch.isdigit():
                if digit_index < len(digits) - 4:
                    result.append('*')
                else:
                    result.append(ch)
                digit_index += 1
            else:
                result.append(ch)
        return ''.join(result)
    elif len(digits) == 9:  # SSN
        return re.sub(r'\d', '*', s)
    else:
        return '*' * len(s)  # fallback


matches = sensitive_pattern.findall(text)
print("Matches:", matches)

masked = sensitive_pattern.sub(mask_sensitive, text)
print("Masked:", masked)


# Practice 4: Typos finder 

'''
Typos removal tool:
- multiple spaces between words
- repeated words
- multiple exclamation points
'''



def clean_text(text):
    typo_1 = re.compile(r'(\s{2,})')
    typo_2 = re.compile(r'!{2,}')
    typo_3 = re.compile(r'\b(\w+)(?:\s+\1\b)+', re.IGNORECASE)
    '''
    \b = word boundary
    (\w+) captures the first word.
    ( \1\b)+ says: “one or more occurrences of a space followed by the same word, ending at a word boundary.”
    IGNORECASE makes case differences irrelevant.
    '''
    clean_text = typo_1.sub(' ', text)        # remove extra spaces
    clean_text = typo_2.sub('!', clean_text)  # fix exclamations
    clean_text = typo_3.sub(r'\1', clean_text) # remove dup words
    print(clean_text)

clean_text("I was super lucky    lucky to be there      !!!")
# "I was super lucky to be there !"
