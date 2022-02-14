#V1 - Light Interfaces
##Classes
### `class Light`  
  Class containing methods for interacting with a light. Properties of the light can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
####Member variables:
- `.name` (read/write)
- `.type` (readonly)
- `.modelid` (readonly)
- `.uniqueid` (readonly)
- `.manufacturername` (readonly)
- `.luminaireuniqueid` (readonly)
- `.streaming` (readonly)
- `.renderer` (readonly)
- `.proxy` (readonly)
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
####Member functions:
- `.set(name=None)`
- `.state.set(on=None, bri=None, hue=None, sat=None, xy=None, ct=None, alert=None, effect=None, colormode=None, reachable=None)`  
  Methods to set multiple values in operation. When setting multiple parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.  
- `.switch_on()`    
  Switches on the light.  
- `.switch_off()`    
  Switches off the light.  
- `.toggle()`    
  Toggles the light between on and off.  
