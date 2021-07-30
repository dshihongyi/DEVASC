

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.65.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}

# Create a resource group
resource "azurerm_resource_group" "Web_Rg" {
  name     = "Web_Rg"
  location = "East US"
}


# Create a virtual network within the resource group
resource "azurerm_virtual_network" "Web_VNet" {
  name                = "Web_VNet"
  resource_group_name = azurerm_resource_group.Web_Rg.name
  location            = azurerm_resource_group.Web_Rg.location
  address_space       = ["10.0.0.0/16"]
}


# Create a Subnet within the virtual network group
resource "azurerm_subnet" "Web_Subnet" {
  name                 = "Web_Subnet"
  resource_group_name  = azurerm_resource_group.Web_Rg.name
  virtual_network_name = azurerm_virtual_network.Web_VNet.name
  address_prefixes     = ["10.0.1.0/24"]
}


# Create a Public IP address
resource "azurerm_public_ip" "Web_Publicip" {
    name                         = "Web_PublicIP"
    location                     = azurerm_resource_group.Web_Rg.location
    resource_group_name          = azurerm_resource_group.Web_Rg.name
    allocation_method            = "Static"
}


#creates a network security group defines a rule to allow SSH traffic on TCP port 22:
resource "azurerm_network_security_group" "Web_Sg" {
    name                = "Web_Sg"
    location            = azurerm_resource_group.Web_Rg.location
    resource_group_name = azurerm_resource_group.Web_Rg.name

    security_rule {
      name                       = "SSH"
      priority                   = 1000
      direction                  = "Inbound"
      access                     = "Allow"
      protocol                   = "Tcp"
      source_port_range          = "*"
      destination_port_range     = "22"
      source_address_prefix      = "*"
      destination_address_prefix = "*"
    }

    security_rule {
      name                       = "Port_5000"
      priority                   = 1010
      direction                  = "Inbound"
      access                     = "Allow"
      protocol                   = "Tcp"
      source_port_range          = "*"
      destination_port_range     = "5000"
      source_address_prefix      = "*"
      destination_address_prefix = "*"
    }
}


# Create a Dynamic Interface within the Subnet
resource "azurerm_network_interface" "Web_Interface" {
  name                = "Web_Interface-nic"
  resource_group_name = azurerm_resource_group.Web_Rg.name
  location            = azurerm_resource_group.Web_Rg.location

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.Web_Subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.Web_Publicip.id
  }
}


# Connect the security group to the network interface
resource "azurerm_network_interface_security_group_association" "Web_Int_Sg_Group" {
    network_interface_id      = azurerm_network_interface.Web_Interface.id
    network_security_group_id = azurerm_network_security_group.Web_Sg.id
}


# Data template Bash bootstrapping file
# data "template_file" "linux-vm-cloud-init" {
#   template = file("/script/azure-myflask-data.sh")
# }


## Create a Linux Virtual Instances
resource "azurerm_linux_virtual_machine" "myflaskapp" {
  name                = "myflaskappvm"
  resource_group_name = azurerm_resource_group.Web_Rg.name
  location            = azurerm_resource_group.Web_Rg.location
  size                = "Standard_B1s"
  admin_username      = "daniel"
  # admin_password      = "DanS5431111"
  # disable_password_authentication = false
  network_interface_ids = [
    azurerm_network_interface.Web_Interface.id,
  ]


  admin_ssh_key {
    username   = "daniel"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKzNZw4aQGSD9UUvrwLtY1PAtWW3WmVhgRtJeSoqeskPjZt0biqgIjyzL7k9Ih4Gqk9trFz1f4NZRbrwTyJHtluTP+eNlgWSGQH6lDI9eGX73jdWl4WDuZL0pyqZ/RJ0kNIbPS8z9EJF/eyY2wccOKKQ03KXBdZtEIuCc6W/M77Sf1pfYYCNKfs2HoiBBedsMvz2uEoXzEVf11qc6Bmo0+t7ERZXA8JntbMeT1HVBbODlkJyUbTFkJGoYK2kmsMAyxbif0Q18CbuQH7p+M86j5oxuyjI7HctPoC/0xmTctIZRnw7vnfzQjybtFmDONevJTzf3KgqFhQhV5cubZk0zx rsa-key-20210628"
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }


  # provisioner "file" {
  #   source      = "script/mysql.sh"
  #   destination = "/mysql.sh"

  #   connection {
  #     type        = "ssh"
  #     user        = "daniel"
  #     host        = "${azurerm_public_ip.Web_Publicip.ip_address}"
  #     private_key = "${file("/ssh/flaskapp")}"
  #     timeout  = "10m"
  #   }
  # }

  provisioner "remote-exec" {
    inline = [
      "sudo git init",
      "sudo git clone https://github.com/dshihongyi/Flask-Dev.git",
      "cd Flask-Dev",
      "sudo apt-get update",
      "sudo apt-get -y upgrade",
      "sudo apt-get -y install python3-pip",
      "sudo apt-get -y install mysql-server libmysqlclient-dev",
      "sudo pip3 install -r requirements.txt",
      "sudo chmod +x ./mysql.sh",
      "sudo ./mysql.sh",
      "exit 0"
      # "python3 ~/Flask-Dev/app.py",
    ]   

    connection {
      type        = "ssh"
      user        = "daniel"
      host        = "${azurerm_public_ip.Web_Publicip.ip_address}"
      private_key = "${file("/ssh/myflaskapp.pem")}"
      timeout  = "30"
    }
  }

  # provisioner "local-exec" {
  #   command = "echo ${azurerm_public_ip.Web_Publicip.id} >> private_ips.txt"
  # }

  # custom_data = base64encode(data.template_file.linux-vm-cloud-init.rendered)
}

output "ip" {
    value = azurerm_public_ip.Web_Publicip.ip_address
}