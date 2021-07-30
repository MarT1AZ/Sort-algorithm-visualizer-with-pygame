# Sorting Visualizer

# Sorting algorithm visualizer


import sys
import math
import random
import pygame
import numpy as NP
from pygame.constants import KEYDOWN, K_RETURN, K_a, K_c, K_d, K_e, K_f, K_k, K_l, K_m, K_r, K_s, K_w, SCALED
pygame.init()
pygame.display.set_caption("Sorting Visualizer")
sys.setrecursionlimit(10**6)

#///COLOR//////////////////////////////////////////////////////////////
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,128,0)
black = (0,0,0)
purple = (127,0,255)
grey = (100,100,100)
yellow = (255,255,0)
brown = (160,82,45)
DarkBlue = (0,51,102)
#///COLOR//////////////////////////////////////////////////////////////

ScreenWidth = 1000
ScreenHeight = 1000
screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
OffSet = 0

#FONT
def AddText(name,size,color,x,y):
    font = pygame.font.Font('AllTheWayToTheSun-o2O0.ttf',size)
    text = font.render(name,True,color)
    screen.blit(text,(x,y))
#FONT

def DrawLine(SX,SY,EX,EY,WIDHT,COLOR):
    pygame.draw.line(screen,COLOR,(SX,SY),(EX,EY),WIDHT)


def DrawRect(X,Y,COLOR,width,height):
    pygame.draw.rect(screen,COLOR,[X,Y,width,height])

def DrawCircle(X,Y,Color,Radius):
    pygame.draw.circle(screen,Color,(X,Y),Radius)

def DrawUIbox1(X,Y,W,H):
    DrawRect(X + 2,Y + 2,black,W + 3,H + 3)
    DrawRect(X,Y,white,W,H)
    DrawRect(X + 1,Y + 1,DarkBlue,W - 2,H - 2)

def DrawSortOption(X,Y,SortName,Select):
    if Select:
        DrawCircle(X,Y,white,6)
        DrawCircle(X,Y,green,5)
        AddText(SortName,20,white,X + 20,Y - 10)
    else:
        DrawCircle(X,Y,white,6)
        DrawCircle(X,Y,black,5)
        AddText(SortName,20,white,X + 20,Y - 10)

def DrawArray(NumArray,Size,OffSet,highlight,color,height,L,R):
    Width_Element = ((ScreenWidth - (Size + 1) * OffSet)/Size)
    BaseHeight = ScreenHeight
    for i in range(1,Size + 1):
        height_element = height * NumArray[i]
        x_position = ((i - 1) * (OffSet + Width_Element) + Width_Element/2 + OffSet)
        if i == highlight:
            DrawLine(x_position,BaseHeight,x_position,BaseHeight - height_element,int(Width_Element/2),red)
        elif i == L or i == R:
            DrawLine(x_position,BaseHeight,x_position,BaseHeight - height_element,int(Width_Element/2),purple)
        else:
            DrawLine(x_position,BaseHeight,x_position,BaseHeight - height_element,int(Width_Element/2),color)

def ClearScreen(color):
    pygame.draw.rect(screen,color,[0,0,ScreenWidth,ScreenHeight])

SLOWNESS = 1
def DrawSortAnimation(NumArray,Size,highlight,color,height,L,R,delay):
    for i in range(1,delay + 1):
        ClearScreen(DarkBlue)
        DrawRect(0,0,DarkBlue,ScreenWidth,195)
        DrawLine(0,195,ScreenWidth,195,4,yellow)
        DrawArray(NumArray,Size,OffSet,highlight,color,height,L,R)
        pygame.display.update()

#array
def SetArray(Size,Range):
    Array = NP.arange(0,Size + 1)
    for i in range(1,Size + 1):
        Array[i] = random.randint(1,Range)
    return Array

