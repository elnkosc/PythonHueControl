# V1 - Group Interfaces
## Classes
### `class Group`  
  Class containing methods for interacting with a group object. Properties of the group can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
#### Member variables:
- `.name` (read/write)
- `.type` (readonly)
- `.lights` (read/write)
- `.sensors` (read/write)
- `.modelid` (readonly)
- `.uniqueid` (readonly)
- `.group_class` (read/write)
- `.recycle` (read/write)
- `.lightlevel.state` (readonly)
- `.lightlevel.lastupdated` (readonly)
- `.lightlevel.dark` (readonly)
- `.lightlevel.dark_all` (readonly)
- `.lightlevel.daylight` (readonly)
- `.lightlevel.daylight_any` (readonly)
- `.lightlevel.lightlevel` (readonly)
- `.lightlevel.lightlevel_min` (readonly)
- `.lightlevel.lightlevel_max` (readonly)
- `.presence.lastupdated` (readonly)
- `.presence.presence` (readonly)
- `.presence.presence_all` (readonly)
- `.state.all_on` (readonly)
- `.state.any_on` (readonly)
- `.action.on` (read/write)
- `.action.bri` (read/write)
- `.action.hue` (read/write)
- `.action.sat` (read/write)
- `.action.xy` (read/write)
- `.action.ct` (read/write)
- `.action.alert` (read/write)
- `.action.effect` (read/write)
- `.action.transitiontime` (read/write)
- `.action.scene` (read/write)
- `.action.bri_inc` (read/write)
- `.action.hue_inc` (read/write)
- `.action.sat_inc` (read/write)
- `.action.xy_inc` (read/write)
- `.action.ct_inc` (read/write)  
#### Member functions:
- `.set(name=None, lights=None, sensors=None, group_class=None, recycle=None)`
- `.action.set(on=None, bri=None, hue=None, sat=None, xy=None, ct=None, alert=None, effect=None, transitiontime=None, scene=None, bri_inc=None, hue_inc=None, sat_inc=None, xy_inc=None, ct_inc=None)`  
  Methods to set multiple values in operation. When setting multiple parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.
- `.switch_on()`    
  Switches on the lights in the group.  
- `.switch_off()`    
  Switches off the lights in the group.  
