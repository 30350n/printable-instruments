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

- [ ] Rings
- [ ] Clouds
- [ ] Ripples

**Warning: Unmarked panels are still in development and haven't been ordered/tested yet!**

### Planned Panels

- Frames
- Braids

## Credits

- **[Mutable Instruments](https://github.com/pichenettes/eurorack)** provided the original hardware design files, which are being used as references in this repository.

- The **[Mutated Mutables](https://github.com/TheSlowGrowth/MutatedMutables)** repository has been very helpful for figuring out the Inkscape to KiCad workflow. Some graphics from the "Doku" layer have been directly adopted in this repository.

## Generating Gerber files

1. Install Inkscape, KiCad.
2. Install the svg2shenzhen extension, according to [the installation instructions](https://github.com/badgeek/svg2shenzhen#install).
3. Open a svg panel file in Inkscape.
4. In Inkscape: Extensions -> Svg2Shenzhen -> 2. Export to KiCad...

   Recommended settings:
   |                |                 |
   | -------------- | --------------- |
   | Export As      | **Project**     |
   | Threshold      | **Default (5)** |
   | Export DPI     | **1016**        |
   | Flatten Bezier | **yes**         |
   | Open Kicad     | **yes**         |

   Click **Apply**

5. In Pcbnew: File -> Plot...

   Recommended settings:
   |                 |                                                                     |
   | --------------- | ------------------------------------------------------------------- |
   | Plot format     | **Gerber**                                                          |
   | Included Layers | **F&#46;Cu, B&#46;Cu, F.SilkS, B.SilkS, F.Mask, B.Mask, Edge.Cuts** |

    Click **Plot**

6. Click **Generate Drill Files...** (still in the Plot window)

   Recommended settings:
   |                 |                 |
   | --------------- | --------------- |
   | Map File Format | **Gerber**      |
   | Drill Units     | **Millimeters** |

   Click **Generate Drill File**
