For this we will use a server with more computational power (e.g. Laptop)
Some information can be found [here](https://gist.github.com/oeway/fc4028c6f4db0b5a72e3372abf9bb437)


### Setting up ImJoy Server

Install imjoy server:

```
pip install imjoy
imjoy --serve --host=21.3.2.4
``

where the host is the local IP address from the server (0.0.0.0 or 127.0.0.1 do not work?)

### ImJoy client

Run this python file on the server (e.g. Laptop) to generate a ImJoy plugin which will be called from Jupyter Notebook (e.g. Opentrons)

```py
from imjoy import connect_to_server

def localize(image):
    return image*2

async def main():
    ws = await connect_to_server(name="localization", server_url="http://21.3.2.4:9527")
    ret = await ws.generate_token()
    print('workspace = "'+ws.config["workspace"]+'"')
    print('token = "'+ret["token"]+'"')
    await ws.export({"localize": localize})

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    #loop.run_forever() # oncumment it if you have it outside a jupyter notebook environment
```

This will give you the `workspace` and `token` in a very cryptic way. Note it for later:

```py
=====workspace=======
 ad34b65f-748a-4ece-9136-a13610b3149e localization
=============token===============
imjoy@eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsiYWQzNGI2NWYtNzQ4YS00ZWNlLTkxMzYtYTEzNjEwYjMxNDllIl0sImV4cGlyZXNfYXQiOm51bGwsInVzZXJfaWQiOiIxODRhNDU3ZC0zNDU0LTRiYmMtYWZkOC1mOWIzNWM1ODk3YjgiLCJwYXJlbnQiOiJhZDM0YjY1Zi03NDhhLTRlY2UtOTEzNi1hMTM2MTBiMzE0OWUiLCJlbWFpbCI6bnVsbCwicm9sZXMiOltdfQ.vy2V9eLQav8gKqTlm79uPdVZdeyVpVymJSzPDrPexiE
```


### ImJoy Jupyer Notebook

This is mainly for debugging the server for example on the Laptop

```py
import numpy as np
from imjoy_rpc import connect_to_server

token = "imjoy@eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsiYWQzNGI2NWYtNzQ4YS00ZWNlLTkxMzYtYTEzNjEwYjMxNDllIl0sImV4cGlyZXNfYXQiOm51bGwsInVzZXJfaWQiOiIxODRhNDU3ZC0zNDU0LTRiYmMtYWZkOC1mOWIzNWM1ODk3YjgiLCJwYXJlbnQiOiJhZDM0YjY1Zi03NDhhLTRlY2UtOTEzNi1hMTM2MTBiMzE0OWUiLCJlbWFpbCI6bnVsbCwicm9sZXMiOltdfQ.vy2V9eLQav8gKqTlm79uPdVZdeyVpVymJSzPDrPexiE"
workspace = "ad34b65f-748a-4ece-9136-a13610b3149e"
serverip = "http://21.3.2.4"

ws = await connect_to_server(server_url=serverip+":9527",
                       workspace=workspace,
                       token=token)
localize_plugin = await ws.getPlugin("localization")
```

The return of the `localize_plugin` should give you something like:

```
{'localize': <function imjoy_rpc.rpc.RPC._gen_remote_method.<locals>.remote_method(*arguments, **kwargs)>,
 '_rintf': '400cdfe6-57db-4977-9187-8da5362966d5'}
```

Now we actually test the plugin:

```py
locations = await localize_plugin.localize(np.ones([100,100]))
print(locations)
```

which gives us:

```py
[[2. 2. 2. ... 2. 2. 2.]
 [2. 2. 2. ... 2. 2. 2.]
 [2. 2. 2. ... 2. 2. 2.]
 ...
 [2. 2. 2. ... 2. 2. 2.]
 [2. 2. 2. ... 2. 2. 2.]
 [2. 2. 2. ... 2. 2. 2.]]
```

### On the Opentrons

Due to the old version of the Jupyter Notebook, the Opentrons has to be used with a different code version:

```py
from imjoy_rpc import connect_to_server
import numpy as np
import asyncio

serverip = "http://21.3.2.4"
workspace = "406c3445-4c74-4a02-8df3-6fc0d01312bf"
token = "imjoy@eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsiNDA2YzM0NDUtNGM3NC00YTAyLThkZjMtNmZjMGQwMTMxMmJmIl0sImV4cGlyZXNfYXQiOm51bGwsInVzZXJfaWQiOiJjMTZlZTk4OS0zNWVjLTQzOTMtODdhNS03MjIwMGNlNzgyMTkiLCJwYXJlbnQiOiI0MDZjMzQ0NS00Yzc0LTRhMDItOGRmMy02ZmMwZDAxMzEyYmYiLCJlbWFpbCI6bnVsbCwicm9sZXMiOltdfQ.ek6glURO6KuHtj6K-YdnLYYy0ggoQ3Q_GJGR80rIRzc"
myimage = np.ones((100,100))

loop = asyncio.get_event_loop()
async def run_plugin():
    global localize_plugin
    global locations
    ws = await connect_to_server(server_url=serverip+":9527",
                           workspace=workspace,
                           token=token)
    localize_plugin = await ws.getPlugin("localization")
    locations = await localize_plugin.localize(myimage)
loop.create_task(run_plugin())
```

and in the next cell:

```py
localize_plugin
locations
```

will give you:

```py
array([[2., 2., 2., ..., 2., 2., 2.],
       [2., 2., 2., ..., 2., 2., 2.],
       [2., 2., 2., ..., 2., 2., 2.],
       ...,
       [2., 2., 2., ..., 2., 2., 2.],
       [2., 2., 2., ..., 2., 2., 2.],
       [2., 2., 2., ..., 2., 2., 2.]])
```



## Opentrons as the master

./generate.sh  -i http://localhost:5000/openapi.json   -p client   -o generated

  ./scripts/generate.sh  \
  -i http://localhost/openapi.json  \
  -p my_client  \
  -o generated

  ./scripts/generate.sh -i <openapi_json> -p <package_name> -o <output_path>
  [-n <import_name>] [--include-auth]
  [--] [*openapi-generator-args]

Purpose
