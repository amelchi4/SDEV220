with open('C:\\Users\\Total\\.vscode\\today.txt', 'r') as x:
    date = x.read()

print(date)

parse = date.split("/")
print(parse)
x.close()