#!/bin/bash

# screenshot and save image

# sudo apt install imagemagick

mkdir -p images_jpg

for image in {0..4};
do
	echo "# ${image} screenshot..."
	scrot img_${image}.png

	echo "converting image png to jpg..."
	convert img_${image}.png img_${image}.jpg
	mv img_${image}.jpg images_jpg/

	rm img_${image}.png

done

echo "All done"


