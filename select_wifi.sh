#!/bin/bash

# This script switches between networks based on the gpio pins.
# To write to and read from the gpio pins the WiringPi library is used.
# See: https://projects.drogon.net/raspberry-pi/wiringpi/

network_folder="$(dirname $0)/network-settings/"
network_changed=0

# Pin numbers on which the hardware module is connected in BCM GPIO numbering.
FED0A=9
FED0B=25
FED0C=11
ad_hoc=8


test_pin() {
    pid=$1
    /usr/local/bin/gpio -g mode $pid in
    result=$(gpio -g read $pid)
    /usr/local/bin/gpio reset
}

copy_network_settings() {
    sudo cp "$network_folder/$1" /etc/network/interfaces
    if [ $# -eq 2 ]; then
        sudo cp "$network_folder/$2" /etc/wpa_supplicant/wpa_supplicant.conf
    fi
    network_changed=1
}

restart_network() {
    { sudo ifdown wlan0
      sudo ifup wlan0
    } &> /dev/null
}


test_pin $FED0A
if [ $result -eq 1 ]; then
    echo "Network FED0A has been selected"
    copy_network_settings "interfaces-default" "wpa_supp_FED0A"
    restart_network
fi

test_pin $FED0B
if [ $result -eq 1 ]; then
    echo "Network FED0B has been selected"
    copy_network_settings "interfaces-default" "wpa_supp_FED0B"
    restart_network
fi

test_pin $FED0C
if [ $result -eq 1 ]; then
    echo "Network FED0C has been selected"
    copy_network_settings "interfaces-default" "wpa_supp_FED0C"
    restart_network
fi

test_pin $ad_hoc
if [ $result -eq 1 ]; then
    echo "The ad-hoc network has been selected"
    copy_network_settings "interfaces-ad-hoc"
    sudo /etc/init.d/isc-dhcp-server start
    restart_network
fi

if [ $network_changed -eq 0 ]; then
    echo "No network has been selected"
fi

