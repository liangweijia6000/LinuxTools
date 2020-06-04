if [ ! -d "~/shareG" ]; then
	mkdir ~/shareG
fi

if [ ! -d "~/shareE" ]; then
	mkdir ~/shareE
fi

if [ ! -d "~/shareH" ]; then
	mkdir ~/shareH
fi

if [ ! -d "~/shareD" ]; then
	mkdir ~/shareD
fi

sudo mount -t cifs -o username=admin,password=123456,dir_mode=0777,file_mode=0777 //10.10.1.220/g ~/shareG
sudo mount -t cifs -o username=admin,password=123456,dir_mode=0777,file_mode=0777 //10.10.1.220/e ~/shareE
sudo mount -t cifs -o username=admin,password=123456,dir_mode=0777,file_mode=0777 //10.10.1.220/h ~/shareH
sudo mount -t cifs -o username=admin,password=123456,dir_mode=0777,file_mode=0777 //10.10.1.220/d ~/shareD
