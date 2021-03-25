# import re
# s = '[qwrtypsdfghjklzxcvbnm]'
# a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
# print('\n'.join(a or ['-1']))
import re

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
REGEX = '(?<=[' + CONSONANTS + '])([' + VOWELS + ']{2,})[' + CONSONANTS + ']'

match = re.findall(REGEX, input(), re.IGNORECASE)
if match:
    print(*match, sep='\n')
else:
    print('-1')


