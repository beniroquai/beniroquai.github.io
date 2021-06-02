# Democratizing Labautomation using UC2, Opentrons, OpenFlexure and ImJoy

An simple open-source approach to bring automated liquid handling and high throughput microscopy to your lab.

---

## Preprint 

The preprint for the *Hi2*  accompanied with a series of applications ca be found on [**BIORXIV**]() 😊 

## *cell*STORM II

This project features:

```
- Large-scale well plate scanning microscope (standalone, UC2-based) 
- Open imaging platform for high-throughput experiments
- GRBL-based motor and Laser controler
- OpenFlexure Server-based GUI and control software
- ImJoy-based image processing system (with ImageJ.js)
- Sample protocols to control the OFM microscope with ImJoy and Opentrons
- Long-term experiments with small deviations of the FOV
- Autofocus, scanning, fluorescence microscopy
- costs <1000€ (for single-wavelength imaging)
```


<p align="center">
<img src="./images/main.png" width="600">
</p>

# Systemdiagram

<p align="center">
<img src="./images/SYSTEM.png" width="500">
</p>

## Subsystem: Hi2 - UC2 High-Throughput Microscope

<p align="center">
<img src="./images/Sub_Hi2.png" width="500">
</p>

## Subsystem: ImJoy - 

<p align="center">
<img src="https://github.com/imjoy-team/ImJoy/raw/master/docs/assets/imjoy-overview.jpg" width="500">
</p>

## Subsystem: Opentrons OT2

<p align="center">
<img src="https://opentrons.com/static/NGS-Library-Prep@2x-d0ab4c4b02a5a86d5d2048a41e2641e1.png" width="300">
</p>

## Subsystem: OpenFlexure Server 

