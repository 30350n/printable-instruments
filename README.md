# Printable Instruments

The Printable Instruments project provides custom PCB panel designs for Mutable Instruments modules. These panels are meant to be ordered from [JLCPCB](https://jlcpcb.com/), but can be easily modified to work with other manufacturers.

All the panels are created using Inkscape. The Inkscape extension [svg2shenzhen](https://github.com/badgeek/svg2shenzhen) is used to generate a KiCad project from the Inkscape svg, which can then be used to generate gerber files.

## Generating Gerber files

1. Install Inkscape, KiCad.
2. Install the svg2shenzhen extension, according to [the installation instructions](https://github.com/badgeek/svg2shenzhen#install).
3. Open a svg panel file in Inkscape.
4. In Inkscape: Extensions -> Svg2Shenzhen -> 2. Export to KiCad...
   Recommended settings:
   |                |             |
   | -------------- | ----------- |
   | Export As      | **Project** |
   | Threshold      | **Default** |
   | Export DPI     | **1016**    |
   | Flatten Bezier | **yes**     |
   | Open Kicad     | **yes**     |

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
