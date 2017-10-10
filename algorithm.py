import math

def mysqrt(a,x):
    y=(x+a/x)/2
    if abs(y-x)< 0.0000000000001:
        return y
    else:
        return mysqrt(a,y)
def runsqr():
    print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff")
    print("__\t_________\t____________\t______")
    for i in range(1,10):
        print("%f\t%f\t%f\t%f"%(i,mysqrt(i,1),math.sqrt(i),mysqrt(i,1)-math.sqrt(i)))

def factorial(a):
    if a == 0:
        return 1
    sum=1
    for i in range(1,a+1):
        sum*=i
    return  sum

def eval_loop():
    while True:
        inputline=input('input string to execute')
        if inputline == 'done':
            break
        try:
            temp=eval(inputline)
            print(temp)
        except:
            print('wrong command')

def runramanujan():
    print(1e-15)
    k=0
    result=0
    while True:
        temp=factorial(4*k)*(1103+26390*k)/((factorial(k)**4)*396**(4*k))
        if temp < 1e-15:
            return 2*mysqrt(2,1)*result/9801
        result+=temp
        k+=1

def checkmilionnumber():
    for i in range(100000,1000000):
        tstr=str(i)
        if(tstr[2]==tstr[-1] and tstr[3]==tstr[-2]):
            tstr=str(i+1)
            if(tstr==tstr[::-1]):
                print(i)
    return 0

if __name__ == '__main__':
    print('work')
    checkmilionnumber()