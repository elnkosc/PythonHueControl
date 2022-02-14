#Basic operation - Version 1
For version 1 of the API:
1. Discover the IPAddress of your Hue Bridge (optional/one-time).
    ```
    ip = discover_bridge()
    ```
3. Create a user for accessing the Hue Bridge (optional/one-time).
    ```
    user_id = create_bridge_user("http://" + ip + "/api", "MyHueApp#MyHueDevice")
    ```
4. Create a Bridge object providing the IP Address and the UserID.
    ```
    bridge = Bridge("MyHueBridge", "http://" + ip + "/api/" + user_id)
    ```
5. Interrogate the Bridge, create and modify Hue Objects. 
    ```
    for light_id in bridge.light_ids:
         light = bridge.light(light_id)
         light.switch_on()
         light.bri = 200
    ```
