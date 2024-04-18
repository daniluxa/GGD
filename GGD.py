import math as m

def v_calc(Q, d):
    v = 4 * Q * Q / (m.pi * d * d)
    return v

def Re_calc(V, d, nu):
    Re = V * d / (nu * 1e-6)
    return Re

def find_Re(Re, d, delta):
    if(Re < 2300):
        return 1
    elif (2300 < Re < 4000):
        return 2
    else:
        if(Re < 10 * d / delta):
            return 3
        elif(10 * d / delta < Re < 560 * d / delta):
            return 4
        else:
            return 5

def trenie_calc(Re_num, Re, d, delta):
    if(Re_num == 2):
        return 0
    elif(Re_num == 1):
        return 64/Re
    elif(Re_num == 3):
        return 0.3164 / (Re**0.25)
    elif(Re_num == 4):
        return 0.11 * (delta / d + 68 / Re)**(0.25)
    else:
        return 0.11 * (delta / d)**0.25

def rashod_calc(lyambda, l, d, V, g):
    h = lyambda * l * V**2 / (2 * g * d)
    return h

def main(Q, d, l, delta, nu):
    V, Re, Re_num, lyamda, h = 0, 0, 0, 0, 0
    g = 9.81

    V = v_calc(Q, d)
    Re = Re_calc(V, d, nu)
    Re_num = find_Re(Re, d, delta)
    if(Re_num == 1):
        print("Режим работы - ламинарный")
    elif(Re_num == 2):
        print("Режим работы - переходный")
    elif(Re_num > 2):
        print("Режим работы - турбулентный")
    else:
        print("Что-то пошло не так")
    lyamda = trenie_calc(Re_num, Re, d, delta)
    h = rashod_calc(lyamda, l, d, V, g)
    print("Коэффициент трения =", lyamda)
    print("Расход =", h * 1e4)


data = {
"Q" : 0,
"d" : 0,
"l" : 0,
"delta" : 0,
"nu" : 0
}

with open("data_input.txt", "r") as file:
    for i in data:
        i = file.read()      # считываем первую строку
        print(str1)

#main(0.05, 0.3, 2120, 0.0002, 1.004)


## auto-py-to-exe