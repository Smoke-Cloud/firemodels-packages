#!/bin/bash
wget https://registrationcenter-download.intel.com/akdlm/irc_nas/18236/l_BaseKit_p_2021.4.0.3422_offline.sh
chmod 755 l_BaseKit_p_2021.4.0.3422_offline.sh
wget https://registrationcenter-download.intel.com/akdlm/irc_nas/18211/l_HPCKit_p_2021.4.0.3347_offline.sh
chmod 755 l_HPCKit_p_2021.4.0.3347_offline.sh

sudo ./l_BaseKit_p_2021.4.0.3422_offline.sh -s -a --silent  --eula accept --intel-sw-improvement-program-consent decline --components intel.oneapi.lin.ippcp.devel:intel.oneapi.lin.tbb.devel:intel.oneapi.lin.dpcpp_dbg:intel.oneapi.lin.dpcpp-ct:intel.oneapi.lin.dpcpp-cpp-compiler:intel.oneapi.lin.dnnl:intel.oneapi.lin.mkl.devel:intel.oneapi.lin.ipp.devel:intel.oneapi.lin.python3:intel.oneapi.lin.ccl.devel:intel.oneapi.lin.dpl:intel.oneapi.lin.vtune
sudo ./l_HPCKit_p_2021.4.0.3347_offline.sh   -s -a --silent  --eula accept --intel-sw-improvement-program-consent decline --components intel.oneapi.lin.inspector:intel.oneapi.lin.mpi.devel:intel.oneapi.lin.itac:intel.oneapi.lin.clck:intel.oneapi.lin.ifort-compiler:intel.oneapi.lin.dpcpp-cpp-compiler-pro    
