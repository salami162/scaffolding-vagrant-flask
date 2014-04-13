# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "berendt/ubuntu-14.04-amd64"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.hostname = "scaffolding"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "forwarded_port", guest: 27017, host: 27018

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  config.vm.provider "virtualbox" do |vb|
    # Don't boot with headless mode
    # vb.gui = true
  
    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end


  # Omnibus Plugin
  # Install: `vagrant plugin install vagrant-omnibus`
  # https://github.com/schisamo/vagrant-omnibus
  config.omnibus.chef_version = '11.6.0'


  # Berkshelf Plugin
  # Install: `vagrant plugin install vagrant-berkshelf`
  # https://github.com/riotgames/vagrant-berkshelf
  config.berkshelf.enabled = true


  # Enable provisioning with chef solo, specifying a cookbooks path, roles
  # path, and data_bags path (all relative to this Vagrantfile), and adding
  # some recipes and/or roles.

  config.vm.provision "chef_solo" do |chef|
    chef.cookbooks_path ="../recipes"
    chef.add_recipe "apt"
    chef.add_recipe "vagrant_extras"
    chef.add_recipe "git"
    chef.add_recipe "nginx"
    chef.add_recipe "curl"
    chef.add_recipe "mongodb::10gen_repo"
    chef.add_recipe "mongodb"
    chef.add_recipe "build-essential"

    # You may also specify custom JSON attributes:
    chef.json = {
      :mongodb => {
        :dbpath     => '/data',
        :smallfiles => true      # Speed up initial journal preallocation
      },
      :application => {
        :name => 'green'
      },
    }
  end
end