def SetArrayRandom(Size):
    Array = NP.arange(0,Size + 1)
    for x in range(1,Size + 1):
        for i in range(1,Size + 1):
            if random.randint(1,2) == 1:
                index1 = random.randint(1,Size)
                index2 = random.randint(1,Size)
                tmp = Array[index1]
                Array[index1] = Array[index2] 
                Array[index2] = tmp
    return Array

def SetArrayRandomRange(Size,Range):
    Array = NP.arange(0,Size + 1)
    for i in range(1,Size + 1):
        Array[i] = random.randint(1,Range)
    for x in range(1,Size + 1):
        for i in range(1,Size + 1):
            if random.randint(1,2) == 1:
                index1 = random.randint(1,Size)
                index2 = random.randint(1,Size)
                tmp = Array[index1]
                Array[index1] = Array[index2] 
                Array[index2] = tmp
    return Array

def SetArrayReverse(Size):
    Array = NP.arange(0,Size + 1)
    for i in range(Size,0,-1):
        Array[i] = Size - i + 1
    return Array

def SetArraySort(Size):
    Array = NP.arange(0,Size + 1)
    for i in range(1,Size + 1):
        Array[i] = i
    return Array

def Max_(x,y):
    if x >= y:
        return x
    else:
        return y

def Min_(x,y):
    if x >= y:
        return y
    else:
        return x

def Euclidean_Distance(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1 - x2,2) + math.pow(y1 - y2,2))

def IsInCircle(x1,y1,x2,y2,radius):
    return Euclidean_Distance(x1,y1,x2,y2) <= radius

def IsInRect(x1,y1,width,height,x,y):
    return x >= x1 and x <= x1 + width and y >= y1 and y <= y1 + height

    
def FindMax(NumArray,Size):
    MaxIndex = 1
    for i in range(1,Size + 1):
        if NumArray[i] > NumArray[MaxIndex]:
            MaxIndex = i
    return NumArray[MaxIndex]

def HowMuchDigit(num):
    for i in range(0,2147483640):
        if math.pow(10,i) <= num and num < math.pow(10,i + 1):
            return i

def ReturnDigit(num,index):
    return int(num/math.pow(10,index)) % 10

def IsArraySort(NumArray,Size,Ascending):
    for i in range(1,Size):
        if Ascending:
            if NumArray[i] > NumArray[i + 1]:
                return False
        else:
            if NumArray[i] < NumArray[i + 1]:
                return False
    return True


def BubbleSort(NumArray,Size,Max,Delay):
    ArrayScale = ((ScreenHeight - 200)/Max)
    Sort = False
    tmp = 1
    n = 0
    while not Sort:
        Sort = True
        for i in range(1,Size - n):
            if NumArray[i] > NumArray[i + 1]:
                Sort = False
                tmp = NumArray[i]
                NumArray[i] = NumArray[i + 1]
                NumArray[i + 1] = tmp
                DrawSortAnimation(NumArray,Size,i + 1,white,ArrayScale,-1,Size - n + 1,Delay)
            DrawSortAnimation(NumArray,Size,i,white,ArrayScale,-1,Size - n + 1,Delay)
        n += 1

def Heapify(NumArray,Size,MaxSize,Max,Delay):
    ArrayScale = ((ScreenHeight - 200)/Max)
    MaxHeap = False
    tmp = 0
    while not MaxHeap:
        MaxHeap = True
        for i in range(1,Size + 1):
            if i == 1:
                continue
            if NumArray[int(i/2)] < NumArray[i]:
                MaxHeap = False
                tmp = NumArray[i]
                NumArray[i] = NumArray[int(i/2)]
                NumArray[int(i/2)] = tmp
                DrawSortAnimation(NumArray,MaxSize,i,white,ArrayScale,-1,-1,Delay)
            DrawSortAnimation(NumArray,MaxSize,i,white,ArrayScale,-1,-1,Delay)
        

