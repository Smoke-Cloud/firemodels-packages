# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

import time


class Cfastc(MakefilePackage):
    """
    CFAST is a two-zone fire model that predicts the thermal environment caused
    by a fire within a compartmented structure.
    """

    maintainers("JakeOShannessy")
    homepage = "https://pages.nist.gov/fds-smv"
    url = "https://github.com/firemodels/cfast/archive/refs/tags/CFAST-7.7.5.tar.gz"
    git = "https://github.com/firemodels/cfast.git0"


    build_directory = "Build"

    version("7.7.4", commit="6b52d0c33bd3760782782ad156e992f0196ca2d9")
    version("7.7.3", commit="80af8c65a8a9d54ec1823cc043f8e278f9804269")
    version("7.7.2", commit="8f924606a394685787630d93e21f86d574c79692")
    version("7.7.1", commit="67bb5b38c01d824e19c07a60e59af74dcb0f435c")
    version("7.7.0", commit="5c5e238f1422ff7524c8fab0aafce6d345711940")
    version("7.5.2", commit="5bb02c08850574b4baeae2c3f57e372872d62077")
    version("7.5.1", commit="0b4b920cf06ee817ebc3de278a12eedcc0683536")
    version("7.4.3", commit="e7ea03fefe2dabe0862110bc0092d9d8feb96675")
    version("7.4.2", commit="3bc2db22d024cef229f607c002733035b51a698d")
    version("7.4.0", commit="26aa3bd74645f2bf0c4c384be7d95606dc052dfe")
    version("7.3.1", commit="6b9b32bbd7d9ef5adaff044b50cb8a62c9c586ba")
    version("7.3.0", commit="839a9c955f62e45716e8cc20db8c9af3c6d1e3da")
    version("7.2.4", commit="d969295bd8dfbce097790844225dbba50fb211f0")
    version("7.2.3", commit="31ef0951cd827fb7f08b090b716a00f6288c8eb5")
    version("7.2.2", commit="31a46d37907e0a3f7f6db47ac5e65c1ba703d7e6")
    version("7.2.1", commit="ee55422a652279437824e11da74202a819a2f9ab")
    version("7.2.0", commit="5b88b97a5a945b792b24dfad72e46e8472334907")
    version("7.1.2", commit="b82e334e84f44854e1685f1d91580b2031eea867")
    version("7.1.1", commit="8f0c67224aaab7a269d60639b29a7beb22c9c695")
    version("7.1.0", commit="7ea5756732fa2db5488647d9d9fbbe7544861cd8")
    version("7.0.1", commit="819e8d78f17a16aa4d0fe2aec6569ad2d8349428")

    depends_on("fortran", type="build")

    requires(
        "%gcc",
        "%intel",
        "%oneapi",
        policy="one_of",
        msg="CFAST builds only with GNU Fortran or Intel Fortran",
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
        "7.7.4": 1673642530,
        "7.7.3": 1652293105,
        "7.7.2": 1635874076,
        "7.7.1": 1627499433,
        "7.7.0": 1624388728,
        "7.5.2": 1591738165,
        "7.5.1": 1589210192,
        "7.4.3": 1572277378,
        "7.4.2": 1569416062,
        "7.4.0": 1562952576,
        "7.3.1": 1554741500,
        "7.3.0": 1528988880,
        "7.2.4": 1511296522,
        "7.2.3": 1502462675,
        "7.2.2": 1493917570,
        "7.2.1": 1480448185,
        "7.2.0": 1478797840,
        "7.1.2": 1468337237,
        "7.1.1": 1461248791,
        "7.1.0": 1459874821,
        "7.0.1": 1449673035,
    }

    def setup_build_environment(self, env) -> None:
        env.set("FFLAGS",'-finit-local-zero -ffpe-trap=invalid,zero,overflow -fbacktrace  -cpp -DGITHASH_PP=\"$(build_version)+g$(commit)\" -DGITDATE_PP=\""$(GIT_DATE)\"" -DBUILDDATE_PP=\""$(BUILD_DATE)\""')
        # env.set("PREFIX", prefix)
        # env.set("BLASLIB", spec["blas"].libs.ld_flags)

    # def cmake_args(self):
    #     args = [
    #         "-DGIT_DATE={0}".format(time.strftime("%a, %d %b %Y %H:%M:%S +0000",
    #                                 time.gmtime(self.revision_dates[self.spec.version.dotted_numeric_string]))),
    #         "-DGIT_BRANCH=release",
    #         "-DGIT_HASH={0}".format(self.spec.version),
    #         "-DGIT_DIRTY=spack",
    #     ]
    #     return args
