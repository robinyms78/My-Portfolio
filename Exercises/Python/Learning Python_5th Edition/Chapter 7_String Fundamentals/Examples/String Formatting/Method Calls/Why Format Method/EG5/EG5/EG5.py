print("%(num)i = %(title)s" %dict(num = 7, title = "Strings"))
print("{num:d} = {title:s}".format(num = 7, title = "Strings"))
print("{num} = {title}".format(**dict(num = 7, title = "Strings")))

import string
t = string.Template("$num = $title")
print(t.substitute({"num":7, "title": "Strings"}))
print(t.substitute(num = 7, title = "Strings"))
print(t.substitute(dict(num = 7, title = "Strings")))