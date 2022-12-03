#!/bin/bash
awk -F, '{ print $2 }' versions.csv | xargs -n 1 git log -1 --format="%ct"
