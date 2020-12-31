install:
	sudo echo "" > /usr/bin/chrimgs
	sudo echo "#!/bin/bash" >> /usr/bin/chrimgs
	sudo echo "python3 /usr/share/chrimgs/chrimgs.py \"\$$@\"" >> /usr/bin/chrimgs
	sudo mkdir /usr/share/chrimgs -p
	sudo cp ./chrimgs.py /usr/share/chrimgs/
	sudo chmod +x /usr/bin/chrimgs
depens:
	pip3 install Image
