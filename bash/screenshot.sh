#!/bin/bash

# start time 
start=$SECONDS

echo "time(start): ${start}"

# screenshot and save image

# sudo apt install imagemagick

mkdir -p images_jpg

for image in {0..500};
do
	echo "# ${image} screenshot..."
	scrot img_${image}.png

	echo "converting image png to jpg..."
	convert img_${image}.png img_${image}.jpg
	mv img_${image}.jpg images_jpg/

	rm img_${image}.png

done

echo "All done"
end=`date +%s.%N`

# end time 
end=$SECONDS

# time execution
echo "duration: $((end-start)) seconds."
