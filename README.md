[![cc-by-sa](https://img.shields.io/badge/License-CC%20BY%20SA%203.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/3.0/)

# ![logo](https://raw.githubusercontent.com/30350n/printable-instruments/master/images/logo_text.png)

The Printable Instruments project provides custom PCB panel designs for Mutable Instruments modules. These panels are meant to be ordered from [JLCPCB](https://jlcpcb.com/), but can be easily modified to work with other manufacturers.

All the panels are created using Inkscape. The Inkscape extension [svg2shenzhen](https://github.com/badgeek/svg2shenzhen) is used to generate a KiCad project from the Inkscape svg, which can then be used to generate gerber files.

Additionally to the Printable Instruments panel designs, this repository also contains panel templates, which can be used to easily create your own designs.

## Overview

![overview](https://raw.githubusercontent.com/30350n/printable-instruments/master/images/overview.png)

### Example Render from the KiCad 3D Viewer

![clouds_rendered](https://raw.githubusercontent.com/30350n/printable-instruments/master/images/clouds_rendered.png)

### Available Panels

- [x] Rings *
- [x] Clouds *
- [x] Ripples (2015) *
- [x] Blinds *
- [x] Veils (2016) *
- [x] Frames * (button holes of the first iteration where a little too large for my taste)
- [x] Links

Panels marked with * are functional, but when I first ordered them from JLCPCB they had some visual flaws. JLCPCB seems to have a problem with filled silkscreen areas, where the silkscreen doesn't fully cover up the solder mask. Sometimes there are also visible lines in those areas.
If somebody orders these from a different manufacturer, be sure to share your experience with them.
I'll try to come up with an alternative design which doesn't have any big filled areas anymore.

**Warning: Unchecked panels are still in development and haven't been ordered/tested yet!**

### Planned Panels

- Braids
- Kinks

## Credits

- **[Mutable Instruments](https://github.com/pichenettes/eurorack)** provided the original hardware design files, which are being used as references in this repository.

- The **[Mutated Mutables](https://github.com/TheSlowGrowth/MutatedMutables)** repository has been very helpful for figuring out the Inkscape to KiCad workflow. Some graphics from the "Doku" layer have been directly adopted in this repository.

## Generating Gerber files

1. Install Inkscape, KiCad.

2. Install the svg2shenzhen extension, according to [the installation instructions](https://github.com/badgeek/svg2shenzhen#install).

3. Open a svg panel file in Inkscape.

4. (optional) When ordering from a different service than JLC, change the "JLCJLCJLCJLC" text, to whatever your manufacturer is using as a template for order numbers.
   Some manufacturers also have options to completely remove the number for a small premium.
   You most certainly don't want the order number on the front of your panel.

5. In Inkscape: Extensions -> Svg2Shenzhen -> 2. Export to KiCad...

   Recommended settings:
   |                |                 |
   | -------------- | --------------- |
   | Export As      | **Project**     |
   | Threshold      | **Default (5)** |
   | Export DPI     | **1016**        |
   | Flatten Bezier | **yes**         |
   | Open Kicad     | **yes**         |

   Click **Apply**

6. (deprecated) By default, all the holes from the Drill layers will be plated through holes, while the bigger holes from the Edge.Cuts layer will be non plated.
   ~~To unfiy this, I'd recommend manually going through the holes in Pcbnew and changing their pad type to "NPTH, Mechanical". Alternatively you can also try to edit the drill files after Step 8.~~
   Update: The plated holes actually aren't only fine, but necessary. With non plated holes the "fake vias" of the logo will look bad.

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
