#V1 - Schedule Interfaces
##Classes
### `class Schedule`  
  Class containing methods for interacting with a schedule object. Properties of a schedule can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
####Member variables:
- `.name` (read/write)
- `.description` (read/write)
- `.localtime` (read/write)
- `.starttime` (read/write)
- `.status` (read/write)
- `.autodelete` (read/write)
- `.command.address` (read/write)
- `.command.method` (read/write)
- `.command.body` (read/write)  
####Member functions:
- `.set(name=None, description=None, localtime=None, starttime=None, status=None, autodelete=None))`
- `.command.set(address=None, method=None, body=None)`  
  Methods to set multiple values in operation. When setting multiple parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.
