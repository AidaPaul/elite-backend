# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "hyperv" do |v, override|
    override.vm.box = "ericmann/trusty64"
  end

  # I don't have a workstation box about, so whoever does - please check whether that box actually works ;)
  config.vm.provider "vmware_workstation" do |v, override|
    override.vm.box = "jdowning/trusty64"
  end

  config.vm.network "forwarded_port", guest: 9090, host: 9191
  config.vm.network "private_network", ip: "192.168.0.51"
  config.vm.synced_folder ".", "/opt/elite-backend"

  # We should embrace it with proper provisor, most likely chef, but this will do for now.
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y git
    sudo apt-get install -y libmysqlclient-dev
    sudo apt-get install -y python3-dev
    git clone git://github.com/bmc/daemonize.git
    cd daemonize
    sh configure
    make
    sudo make install
    cd ~
    wget https://bootstrap.pypa.io/get-pip.py &> /dev/null
    sudo python3 get-pip.py
    sudo pip3 install -r /opt/elite-backend/requirements.txt
    ln -s /opt/elite-backend/manage.py ~/manage.py
    daemonize -p /opt/elite-backend/elite-backend.pid /usr/bin/python3 /opt/elite-backend/manage.py runserver 0.0.0.0:9090
  SHELL
end
