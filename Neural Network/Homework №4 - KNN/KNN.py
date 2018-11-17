import numpy as np
import pandas as pd
import scipy
from matplotlib import pylab, gridspec, pyplot as plt

plt.style.use('fivethirtyeight')

#Filename_reds = 'C:\\Users\\Данил\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\jupyter\\folder\\Homework_4_KNN\\reds.txt'
#Filename_blues = 'C:\\Users\\Данил\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\jupyter\\folder\\Homework_4_KNN\\blues.txt'

Filename_reds = "C:/Users/DOPopov/PycharmProjects/Homework_4_KNN/reds.txt"
Filename_blues = "C:/Users/DOPopov/PycharmProjects/Homework_4_KNN/blues.txt"

reds = pd.read_csv(Filename_reds, sep=',', header=None)
blues = pd.read_csv(Filename_blues, sep=',', header=None)
a = [x for x in range(800)]
red_pairs=[[i,reds[1][i]] for i in range(800)]
blue_pairs=[[i,blues[1][i]] for i in range(800)]

plt.scatter(a, [red_pairs[i][1] for i in range (800)], label='reds', color='r')
plt.scatter(a, [blue_pairs[i][1] for i in range (800)], label='blue', color='b')
plt.title('Plot')
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.show()

def guess_class(x,y,k):
    '''
        Функция отрисовки окрестности точки (x,y) и функция поиска расстояния между точками b,c на плоскости
    '''
    def draw_points(x,y):
        plt.figure(figsize=(5,5))
        plt.grid(ls='--')
        plt.scatter(a,[red_pairs[i][1] for i in range (800)], label='reds', color='r')
        plt.scatter(a,[blue_pairs[i][1] for i in range (800)], label='blue', color='b')
        plt.scatter(x,y)
        plt.xlim(x-4, x+4)
        plt.ylim(y-4, y+4)
        plt.show()
    draw_points(x,y)
    #for i in range (800):
        #distance_2d([a[i],red_pairs[i][1]],[x,y])
    
    def distance_2d(b,c):
        '''
           Функция подсчета расстояния между двумя точками. Здесь b и с -- координаты точек на плоскости.
        '''
        return (np.sqrt(np.power((x - b), 2) + np.power((y - c), 2)))
        
    def calculate_k_distances(class_points):
        '''
        Функция подсчета расстояния до k ближайших точек класса class_points
        '''
        arr_dist = np.zeros(800)
        for i in range (800):
            arr_dist[i] = distance_2d(class_points[i][0], class_points[i][1])
        arr_dist = np.sort(arr_dist)
        return (arr_dist[0:3])
        
            
    b = np.array(calculate_k_distances(blue_pairs)) # расстояния до ближайших k соседей класса blue
    r = np.array(calculate_k_distances(red_pairs)) # расстояния до ближайших k соседей класса red
    print (r)
     # вам необходимо проверить расстояния до ближайших k точек и посмотреть, какой класс встречается чаще всего. 
        #ГОЛОСОВАНИЕ
    print ("ГОЛОСОВАНИЕ")
    votes_b = 0
    votes_r = 0
    for i in range(3):
        if (b[i] > r[i]):
            votes_b += 1
        elif (b[i] < r[i]):
            votes_r += 1
    print ("blue: ", votes_b / 3, " reds:", votes_r / 3)
    if (votes_b > votes_r):
        print ("Эта точка принадлежит синему классу")
    elif (votes_b < votes_r):
        print("Эта точка принадлежит красному классу")

    print("ГОЛОСОВАНИЕ ЗАВЕРШЕНО")
guess_class(200,2,3)