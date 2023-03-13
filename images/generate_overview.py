import os, subprocess, shutil
from functools import partial
from PIL import Image, ImageDraw

output = "images/overview.webp"
height = 1285 * 2
directory = "."
workdir = os.path.join(".", "tmp")

if not os.path.exists(workdir):
    os.mkdir(workdir)

images = []
for filepath in sorted(map(partial(os.path.join, directory), os.listdir(directory))):
    if os.path.isfile(filepath) and filepath.endswith(".svg") and not filepath.endswith("_template.svg"):
        pngpath = os.path.join(workdir, os.path.basename(filepath).split(".")[0] + ".png")
        
        command = f"inkscape {filepath} -o {pngpath} -C -b white -y 1.0 --export-type=png, --export-height={height}"
        subprocess.run(command, check=True)

        images.append(Image.open(pngpath))

overview = Image.new("RGBA", (sum(map(lambda image: image.width, images)) + len(images) - 1, height))
overviewDraw = ImageDraw.Draw(overview) 
offset = 0
for image in images:
    overview.paste(image, (offset, 0))
    offset += image.width
    overviewDraw.line((offset, 0, offset, height), fill="#444444", width=15)
    offset += 1

overview.save(output)

for image in images:
    image.close()

shutil.rmtree(workdir)
