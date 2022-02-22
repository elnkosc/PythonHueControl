# V1 - Bridge Interfaces
## Functions
- `discover_bridge()`  
  Scans the LAN for available Hue Bridges.  
  RETURNS: IP Address of a Hue Bridge if found, otherwise None.
- `create_bridge_user(uri, device_type, generate_client_key=False, wait_time=60)`  
  Creates a username on the Hue bridge by providing the API URL of the bridge and devicetype (consists of <app name>#<device name> by convention). Optionally creates a client API key. By default user has 60 seconds to press te link button on the bridge, but this delay may be changed by the user.  
  RETURNS: Username (or None in case of failure), Client Key (None in case not requested)  
## Classes
###`class Bridge`  
  Class containing methods for interacting with the bridge. Properties of the bridge can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
#### Member variables:
- `.light_ids` (list of IDs)
- `.group_ids` (list of IDs)
- `.sensor_ids` (list of IDs)
- `.scene_ids` (list of IDs)
- `.rule_ids` (list of IDs)
- `.schedule_ids` (list of IDs)
- `.config` (Configuration object)
#### Member functions:
- `light(light_id)`  
  `group(group_id)`  
  `sensor(sensor_id)`  
  `schedule(schedule_id)`  
  `scene(scene_id)`  
  `rule(rule_id)`  
  Methods to create objects from bridge assets.  
  RETURNS: object based on a provided id.  
- `search_lights()`  
  `search_sensors()`  
  Start searching for new lights/sensors.
- `new_sensors`  
  `new_lights`  
  RETURNS: new lights/sensors found.
- `create_group(name, lights, group_type="LightGroup", group_class="Other")`
  `create_schedule(name, localtime, address, method, body, description="", status="enabled", autodelete="true", recycle="false")`  
  `create_rule(name, status, conditions, actions)`  
  `create_scene(name, recycle, scene_type, lights=None, group=None)`  
  `create_lightstates_scene(name, lights, appdata, lightstates)`  
  Creates new object.  
  RETURNS: Object or `None` if not successful
