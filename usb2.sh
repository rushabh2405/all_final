# SSH into your Pi
PI_HOSTNAME="raspberrypi" # Change to your pi's hostname
PI_SSH_USERNAME="pi"      # Change to your Pi username

# Connect to the Pi (default password is "raspberry")
ssh "${PI_SSH_USERNAME}@${PI_HOSTNAME}"

# Install pre-requisites
sudo apt-get update && \
  sudo apt-get install -y \
    git \
    python-pip \
    python3-venv

# Install Key Mime Pi
git clone https://github.com/mtlynch/key-mime-pi.git
cd key-mime-pi
sudo ./enable-usb-hid
sudo reboot
