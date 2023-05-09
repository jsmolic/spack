# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.package import *


class Systemd(MesonPackage):
    """systemd is a suite of basic building blocks for a Linux system.
    It provides a system and service manager that runs as PID 1 and starts the rest
    of the system."""

    homepage = "https://systemd.io/"
    url = "https://github.com/systemd/systemd/archive/refs/tags/v253.tar.gz"

    maintainers("jsmolic")

    version("253", sha256="acbd86d42ebc2b443722cb469ad215a140f504689c7a9133ecf91b235275a491")

    depends_on("gperf", type="build")
    depends_on("libcap")
    depends_on("pkgconfig", type="build")
    depends_on("py-jinja2", type="build")
    depends_on("util-linux")
    depends_on("ninja")

    build_directory = "build"

    def meson_args(self):
        args = [ "-Drootprefix={0}".format(self.prefix) ]
        return args

    def install(self, spec, prefix):
        os.environ["DESTDIR"] = prefix
        make("install")
