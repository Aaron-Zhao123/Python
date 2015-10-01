import random
import sys
import os


def main():
    x_value=[1,0,1,0]
    d_value=[0,0,1,0]

    for j in range (0,4):
        if(j==0)
            MSD(d_valu)


    return


def MSD(vec_in,vec_out):
    tmp=int('1000',2)
    vec_out=bin(bin(vec_in&tmp)|vec_out)
    return vec_out;

def second_digit(vec_in,vec_out):
    tmp=int('0100',2)
    vec_out=bin(bin(vec_in,&tmp)|vec_out)
    return vec_out;

def thrid_digit(vec_in,vec_out):
    tmp=int('0010',2)
    vec_out=bin(bin(vec_in&tmp)|vec_out)
    return vec_out;

def LSD(vec_in,vec_out):
    tmp=int('0001',2)
    vec_out=bin(bin(vec_in&tmp)|vec_out)
    return vec_out;
