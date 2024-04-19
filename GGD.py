import math as m
import codecs
import matplotlib.pyplot as plt

data1 = {
    "Q" : 0,
    "d" : 0,
    "l" : 0,
    "delta" : 0,
    "nu" : 0
}

data2 = {
    "Q" : 0,
    "d" : 0,
    "l" : 0,
    "delta" : 0,
    "nu" : 0
}

data3 = {
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

def main(Q, d, l, delta, nu, number):
    V, Re, Re_num, lyamda, h = 0, 0, 0, 0, 0
    g = 9.81

    V = v_calc(Q, d)
    Re = Re_calc(V, d, nu)
    Re_num = find_Re(Re, d, delta)


    with codecs.open("data_output.txt", 'a', "utf-8") as file:
        file.write(f"{number}-й трубопровод\n")

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
        file.write(f"Расход = {h}\n\n")

def graph(d, l, delta, nu, n):
    Q_list = []
    h_list = []
    Q = 0
    V, Re, Re_num, lyamda, h = 0, 0, 0, 0, 0
    g = 9.81

    for i in range(12):
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


    with codecs.open("data_graph.txt", 'a', "utf-8") as file:
        file.write(f"{n}-ый трубопровод\n")
        for i in range(12):
            file.write(f"Q = {Q_list[i]}, h = {h_list[i]}\n")
        file.write("\n")

with open("data_input.txt", "r") as file:

    for i in data1:
        data1[i] = float(file.readline().split('=')[1].strip())
    file.readline()

    for i in data2:
        data2[i] = float(file.readline().split('=')[1].strip())
    file.readline()

    for i in data3:
        data3[i] = float(file.readline().split('=')[1].strip())


with codecs.open("data_output.txt", 'w', "utf-8") as file:
       file.write("")
with codecs.open("data_graph.txt", 'w', "utf-8") as file:
       file.write("")

main(data1["Q"], data1["d"], data1["l"], data1["delta"], data1["nu"], 1)
graph(data1["d"], data1["l"], data1["delta"], data1["nu"], 1)

main(data2["Q"], data2["d"], data2["l"], data2["delta"], data2["nu"], 2)
graph(data2["d"], data2["l"], data2["delta"], data2["nu"], 2)

main(data3["Q"], data3["d"], data3["l"], data3["delta"], data3["nu"], 3)
graph(data3["d"], data3["l"], data3["delta"], data3["nu"], 3)

main(data3["Q"], data3["d"], data1["l"] + data2["l"] + data3["l"], data3["delta"], data3["nu"], 4)
graph(data3["d"], data1["l"] + data2["l"] + data3["l"], data3["delta"], data3["nu"], 4)

plt.xlabel("Расход воды через трубопровод")
plt.ylabel("Общие потери напора")
plt.grid()
plt.legend(('1-ый', '2-ый', '3-ый', 'суммарный'))
plt.show()


## auto-py-to-exe