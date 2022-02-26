import time
import random
import sys
from pythonhuecontrol.v1.bridge import Bridge
from pythonhuecontrol.v1.bridge import discover_bridge

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        raise Exception("No username provided")

    ip = discover_bridge()
    if len(ip) == 0:
        raise Exception("Could not find bridge")

    bridge = Bridge(username, "http://" + ip + "/api/" + username)

    # select random light if not provide as 2nd command line parameter
    if len(sys.argv) > 2:
        light = bridge.light(sys.argv[2])
    else:
        if len(bridge.light_ids) > 0:
            light = bridge.light(bridge.light_ids[random.randint(0, len(bridge.light_ids) - 1)])
        else:
            raise Exception("No lights found")

    # select random light if not provide as 2nd command line parameter
    if len(sys.argv) > 3:
        group = bridge.group(sys.argv[3])
    else:
        if len(bridge.group_ids) > 0:
            group = bridge.group(bridge.group_ids[random.randint(0, len(bridge.group_ids) - 1)])
        else:
            # use default group "0" (all lights)
            group = bridge.group("0")

    print("Light:", light.name)
    light.switch_on()
    time.sleep(1)
    light.single_blink()
    time.sleep(1)
    light.multiple_blinks()
    time.sleep(1)
    light.color_loop()
    time.sleep(1)
    light.brightness_loop()
    time.sleep(1)
    light.toggle()
    time.sleep(1)
    light.toggle()
    time.sleep(1)
    for i in range(15):
        light.set_rgb_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        time.sleep(1)

    print("Group:", group.name)
    group.switch_on()
    time.sleep(1)
    group.single_blink()
    time.sleep(1)
    group.multiple_blinks()
    time.sleep(1)
    group.color_loop()
    time.sleep(1)
    group.brightness_loop()
    time.sleep(1)
    for i in range(15):
        group.set_rgb_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        time.sleep(1)

    bridge.all_off()
