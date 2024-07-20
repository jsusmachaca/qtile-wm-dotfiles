#!/bin/sh

sleep 0.5

#[Battery Icon]
cbatticon &

#[Volume Icon]
volumeicon &

#[Networking Applet]
nm-applet &

#[Mounted Disks]
# udiskie -t &

#[Bluetooth Applet]
blueman-applet &