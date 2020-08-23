# Design Guidelines

## Lines

stroke: 0.25mm

## Text

* font: comfortaa

|             | fontsize | stroke | letter case | spacing |     x |    y* |
| ----------- | -------- | ------ | ----------- | ------- | ----- | ----- |
| module name |     15pt |      - | capitalized |     0px |  22mm | 5.7mm |
| module desc |      8pt |      - |  lower case |     0px | ~50mm | 5.7mm |
| big label   |      8pt | 0.15mm |  upper case |   0.5px |     - |     - |
| small label |      6pt | 0.15mm |  upper case |   0.5px |     - |     - |
| button      |      6pt | 0.10mm |  lower case |     0px |     - |     - |

y*: position of helpline (0.5mm stroke)

## Module Icon

|          |        x |       y |    w/h | stroke |
| -------- | -------- | ------- | ------ | ------ |
| F.Silk   | 15.000mm | 1.000mm | 5.80mm | 0.25mm |
| F&#46;Cu | 14.875mm | 0.875mm | 6.05mm | 0.50mm |

## PI Logo

* copy Drill subgroup to Drill layer

|        |        x |     y |
| ------ | -------- | ----- |
| F.Silk | centered | 122mm |

## Labels

|             |       y* |
| ----------- | -------- |
| audio jack  |   -5.5mm |
| 2PS knob    |  +12.5mm |
| 3PS knob    |  +13.8mm |

y*: position of helpline (0.5mm stroke)

## Frames

|        | stroke |  width* | height |
| ------ | ------ | ------- | ------ |
| output |  3.0mm | +12.5mm | 14.5mm |

* snap to diagonal line, -0.5mm y offset

width*: width of the rectangle, with stroke

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
