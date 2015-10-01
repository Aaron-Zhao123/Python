import sys
import math
def main():
    print 'try this'
    x_ini = 2.0
    b_value = 3.0
    iteration_num = 5
    x=[None]*iteration_num  #initial x
    error=[None]*iteration_num  #initial error
    x[0] = x_ini

    #execute
    for i in range (0,iteration_num-1):
        x[i+1] = float (x[i] - float(x[i] * x[i] - b_value) / float(2 * x[i]))

    for i in range (0,iteration_num):
        error[i] = x[i] - math.sqrt(b_value)
    print x
    print error



    return
if __name__ == "__main__": main()

