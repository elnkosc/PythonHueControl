#V1 - Sensor Interfaces
##Classes
### `class Sensor`  
  Class containing methods for interacting with a sensor. Properties of the sensor can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
####Member variables:
- `.name` (read/write)
- `.type` (readonly)
- `.modelid` (readonly)
- `.uniqueid` (readonly)
- `.manufacturername` (readonly)
- `.swversion` (readonly)
- `.recycle` (readonly)
- `.config.on` (read/write)
- `.config.reachable` (readonly)
- `.config.battery` (readonly)
- `.state.presence` (read/write)  
####Member functions:
- `.set(name=None)`
- `.config.set(on=None)`
- `.state.set(presence=None)`  
  Methods to set multiple values in operation. When setting multiple parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.  