def HeapSort(NumArray,Size,Max,Delay):
    ArrayScale = ((ScreenHeight - 200)/Max)
    n = 0
    tmp = 0
    while n < Size:
        Heapify(NumArray,Size - n,Size,Max,Delay)
        tmp = NumArray[1]
        NumArray[1] = NumArray[Size - n]
        NumArray[Size - n] = tmp
        n += 1

def SelectionSort(NumArray,Size,Max,Delay):
    ArrayScale = ((ScreenHeight - 200)/Max)
    n = 0
    KeyAtIndex = 1
    for n in range(0,Size):
        KeyAtIndex = 1 + n
        for i in range(1 + n,Size + 1):
            if NumArray[i] < NumArray[KeyAtIndex]:
                KeyAtIndex = i
            DrawSortAnimation(NumArray,Size,i,white,ArrayScale,-1,-1,Delay)
        tmp = NumArray[KeyAtIndex]
        NumArray[KeyAtIndex] = NumArray[1 + n]
        NumArray[1 + n] = tmp
        DrawSortAnimation(NumArray,Size,-1,white,ArrayScale,1 + n,KeyAtIndex,Delay)

def InsertionSort(NumArray,Size,Max,Delay):
    ArrayScale = ((ScreenHeight - 200)/Max)
    Sort = False
    n = 1
    InsertionIndex = - 1
    while n < Size:
        for i in range(n,0,-1):
            if i == 1:
                if NumArray[i] >= NumArray[n + 1]:
                    InsertionIndex = i
                    break
            else:
                if NumArray[i] >= NumArray[n + 1] and NumArray[n + 1] >= NumArray[i - 1]:
                    InsertionIndex = i
                    break
                else:
                    continue
            DrawSortAnimation(NumArray,Size,i,white,ArrayScale,-1,-1,Delay)
        tmp = NumArray[n + 1]
        if InsertionIndex != - 1:
            for i in range(n + 1,InsertionIndex,-1): # n + 1 to InsertionIndex + 1
                NumArray[i] = NumArray[i - 1]
                DrawSortAnimation(NumArray,Size,i,white,ArrayScale,-1,-1,Delay)
            NumArray[InsertionIndex] = tmp
        InsertionIndex = -1
        n += 1

def ShakerSort(NumArray,Size,Max,Delay):
    ArrayScale = ((ScreenHeight - 200)/Max)
    l = 0
    r = 0
    Sort = False
    direction = "LtoR" # "RtoL"
    while not Sort:
        Sort = True
        if direction == "LtoR":
            for i in range(1 + l,Size - r):
                if NumArray[i] > NumArray[i + 1]:
                    NumArray[i],NumArray[i + 1] = NumArray[i + 1],NumArray[i]
                    Sort = False
                    DrawSortAnimation(NumArray,Size,i,white,ArrayScale,l + 1,Size - r,Delay)
                    DrawSortAnimation(NumArray,Size,i + 1,white,ArrayScale,l + 1,Size - r,Delay)
                DrawSortAnimation(NumArray,Size,i,white,ArrayScale,l + 1,Size - r,Delay)
            r += 1
            direction = "RtoL"
        else:
            for i in range(Size - r,l,-1):
                if NumArray[i] < NumArray[i - 1]:
                    NumArray[i],NumArray[i - 1] = NumArray[i - 1],NumArray[i]
                    Sort = False
                    DrawSortAnimation(NumArray,Size,i,white,ArrayScale,l + 1,Size - r,Delay)
                    DrawSortAnimation(NumArray,Size,i - 1,white,ArrayScale,l + 1,Size - r,Delay)
                DrawSortAnimation(NumArray,Size,i,white,ArrayScale,l + 1,Size - r,Delay)
            l += 1
            direction = "LtoR"

