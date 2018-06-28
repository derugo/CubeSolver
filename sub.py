import random
import numpy as np
import collections
import cv2
import timeit
association_other={'G':'OWRY4682',
             'R':'GWBY4484',
             'Y':'OGRB6666',
             'B':'RWOY4282',
             'O':'WGYB8884',
             'W':'OGRB2222'}
association_same={1:7,2:8,3:1,4:2,5:3,6:4,7:5,8:6}
color_1={'R':'0,0,240','B':'240,0,0','G':'0,240,0','O':'0,100,240','Y':'0,220,240','W':'240,240,240','X':'0,0,0'}

coor_association={0:'-12,-12',1:'-12,0',2:'-12,12',3:'0,12',4:'12,12',5:'12,0',6:'12,-12',7:'0,-12'}
sum1=0

img = cv2.imread('G:/rick.jpg',1)

def initialize():
    six_sides=['W','G','Y','R','B','O']
    shuffled_color=[]
    for color in six_sides:
        for i in xrange(8):
            shuffled_color.append(color)
    random.shuffle(shuffled_color)
    cube_state=[]
    temp=0
    for color in six_sides:
        cube_state.append((color,shuffled_color[temp:temp+8]))
        temp+=8
    return cube_state
def turn_other(mid_color,cube_state):
    temp_list3=list(association_other[mid_color])
    sum1=0
    iterate_color=['X','X','X']
    temp_color=[]

    for index,val in enumerate(temp_list3[0:4]):
        for face_color in cube_state:
            if val==face_color[0]:
                for y in range(int(temp_list3[index + 4]) - 1, int(temp_list3[index + 4]) + 2):
                    if y==9:
                      y=1
                    temp_color.append(face_color[1][y-1])
    d=collections.deque(temp_color)
    d.rotate(3)
    temp_color=list(d)
    index2=0
    for index,val in enumerate(temp_list3[0:4]):
        for face_color in cube_state:
            if val==face_color[0]:
                for y in range(int(temp_list3[index + 4]) - 1, int(temp_list3[index + 4]) + 2):
                    if y==9:
                        y=1
                    face_color[1][y-1]=temp_color[index2]
                    index2+=1

    # print cube_state
    return sum1
def turn(mid_color,cube_state):
    temp_list1=[]
    for color_list in cube_state:
        if color_list[0]==mid_color:
            for p1 in range(0,8):
                temp_list1.append(color_list[1][p1])
            for p in range(1,9):
                l=int(association_same[p]-1)
                color_list[1][p-1] = temp_list1[l]
    sum1=turn_other(mid_color,cube_state)
    return sum1

def color_face(coor_x,coor_y,col,img):

    color_list=list(color_1[col].split(","))
    color_list=map(int,color_list)

    for x in range(-4,5):
        for y in range(-4,5):
            for z in range(0,3):
                img[coor_x+x][coor_y+y][z]=color_list[z]
    return img

def one_side(mid_coor_x,mid_coor_y,mid_color,face_color):
    count=0
    color_face(mid_coor_x, mid_coor_y,mid_color, img)
    for d in range(0,8):
        list1=map(int,coor_association[d].split(","))
        color_face(mid_coor_x+list1[0],mid_coor_y+list1[1],face_color[count],img)
        count+=1
    return True

def driver():
    x=0
    y=0
    for color in cube_state:
        one_side(45+x, 45+y, color[0],color[1])
        x+=45
        y+=45
    return

def count_colors():
    count=0
    list2=[]
    for color1 in cube_state:
        for ct1 in color1[1]:
            list2.append(ct1)
    print collections.Counter(list2)
    return count

def reverse(mid_color,score1):

    for t in xrange(0,4):
        turn(choice,cube_state)
        pp=score()
        if pp>score1:
            # print "done"
            return
    return
def score():
    score_card=0
    for color_name in cube_state:
        for x in range(0,8):
            if color_name[0]=='R':
                if 'R'==color_name[1][x]:
                    score_card+=1
    return score_card

if __name__ == '__main__':
    start=timeit.default_timer()
    cube_state = initialize()
    choice1=['W','R','Y','G','B','O']
    score_card1=0
    choice=[]
    temp_score=00
    while(True):
        choice=random.choice(choice1)
        count=0
        turn(choice, cube_state)
        score_card1=score()
        count+=1
        if score_card1<temp_score:
            reverse(choice,score_card1)

        else:
            driver()
            temp_score = score_card1
            print score_card1,choice,count

        cv2.imshow('image', img)
        cv2.waitKey(1)
    stop=timeit.default_timer()
    print stop-start








