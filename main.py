import time
import random
from pythonhuecontrol.v1.bridge import Bridge

EFFECT_DURATION = 5.0

if __name__ == '__main__':
    bridge = Bridge("SB6zdKCx9eQiDvu7WzKII47MPSbqWsYCkFxM0h5r",
                    "http://192.168.1.48/api/SB6zdKCx9eQiDvu7WzKII47MPSbqWsYCkFxM0h5r")

    l = bridge.light("20")
    print(l.name)
    l.state.on = True
    print(l.name)
    l.state.on = False
    print(l.name)
    exit(1)

    dim_lights = []
    for group_id in bridge.groups:
        group = bridge.group(group_id)
        if "Woonkamer" in group.name:
            group.switch_on()
            for light_id in group.lights:
                light = bridge.light(light_id)
                if "Dimmable light" in light.type:
                    dim_lights.append([light, random.randint(0, 254), True])

    n = 10
    step = 25
    while n > 0:
        start = time.time()
        for i in range(0, 255, step):
            for light in dim_lights:
                light[0].state.bri = light[1]
                if light[2]:
                    light[1] += step
                    if light[1] > 254:
                        light[1] = 254
                        light[2] = False
                else:
                    light[1] -= step
                    if light[1] < 0:
                        light[1] = 0
                        light[2] = True

        stop = time.time()
        if stop - start > EFFECT_DURATION:
            if step > 0:
                step -= 1
        else:
            if step < 127:
                step += 1

        n -= 1
