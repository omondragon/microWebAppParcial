# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define :servidorWeb do |servidorWeb|
    servidorWeb.vm.box = "bento/ubuntu-22.04-arm64"
    servidorWeb.vm.network :private_network, ip: "192.168.80.3"
    servidorWeb.vm.provision "file", source: "frontend", destination: "/home/vagrant/frontend"
    servidorWeb.vm.provision "file", source: "microUsers", destination: "/home/vagrant/microUsers"
    //servidorWeb.vm.provision "file", source: "microProducts", destination: "/home/vagrant/microProducts"
    //servidorWeb.vm.provision "file", source: "microOrders", destination: "/home/vagrant/microOrders"
    servidorWeb.vm.provision "file", source: "init.sql", destination: "/home/vagrant/init.sql"
    servidorWeb.vm.provision "shell", path: "script.sh"
    servidorWeb.vm.hostname = "servidorWeb"
  end
end
