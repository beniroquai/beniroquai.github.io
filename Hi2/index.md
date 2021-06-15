# Democratizing Labautomation using UC2, Opentrons, OpenFlexure and ImJoy

An simple open-source approach to bring automated liquid handling and high throughput microscopy to your lab.

---

## Preprint

The preprint for the *Hi2*  accompanied with a series of applications ca be found on [**BIORXIV**]() 😊

## High-throughput for UC2: ***Hi2***

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

In the manuscript we present two different setups. A dedicated github repository for the self-contained XYZt scanning microscope for the Opentrons (i.e. ***OpenMicroTrons***) can be found [here](https://github.com/beniroquai/Opentrons-Microscope-Platereader).

Below you will find in-depth explanation for the Hi2 openUC2-based well-scanning microscope.

<p align="center">
<img src="./images/main.png" width="700">
</p>


# Quickstart

You are keen on starting your own automated workflow? You can have a look in the [Jupyter Notebooks](https://github.com/openUC2/UC2-Hi2/tree/master/JUPYTER) which give you an idea how such a workflow may look like. These Notebooks run on the Raspberry Pi inside the Opentrons and handle:

* Pipetting commands using the Opentrons OT2
* microscopic imaging using the Openflexure Server and the openUC2 Microscope
* Image Processing using the ImJoy Plugin environemnt

It requires a number of steps to setup everything. Below we hope to give you some guidance to get this working.

A rough schematic of how the different components interact with each other is illustrated in the figure below:

<p align="center">
<img src="./images/SYSTEM.png" width="500">
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

## Subsystem: Hi2 - UC2 High-Throughput Microscope

The two new components for the openUC2 framework which were developed for the already existing modular optical toolkit are the high-throughput XY-stage and the rapidly scanning z-stage. Both stage types are based on CNC components, here the XY stage is in large part derived from a commercially avaialbe laser engraver (Neje Master Mini 2). The Z-stage relies on a NEMA11 motor and a MGN12H linear bearing mechanism combined with a magnetic-bearing mechanism to realiz wobble-reduced motion along the Z-axis.

<p align="center">
<img src="./images/Sub_Hi2.png" width="500">
</p>

## Electronics and Code

We rely on a commercially available open-source CNC/3D printing board [Makerbase mks DLC](https://github.com/makerbase-mks/MKS-DLC), which can control the LED, the Laser using PWM and all steppers using the [GRBL](https://github.com/grbl/grbl) firmware. All commands are delivered using G-Code. In order to use the microscope, one simply needs to flash the GRBL softwrae on the MKS board using the Arduino IDE.


## Optical setup

The UC2-based microscope relies on a wide-field fluorescence microscope, where a fiber-coupled laser diode provides a suitable excitation field for AF647 dyes. The objective lens can easily be moved using the NEMA motor driven Z-stage

<p align="center">
<img src="./IMAGES/setup_1.png" width="700">
</p>


### Bill of Material (BOM)

Along with the 3D printed parts in the Github-repository, you need a set of mechanical, electrical and optical parts summarized in the BOM below:

***Dead Link?***: Ebay is not really a reliable source since resellers may discontinue the product. In case you're looking for a component which can not be found, file an issue [here](https://github.com/beniroquai/dSTORM-on-a-Chi-ea-p/) - alternatively: Copy the name under "Details" and search for it in Ebay. (E.g. "3450 300mW 637nm Dot Laser Module TTL/analog 12VDC" site:laserlands.net) Good luck 🍀

Amazon is more reliable, but personally we try to avoid ordering there (Sorry..). We try to update the list with Amazon links

For the whole system to work you will need the following UC2 modules which you can get from our website:




|  Quantity | Details  |  Price (per piece)|
|---|---|---|
|1x| MKS DLC 2.0  CNC Shield + Stepper Controlers + 12V Powersupply + USB Cable| 30 € |
|2x |[45° Thorlabs Mirror Cube](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Mirror_45_Thorlabs)| 60€ |
|1x |[Z-stage Cube with NEMA Motor](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Z-STAGE_NEMA_MGN)| ~50€ |
|4x |[Thorlabs Cage Cube](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Thorlabs)|  30€ |
|1x |[Allied Vision Cube](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_AlliedVision_Alvium)|  350 €|
|8x |[Empty Cube (IM)](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Base)|  20 € |
|16 x |[Puzzle Base Plate ](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_Baseplate)| ~5€ |
|1 x |[Dichroic Mirror Cube ](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Dichroic_Beamsplitter)| ~50€ |
|1x |[Hi2 Module](https://github.com/openUC2/UC2-Hi2)| 200€ |

As a laser we used a fiber-coupled 635nm laser from micos for around 80€ threaded into a Thorlabs cage.
As a dichroic mirror we use Comar IY740 + a suitable emission filter (number will follow!).

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

Please refer to the comprehensive guid in the [ImJoy subpage](./imjoy.md)

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
