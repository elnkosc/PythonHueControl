# PythonHueControl
The most **complete**, yet **simple** to use, Python library for Philips Hue control supporting both version 1 and 2 of the API.

## Overview
This Python package contains the classes and functions to interface with the Philips Hue bridge. It consists of the following files:
* pythonhuecontrol - generic definitions applicable to both v1 and v2 of the API
    * v1 - generic definitions for v1 of the API only
      * bridge - definitions for interacting with the bridge (configuration of and adding lights/sensors/rules/groups/scenes/schedules)
      * light - definition for controlling lights
      * group - definitions for controlling groups
      * rule - definitions for controlling rules
      * scene - definitions for controlling scenes
      * schedule - definitions for controlling schedules
      * sensor - definitions for controlling sensors
      * resourcelinks - definitions for controlling resourcelinks
    * v2 - UNDER CONSTRUCTION

Details can be found in teh README files for the different sub-packages.  

Hue Bridges up to software version 1948086000 support API V1. From version 1948086000 API V2 is support in addition to V1. In the future V1 will be depricated.

## Installation
This library is available from PyPi. Make sure Python and Pip are installed on your system. The from the commandline run:
```
pip install pythonhuecontrol
```
This will install interfaces for both version 1 and version 2 of the API.
