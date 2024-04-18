import math as m
import codecs
import matplotlib.pyplot as plt

data = {
    "Q" : 0,
    "d" : 0,
    "l" : 0,
    "delta" : 0,
    "nu" : 0
}

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
        if Re != 0:
            return (64/Re)
        else:
            return 0
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

    
    with codecs.open("data_output.txt", 'w', "utf-8") as file:
        if(Re_num == 1):
            file.write("Режим работы - ламинарный\n")
        elif(Re_num == 2):
             file.write("Режим работы - переходный\n")
        elif(Re_num > 2):
             file.write("Режим работы - турбулентный\n")
        else:
             file.write("Что-то пошло не так")
        lyamda = trenie_calc(Re_num, Re, d, delta)
        h = rashod_calc(lyamda, l, d, V, g)
        file.write(f"Коэффициент трения = {lyamda}\n")
        file.write(f"Расход = {h}\n")

def graph(d, l, delta, nu):
    Q_list = []
    h_list = []
    Q = 0
    V, Re, Re_num, lyamda, h = 0, 0, 0, 0, 0
    g = 9.81

    for i in range(20):
        qq = Q / 1000
        V = v_calc(qq, d)
        Re = Re_calc(V, d, nu)
        Re_num = find_Re(Re, d, delta)

        lyamda = trenie_calc(Re_num, Re, d, delta)
        h = rashod_calc(lyamda, l, d, V, g)

        h_list.append(h)
        Q_list.append(Q)
        Q += 5
    plt.plot(Q_list, h_list)
    plt.xlabel("Расход воды черех трубопровод")
    plt.ylabel("Общие потери напора")
    plt.show()

    with codecs.open("data_graph.txt", 'w', "utf-8") as file:
        for i in range(20):
            file.write(f"x = {Q_list[i]}, y = {h_list[i]}\n")

with open("data_input.txt", "r") as file:

    for i in data:
        data[i] = float(file.readline().split('=')[1].strip())

main(data["Q"], data["d"], data["l"], data["delta"], data["nu"])
graph(data["d"], data["l"], data["delta"], data["nu"])


## auto-py-to-exe