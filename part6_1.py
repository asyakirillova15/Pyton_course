import time


class TrafficLight:
    __color = [('\033[31mк  ', 7), (' \033[33mж ', 2), ('  \033[32mз', 5)]

    def running(self):
        flag_ = True
        count = 0
        len_list = len(self.__color) - 1
        while True:
            if flag_:
                count += 1
            else:
                count -= 1

            if count == len_list:
                flag_ = False
            if count == 0:
                flag_ = True

            print('\r', end='')
            print(self.__color[count][0], end='')
            time.sleep(self.__color[count][1])


a = TrafficLight()
a.running()
