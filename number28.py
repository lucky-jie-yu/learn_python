#对文件的基本操作，包括open,read,write
with open("example.txt", "wt") as out_file:
    out_file.write("该文本会写到文件中\n看到我了吧！")
with open("example.txt", "rt") as in_file:
    text = in_file.read()

print(text)