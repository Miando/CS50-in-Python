#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT", "No name")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>hello</title>
        </head>
        <body>""")
print("<h1>hello , {}</h1>".format(text1))

print("""</body>
        </html>""")
