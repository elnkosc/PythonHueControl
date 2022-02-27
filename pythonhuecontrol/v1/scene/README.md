# V1 - Scene Interfaces
## Classes
### `class Scene`  
  Class containing methods for interacting with a scene object. Properties of the scene can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
#### Member variables:
- `.name` (read/write)
- `.type` (readonly)
- `.group` (readonly)
- `.lights` (read/write)
- `.owner` (readonly)
- `.recycle` (readonly)
- `.locked` (readonly)
- `.picture` (readonly)
- `.image` (readonly)
- `.lastupdated` (readonly)
- `.version` (readonly)
- `.appdata.version` (readonly)
- `.appdata.data` (readonly)
- `.lightstates` (read/write)  
#### Member functions:
- `.set(name=None, lights=None)`
  Method to set multiple values in operation. When setting multiple parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.  
