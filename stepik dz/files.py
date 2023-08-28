# fw = open('filesss/file1.txt', 'w')
# fw.write("var")
# fw.close()

fr = open("../filesss/file.txt", 'r')
text = fr.read()
fr.close()
print(text)