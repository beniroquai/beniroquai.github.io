# cellSTORM 2

A low-cost superresolution imaging device based on a cellphone camera and photonic waveguide chips

---

## Abstract

In microscopic imaging, where an optimum between high throughput, high resolution, small time-scales and low light exposure is of high interest, a high price tag and complex optical systems is usually inevitable. This is especially true for super-resolution (SR) methods like single molecule imaging techniques (e.g. dSTORM, PALM, DNA-Paint). Recent advances in waveguide-based imaging have opened new opportunities by separating the illumination- and detection-path by taking advantage of the evanescent field inside a high refractive index photonic waveguide which excites fluorescently labeled cells growing on its surface (i.e. TIRF).
Combining this with recent advances of low cost and off-the-shelf components like cellphone cameras, entertainment lasers and optical-pickups (OPU), we built the first 3D printed microscope which can perform dSTORM measurements for an overall price of <1000€ fitting on the palm of hand. Using fluctuation-based SR methods like ESI or MUSCAL, this device can also perform inexpensive TIRF experiments in living environments (i.e. incubator). We show dSTORM results of fixed HeLa and HUVEC cells labeled with Alexa Fluo 647® to give a proof-of-principle for a change in paradigm – science for a dime.
With a lateral resolution of about 100nm, an axial sectioning of 150nm and a FOV of 400x400µm2 this device gives a new tool to biologists to study cell dynamics on the cheap. All sources and design files are shared in an online repository to attempt democratization in scientific research and make cutting-edge research not only available but also affordable.
Additionally we show the recent advances in the open-source toolbox UC2 which not only is good for out-reach activities in STEM-research but paving the way to democratize super-resolution microscopy.

## cellSTORM II

The compact device features:

```
- autofocus
- automatic coupling mechanism
- on-device superresolution imaging
- survives cell incubators for several days
- performs autonomous imaging over several days
- dSTORM with <100 nm optical resolution
- costs <1000€ (for single-wavelength imaging)
- optical resolution down to 100nm
- multiple wavelength can be used (sequentially)
- using photonic waveguide chips TIRF is possible
```


<p align="center">
<img src="./images/cellSTORM_v5.png" width="500">
</p>



## Super-Resolution using Fluctuating Intensity (SRRF, ESI, SOFI, etc..) 

Using SRRF from the Henrique lab it's possible to quickly increase the resolution even without complicated STORM protocols:

<p align="center">
<img src="./images/image_1.png" width="500">
</p>

The image of actin labelled HUVEC cells is acquired using a 60x, 0.85NA objective lens. While moving the coupling lens, the varying intensity pattern caused by a changing mode field pattern can be used to increase the lateral resolution of fluorescently labeled samples at low excitation power. This is suitable for live-cell imaging. 

## Super-Resolution using SMLM (*d*STORM)

With high enough coupling efficiency and laser intensity, the setup enables super-resolution with a final resolution <100nm on a large field of view (FOV). This is well suited not only for educational purposes, but also for research outside the ordinary research and optics labs. 

<p align="center">
<img src="./images/cellstorm_dstorm_hela_60x.png" width="500">
</p>

cellstorm_dstorm_hela_60x.png

# Hardware

## CAD Designs

If you want to replicate the device, you can find a detailed description with all necessary parts to order in this repsitory:

[CAD-Repository](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/tree/master/CAD)

