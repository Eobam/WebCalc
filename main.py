
f = open('index.html', 'w')

html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Welcome To GFG</h2>

<p>Default code has been loaded into the Editor.</p>

</body>
</html>
"""

f.write(html_template)

# close the file
f.close()