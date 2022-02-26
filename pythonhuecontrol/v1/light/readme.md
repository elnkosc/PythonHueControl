# V1 - Light Interfaces
## Classes
### `class Light`  
  Class containing methods for interacting with a light. Properties of the light can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
#### Member variables:
- `.name` (read/write)
- `.type` (readonly)
- `.modelid` (readonly)
- `.uniqueid` (readonly)
- `.manufacturername` (readonly)
- `.productname` (readonly)
- `.luminaireuniqueid` (readonly)
- `.swversion` (readonly)
- `.state.on` (read/write)
- `.state.bri` (read/write)
- `.state.hue` (read/write)
- `.state.sat` (read/write)
- `.state.xy` (read/write)
- `.state.ct` (read/write)
- `.state.alert` (read/write)
- `.state.effect` (read/write)
- `.state.colormode` (read/write)
- `.state.reachable` (read/write)
- `.state.transitiontime` (write only)
- `.state.bri_inc` (write only)
- `.state.hue_inc` (write only)
- `.state.sat_inc` (write only)
- `.state.xy_inc` (write only)
- `.state.ct_inc` (write only)
- `.capabilities.certified` (readonly)
- `.capabilities.control.mindimlevel` (readonly)
- `.capabilities.control.maxlumen` (readonly)
- `.capabilities.control.colorgamuttype` (readonly)
- `.capabilities.control.colorgamut` (readonly)
- `.capabilities.control.ct.min` (readonly)
- `.capabilities.control.ct.max` (readonly)
- `.streaming.renderer` (readonly)
- `.streaming.proxy` (readonly)
#### Member functions:
- `.set(name=None)`
- `.state.set(on=None, bri=None, hue=None, sat=None, xy=None, ct=None, alert=None, effect=None, colormode=None, reachable=None, transitiontime=None, bri_inc=None, hue_inc=None, sat_inc=None, xy_inc=None, ct_inc=None)`  
  Methods to set multiple values in operation. When setting multiple parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.  
- `.switch_on()`    
  Switches on the light.  
- `.switch_off()`    
  Switches off the light.  
- `.toggle()`    
  Toggles the light between on and off.  
- `.set_rgb_color(red, green, blue)`  
  Set RGB color for color lights
- `.set_hex_color(hex_color)`  
  Set RGB color for color lights by providing hex string
- `.single_blink()`  
  Let light blink once
- `.multiple_blinks()`  
  Let light blink for 15 seconds
- `.color_loop()`  
  Let color light go through its full color palette
- `.brightness_loop()`  
  Let light go through its full brightness range
