f = open('newfile.txt', 'a')
lines = ['hello', 'world', 'welcome', 'to', 'file', 'IO']
f.writelines(lines)
f.close()