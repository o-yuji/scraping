import re

URL = "http://www.amazon.co.jp/dp/B07T9TCPZX"

pattern = "https?://[^/]+/"

patternA = re.compile("xy+")

m = patternA.match("xyyyyy")
# print(m)

m = re.search("<.*?>","<html><head><title>test</title></head><body></body></html>")
# print(m)

m = re.search("[a-z]+","xyzXYZ",flags = re.IGNORECASE)

text = """
abc,789,RST
def,434,JDH
hij,834,HHD
"""

# m = re.findall("[a-z]+$",text,flags = re.MULTILINE)

pattern = re.compile("""
                     (?P<year>[0-9]{4})\/  #年/
                     (?P<month>[0-9]{1,2})\/  #月/
                     (?P<date>[0-9]{1,2}) #日
                     """,re.VERBOSE)

m = pattern.search("Today is 2023/07/09")

# m = re.match(pattern, URL)
# m = re.search("x.z","vxxyz")
# m = re.finditer("x.z","vxxyz vwxaz xgz xxz")
# m = re.fullmatch("x.z","xyz")
# m = re.sub("x.z","abc","vwxyz")
# m = re.search("","abcde")
# m = re.search("[a-zA-Z]","z")``
# m = re.search("(a|b)c","ac")
# m = re.search("\w","1")

if m is None:
  print("条件に一致しませんでした。")
else:
  print(m.group("year"))
  print(m.span())
  print(m)
  # for val in m:
  #   print(val.group())
  #   print(val.span())