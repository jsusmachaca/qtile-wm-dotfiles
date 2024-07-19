#!/bin/sh

#[Battery Icon]
cbatticon &

#[Networking Applet]
nm-applet &

#[Volume Icon]
volumeicon &

#[Mounted Disks]
# udiskie -t &

#[Bluetooth Applet]
blueman-applet &
