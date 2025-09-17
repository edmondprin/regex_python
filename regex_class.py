'''
The ? matches zero or one instance of the preceding qualifier (= optional)
The * matches zero or more instances of the preceding qualifier.
The + matches one or more instances of the preceding qualifier.
The {n} matches exactly n instances of the preceding qualifier.
The {n,} matches n or more instances of the preceding qualifier.
The {,m} matches 0 to m instances of the preceding qualifier.
The {n,m} matches at least n and at most m instances of the preceding
qualifier.
{n,m}? or *? or +? performs a non-greedy match of the preceding
qualifier.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
The \d, \w, and \s match a digit, word, or space character, respectively.
The \D, \W, and \S match anything except a digit, word, or space
character, respectively. [abc] matches any character between the
square brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the square brackets.
(Hello) groups 'Hello' together as a single qualifier.



Use of backlash ("\") in Regex:

1/ escape character: to match literally characters that otherwise have special meanings:
. * + ? ( )

import re
pattern = re.compile(r'\.')
print(pattern.findall("a.b.c"))  # ['.', '.']

2/ special sequences: to introduce shortcuts for common character classes:
\d \D \w \W \s \S

pattern = re.compile(r'\d+')
print(pattern.findall("Room 42, Level 3"))  # ['42', '3']

3/ group references in substitution: refer to captured groups when doing replacements with .sub()
\1 (first group) \2 (second group, and so on)

pattern = re.compile(r'(\w+) (\w+)')
print(pattern.sub(r'\2, \1', "John Smith"))  # "Smith, John"

4/ word boundaries and anchors: introduces anchors that match positions rather than characters
\b (word boudary)  \B (non-word boundary)  \A (start of string) \Z (end of string)

pattern = re.compile(r'\bcat\b')
print(pattern.findall("The cat sat on the catalog"))  # ['cat']


'''



import re
mar = "hello"
for i in mar:
    if not i.isdigit():
        print("ok")


def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in text[0:3]:  # i is the character itself
        if not i.isdigit():
            return False
    if text[3] != "-":
        return False
    for i in text[4:7]:
        if not i.isdigit():
            return False
    if text[7] != "-":
        return False
    for i in text[8:12]:
        if not i.isdigit():
            return False
    return True


'''

 for i in range(8, 12): # i is the index
        if not text[i].isdigit():
            return False
'''

print(is_phone_number("512-534-7634"))
print(is_phone_number("hello maia"))


def is_phone_number(text):
    return bool(re.fullmatch(r"\d{3}-\d{3}-\d{4}", text))
# matches entire string only


# sliding window
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')

'''
1. Import the re module.
2. Pass the regex string to re.compile() to get a Pattern object.
3. Pass the text string to the Pattern object’s search() method to get a Match
object.
4. Call the Match object’s group() method to get the string of the matched text.
'''
# import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
print(match_obj.group())
# matches first occurence in any string

# raw string (r'') — always recommended in regex to avoid backslash issues.

match_list = phone_num_pattern_obj.findall(
    "415-234-2342 and also 534-123-6542")
print(match_list)


phone_re = re.compile(r'(\d\d\d)-(\d\d\d\-\d\d\d\d)')
mo = phone_re.search("My number is 415-555-4242.")
print(mo.group(1))  # returns first group of matched text
print(mo.group(2))  # returns second group of matched text
print(mo.group(0))  # returns full matched text
print(mo.group())  # idem
print(mo.groups())  # retrieve all groups at once in a tuple
area_code, phone_number = mo.groups()
print(f"Area code: {area_code}")
print(f"Phone number: {phone_number}")

# Using escape characters
pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d\-\d\d\d\d)')
mo = pattern.search("My phone number is (415) 555-4242.")
print(mo.group(1))
print(mo.group(2))

# Special meaning: $ () * + - . ? [\] ^ {|}


# Matching characters from alternate groups (using pipe as alternation operator)

