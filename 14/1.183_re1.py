import re

pattern = re.compile('this')

st = 'search this inside of this text please!'

a = re.search('this', st)
b = pattern.search(st)
c = pattern.match(st) 
d =  pattern.findall(st)
e = pattern.fullmatch(st)
print(a.span())
print(a.start())
print(a.end())
# it means group from regular expression
print(a.group())

print(b)
print(c)
print(d)