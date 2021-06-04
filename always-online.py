import requests, time

cookie = "bonk"

while True:

    xsrfRequest = requests.post("https://auth.roblox.com/v2/logout", cookies={
        '.ROBLOSECURITY': cookie
    })
    xtoken = xsrfRequest.headers["x-csrf-token"]

    reg_presence = requests.post('https://presence.roblox.com/v1/presence/register-app-presence', 
    
    data={
        "location": "Home",
        "placeId": 0,
        "disconnect": "true"
        },

    cookies={
        '.ROBLOSECURITY': cookie
            },

    headers={
        'x-csrf-token' : xtoken
    })

    print(reg_presence.text)

    time.sleep(15)
