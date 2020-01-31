import re

email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password = re.compile(r"[a-zA-Z0-9$%@#]{8,}\d")

ask_password = input("Enter password at least 8 char and up/low letters and %@#$ ").split()
password2 = '123zxcZXC$#@%8'

check = password.fullmatch(password2)
print(check)

# # "#$r7907@" static example
# i = 0
# while i < 3:
#     test_str = input('Enter password please')
    

#     matches = re.finditer(regex, test_str, re.MULTILINE)

#     for matchNum, match in enumerate(matches, start=1):
        
#         print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
#         for groupNum in range(0, len(match.groups())):
#             groupNum = groupNum + 1
            
#             print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
#     i += 1