#!/usr/bin/python
# coding=utf-8

import platform
import os
import shutil
import sys
from xml.dom import minidom, Node
import random

class TodoElement:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.weight = 0
        self.time = 0
        self.uniqueness = True


RealList = []
haveTime = 0
thingSet = set()

def ReadXML():
    doc = minidom.parse('./config.xml')
    todolist = doc.getElementsByTagName('todolist')
    count = 0
    for element in todolist:
        ele = TodoElement()
        ele.id = int(element.attributes['id'].value)
        ele.name = element.attributes['name'].value
        ele.weight = int(element.attributes['weight'].value)
        ele.time = int(element.attributes['time'].value)
        if element.attributes['uniqueness'].value == "True":
            ele.uniqueness = True
        else:
            ele.uniqueness = False
        RealList.append(ele)
    return

def DoDice():
    global haveTime
    global thingSet
    totalweight = 0
    for thing in RealList:
        if thing.time > haveTime:
            continue
        if thing.uniqueness == True and thing.id in thingSet:
            continue
        totalweight = totalweight + thing.weight
    if totalweight == 0:
        return False
    rand = random.uniform(0, totalweight)
    for thing in RealList:
        if thing.time > haveTime:
            continue
        if thing.uniqueness == True and thing.id in thingSet:
            continue
        if rand > thing.weight:
            rand = rand - thing.weight
            continue
        else:
            haveTime = haveTime - thing.time
            if thing.uniqueness == True:
                thingSet.add(thing.id)
            print("id:", thing.id, thing.name, ", taketime:", thing.time)
            break
    return True

if __name__ == "__main__":
    haveTime = int(input("inputtime:"))
    ReadXML()
    while DoDice():
        continue
