[![cc-by-sa](https://img.shields.io/badge/license-CC%20BY%20SA%203.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/3.0/)

# ![logo](https://raw.githubusercontent.com/30350n/printable-instruments/master/images/logo_text.png)

The Printable Instruments project provides custom PCB panel designs for Mutable Instruments modules.
These panels are meant to be ordered from PCB manufacturers such as [PCBWay](https://www.pcbway.com/)
or [JLCPCB](https://jlcpcb.com/).

All the panels are created using Inkscape.
The Inkscape extension [svg2shenzhen](https://github.com/badgeek/svg2shenzhen) is used to
generate a KiCad project from the Inkscape svg, which can then be used to generate gerber files.

Additionally to the Printable Instruments panel designs, this repository also contains panel
templates, which can be used to easily create your own designs.

## Version 2.0 Sponsorship

The development of the Braids panel and the 2.0 release of this project was generously sponsored
by [PCBWay](https://www.pcbway.com/), who provided free samples of the Braids panel!

## Overview

![overview](images/overview.webp)

### Braids panel, manufactured by [![PCBWay](https://img.shields.io/badge/PCBWAY-11A73B?style=for-the-badge)](https://www.pcbway.com/)

![braids_pcbway](images/braids_pcbway.webp)

### Available Panels

- [x] Rings
- [x] Clouds
- [x] Ripples (2015)
- [x] Blinds
- [x] Veils (2016)
- [x] Frames
- [x] Links
- [x] Marbles
- [x] Braids

**Warning: Unchecked panels are still in development and haven't been ordered/tested yet!**

## Credits

- **[Mutable Instruments](https://github.com/pichenettes/eurorack)** provided the original hardware design files, which are being used as references in this repository.

- The **[Mutated Mutables](https://github.com/TheSlowGrowth/MutatedMutables)** repository has been very helpful for figuring out the Inkscape to KiCad workflow. Some graphics from the "Doku" layer have been directly adopted in this repository.

## Derivative Work

- [angiamusic](https://github.com/angiamusic) made a really nice [Frames panel](https://github.com/angiamusic/Valance_Panel) based on this project

## Getting the Gerber files

**Note: for v2.0+ there's pregenerated gerber files in the [latest release](https://github.com/30350n/printable-instruments/releases/latest).** 

You can simply download the `printable-instruments-gerbers.zip`, unpack it and upload any of
the contained gerber archives to your favorite board house.

### Generating the Gerber files yourself

1. Install Inkscape, KiCad.

2. Install the svg2shenzhen extension, according to [the installation instructions](https://github.com/badgeek/svg2shenzhen#install).

3. Open a svg panel file in Inkscape.

4. (optional) When ordering from a different service than JLC, change the "JLCJLCJLCJLC" text, to whatever your manufacturer is using as a template for order numbers.
   Some manufacturers also have options to completely remove the number for a small premium.
   You most certainly don't want the order number on the front of your panel.

5. In Inkscape: Extensions -> Svg2Shenzhen -> 2. Export to KiCad...

   Recommended settings:
   |                |                    |
   | -------------- | ------------------ |
   | Export As      | **Project**        |
   | Threshold      | **Default (5)**    |
   | Export DPI     | **Default (1200)** |
   | Flatten Bezier | **yes**            |
   | Open Kicad     | **yes**            |

   Click **Apply**

6. By default, all the holes from the Drill layers will be plated through holes, which will leave a small, visible ring
   of copper exposed.
   To fix this, I'd recommend manually going through all the holes, except the small vias from the bottom logo
   (because for those, the effect is actually wanted) in Pcbnew and changing their pad type to "NPTH, Mechanical".

7. In Pcbnew: File -> Plot...

   Recommended settings:
   |                 |                                                                     |
   | --------------- | ------------------------------------------------------------------- |
   | Plot format     | **Gerber**                                                          |
   | Included Layers | **F&#46;Cu, B&#46;Cu, F.SilkS, B.SilkS, F.Mask, B.Mask, Edge.Cuts** |

    Click **Plot**

8. Click **Generate Drill Files...** (still in the Plot window)

   Recommended settings:
   |                 |                 |
   | --------------- | --------------- |
   | Map File Format | **Gerber**      |
   | Drill Units     | **Millimeters** |

   Click **Generate Drill File**

## Older Versions

- ### Version 1.0
  
  I wasn't completely happy with this first version design wise,
  mainly because many of the module icon designs where copied from the original MI panel designs.
  The icons which weren't also had some consistency issues which I tried to resolve.

  They also had some visible flaws when I first ordered them from JLCPCB.
  Many of the (cheaper) PCB Manufacturers seem to have a problem with filled silkscreen areas,
  where the silkscreen doesn't fully cover up the solder mask.
  Sometimes there are also visible lines in those areas.
  Because of that all the filled areas got removed.