# r'Cat|Dog' will match either cat or dog
import re
words_to_find = re.compile(f'Cat|Dog', re.IGNORECASE)
where_to_search_first = words_to_find.search("Hello, my name is Maia. I have 3 birds, 21 snakes, 10 cats and 5 dogs")
matches= words_to_find.findall("Hello, my name is Maia. I have 3 birds, 21 snakes, 10 cats and 5 dogs")
print(f"First: {where_to_search_first.group()}")
print(f"All: {matches}")

pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')
print(match.group())  # "Catch"
print(match.group(1))  # 'ch'
print(match.group(0))  # 'Catch'


# Returning all matches

# import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # no groups in regex
# ['415-444-9323', '212-435-1434']: returns list of strings if no groups in regex
print(pattern.findall('Cell: 415-444-9323 Work: 212-435-1434'))

# if groups in regex, returns list of tuples
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# [('412', '543', '1234'), ('532', '534', '2342'), ('234', '543', '2432')]
print(pattern.findall('Cell: 412-543-1234 Work: 532-534-2342 Home: 234-543-2432'))

# findall() does not overlap matches
pattern = re.compile(r'\d{3}')
print(pattern.findall('1234')) # ['123']
print(pattern.findall('12345')) # ['123']
print(pattern.findall('123456')) # ['123', '456']

# Qualifier syntax
'''
r'\d{3}-\d{3}-\d{4}'
qualifiers: r'\d' '-'
quantifiers: '{3}' '{4}'
'''

# Using character classes and negative character classes

vowel_pattern = re.compile(r'[aeiouAEIOU]') # same as 'a | e | i | o | u | A | E | I | O | U
print(len(vowel_pattern.findall("Maia")))
print(len(vowel_pattern.findall("mATTEO")))
print(len(vowel_pattern.findall("vERONICA")))
print(len(vowel_pattern.findall("edmond")))

# include ranges of letters and numbers
vowel_pattern = re.compile(r'[a-zA-Z0-9]') # match all lowercase letters, uppercase letters, and numbers. No need to escape characters such as () inside []
print(vowel_pattern.findall("Hello, j'a^&i 20{00 fr}a[ncs sur m<>/oi! $%"))

parentheses_finder = re.compile('[()]')
result = parentheses_finder.findall("hey (Darling), how are you?")
print(result)
# re.compile(r'\((.*?)\)') if you want to extract text in ()

# No need to add r'...' before the pattern if it doesn't contain any backslashes (\).


# Placing a ^ (caret) just after character class's opening makes it a negative character class: match all characters that are not in the character class.

consonant_pattern = re.compile(r'[^aeiouAEIOU]')
print(len(consonant_pattern.findall("Veronica")))
print(len(consonant_pattern.findall("Matteo")))
print(len(consonant_pattern.findall("Maia")))
print(len(consonant_pattern.findall("Edmond"))) 


# Shorthand character classes
'''
\d      Any numeric digit from 0 to 9 (0|1|2|3|4|5|6|7|8|9 or [0-9])
\D      Any character that is not a numeric digit from 0 to 9.
\w      Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W      Any character that is not a letter, numeric digit, or the underscore character.
\s      Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S      Any character that is not a space, tab, or newline character.
'''

