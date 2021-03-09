# Design Guidelines

## Lines

stroke: 0.25mm

## Text

* font: comfortaa

|             | fontsize | stroke | letter case | spacing |     x |    y* |
| ----------- | -------- | ------ | ----------- | ------- | ----- | ----- |
| module name |     15pt |      - | capitalized |     0px |  22mm | 5.7mm |
| module desc |      8pt |      - |  lower case |     0px | ~50mm | 5.7mm |
| pot label   |      6pt | 0.15mm |  upper case |   0.5px |     - |     - |
| jack label  |      7pt | 0.15mm |  upper case |   0.5px |     - |     - |
| pot n label |      7pt | 0.15mm |  upper case |   0.5px |     - |     - |
| small label |      4pt | 0.10mm |  upper case |   0.5px |     - |     - |

module name for panels <= 6HP:

* x: centered
* y*: 17mm
* fonsize: 12pt

### Label positions

|            | y\* (below) | y\* (above) |
| ---------- | ----------- | ----------- |
| audio jack |      +7.0mm |      -5.5mm |
| 1PS knob   |     +12.0mm |           - |
| 2PS knob   |     +12.5mm |      -9.5mm |
| 3PS knob   |     +13.8mm |           - |
| 6PS knob   |     +21.5mm |           - |

y*: position of helpline (0.5mm stroke)

## Module Icon

|          |        x |       y |    w/h* | stroke |
| -------- | -------- | ------- | ------- | ------ |
| F.Silk   | 15.000mm | 1.000mm |  5.80mm | 0.25mm |
| F&#46;Cu | 14.875mm | 0.875mm |  6.05mm | 0.50mm |

for 4HP panels:

* x: 11.500mm / 11.375mm

w/h*: with stroke

## PI Logo

* copy Drill subgroup to Drill layer

| hp          | type       |        x |     y |
| ----------- | ---------- | -------- | ----- |
| < 8HP       | icon only  | centered | 122mm |
| 8HP         | text_small |   13.5mm | 122mm |
| 10HP - 12HP | text_small | centered | 122mm |
| > 12HP      | text       | centered | 122mm |

## Frames

|        | stroke |  height |
| ------ | ------ | ------- |
| output |  3.0mm |  14.0mm |

* snap bottom to jacks +1.0mm y offset

width: snap to bounding box, without stroke
height: height of the rectangle, with stroke

## Ornament Lines

|        |     y |
| ------ | ----- |
| top    |   8mm |
| bottom | 118mm |

## Small Attenuverter Markings

* y offset: -5.5mm

## A100 Mounting Slots

* width: 1mm + 3.2mm radius

## Credits

* B.Mask Boxes: 1mm stroke
* TSKF y: 119mm

## Holes

|                     |       r |      d | layer     |
| ------------------- | ------- | ------ | --------- |
| mounting hole       |   1.6mm |  3.2mm | Drill     |
| 3mm led             |   1.5mm |  3.0mm | Drill     |
| 5mm led             |   2.5mm |  5.0mm | Drill     |
| button              |   2.5mm |  5.0mm | Drill     |
| big button          |   4.5mm |  9.0mm | Edge.Cuts |
| illuminated button  |   4.0mm |  8.0mm | Edge.Cuts |
| audio jack          | 3.125mm | 6.25mm | Drill     |
| potentiometer       | 3.750mm | 7.50mm | Edge.Cuts |
| small potentiometer | 3.375mm | 6.75mm | Edge.Cuts |

## Layers

* doku
* help
  * fab (stroke: 0.2mm)
* ref
  * fab
  * graphics
* Drill
* Edge.Cuts (stroke: 0.2mm)
* F&#46;Cu
* B&#46;Cu
* F.Silk
* B.Silk
* F.Mask
* B.Mask
