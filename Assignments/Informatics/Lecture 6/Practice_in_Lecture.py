'''
Created on 2016. 10. 6.

@author: korea
'''
print(abs(5)) #5
print(abs(-5)) #5
print(pow(2, 3)) #8
print(pow(7, 4)) #2401

max(7, 11) # 11
max(33, 125, 503, 1) #503
max(3*11, 5**3, 512-9, 1024**0) #503
max(3*11, pow(5, 3), 512-9, pow(1024, 0)) #503

# def name([parameter, ...]):
#     statements

def double(x):
    return 2 * x

double( 12 ) #24
double( 'lava' ) #lavalava
double([ 1 ,  2 ,  3 ])  #[ 1 ,  2 ,  3 ,  1 ,  2 ,  3 ]

def classify(rock):
    if rock in ['basalt', 'granite']:
        type = 'igeneous rock'
    elif rock in ['sandstone', 'shale']:
        type = 'sendimentary rock'
    else:
        type = 'metamorphic rock'
    return type # return leads result = type( = classify(stone))

stone = 'sandstone'
result = classfiy(stone)

def add(a):
    b= a + 1
    return b
def double(c):
    d = 2 * add(c)
    return d # scope could use local and global variables
value = 10
result = double(value)
print(result)

def sign(number):
    if number > 0:
        return 1
    elif number == 0:
        return 0
    else:
        return -1
print(sign(-9))

# if there is no specific value in return, it becomes 'None'.