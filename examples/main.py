import time
import random
from datetime import datetime
from pythonhuecontrol.v1.bridge import Bridge
from pythonhuecontrol.v1 import map_from_dict
from pythonhuecontrol.v1.bridge import create_bridge_user
from pythonhuecontrol.v1.bridge import discover_bridge
from pythonhuecontrol.v1.scene import SceneLightState

EFFECT_DURATION = 4.0

if __name__ == '__main__':
    bridge = Bridge("SB6zdKCx9eQiDvu7WzKII47MPSbqWsYCkFxM0h5r",
                    "http://192.168.1.48/api/SB6zdKCx9eQiDvu7WzKII47MPSbqWsYCkFxM0h5r")

    print(bridge.config.name)
    s = bridge.scene("zhUd2vUGaSJ9Nb7")
    print(s.name)
    scl = SceneLightState(bri=254)
    s.lightstates["4"] = scl
    print(s.lightstates["4"].bri)
    exit(1)

    dim_lights = []
    for group_id in bridge.group_ids:
        group = bridge.group(group_id)
        if group.name in ["Woonkamer", "Tussenkamer", "Serre", "Keuken"]:
            group.switch_on()
            for light_id in group.lights:
                light = bridge.light(light_id)
                if "Dimmable light" in light.type:
                    dim_lights.append([light, random.randint(0, 254), True])

    y = map(lambda x: x[0].name, dim_lights)
    print(list(y))
    exit(1)

    n = 10
    step = 30
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
        print("step: ", step, " duration: ", stop-start)
        if stop - start > EFFECT_DURATION:
            if step < 125:
                step += 2
        else:
            if step > 1:
                step -= 2

        n -= 1
