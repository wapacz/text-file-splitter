#!/usr/bin/python

A = open("fileA.txt")
B = open("fileB.txt","w")
C = open("fileC.txt","w")
lines = A.readlines()
B.writelines(lines[:len(lines)/2])
C.writelines(lines[len(lines)/2:])
A.close()
B.close()
C.close()