We now also have a pictures tutorial with a step-by-step guide on how to build the cellSTORM microscope [here](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/tree/master/CAD#assembly)


## Electronics and Code

To move the lenses or control the Laser intensity, we relied on Espressife EPS32s. The drawings for the electronic connections as well as the code to control them wirelessly using MQTT can be found here:

[cellSTORM Electronics](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/tree/master/ELECTRONICS)

## Bill of Material (BOM)

Along with the 3D printed parts in the Github-repository, you need a set of mechanical, electrical and optical parts summarized in the BOM below: 

|  Type | Details  |  Price | Link  |
|---|---|---|---|
| Laser |  3450 300mW 637nm Dot Laser Module TTL/analog 12VDC |  50 € | [Laserlands](https://www.laserlands.net/diode-laser-module/600nm-640nm-orange-red-laser-module/200mw-300mw-637nm-638nm-laser-diode-module-ttl-stage-lighting-dj-show-12vdc.htmll)  |
| Objective Lens | BRESSER DIN-Objektiv 60x, NA 0.85, 160/0.17 |  45 € | [Ebay](https://www.ebay.de/itm/BRESSER-DIN-Objektiv-60x/112674628997)  |
| 2x Mirror  | PF10-03-P01	Ø1" Protected Silver Mirror |  50 € | [Thorlabs](https://www.thorlabs.com/thorproduct.cfm?partnumber=PF10-03-P01)  |
| 2x XY-Stages  | XY Axis Manual Trimming Platform Linear Stage Tuning Sliding Table 40/50/60/90mm, 60x60mm |  80 € | [Ebay](https://www.ebay.de/itm/XY-Axis-Manual-Trimming-Platform-Linear-Stage-Tuning-Sliding-Table-40-50-60-90mm/202315259419?var=502290711250)  |
| Longpass (640)  |  Various |  200 € | [Chroma]()  |
| Ocular | MIKROSKOP OKULAR PAAR  PERIPLAN H 10 X  LEITZ WETZLAR GERMANY  |  8 € | [Ebay](https://www.ebay.de/itm/MIKROSKOP-OKULAR-PAAR-PERIPLAN-H-10-X-LEITZ-WETZLAR-GERMANY/133235531027)  |
| ESP32 | 3x ESP32 ESP32S WLAN Dev Kit Board Development Bluetooth Wifi WROOM32 NodeMCU |  7 € | [Ebay](https://www.ebay.de/itm/ESP32-ESP32S-WLAN-Dev-Kit-Board-Development-Bluetooth-Wifi-WROOM32-NodeMCU/183862848786)  |
| LED Buk driver | 3x SPARKFUN ELECTRONICS INC. COM-13705 |  18 € | [Spparkfun](https://www.tme.eu/en/details/sf-com-13705/other-modules/sparkfun-electronics-inc/com-13705/)  |
| Wires  |  Various |  10 € | [ebay]()  |
| Nikel Blech 1mm x 40mm x 40mm  |  Various |  10 € | [ebay]()  |
| Screws, M3  |  Various |  10 € | [ebay]()  |
| Powersupply  | 5V, 3A, Various |  10 € | [ebay]()  |
| Raspberry Pi + SD + Powersupply + Housing  | Raspberry Pi 3 Set /Bundle: 16GB SD-Karte, HDMI, original Netzteil und Gehäuse | 70 € | [ebay](https://www.ebay.de/itm/Raspberry-Pi-3-Set-Bundle-16GB-SD-Karte-HDMI-original-Netzteil-und-Geh%C3%A4use/152322890678)  |
| Optical Pickup | Objektiv Optik Laser KES-400A PLAYSTATION 3 Nicht Funktioniert für Ersatzteil | 1 € | [ebay](https://www.ebay.de/itm/Objektiv-Optik-Laser-KES-400A-PLAYSTATION-3-Nicht-Funktioniert-fur-Ersatzteil/333375976216?hash=item4d9ec1b318:g:W~gAAOSwJytdEPeV)  |
| PLA filament | 3D Drucker Filament 1kg PLA 1,75mm ⌀ Durchmesser Spule Rolle 1000g Made in DE | 12,50 € | [ebay](https://www.ebay.de/itm/3D-Drucker-Filament-1kg-PLA-1-75mm-Durchmesser-Spule-Rolle-1000g-Made-in-DE/401619975552?var=671364352133)  |
| Cellphone+Camera| Huawei P20 Pro 128GB 6GB RAM Single Sim Twilight, TOP Zustand | 300 € | [ebay](https://www.ebay.de/itm/Huawei-P20-Pro-128GB-6GB-RAM-Single-Sim-Twilight-TOP-Zustand/202426288360?epid=245211024&_trkparms=ispr%3D1&hash=item2f218c08e8:g:fDwAAOSwcMhbjrHw&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qWU8wofHFb0GAwioguOTaoJZUEd6Kmj3qcf5WQVuTfMjy9le23ynzfCHdo66AJX8OIVzUlpON%2FSXRvziWE8fbjF%2FJbPnromf1vM3o2SZImfoOPAtwLwmT3LsX2zwLcBwc8L%2FlKsgTh4o9aG5VykR%2BMT3OKKmLus4xdturhn6hOxENJ%2FRQ7ui2g3jk%2B2DJtV0v3k8jIeY8mT6KnWO3nk1y0EEiRKICDeY6NC1EAHpCG%2B2D8DaP5CauTijjarDueiPS8sZ9PzZeQ3UobjknhhhzRNziWBz3WEiYZGqFaFBuZIh5CgoRQ0YVdVz3CaQt%2FG0vab9AeNHwLil3axIzGHdA%2Bw9DK8KmvarnacnhiqAID2qCldhiyO2HdJRPAFaZTtW%2F%2FC0w%2FILUJNntX%2BCReqNH%2FMCiUakZqbnUfRucVaooF%2Frgr9XlM2NC9FWCcpCJS7p6C7FL%2FAtYt%2BJ7twuiVXHGdoTPRGIdrBb%2Fw5%2FHIbF3%2BJpHW3gkE6H3wl990zHgZ5lwddpaq9ZRqEAhQLzjXC9tjakdwkxQ0hDQYuoYM2WuU5q7NQTF0R7uBg0JH3p7NPq%2FeoQlQnhZ1EwR8bzhCxe%2BM60n7na3Fst8CNr3w6C4QhcBRB5t8rQ7zRj9fjb0oB1XGGz7K8PKnRd2BgZEgHE8KwsoD9FaVDMRhaJCV0WOn%2B1F50NQuiAVxPjynhhHBaCqdM22OykGPcT9d%2BHRifV%2FUd8tDMyQIE%2BjpkiQwKAT3u7A%3D%3D&checksum=202426288360d41b88aa313246eba96280a82f870dd4&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qWU8wofHFb0GAwioguOTaoJZUEd6Kmj3qcf5WQVuTfMjy9le23ynzfCHdo66AJX8OIVzUlpON%2FSXRvziWE8fbjF%2FJbPnromf1vM3o2SZImfoOPAtwLwmT3LsX2zwLcBwc8L%2FlKsgTh4o9aG5VykR%2BMT3OKKmLus4xdturhn6hOxENJ%2FRQ7ui2g3jk%2B2DJtV0v3k8jIeY8mT6KnWO3nk1y0EEiRKICDeY6NC1EAHpCG%2B2D8DaP5CauTijjarDueiPS8sZ9PzZeQ3UobjknhhhzRNziWBz3WEiYZGqFaFBuZIh5CgoRQ0YVdVz3CaQt%2FG0vab9AeNHwLil3axIzGHdA%2Bw9DK8KmvarnacnhiqAID2qCldhiyO2HdJRPAFaZTtW%2F%2FC0w%2FILUJNntX%2BCReqNH%2FMCiUakZqbnUfRucVaooF%2Frgr9XlM2NC9FWCcpCJS7p6C7FL%2FAtYt%2BJ7twuiVXHGdoTPRGIdrBb%2Fw5%2FHIbF3%2BJpHW3gkE6H3wl990zHgZ5lwddpaq9ZRqEAhQLzjXC9tjakdwkxQ0hDQYuoYM2WuU5q7NQTF0R7uBg0JH3p7NPq%2FeoQlQnhZ1EwR8bzhCxe%2BM60n7na3Fst8CNr3w6C4QhcBRB5t8rQ7zRj9fjb0oB1XGGz7K8PKnRd2BgZEgHE8KwsoD9FaVDMRhaJCV0WOn%2B1F50NQuiAVxPjynhhHBaCqdM22OykGPcT9d%2BHRifV%2FUd8tDMyQIE%2BjpkiQwKAT3u7A%3D%3D&checksum=202426288360d41b88aa313246eba96280a82f870dd4) |
| Ball Magents | T::A Kugelmagnete 5 6 10 mm N45 Neodym Magnete NdFeB Menge wählbar extrem stark | 4 € | [ebay](https://www.ebay.de/itm/T-A-Kugelmagnete-5-6-10-mm-N45-Neodym-Magnete-NdFeB-Menge-w%C3%A4hlbar-extrem-stark/122187457941?var=422432026780)  |


# Software 

As the software we relied on three different APPs for recent Android phones (in our case Huawei P20 Pro).

Briefly summarized and in-detail described below:

|  Name | Purpose  |  Source  | 
|  STORM-Controler | Remote control (MQTT) to control things like laser intensity, coupling lens, focus  |  [APP: STORM-Controler](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/tree/master/ANDROID/STORM-Controller)  | 
|  STORM-Imager | Control long-term image acquisition by enabling auto-focus and auto-coupling, schedule fluctuating intensity measurements inside incubators   |   [APP: STORM-Imager](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p-ANDROID)  | 
|  FreeDCam | Full control over the cellphones camera: RAW and video image acquisition |   [FreeDCam](https://github.com/beniroquai/FreeDcam/tree/cellstorm) | 


## Android APP: STORM-Controler

To control the Lens or Laser using a customized MQTT controler APP, you can visit this repository:

[APP: STORM-Controler](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/tree/master/ANDROID/STORM-Controller)

This app allows basic hardware controls:
<p align="center">
<img src="./images/cellSTORM_app.png" width="200">
</p>

## Android APP: STORM-Imager

This is the APP which can record images, control the device and predict a super-resolved result form the camera live stream. The APP can be found here:

[APP: STORM-Imager](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p-ANDROID)


### Autofocus inside the APP:

It's just an example how the cellphone maintains the focus. This is done by maximizing the focus metric (i.e. standard deviation over z) as a function of the focus motor position.

<p align="center">
<img src="./images/autofocus.gif" width="300">
</p>


### SOFI-based superresolution imaging inside the APP:

This is an example of the SOFI-based superresolution imaging using the neural network mentioned below. We used fixed *e.coli* labelled with ATTO 647.
The fluctuation of the illumination is the result of the discrete mode pattern in the singlemode waveguide chip. The input field changes the intensity pattern.   

<p align="center">
<img src="./images/ondevicesr.gif" width="300">
</p>

## Android APP: FreeDCam (cellSTORM module)

For the *d*STORM experiments we used the open source APP [FreeDCam](https://github.com/beniroquai/FreeDcam/tree/cellstorm) originally developed and mainted by [killerink](https://github.com/KillerInk/FreeDcam). We provide a modified version for the Huawei P9 and P20 which is used in this work. It enables

1. fast read-out and saving of cropped RAW frames to the SD-cad
2. stream the RAW buffer to a c-server

To stream the data to a server [this manual](https://github.com/beniroquai/FreeDcam/tree/cellstorm/server_mac) gives some more detailed information. It requires Android Studio which compiles the c program into an executable. Inside the APP you need to select the IP of the server.

Many thanks to [@Killerink](https://github.com/KillerInk/) to make this work!

### Settings for FreeDCam (Huawei P20 Pro) 

We used the following settings:

***Video Settings:***
<p align="center">
<img src="./images/ScreenshotFreedcamSettings (2).jpg" width="200">
</p>

***General Settings:***
<p align="center">
<img src="./images/ScreenshotFreedcamSettings (3).jpg" width="300">
</p>

<p align="center">
<img src="./images/ScreenshotFreedcamSettings (4).jpg" width="300">
</p>

***Acquisition Settings:***
<p align="center">
<img src="./images/ScreenshotFreedcamSettings (1).jpg" width="300">
</p>


## NN-based Super-Resolution Imaging: "Learn2Fluct"

The python and tensorflow-based neural network to use "SOFI"-like image reconstruction based on ```convLSTM2D``` layers on a cellphone can be found here:

[Neural Network](https://github.com/beniroquai/dSTORM-on-the-chea-i-p-Learn2Fluct)

It aims to transfer a stack of noisy low resolution images with varying illumination pattern:

<p align="center">
<img src="./images/mytest_obj-2.gif" width="300">
</p>

into high resolution images:

<p align="center">
<img src="./images/mytest_gt-1.png" width="300">
</p>

It is part of the APP "STORM-Imager" and can be used as an interactive website (Live-Demo). To train the model have a look in the recent ```Tensorflow==2.3.0``` implementation using ```Keras```  and ```TFLite``` which can be found in the Github-Reopository [here](https://github.com/beniroquai/dSTORM-on-the-chea-i-p-Learn2Fluct/tree/master/TF2_KERAS).

### Live-Demo using Webcam

We implemented a live-demo of the pre-trained SOFI-network which is available [here](./STORMjs/index.html). It runs in Javascript and does not transfer any (!) data to the internet. It runs locally once the model of the neural network is downloaded. 

***Note:*** It's in an experimental stage. It's not optimized for performance. We do not guarantee for proper functionality. Use it on your own risk!

<p align="center">
<img src="./images/cellstorm_tensoflowjs_screenshot.png" width="500">
</p>




### Google Colab

Please have a look [here](https://colab.research.google.com/drive/1AkMT-O8qXnH9ikavBGUPaXuKVTPuJ_34?usp=sharing)

# Tutorials 

## Video Tutorials to setup the cellSTORM device

### cellSTORM - Part 1: Setup the MQTT server and connect the cellphone
https://www.youtube.com/watch?v=gefJPZ8_ua8&feature=youtu.be

### cellSTORM - Part 2: Align the lens (OPU) and the laser
https://www.youtube.com/watch?v=GFoVPgfUFtI&feature=youtu.be

### cellSTORM - Part 3: Adding the waveguide chip and start coupling
https://www.youtube.com/watch?v=-dWIeXHAiBc&feature=youtu.be

### cellSTORM - Part 4: Setup the optical part
https://www.youtube.com/watch?v=qdbaAQTLw-c&feature=youtu.be

### cellSTORM - Part 5: Setup the imaging using the cellphone
https://www.youtube.com/watch?v=fhmkS0Ywucg&feature=youtu.be

### cellSTORM - Part 6: Setup the FreeDCam for best SNR performance
https://www.youtube.com/watch?v=Evdc-384KZk&feature=youtu.be

# Contribute

If you have a question or found an error, please file an issue! We are happy to improve the device!  

# License

Please have a look into the dedicated [License file](LICENSE.MD).

# Disclaimer

We do not give any guarantee for the proposed setup. Please use it at your own risk. Keep in mind that Laser source can be very harmful to your eye and your environemnt!
