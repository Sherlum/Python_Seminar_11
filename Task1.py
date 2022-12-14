from itertools import cycle
from time import sleep


class TrafficLight:
    __color = cycle([
        {'signal': 'Красный', 'duration': 7},
        {'signal': 'Желтый', 'duration': 2},
        {'signal': 'Зеленый', 'duration': 6},
        {'signal': 'Желтый', 'duration': 2}
    ])

    def running(self):
        light = next(self.__color)
        print(f"Сигнал {light['signal']}, пауза {light['duration']} сек.")
        sleep(light['duration'])


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()