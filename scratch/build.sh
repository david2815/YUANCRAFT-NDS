#!/bin/bash
export DEVKITPRO=/opt/devkitpro
export DEVKITARM=/opt/devkitpro/devkitARM
export PATH=$DEVKITARM/bin:$DEVKITPRO/tools/bin:$PATH

cd "/c/Users/David/Desktop/YUANCRAFT NDS PORT"
make -j4