def Merge(NumArray,L,M,R,Size,Max,Delay):
    ArrayScale = ((ScreenHeight - 200)/Max)
    Lsize = M - L + 1
    Rsize = R - (M + 1) + 1
    SubArrayL = NP.arange(0,Lsize + 1) #use only 1 to Lsize
    SubArrayR = NP.arange(0,Rsize + 1) #use only 1 to Rsize
    for l in range(1,Lsize + 1):
        SubArrayL[l] = NumArray[L + l - 1]
    for r in range(1,Rsize + 1):
        SubArrayR[r] = NumArray[M + 1 + r - 1]
    i = 1
    j = 1
    k = L
    while i <= Lsize and j <= Rsize:
        if SubArrayL[i] > SubArrayR[j]:
            NumArray[k] = SubArrayR[j]
            j += 1
            DrawSortAnimation(NumArray,Size,j,white,ArrayScale,L,R,Delay)
        else:
            NumArray[k] = SubArrayL[i]
            i += 1
            DrawSortAnimation(NumArray,Size,i,white,ArrayScale,L,R,Delay)
        k += 1
        DrawSortAnimation(NumArray,Size,k,white,ArrayScale,L,R,Delay)

    while i <= Lsize:
        NumArray[k] = SubArrayL[i]
        i += 1
        k += 1
        DrawSortAnimation(NumArray,Size,i,white,ArrayScale,L,R,Delay)
        DrawSortAnimation(NumArray,Size,k,white,ArrayScale,L,R,Delay)
    while j <= Rsize:
        NumArray[k] = SubArrayR[j]
        j += 1
        k += 1
        DrawSortAnimation(NumArray,Size,j,white,ArrayScale,L,R,Delay)
        DrawSortAnimation(NumArray,Size,k,white,ArrayScale,L,R,Delay)




def MergeSort(NumArray,Size,Max,Delay):
    ArrayScale = ((ScreenHeight - 200)/Max)
    MergeSize = 1
    leftStart = 1
    while MergeSize <= Size:
        #for i in range(1,Size + 1,MergeSize):
        leftStart = 1
        while leftStart <= Size:
            # if i + MergeSize >= Size:
            #     L = i
            #     R = Size
            #     M = math.floor((L + R)/2)
            #     Merge(NumArray,L,M,R,Size,Max)
            #     DrawSortAnimation(NumArray,Size,M,white,ArrayScale,L,R)
            # else:
            L = leftStart
            R = Min_(L +  2 * MergeSize - 1,Size)
            M = Min_(L + MergeSize - 1,Size)
            Merge(NumArray,L,M,R,Size,Max,Delay)
            DrawSortAnimation(NumArray,Size,M,white,ArrayScale,L,R,Delay)
            leftStart += 2 * MergeSize 

        MergeSize *= 2

def partition(NumArray,L,H,Size,Max,Delay):
    pivot = NumArray[H]
    i = L - 1

    for j in range(L,H):
        if NumArray[j] <= pivot:
            i += 1
            NumArray[i],NumArray[j] = NumArray[j],NumArray[i]
            DrawSortAnimation(NumArray,Size,i,white,ArrayScale,L,H,Delay)
        DrawSortAnimation(NumArray,Size,j,white,ArrayScale,L,H,Delay)
    NumArray[i + 1],NumArray[H] = NumArray[H],NumArray[i + 1]
    return i + 1

def QuickSort(NumArray,L,H,Size,Max,Delay): # L is 1 , H is Size
    if L < H:
        M = partition(NumArray,L,H,Size,Max,Delay)
        QuickSort(NumArray,L,M - 1,Size,Max,Delay)
        QuickSort(NumArray,M + 1,H,Size,Max,Delay)





    







def DrawPlus(x,y,width,color):
    DrawLine(x - 4,y,x + 4,y,width,color)
    DrawLine(x,y - 4,x,y + 4,width,color)

def DrawMinus(x,y,width,color):
    DrawLine(x - 4,y,x + 4,y,width,color)
    










        
        

        



        


    
            
    
                







   


