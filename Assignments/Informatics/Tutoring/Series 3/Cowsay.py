strlist = input().split()
width = int(input())

full_sentence = " ".join(strlist)
if width > len(full_sentence):
    width = len(full_sentence)

contents = ""
line, count =" ", 0
for word in strlist:
    if len(line)+len(word) <= width+1:
        line += word+' '
        count += len(word)+1
    else:
        contents += '|{}|\n'.format(line.center(width+2))
        line =  " "+word+' '
        count = len(word)+1
contents += '|{}|\n'.format(line.center(width+2))

speech_bubble = "+{}+\n{}\n+{}+".format((width+2)*"-", contents.strip(),(width+2)*"-")

print(speech_bubble)
