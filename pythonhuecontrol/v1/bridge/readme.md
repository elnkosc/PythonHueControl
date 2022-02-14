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
- `.light_ids`
- `.group_ids`
- `.sensor_ids`
- `.scene_ids`
- `.rule_ids`
- `.schedule_ids`
- `.config.name` (read/write)
- `.config.whitelist` (read only)
- `.config.portalstate` (read only)
- `.config.apiversion` (read only)
- `.config.swversion` (readonly)
- `.config.proxyaddress` (read/write)
- `.config.proxyport` (read/write)
- `.config.linkbutton` (read/write)
- `.config.ipaddress` (read/write)
- `.config.mac` (readonly)
- `.config.netmask` (read/write)
- `.config.gateway` (read/write)
- `.config.dhcp` (read/write)
- `.config.portalservices` (readonly)
- `.config.utc` (read/write)
- `.config.localtime` (readonly)
- `.config.timezone` (read/write)
- `.config.zigbeechannel` (read/write)
- `.config.modelid` (readonly)
- `.config.bridgeid` (readonly)
- `.config.factorynew` (readonly)
- `.config.replacesbridgeid` (readonly)
- `.config.replacesbridgeid` (readonly)
- `.config.starterkitid` (readonly)
- `.config.touchlink` (read/write)  
- `.config.internetservices.internet` (readonly)
- `.config.internetservices.remoteaccess` (readonly)
- `.config.internetservices.time` (readonly)
- `.config.internetservices.swupdate` (readonly)
- `.config.backup.status` (readonly)
- `.config.backup.errorcode` (readonly)
- `.config.swupdate.checkforupdate` (read/write)
- `.config.swupdate.updatestate` (readonly)
- `.config.swupdate.notify` (read/write)
- `.config.swupdate.url` (read/write)
- `.config.swupdate.text` (read/write)
- `.config.swupdate.devicetypes.bridge` (readonly)
- `.config.swupdate.devicetypes.lights` (readonly)
- `.config.swupdate.devicetypes.sensors` (readonly)
- `.config.swupdate2.bridge` (readonly)
- `.config.swupdate2.checkforupdate` (read/write)
- `.config.swupdate2.state` (readonly)
- `.config.swupdate2.install` (read/write)
- `.config.swupdate2.lastchange` (readonly)
- `.config.swupdate2.lastinstall` (readonly)
- `.config.swupdate2.autoinstall.on` (readonly)
- `.config.swupdate2.autoinstall.updatetime` (readonly)  
#### Member functions:
- `.config.set(name=None, proxyaddress=None, proxyport=None, linkbutton=None, ipaddress=None, netmask=None, gateway=None, dhcp=None, utc=None, timezone=None, zigbeechannel=None, touchlink=None)`  
  `.swupdate.set(self, checkforupdate=None, notify=None, url=None, text=None)`  
  `.swupdate2.set(self, checkforupdate=None, install=None)`    
  Methods to set multiple values in operation. When setting multiple bridge parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.  
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
  `create_schedule(name, localtime, command, description="", status="enabled", autodelete="true", recycle="false")`  
  `create_rule(name, status, conditions, actions)`  
  `create_scene(name, recycle, scene_type, lights=None, group=None)`  
  `create_lightstates_scene(name, lights, appdata, lightstates)`  
  Creates new object.  
  RETURNS: Object or `None` if not successful