Sort_Option = "QuickSort"
ArraySizeDefault = 500
NumArray1Size = ArraySizeDefault # MAX 333 OFFSET = 1
NumArray1 = SetArrayRandom(NumArray1Size)
NumArraySize2 = ArraySizeDefault
NumArrayRange = 300
HighestElement = FindMax(NumArray1,NumArray1Size)

Sort = True
UI_on = True
T = True
F = False
a = 1
b = 2
ClickCooldown = 20
ClickAllow = 5
#print(NumArray)
#NumArray = BubbleSort(NumArray,NumArraySize,False)
#print(NumArray)

running = T
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = F
    keys = pygame.key.get_pressed()
    mx ,my = pygame.mouse.get_pos()
    Coordinate_mouse = NP.array([mx,my])
    click = pygame.mouse.get_pressed()
    ClearScreen(DarkBlue)

    if UI_on:
        DrawRect(0,0,DarkBlue,ScreenWidth,195)
        DrawLine(0,195,ScreenWidth,195,4,yellow)

        DrawRect(22,22,black,203,33) # shadow
        DrawRect(20,20,white,200,30)
        DrawRect(21,21,DarkBlue,170,28) 
        DrawRect(192,21,DarkBlue,27,13)
        DrawRect(192,35,DarkBlue,27,14)
        DrawPlus(205,27,2,white)
        DrawMinus(205,41,2,white)
        if IsInRect(192,21,27,13,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            NumArraySize2 += 1
        if IsInRect(192,35,27,14,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            NumArraySize2 -= 1
            if NumArraySize2 < 1:
                NumArraySize2 = 1
        AddText("Array Size : " + str(NumArraySize2),20,white,24,28)




        DrawRect(22,72,black,203,33) # shadow
        DrawRect(20,70,white,200,30)
        DrawRect(21,71,DarkBlue,170,28)
        DrawRect(192,71,DarkBlue,27,13)
        DrawRect(192,85,DarkBlue,27,14)
        DrawPlus(205,77,2,white)
        DrawMinus(205,91,2,white)
        if IsInRect(192,71,27,13,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            NumArrayRange += 1
        if IsInRect(192,85,27,14,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            NumArrayRange -= 1
            if NumArrayRange < 1:
                NumArrayRange = 1
        AddText("Range : " + str(NumArrayRange),20,white,24,78)




        DrawUIbox1(20,120,55,30)
        AddText("play",20,yellow,28,124)
        if IsInRect(20,120,55,30,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            Sort = F

        DrawUIbox1(100,120,90,30)
        AddText("Delay : " + str(SLOWNESS),20,white,108,124)

        DrawUIbox1(200,120,30,30)
        DrawPlus(215,135,2,white)
        if IsInRect(200,120,30,30,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            SLOWNESS += 1

        DrawUIbox1(240,120,30,30)
        DrawMinus(255,135,2,white)
        if IsInRect(240,120,30,30,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            SLOWNESS -= 1
            if SLOWNESS < 1:
                SLOWNESS = 1

        DrawUIbox1(240,70,130,30)
        AddText("random range",20,yellow,249,75)
        if IsInRect(240,70,130,30,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            NumArray1 = SetArrayRandomRange(NumArraySize2,NumArrayRange)
            HighestElement = FindMax(NumArray1,NumArraySize2)
            NumArray1Size = NumArraySize2



        DrawUIbox1(240,20,80,30)
        AddText("random",20,yellow,249,25)
        if IsInRect(240,20,80,30,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            NumArray1 = SetArrayRandom(NumArraySize2)
            HighestElement = FindMax(NumArray1,NumArraySize2)
            NumArray1Size = NumArraySize2


        DrawUIbox1(340,20,60,30)
        AddText("Sort ",20,yellow,349,25)
        if IsInRect(340,20,60,30,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            NumArray1 = SetArraySort(NumArraySize2)
            NumArray1Size = NumArraySize2
            HighestElement = FindMax(NumArray1,NumArraySize2)



        DrawUIbox1(420,20,90,30)
        AddText("Reverse ",20,yellow,429,25)
        if IsInRect(420,20,90,30,mx,my) and click[0] == 1 and ClickCooldown >= ClickAllow:
            ClickCooldown = 0
            NumArray1 = SetArrayReverse(NumArraySize2)
            NumArray1Size = NumArraySize2
            HighestElement = FindMax(NumArray1,NumArraySize2)



        DrawUIbox1(540,20,400,160)
        DrawSortOption(560,40,"Bubble Sort",Sort_Option == "BubbleSort")
        if IsInCircle(mx,my,560,40,6) and click[0] == 1 and ClickCooldown > ClickAllow:
            ClickCooldown = 0
            Sort_Option = "BubbleSort"
        DrawSortOption(560,80,"Heap Sort",Sort_Option == "HeapSort")
        if IsInCircle(mx,my,560,80,6) and click[0] == 1 and ClickCooldown > ClickAllow:
            ClickCooldown = 0
            Sort_Option = "HeapSort"
        DrawSortOption(560,120,"Selection Sort",Sort_Option == "SelectionSort")
        if IsInCircle(mx,my,560,120,6) and click[0] == 1 and ClickCooldown > ClickAllow:
            ClickCooldown = 0
            Sort_Option = "SelectionSort"
        DrawSortOption(560,160,"Insertion Sort",Sort_Option == "InsertionSort")
        if IsInCircle(mx,my,560,160,6) and click[0] == 1 and ClickCooldown > ClickAllow:
            ClickCooldown = 0
            Sort_Option = "InsertionSort"
        DrawSortOption(730,40,"Cocktail Shaker Sort",Sort_Option == "CocktailShakerSort")
        if IsInCircle(mx,my,730,40,6) and click[0] == 1 and ClickCooldown > ClickAllow:
            ClickCooldown = 0
            Sort_Option = "CocktailShakerSort"
        DrawSortOption(730,80,"Merge Sort",Sort_Option == "MergeSort")
        if IsInCircle(mx,my,730,80,6) and click[0] == 1 and ClickCooldown > ClickAllow:
            ClickCooldown = 0
            Sort_Option = "MergeSort"
        DrawSortOption(730,120,"Quick Sort",Sort_Option == "QuickSort")
        if IsInCircle(mx,my,730,120,6) and click[0] == 1 and ClickCooldown > ClickAllow:
            ClickCooldown = 0
            Sort_Option = "QuickSort"

        # Bubble
        # Heap
        # Selection
        # Insertion
        # cocktail




















    if not Sort:
        if Sort_Option == "BubbleSort":
            BubbleSort(NumArray1,NumArray1Size,HighestElement,SLOWNESS)
        elif Sort_Option == "HeapSort":
            HeapSort(NumArray1,NumArray1Size,HighestElement,SLOWNESS)
        elif Sort_Option == "SelectionSort":
            SelectionSort(NumArray1,NumArray1Size,HighestElement,SLOWNESS)
        elif Sort_Option == "InsertionSort":
            InsertionSort(NumArray1,NumArray1Size,HighestElement,SLOWNESS)
        elif Sort_Option == "CocktailShakerSort":
            ShakerSort(NumArray1,NumArray1Size,HighestElement,SLOWNESS)
        elif Sort_Option == "MergeSort":
            MergeSort(NumArray1,NumArray1Size,HighestElement,SLOWNESS)
        elif Sort_Option == "QuickSort":
            QuickSort(NumArray1,1,NumArray1Size,NumArray1Size,HighestElement,SLOWNESS)
        Sort = T
    ArrayScale = ((ScreenHeight - 200)/HighestElement)
    DrawArray(NumArray1,NumArray1Size,OffSet,-1,white,ArrayScale,-1,-1)
    
    
    

    






    ClickCooldown += 1
    pygame.display.update()