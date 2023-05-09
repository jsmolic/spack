# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Glibc(AutotoolsPackage):
    """The GNU C Library project provides the core libraries for the GNU system
    and GNU/Linux systems, as well as many other systems that use Linux as the kernel.
    These libraries provide critical APIs including ISO C11, POSIX.1-2008, BSD,
    OS-specific APIs and more. These APIs include such foundational facilities as open,
    read, write, malloc, printf, getaddrinfo, dlopen, pthread_create, crypt, login,
    exit and more.

    The GNU C Library is designed to be a backwards compatible, portable, and
    high performance ISO C library. It aims to follow all relevant standards
    including ISO C11, POSIX.1-2008, and IEEE 754-2008."""

    homepage = "https://www.gnu.org/software/libc/libc.html"
    url = "http://ftp.gnu.org/gnu/glibc/glibc-2.37.tar.xz"

    maintainers("jsmolic")

    version("2.37", sha256="2257eff111a1815d74f46856daaf40b019c1e553156c69d48ba0cbfc1bb91a43")
    version("2.36", sha256="1c959fea240906226062cb4b1e7ebce71a9f0e3c0836c09e7e3423d434fcfe75")
    version("2.35", sha256="5123732f6b67ccd319305efd399971d58592122bcc2a6518a1bd2510dd0cf52e")
    version("2.34", sha256="44d26a1fe20b8853a48f470ead01e4279e869ac149b195dda4e44a195d981ab2")
    version("2.33", sha256="2e2556000e105dbd57f0b6b2a32ff2cf173bde4f0d85dffccfd8b7e51a0677ff")
    version("2.32", sha256="1627ea54f5a1a8467032563393e0901077626dc66f37f10ee6363bb722222836")
    version("2.31", sha256="9246fe44f68feeec8c666bb87973d590ce0137cca145df014c72ec95be9ffd17")
    version("2.30", sha256="e2c4114e569afbe7edbc29131a43be833850ab9a459d81beb2588016d2bbb8af")
    version("2.29", sha256="f3eeb8d57e25ca9fc13c2af3dae97754f9f643bc69229546828e3a240e2af04b")
    version("2.28", sha256="b1900051afad76f7a4f73e71413df4826dce085ef8ddb785a945b66d7d513082")
    version("2.27", sha256="5172de54318ec0b7f2735e5a91d908afe1c9ca291fec16b5374d9faadfc1fc72")
    version("2.26", sha256="e54e0a934cd2bc94429be79da5e9385898d2306b9eaf3c92d5a77af96190f6bd")
    version("2.25", sha256="067bd9bb3390e79aa45911537d13c3721f1d9d3769931a30c2681bfee66f23a0")
    version("2.24", sha256="99d4a3e8efd144d71488e478f62587578c0f4e1fa0b4eed47ee3d4975ebeb5d3")
    version("2.23", sha256="94efeb00e4603c8546209cefb3e1a50a5315c86fa9b078b6fad758e187ce13e9")
    version("2.22", sha256="eb731406903befef1d8f878a46be75ef862b9056ab0cde1626d08a7a05328948")
    version("2.21", sha256="aeeb362437965a5d3f40b151094ca79def04a115bd363fdd4a9a0c69482923b8")
    version("2.20", sha256="f84b6d42aecc288d593c397b0a3d02260a33ee686bce0c634eb9b32798f36ba5")
    version("2.19", sha256="2d3997f588401ea095a0b27227b1d50cdfdd416236f6567b564549d3b46ea2a2")
    version("2.18", sha256="2cb4e1e381928f1e5e55e71ab1ba8e0ea7ede75ff9709770435bfd018ea257a3")
    version("2.17", sha256="6914e337401e0e0ade23694e1b2c52a5f09e4eda3270c67e7c3ba93a89b5b23e")
    version("2.16.0", sha256="1edc36aa2a6cb7127971fce8e02eecffe9c7956297ad3ef10dd4c09f486d5924")
    version("2.15", sha256="321ec482abdc27b03244f7b345ee22dc431bc55daf9c000a4e7b040fbdbecb50")
    version("2.14.1", sha256="984dcfcf2621494b56be3c2f625fa418231c1cb2eb07143ca4a587a6b250b468")
    version("2.14", sha256="4b20592dd4c841e54fde4c0f1d28cc75f91fb61fb3e91a906d5025dd187bfb08")
    version("2.13", sha256="98ee47fc77b01d5805e2cad3ed8e5515220ff32626a049dff3d5529b8f8bdcc1")
    version("2.12.2", sha256="0eb4fdf7301a59d3822194f20a2782858955291dd93be264b8b8d4d56f87203f")
    version("2.12.1", sha256="9e633fb278b411a90636cc1c4bf1ffddcc8b0d214f5bacd74bfcdaac81d6035e")
    version("2.11.3", sha256="5dccd5e462d08e8fa09d787f7e80c2de36adc9ba999927c6efa2ca9aad39302b")
    version("2.11.2", sha256="3e13bf9fc4ebb85e7fc845dd1d0a8659932222f6d95f6adc6adf8d54af97780d")
    version("2.11.1", sha256="686b3ec570f77349ea440bfe6f8e99222bf7206c222f0707015b747c2b58f508")
    version("2.11", sha256="9b3a7b924e152a85a3e000e95bc9c20c1462d876f5d6de1bc0b280d956dfd6af")

    depends_on("binutils", type="build")
    depends_on("gawk", type="build")
    depends_on("bison", type="build")
    build_directory = "spack-build"

    # Linux kernel headers 2.6.19 or later are required
    # depends_on("linux-headers")

    dynamic_linker = 'lib/ld-linux-x86-64.so.2'

    def install(self, spec, prefix):
        configure_args = [
            "--prefix={0}".format(prefix),
            "--disable-dependency-tracking",
            "--disable-debug",
            "--enable-obsolete=rpc",
            "--with-binutils={0}".format(spec['binutils'].prefix.bin)
        ]

        # Fix error: selinux/selinux.h: No such file or directory
        configure_args.append('--without-selinux')

        with working_dir("build", create=True):
            configure = Executable('../configure')
            configure(*configure_args)

            make()
            make('install')

        force_symlink('ld-linux-x86-64.so.2', join_path(prefix.lib, 'ld.so'))
