# V1 - Rule Interfaces
## Classes
### `class Rule`  
  Class containing methods for interacting with a rule object. Properties of the rule can easily be accessed/modified by getting/setting class member values (that are implemented using getters/setters and will directly be mirrored on the bridge).
#### Member variables:
- `.name` (read/write)
- `.owner` (readonly)
- `.created` (readonly)
- `.lasttriggered` (readonly)
- `.timestriggered` (readonly)
- `.status` (read/write)
- `.conditions` (read/write)
- `.actions` (read/write)
#### Member functions:
- `.set(name=None, status=None, conditions=None, actions=None)`
  Method to set multiple values in operation. When setting multiple parameters, this method will only make a single REST call in comparison to using the member variables directly. Each assignment will result in a separate REST call.
### `class RuleAction`  
  Class containing action info.
#### Member variables:
- `.address` (read/write)
- `.method` (read/write)
- `.body` (read/write)
### `class RuleCondition`  
  Class containing condition info.
#### Member variables:
- `.address` (read/write)
- `.operator` (read/write)
- `.value` (read/write)
