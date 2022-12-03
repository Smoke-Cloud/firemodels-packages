#!/bin/bash
wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
add-apt-repository "deb https://apt.repos.intel.com/oneapi all main"
apt-get update
