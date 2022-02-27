# V1 - ResourceLinks Interfaces
## Classes
### `class ResourceLinks`  
  Class containing methods for interacting with ResourceLinks. Properties of the ResourceLinks can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
#### Member variables:
- `.name` (read/write)
- `.description` (read/write)
- `.type` (read/write)
- `.classid` (read/write)
- `.owner` (read/write)
- `.recycle` (read/write)
- `.links` (read/write)
#### Member functions:
- `.set(name=None, description=None, resource_type=None, classid=None, owner=None, recycle=None, links=None)`
  Method to set multiple values in operation. When setting multiple parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.  
