import os

#updates
os.system('sudo apt update')
os.system('sudo apt upgrade -y')

#libra office
os.system('sudo apt install libreooffice -y')

#kdenlive
os.system('sudo apt install kdenlive -y')

#net tools
os.system('sudo apt install net-tools -y')

#ssh server
os.system('sudo apt install openssh-server -y')

#google chrome
os.system('sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -y')
os.system('sudo sudo apt install ./google-chrome-stable_current_amd64.deb -y')

#vlc
os.system('sudo apt install vlc -y')

#blinder
os.system('sudo apt install blender -y')

#audacity
os.system('sudo add-apt-repository ppa:ubuntuhandbook1/audacity -y')
os.system('sudo apt-get update')
os.system('sudo apt-get install audacity -y')

#caffeine
os.system('sudo add-apt-repository ppa:eugenesan/ppa -y')
os.system('sudo apt-get update')
os.system('sudo apt-get install caffeine -y')

#dropbox
os.system('sudo apt-get install nautilus-dropbox -y')

#QtQr
os.system('sudo add-apt-repository ppa: qr-tools-developers/qr-tools-stable -y')
os.system('sudo apt-get update')
os.system('sudo apt-get install qtqr -y')

#update
os.system('sudo apt update')
os.system('sudo apt upgrade -y')

#reboot
os.system('sudo reboot now')
