round = int(input())

c, o = 0, 0
for i in range(round):
    correct_answer = input()
    challenger_answer = input()
    crack_answer = input()

    if correct_answer == challenger_answer:
        c += 1
        if crack_answer == 'correct':
            o += 1
    elif crack_answer == 'wrong':
        o += 1

if c > o or round/2 > crack_answer:
    print("challenger wins {} points against {}".format(c, o))
elif c < o:
    print("crack wins {} points against {}".format(o, c))
else:
    print("ex aequo: both contestants score {} points".format(c))

























round = int(input())

o = 0
c = 0

for i in range(round):

    correct_answer= input()
    challenger_answer = input()
    assessment = input()

    if correct_answer is challenger_answer:
        o += 1
        if assessment == 'correct':
            c += 1
    elif assessment == 'wrong':
            c += 1

if c < o or round/2 > c:
    print("challenger wins {} points against {}".format(o, c))
elif c > o:
    print("crack wins {} points against {}".format(c, o))
else:
    print("ex aequo: both contestants score {} points".format(o))
