import csv
import numpy as np
from sklearn.preprocessing import normalize
import cv2 as cv
import math

def nondomsort(fitness):
    values1 = []
    values2 = []
    for fit in fitness:
        values1 += [fit[0]]
        values2 += [fit[1]]
    S=[[] for i in range(0,len(values1))]
    front = [[]]
    n=[0 for i in range(0,len(values1))]
    rank = [0 for i in range(0, len(values1))]

    for p in range(0,len(values1)):
        S[p]=[]
        n[p]=0
        for q in range(0, len(values1)):
            if (-values1[p] > -values1[q] and -values2[p] > -values2[q]) or (-values1[p] >= -values1[q] and -values2[p] > -values2[q]) or (-values1[p] > -values1[q] and -values2[p] >= -values2[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif (-values1[q] > -values1[p] and -values2[q] > -values2[p]) or (-values1[q] >= -values1[p] and -values2[q] > -values2[p]) or (-values1[q] > -values1[p] and -values2[q] >= -values2[p]):
                n[p] = n[p] + 1
        if n[p]==0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)
    i = 0
    while(front[i] != []):
        Q=[]
        for p in front[i]:
            for q in S[p]:
                n[q] =n[q] - 1
                if( n[q]==0):
                    rank[q]=i+1
                    if q not in Q:
                        Q.append(q)
        i = i+1
        front.append(Q)
    del front[len(front)-1]
    return front

def getdata(path):
    fitness = []
    gene = []
    dirpos = []
    gen = []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        for row in reader:
            if float(row[-2].replace('[','')) < 999999.0:
                gen += [int(row[0])]
                fitness += [[float(row[-2].replace('[','')), float(row[-1].replace(']',''))]]
                gene +=[[int(row[1].replace('[','')), int(row[2]),int(row[3]),int(row[4].replace(']',''))]]
                dirpos += [[[int(row[5].replace('[[','')),int(row[6].replace(']',''))],[int(row[7].replace('[','')),int(row[8].replace(']',''))],[int(row[9].replace('[','')),int(row[10].replace(']',''))],[int(row[11].replace('[','')),int(row[12].replace(']]',''))]]]
    return gen, fitness, gene, dirpos

def getfrontdata(path):
    fitness = []
    front = []
    gene = []
    dirpos = []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        for row in reader:
            if float(row[-2].replace('[','')) < 999999.0:
                front += [int(row[0])]
                fitness += [[float(row[-2].replace('[','')), float(row[-1].replace(']',''))]]
                gene +=[[int(row[1].replace('[','')), int(row[2]),int(row[3]),int(row[4].replace(']',''))]]
                dirpos += [[[int(row[5].replace('[[','')),int(row[6].replace(']',''))],[int(row[7].replace('[','')),int(row[8].replace(']',''))],[int(row[9].replace('[','')),int(row[10].replace(']',''))],[int(row[11].replace('[','')),int(row[12].replace(']]',''))]]]
    return front, fitness, gene, dirpos

def getbestsol(fitness, gene, dirpos):
    front = nondomsort(fitness)
    values1 = []
    values2 = []
    for fit in fitness:
        values1 += [fit[0]]
        values2 += [fit[1]]
    norm1 = values1 / np.linalg.norm(values1)
    norm2 =  values2 / np.linalg.norm(values2)
    val = []
    for n1,n2 in zip(norm1,norm2):
        val += [math.sqrt(n1**2 + n2**2)]
    i = 0
    for v in val:
        if min(val) == v:
            idx = i
        i+= 1
    return idx, values1, values2, front