pattern = re.compile(r'\d+\s\w+') # matches text with one or more digits (\d+), followed by whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+)
print(pattern.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"))


# Matching everything with dot character

at_re = re.compile(r'.at') # match any 3-character substring where the last two characters are at, the dot character will match just one character,
print(at_re.findall("The cat in the hat sat on the flat mat")) # ['cat', 'hat', 'sat', 'lat', 'mat']

# To match all whole words ending in "at"
at_re = re.compile(r'\b\w*at\b')
print(at_re.findall("The cat in the hat sat on the flat mat")) # ['cat', 'hat', 'sat', 'flat', 'mat']

'''
\b = word boundary
\w* = zero or more word characters
at = literal "at"
\b = another word boundary
'''

import re

text = "First Name: Edmond"
pattern = r"First Name: ([A-Za-z]+)"
match = re.search(pattern, text)

if match:
    print("group(0):", match.group(0))  # Full match → "First Name: Edmond"
    print("group(1):", match.group(1))  # Captured group → "Edmond"


# Quantifier syntax

# If not quantifier following a qualifier, the qualifier must appear exactly once: r'\d' = r'\d{1}'

# Matching an optional pattern (with ?)
# The ? flags the preceding qualifier as optional (should match 0 or more of preceding qualifier)

pattern = re.compile(r'42!?') # pattern ! is optional
print(pattern.search('42!')) # <re.Match object; span=(0, 3), match='42!'>
print(pattern.search('42')) # <re.Match object; span=(0, 2), match='42'>
print(pattern.search('4')) # None


pattern = re.compile(r'42?!')
print(pattern.search('42!')) # <re.Match object; span=(0, 3), match='42!'>
print(pattern.search('4!')) # <re.Match object; span=(0, 2), match='4!'>
print(pattern.search('42') == None) # True (because ! is required)


# to make multiple characters optional, place them in a group and put the ? after the group

pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match1 = pattern.search("My number is 415-333-2122")
print(match1.group()) # '415-333-2122'
print(match1.group(1)) # '415'
# print(match1.group(2)) = error since only 1 group is defined, we would need r'(\d{3})-(\d{3}-\d{4})'

match2 = pattern.search("Her phone number is 444-2354")
print(match2.group()) # '444-2354'
print(match2.group(0)) # '444-2354'


# Matching zero or more qualifiers (with *)
# * means match zero or more: The qualifier preceding the star can occur any number of times in the text: It can be completely absent or repeated over and over

pattern = re.compile(r'Eggs( and spam)*')
print(pattern.search('Eggs')) # <re.Match object; span=(0, 4), match='Eggs'>
print(pattern.search('Eggs and spam')) # <re.Match object; span=(0, 13), match='Eggs and spam'>
print(pattern.search('Eggs and spam and spam')) # <re.Match object; span=(0, 22), match='Eggs and spam and spam'>
print(pattern.search('Eggs and spam and spam and spam')) # <re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>


# Matching one or more qualifiers (with +)
# + requires qualifier to appear at least once (unlike *)

pattern = re.compile(r'Eggs( and spam)+')
print(pattern.search('Eggs')) # None
print(pattern.search('Eggs and spam')) # <re.Match object; span=(0, 13), match='Eggs and spam'>
print(pattern.search('Eggs and spam and spam')) # <re.Match object; span=(0, 22), match='Eggs and spam and spam'>
print(pattern.search('Eggs and spam and spam and spam')) # <re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>


# Matching a specific number of qualifiers
# Possibility to specify a range: (Ha){3,5} = min, max
# Can leave out 1st or 2nd number: (Ha){3,} / (Ha)(,5)
# (Ha){3} = HaHaHa
# (Ha){3,5} = (HaHaHa)|(HaHaHaHa)|(HaHaHaHaHa)

import re
haRegex = re.compile(r'(Ha){3}')
match1 = haRegex.search('HaHaHa')
print(match1.group()) # HaHaHa
print(match1) # <re.Match object; span=(0, 6), match='HaHaHa'>

match = haRegex.search('HaHa')
print(match == None) # True


# Greedy and non-greedy matching
# Python regex are greedy by default: in ambiguous situations, they will match the longest string possible.

import re
greedy_pattern = re.compile(r'(Ha){3,5}')
match1 = greedy_pattern.search('HaHaHaHaHa')
print(match1.group()) # HaHaHaHaHa

# Non-greedy (lazy) version of curly brackets (shortest string possible), must follow curly bracket with a question mark.
import re
lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHa')
print(match2.group()) # HaHaHa

# ? can declare a lazy match or an optional qualifier (2 different Regex meanings)


# Matching everything (using .*)
# . = any single character except newline
# * = zero or more of preceding character

import re
name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
name_match = name_pattern.search("First Name: Ed Last Name: Prin")
print(name_match.group(1))
print(name_match.group(2))

# .* = greedy

import re
greedy_re = re.compile(r'<.*>')
match1 = greedy_re.search('<To serve man> for dinner.>')
print(match1.group()) # <To serve man> for dinner.>


# .*? = lazy

lazy_pattern = re.compile(r'<.*?>')
match2 = lazy_pattern.search("<To serve man> for dinner.>")
print(match2.group()) # <To serve man>


# Matching newline characters (with re.DOTALL as 2nd argument)

# match everything up to the 1st newline
import re
no_newline = re.compile('.*')
print(no_newline.search('Serve the public trust.\nProtect the innocent.' \
'\nUphold the law.').group()) # Serve the public trust.

# match everything
newline_re = re.compile('.*', re.DOTALL)
print(newline_re.search('Serve the public trust.\nProtect the innocent.' \
'\nUphold the law.').group()) # Serve the public trust.\nProtect the innocent.\nUphold the law.


# Matching at the start and end of a string
# Use ^ at start of regex to indicate that match must occur at beginning of searched text
import re
begins_with_hello = re.compile(r'^Hello') # matches strings that begin with "hello"
print(begins_with_hello.search('Hello, world!')) # <re.Match object; span=(0, 5), match='Hello'>
print(begins_with_hello.search('He said "Hello."')) # None

# Use $ at end of regex to indicate that match must end with this regex pattern
import re
ends_with_number = re.compile(r'\d$') # matches strings that end with a numeric character between 0 and 9
print(ends_with_number.search('Your number is 42')) # <re.Match object; span=(16, 17), match='2'>
print(ends_with_number.search("Your number is fourty two.")) # None 


# Use ^ amd $ together to indicate that entire string must match the regex
# carrots cost dollars” to remember that the caret comes first and the dollar sign comes last.
import re
whole_string_is_num = re.compile(r'^\d+$') # matches strings that both begin and end with one or more numeric characters
print(whole_string_is_num.search('1234567890')) # <re.Match object; span=(0, 10), match='1234567890'>
print(whole_string_is_num.search('12345xyw67890')) # None

# You can also use \b to make a regex pattern match only on a word boundary:
# the start of a word, end of a word, or both the start and end of a word

import re
pattern = re.compile(r'\bcat.*?\b')
print(pattern.findall("The cat found a catapult catalog in the catacombs.")) # ['cat', 'catapult', 'catalog', 'catacombs']

# \B matches anything that is not a word boundary (useful for finding matches in the middle of a word)

import re
pattern = re.compile(r'\Bcat\B')
print(pattern.findall('certificate')) # Match
print(pattern.findall('catastrophe')) # No match


# Case-insensitive matching (using re.IGNORECASE or re.I)

pattern = re.compile(r'Robocop', re.I)
print(pattern.search("rOBOCop is so cool").group()) # rOBOCop
print(pattern.search("ROBOCop is so marvelous").group()) # ROBOCop

# Substituting strings (with sub())

import re
agent_pattern = re.compile(r'Agent \w+')
print(agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.')) # CENSORED contacted CENSORED.

# Back reference

import re
agent_pattern = re.compile(r'Agent (\w)\w*') # group 1 = first letter of agent's name
print(agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.')) # A**** contacted B****.
# The \1 in the regular expression string is replaced by whatever text was matched by group 1—that is, the (\w) group of the regular expression.

# Managing complex regexes with verbose mode (with re.VERBOSE)

'''
The re.VERBOSE flag means:
You can split the regex across multiple lines.
You can add spaces and comments inside the regex for readability.
Spaces are ignored unless escaped or inside a character class ([]).
'''

# pattern = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext\.)\s*\d{2,5})?)')

pattern = re.compile(r'''(
(\d{3}|\(\d{3}\))? # Optional area code (3 digits or 3 digits in parentheses)
(\s|-|\.)? # Optional separator (can be whitespace, dash or dot)
\d{3} # First three digits
(\s|-|\.) # Separator (mandatory: no ?)
\d{4} # Last four digits
(\s*(ext|x|ext\.)\s*\d{2,5})? # Optional extension
)''', re.VERBOSE)


# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE (with pipe character)
# re.compile() function takes only a single value as its second argument.

some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL)
some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
