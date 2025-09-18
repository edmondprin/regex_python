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


# Practice 1
import re

text = "Last night I was curious about that story I read about wild animals. So I visited https://www.nationalgeo.org and also http://wildanimals.org "

website_finder = re.compile(r'https?://[^\s]+')
# [^\s]+ is the same as \S+

'''
https? → matches http or https (s is optional).
:// → literal ://.
[^\s]+ → one or more characters that are not whitespace (so the URL stops at a space). It matches the longest contiguous run of characters that are not whitespace. It grabs “one or more non-whitespace characters,” greedily.
'''

# website_finder2 = re.match(r'^https', text)
# print(website_finder2.group())

find_those = website_finder.findall(text)
print(find_those)


# Practice #3

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
