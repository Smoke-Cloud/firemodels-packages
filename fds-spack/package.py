# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

import time


class Fdsc(CMakePackage):
    """
    Fire Dynamics Simulator (FDS) is a large-eddy simulation (LES) code for low-speed flows,
    with an emphasis on smoke and heat transport from fires.
    FDS and Smokeview are free and open-source software tools provided by the National Institute
    of Standards and Technology (NIST) of the United States Department of Commerce. Pursuant
    to Title 17, Section 105 of the United States Code, this software is not subject to copyright
    protection and is in the public domain. View the full disclaimer for NIST-developed software.
    """

    maintainers("kjrstory", "JakeOShannessy")
    homepage = "https://pages.nist.gov/fds-smv"
    url = "https://github.com/firemodels/fds/archive/refs/tags/FDS-6.8.0.tar.gz"
    git = "https://github.com/firemodels/fds.git"
    old_git = "https://github.com/firemodels/fds-smv_deprecated.git"

    version("6.10.1", commit="12efa168d7c96257065a0a4dab3f68b3af8aa072", git=git)
    version("6.10.0", commit="618ac072817cb4f287ea5b3d8360dda78339e3a1", git=git)
    version("6.9.1",  commit="889da6ae08d08dae680f7c0d8de66a3ad1c65375", git=git)
    version("6.9.0",  commit="63395692607884566fdedb5db4b5b4d98d3bcafb", git=git)
    version("6.8.0",  commit="886e0096535519b7358a3c4393c91da3caee5072", git=git)
    version("6.7.9",  commit="ec52dee4274fcf994d358c8b0f883eec8f67e041", git=git)
    version("6.7.8",  commit="fbf3e11eee06c89b85fcc936e592bcf27bb9827f", git=git)
    version("6.7.7",  commit="fe0d4ef38f955b2a298ac9124ea3d8f085704edd", git=git)
    version("6.7.6",  commit="5064c500c065b7abc5a34e0ae569a7ad7ec61ec8", git=git)
    version("6.7.5",  commit="71f02560677bb87dace8c81f2e5b817d24e70c46", git=git)
    version("6.7.4",  commit="bfaa110f1c29c157bf5f00143925c6501dd9c79a", git=git)
    version("6.7.3",  commit="9a07c366b6439f7c5b6d89a7b3d97f117b6eeaf2", git=git)
    version("6.7.1",  commit="14cc738f98632e4e7945d7e325f193180b021b8e", git=git)
    version("6.7.0",  commit="5ccea76d225537ef523709c97027cbf081f60108", git=git)
    version("6.6.0",  commit="88ae75a14dbfeef8d77bfcca1997878a14de5c8a", git=git)
    version("6.5.3",  commit="eb56ed1a8a2205333c5b98d636226159ba063d20", git=git)
    version("6.5.2",  commit="4e9103f2e61e60eb23eed8ad3397e8ac66e16216", git=old_git)
    version("6.5.1",  commit="9ea0a920d7816dba678888d69ff6b4393f2a850a", git=old_git)
    version("6.5.0",  commit="ec73757ffabc1ff0f219c1642ef522ca184ff06b", git=old_git)
    version("6.4.0",  commit="59962898c0dbd5926605eed69ed2690c720ca001", git=old_git)
    version("6.3.2",  commit="f5004c4e1e9dc3a9ccc8644b221ca14664dea5dc", git=old_git)
    version("6.3.1",  commit="352eda994c0639660ccc86bbc230b51d00592e8c", git=old_git)
    version("6.3.0",  commit="f7f414800cb6e0829433ad150b0da71d4074ed9d", git=old_git)
    version("6.2.0",  commit="a16945293f61e4de274c9bd714ceca40bb0a2028", git=git)
    version("6.1.2",  commit="689afcd4c59504cc031b860fd081d935a2a3351f", git=old_git)
    version("5.5.3",  commit="bf0a6a88f318803adb96edef5c547746fc77e4a5", git=git)

    variant("openmp", default=False, description="Enable OpenMP support")
    variant("sundials", default=False, when="@6.10:",
            description="Enable SUNDIALS")
    variant("hypre", default=False, when="@6.10:", description="Enable HYPRE")

    # conflicts("%gcc", when="+openmp",
    #           msg="GCC already provides OpenMP support")

    depends_on("fortran", type="build")

    depends_on("mpi")
    depends_on("mkl")
    depends_on("sundials@6.7.0+mpi", when="+sundials")
    depends_on("hypre@2.33.0+mpi", when="+hypre")

    requires(
        "%gcc",
        "%intel",
        "%oneapi",
        policy="one_of",
        msg="FDS builds only with GNU Fortran or Intel Fortran",
    )

    requires(
        "^intel-oneapi-mkl", policy="one_of", msg="FDS builds require Intel oneAPI MKL library"
    )

    requires(
        "^openmpi",
        when="platform=linux %gcc",
        msg="OpenMPI can only be used with GNU Fortran on Linux platform",
    )

    # requires(
    #     "^openmp",
    #     when="%oneapi",
    #     msg="OpenMP can only be used with GNU Fortran on Linux platform",
    # )

    conflicts(
        "~openmp",
        when="@6.7.6:6.7.7",
        msg="versions 6.7.6 and 6.7.7 only builds correctly with OpenMP enabled",
    )

    requires(
        "^intel-oneapi-mpi^intel-oneapi-mkl",
        when="platform=linux %oneapi",
        msg="Intel oneAPI MPI and MKL can only be used with oneAPI Fortran on Linux platform",
    )

    requires(
        "^openmpi%intel",
        when="platform=darwin",
        msg="OpenMPI can only be used with Intel Fortran on macOS",
    )

    patch("fds-5.5.3.patch", when="@5.5.3:6.9.1")
    patch("fds-6.1.2.patch", when="@6.1.2:6.9.1")
    patch("fds-6.2.0.patch", when="@6.2.0:6.9.1")
    patch("fds-6.5.3.patch", when="@6.5.3:6.9.1")
    patch("fds-6.6.0.patch", when="@6.6.0:6.9.1")
    patch("fds-6.7.5.patch", when="@6.7.5:6.9.1")
    patch("fds-6.7.6.patch", when="@6.7.6:6.9.1")
    patch("fds-6.7.7.patch", when="@6.7.7:6.9.1")
    patch("fds-6.7.8.patch", when="@6.7.8:6.9.1")
    patch("fds-6.8.0.patch", when="@6.8.0:6.9.1")
    patch("fds-6.10.0.patch", when="@6.10.0:")

    sanity_check_is_dir = ["bin"]

    revision_dates = {
        "6.10.1": 1743629938,
        "6.10.0": 1741367545,
        "6.9.1": 1712523906,
        "6.9.0": 1710957557,
        "6.8.0": 1681816000,
        "6.7.9": 1656268600,
        "6.7.8": 1653430065,
        "6.7.7": 1637273422,
        "6.7.6": 1622132350,
        "6.7.5": 1597954741,
        "6.7.4": 1583507866,
        "6.7.3": 1572460023,
        "6.7.1": 1549301185,
        "6.7.0": 1529946203,
        "6.6.0": 1509566609,
        "6.5.3": 1484860379,
        "6.5.2": 1472070586,
        "6.5.1": 1467767951,
        "6.5.0": 1466630786,
        "6.4.0": 1460042679,
        "6.3.2": 1447798481,
        "6.3.1": 1447107952,
        "6.3.0": 1443669647,
        "6.2.0": 1428761563,
        "6.1.2": 1411759630,
        "5.5.3": 1288364829,
    }

    def cmake_args(self):
        args = [
            "-DUSE_HYPRE={0}".format("ON" if "+hypre" in self.spec else "OFF"),
            "-DUSE_OPENMP={0}".format("ON" if "+openmp" in self.spec else "OFF"),
            "-DUSE_SUNDIALS={0}".format(
                "ON" if "+sundials" in self.spec else "OFF"),
            "-DGIT_DATE={0}".format(time.strftime("%a, %d %b %Y %H:%M:%S +0000",
                                    time.gmtime(self.revision_dates[self.spec.version.dotted_numeric_string]))),
            "-DGIT_BRANCH=release",
            "-DGIT_HASH={0}".format(self.spec.version),
            "-DGIT_DIRTY=spack",
        ]
        # if self.spec.satsifies("@6.10.0:"):
        args.append("-DUSE_SYSTEM_SUNDIALS=ON")
        args.append("-DUSE_SYSTEM_HYPRE=ON")
        return args