[SRC](https://openflexure.org/projects/microscope/develop)
<p align="center">
<img src="https://openflexure.org/assets/plugins.png" width="500">
</p>




# Hardware

## CAD Designs

If you want to replicate the device, you can find a detailed description with all necessary parts to order in this repsitory:

[CAD-Repository](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/tree/master/CAD)

## Assembly Tutorials

We now also have a pictures tutorial with a step-by-step guide on how to build the cellSTORM microscope [here](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/tree/master/CAD#assembly)


## Electronics and Code

To move the lenses or control the Laser intensity, we relied on Espressife EPS32s. The drawings for the electronic connections as well as the code to control them wirelessly using MQTT can be found here:

[cellSTORM Electronics](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/tree/master/ELECTRONICS)

## Bill of Material (BOM)

Along with the 3D printed parts in the Github-repository, you need a set of mechanical, electrical and optical parts summarized in the BOM below:

***Dead Link?***: Ebay is not really a reliable source since resellers may discontinue the product. In case you're looking for a component which can not be found, file an issue [here](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/) - alternatively: Copy the name under "Details" and search for it in Ebay. (E.g. "3450 300mW 637nm Dot Laser Module TTL/analog 12VDC" site:laserlands.net) Good luck 🍀 

Amazon is more reliable, but personally we try to avoid ordering there (Sorry..). We try to update the list with Amazon links

|  Type | Details  |  Price | Link  |
|---|---|---|---|
| Laser 635/637 nm |  3450 300mW 637nm Dot Laser Module TTL/analog 12VDC |  50 € | [Laserlands](https://www.laserlands.net/diode-laser-module/600nm-640nm-orange-red-laser-module/635dot/200mw-300mw-637nm-638nm-laser-diode-module-ttl-stage-lighting-dj-show-12vdc.html)  |
| Objective Lens | BRESSER DIN-Objektiv 60x, NA 0.85, 160/0.17 |  45 € | [Ebay](https://www.ebay.de/itm/112674628997)  |
| 2x Mirror  | PF10-03-P01	Ø1" Protected Silver Mirror |  50 € | [Thorlabs](https://www.thorlabs.com/thorproduct.cfm?partnumber=PF10-03-P01)  |
| 2x XY-Stages  | XY Axis Manual Trimming Platform Linear Stage Tuning Sliding Table 40/50/60/90mm, 60x60mm |  80 € | [Ebay](https://www.ebay.de/itm/60x60mm-XY-Axis-Trimming-Station-Displacement-Platform-Linear-Stage-Sliding-Tabl/124016151256?hash=item1cdff04ad8:g:MxUAAOSwx3Vd-y2d)  |
| Longpass (640)  |  Chroma 675/50 well suitable for Alexa Fluor 647  |  200-350 € | [Chroma](https://www.ahf.de/en/products/spectral-analysis-photonic/optical-filters/individual-filters/bandpass-filters/600-699-nm/2448/675/50-et-bandpass)  |
| Ocular | MIKROSKOP OKULAR PAAR  PERIPLAN H 10 X  LEITZ WETZLAR GERMANY  |  10-90 € | [Wie-Tec](https://wie-tec.de/Leitz-Mikroskop-Okular-Periplan-GF-10X-mit-festen-Pointer) (Ebay is cheaper, 10x matters!)  |
| ESP32 | ESP32 ESP32S WLAN Dev Kit Board Development Bluetooth Wifi WROOM32 NodeMCU |  7 € | [Amazon](https://www.amazon.de/AZDelivery-NodeMCU-Development-Nachfolgermodell-ESP8266/dp/B071P98VTG/ref=sr_1_1_sspa?dchild=1&keywords=esp32+wroom&qid=1599391362&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExM0FXWE5FVTJFMkpYJmVuY3J5cHRlZElkPUEwMDA0MTA3MlIxS1BPNUpWRlFTNCZlbmNyeXB0ZWRBZElkPUEwNTEwODcyMkszVVFaWFlVOVk1VyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)  |
| LED Buk driver | 3x SPARKFUN ELECTRONICS INC. COM-13705 |  18 € | [Spparkfun](https://www.tme.eu/en/details/sf-com-13705/other-modules/sparkfun-electronics-inc/com-13705/)  |
| Wires  |  Various |  10 € | [Amazon](https://www.amazon.de/Donau-Elektronik-GMBH-Original-Kupfer/dp/B01BI1G88C/ref=sr_1_5?dchild=1&keywords=kabel+litze&qid=1599391500&sr=8-5)  |
| Powersupply  | 5V, 3A, Various |  10 € | [Amazon](https://www.amazon.de/HomeSpot-Raspberry-Ladeger%C3%A4t-Netzschalter-Kompatibel/dp/B078567K85/ref=sr_1_5?dchild=1&keywords=5V+netzteil+usb+3A&qid=1599391564&sr=8-5)  |
| Raspberry Pi + SD + Powersupply + Housing  | Raspberry Pi 3 Set /Bundle: 16GB SD-Karte, HDMI, original Netzteil und Gehäuse | 70 € | [Amazon](https://www.amazon.de/UCreate-Raspberry-Pi-Desktop-Starter/dp/B07BNPZVR7/ref=sr_1_3?dchild=1&keywords=Raspberry+Pi+set&qid=1599391626&sr=8-3)  |
| Optical Pickup | Objektiv Optik Laser KES-400A PLAYSTATION 3 Nicht Funktioniert für Ersatzteil (**HINT:** Look for KES-400A replacement parts @ Ebay; Sometimes you get 10 pieces for 10€) | 1 € | [ebay](https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=kes400a+&_sacat=0)  |
| PLA filament | Prusament PLA Prusa Galaxy Black 1kg | 25,00 € | [Prusa](https://shop.prusa3d.com/de/prusament/711-prusament-pla-prusa-galaxy-black-1kg.html)  |
| Cellphone+Camera| Huawei P20 Pro 128GB 6GB RAM Single Sim Twilight, TOP Zustand | 300 € | [Amazon](https://www.amazon.de/Huawei-P20-Pro-Dual-General%C3%BCberholt-Schwarz/dp/B07GBD8FQM/ref=sr_1_6?dchild=1&keywords=huawei+p20+pro&qid=1599391774&sr=8-6) |
| Ball Magents | T::A Kugelmagnete 5 6 10 mm N45 Neodym Magnete NdFeB Menge wählbar extrem stark | 10 € | [Amazon](https://www.amazon.de/eLander-Neodym-Super-Magnete-Glas-Magnetboards-Magnettafel-K%C3%BChlschrank/dp/B075V2G73J/ref=sr_1_5?dchild=1&keywords=kugelmagnete+5+mm&qid=1599391804&sr=8-5)  |
| Screws | M3 DIN912 Hex-Key Screws, *HINT:* screws need to be ferro-magnetic (i.e. galvanized!), M3 DIN912 at various lenght may work; we usually have tons of them from the [@openUC2](youseetoo.org)-Project | 10 € | [Amazon](https://www.amazon.de/Zylinder-Innensechskant-Schraube-Vollgewinde-verzinkt/dp/B01MRNRJDZ/ref=sr_1_2_sspa?dchild=1&keywords=m3+schrauben+verzinkt&qid=1599391871&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHWEMzTTZXM1kzMVUmZW5jcnlwdGVkSWQ9QTA2MTcwNzQzQ1ZHWUs1Rk1QUTRSJmVuY3J5cHRlZEFkSWQ9QTA1OTgyNTNPOU1KSzFaQlVIOEQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl)  |
| Micrometer Screw | RS Electronic 0,1 mm resolution | 40 € | [RS Electronics](https://de.rs-online.com/web/p/mikrometer/7857878/?cm_mmc=DE-PLA-DS3A-_-google-_-PLA_DE_DE_Mess-_und_Pr%C3%BCftechnik_Whoop-_-(DE:Whoop%21)+Mikrometer-_-7857878&matchtype=&pla-342919224201&gclid=Cj0KCQiA962BBhCzARIsAIpWEL0P7-vfA1X5h5AeTN2rp-olhvvnkT95evhjPH9cdIwxzO4EtaosYrkaAvGXEALw_wcB&gclsrc=aw.ds)  |

***ATTENTION:*** In case any parts are missing, please file an issue or contact us! We are happy to help out and to improve 😊 


# Software 

GOAL: 

## Nvidia Jetson Nano 

### Prerequirements 

### Installation 

### Testing


## Opentrons OT2
 
GOAL: 

### Prerequirements 

### Installation 

### Testing 
 
## OpenFlexure Microscope (Server/GUI)

### Step-by-step: GUI




## ImJoy inside Opentrons' Jupyter Notebook

For this we will use a server with more computational power (e.g. Laptop)

### Setting up ImJoy Server

Install imjoy server:

`
pip install imjoy
imjoy --serve --host=21.3.2.4
`

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
token = "imjoy@eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsiYTQ1NWRlYjktMzc5YS00Y2Q5LTg2MmQtZWMxMmE0NjBkMmQ2Il0sImV4cGlyZXNfYXQiOm51bGwsInVzZXJfaWQiOiIyOGZlYzNhMi03OWFjLTQyYWQtYjRmZi1iNTgxMWIxMjUyYTciLCJwYXJlbnQiOiJhNDU1ZGViOS0zNzlhLTRjZDktODYyZC1lYzEyYTQ2MGQyZDYiLCJlbWFpbCI6bnVsbCwicm9sZXMiOltdfQ.d2FfZMEB-5OyO0rkx7-FLfXFehq6n3A0lrCmrrNU-wM"
workspace = "a455deb9-379a-4cd9-862d-ec12a460d2d6"
serverip = "http://21.3.2.4"
import asyncio
loop = asyncio.get_event_loop()
async def run_plugin():
    ws = await connect_to_server(server_url=serverip+":9527", 
                           workspace=workspace, 
                           token=token)
    localize_plugin = await ws.getPlugin("localization")
    locations = await localize_plugin.localize(myimage)
    print(locations)
loop.create_task(run_plugin())
```


Not working yet...



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

## Setting up 

## Jupyter Notebook 

## REsults 

# OFM as the master 

Purpose 

## Setting up 

## Jupyter Notebook 

## REsults 



# Datasets 

We provide many datasets in a publicly accessible repository. Please have a look at [ZENODO]() [***Comming Soon - need to wait for all data first***]

***Note:*** Not all the experiments are fully documented. If you need additional experimental parameters, please don't hesitate to get back to us so that we can add this! 

# Tutorials
# Related projects 

[iGEM Marburg 2019](https://github.com/igemsoftware2019/iGemMarburg2019/blob/fe84cfb141d7be023d2438a85184a40772899c5b/GUI/ColonyPickingGUI/ColonyPickerGUI.py)

# Contribute

If you have a question or found an error, please file an issue! We are happy to improve the device!  

# License

Please have a look into the dedicated [License file](LICENSE.MD).

# Disclaimer

We do not give any guarantee for the proposed setup. Please use it at your own risk. Keep in mind that Laser source can be very harmful to your eye and your environemnt!
