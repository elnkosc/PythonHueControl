import time
import random
import sys
from pythonhuecontrol.v1.bridge import Bridge
from pythonhuecontrol.v1.bridge import create_bridge_user
from pythonhuecontrol.v1.bridge import discover_bridge

if __name__ == '__main__':
    ip = discover_bridge()
    if len(ip) > 0:
        print("Found bridge at address: ", ip)
    else:
        print("Could not find bridge")
        exit(1)

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Please provide user ID of bridge (or leave empty to create new user: ")

    if len(username) == 0:
        print("Please push link button on bridge...")
        username, clientkey = create_bridge_user("http://" + ip + "/api", "PythonHueControl#TestApp")
        if username is not None:
            print("Username: ", username)
        else:
            print("Could not create user")
            exit(1)

    bridge = Bridge(username, "http://" + ip + "/api/" + username)

    print("\nConnected to bridge:", bridge.config.name)
    print("Software Version   :", bridge.config.swversion)
    print("API Version        :", bridge.config.apiversion)

    print("\nConnected Lights (", len(bridge.light_ids),"):", sep="")
    light_list = []
    for light_id in bridge.light_ids:
        light_list.append(bridge.light(light_id))
        print(light_list[-1].identity, " - ", light_list[-1].name, ", ", light_list[-1].type, ", On=",
              light_list[-1].state.on, sep="")

    print("\nDefined Groups (", len(bridge.group_ids), "):", sep="")
    group_list = []
    for group_id in bridge.group_ids:
        group_list.append(bridge.group(group_id))
        print(group_list[-1].identity, " - ", group_list[-1].type, ", ", group_list[-1].name, sep="")

    print("\nConnected Sensors (", len(bridge.sensor_ids), "):", sep="")
    sensor_list = []
    for sensor_id in bridge.sensor_ids:
        sensor_list.append(bridge.sensor(sensor_id))
        print(sensor_list[-1].identity, " - ", sensor_list[-1].type, ", ", sensor_list[-1].name, sep="")

    print("\nDefined Scenes (", len(bridge.scene_ids), "):", sep="")
    scene_list = []
    for scene_id in bridge.scene_ids:
        scene_list.append(bridge.scene(scene_id))
        print(scene_list[-1].identity, " - ", scene_list[-1].type, ", ", scene_list[-1].name, sep="")

    print("\nDefined Rules (", len(bridge.rule_ids), "):", sep="")
    rule_list = []
    for rule_id in bridge.rule_ids:
        rule_list.append(bridge.rule(rule_id))
        print(rule_list[-1].identity, " - ", rule_list[-1].name, ", ", rule_list[-1].status, sep="")

    print("\nDefined Schedules (", len(bridge.schedule_ids), "):", sep="")
    schedule_list = []
    for schedule_id in bridge.schedule_ids:
        schedule_list.append(bridge.schedule(schedule_id))
        print(schedule_list[-1].identity, " - ", schedule_list[-1].name, " - ", schedule_list[-1].description, sep="")

    print("\nDefined Resourcelinks (", len(bridge.resourcelinks_ids), "):", sep="")
    resourcelinks_list = []
    for resourcelinks_id in bridge.resourcelinks_ids:
        resourcelinks_list.append(bridge.resourcelinks(resourcelinks_id))
        print(resourcelinks_list[-1].identity, " - ", resourcelinks_list[-1].name, " - ",
              resourcelinks_list[-1].description, sep="")

    print("\nCapabilities:", sep="")
    print("Lights        : ", bridge.capabilities.lights.total - bridge.capabilities.lights.available, sep="")
    print("Groups        : ", bridge.capabilities.groups.total - bridge.capabilities.groups.available, sep="")
    print("Sensors       : ", bridge.capabilities.sensors.total - bridge.capabilities.sensors.available, sep="")
    print("Scenes        : ", bridge.capabilities.scenes.total - bridge.capabilities.scenes.available, sep="")
    print("Rules         : ", bridge.capabilities.rules.total - bridge.capabilities.rules.available, sep="")
    print("Schedules     : ", bridge.capabilities.schedules.total - bridge.capabilities.schedules.available, sep="")
    print("Resourcelinks : ", bridge.capabilities.resourcelinks.total - bridge.capabilities.resourcelinks.available, sep="")
    print("Streaming     : ", bridge.capabilities.streaming.total - bridge.capabilities.streaming.available, sep="")
    print("Amount of TZs : ", len(bridge.capabilities.timezones.values), sep="")

    input("\nPress ENTER to start random light effects on randomly selected lights (for 1 minute)...")
    sec = 0
    while sec < 60:
        time.sleep(1)
        light = light_list[random.randint(0, len(light_list)-1)]
        print(light.name, "-", light.productname, "-", light.manufacturername)
        if "dimmable" in light.type.lower():
            light.state.set(on=True, bri=random.randint(0, 254), transitiontime=0)
        if "color" in light.type.lower():
            light.state.set(on=True, xy=[random.random()*0.7, random.random()*0.8], transitiontime=0)
        sec += 1

    print("\nSwitching all lights off")
    for light in light_list:
        light.switch_off()
