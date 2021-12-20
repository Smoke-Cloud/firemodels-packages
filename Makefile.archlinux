#default: 5.5.3 6.1.2 6.2.0 6.3.0 6.3.1 6.3.2 6.4.0 6.5.0 6.5.1 6.5.3
.PHONY: default check

default: fds-6.1.2+smokecloud.ifort-6.1.2-1-x86_64.pkg.tar.zst \
	fds-6.2.0+smokecloud.ifort-6.2.0-1-x86_64.pkg.tar.zst \
	fds-6.3.0+smokecloud.ifort-6.3.0-1-x86_64.pkg.tar.zst \
	fds-6.3.1+smokecloud.ifort-6.3.1-1-x86_64.pkg.tar.zst \
	fds-6.3.2+smokecloud.ifort-6.3.2-1-x86_64.pkg.tar.zst \
	fds-6.4.0+smokecloud.ifort-6.4.0-1-x86_64.pkg.tar.zst \
	fds-6.5.0+smokecloud.ifort-6.5.0-1-x86_64.pkg.tar.zst \
	fds-6.5.1+smokecloud.ifort-6.5.1-1-x86_64.pkg.tar.zst \
	fds-6.5.2+smokecloud.ifort-6.5.2-1-x86_64.pkg.tar.zst \
	fds-6.5.3+smokecloud.ifort-6.5.3-1-x86_64.pkg.tar.zst \
	fds-6.6.0+smokecloud.ifort-6.6.0-1-x86_64.pkg.tar.zst \
	fds-6.7.0+smokecloud.ifort-6.7.0-1-x86_64.pkg.tar.zst \
	fds-6.7.1+smokecloud.ifort-6.7.1-1-x86_64.pkg.tar.zst \
	fds-6.7.3+smokecloud.ifort-6.7.3-1-x86_64.pkg.tar.zst \
	fds-6.7.4+smokecloud.ifort-6.7.4-1-x86_64.pkg.tar.zst \
	fds-6.7.5+smokecloud.ifort-6.7.5-1-x86_64.pkg.tar.zst \
	fds-6.7.6+smokecloud.ifort-6.7.6-1-x86_64.pkg.tar.zst \
	fds-6.7.7+smokecloud.ifort-6.7.7-1-x86_64.pkg.tar.zst
	# fds-5.5.3+smokecloud.ifort-5.5.3-1-x86_64.pkg.tar.zst
check: 
	echo "" | /opt/FDS/5.5.3+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.1.2+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.2.0+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.3.0+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.3.1+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.3.2+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.4.0+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.5.0+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.5.1+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.5.2+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.5.3+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.6.0+smokecloud.ifort/bin/fds 1
	echo "" | /opt/FDS/6.7.0+smokecloud.ifort/bin/fds 1
	/opt/FDS/6.7.1+smokecloud.ifort/bin/fds 1
	/opt/FDS/6.7.3+smokecloud.ifort/bin/fds 1
	/opt/FDS/6.7.4+smokecloud.ifort/bin/fds 1
	/opt/FDS/6.7.5+smokecloud.ifort/bin/fds 1
	/opt/FDS/6.7.6+smokecloud.ifort/bin/fds 1
	/opt/FDS/6.7.7+smokecloud.ifort/bin/fds 1
	echo "Each version successfully executed"

install: default
	pacman -U fds-6.7.7+smokecloud.ifort-6.7.7-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.6+smokecloud.ifort-6.7.6-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.5+smokecloud.ifort-6.7.5-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.4+smokecloud.ifort-6.7.4-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.3+smokecloud.ifort-6.7.3-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.1+smokecloud.ifort-6.7.1-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.0+smokecloud.ifort-6.7.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.6.0+smokecloud.ifort-6.6.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.5.3+smokecloud.ifort-6.5.3-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.5.2+smokecloud.ifort-6.5.2-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.5.1+smokecloud.ifort-6.5.1-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.5.0+smokecloud.ifort-6.5.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.4.0+smokecloud.ifort-6.4.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.3.2+smokecloud.ifort-6.3.2-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.3.1+smokecloud.ifort-6.3.1-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.3.0+smokecloud.ifort-6.3.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.2.0+smokecloud.ifort-6.2.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.1.2+smokecloud.ifort-6.1.2-1-x86_64.pkg.tar.zst --noconfirm
	# pacman -U fds-5.5.3+smokecloud.ifort-5.5.3-1-x86_64.pkg.tar.zst --noconfirm

fds-5.5.3+smokecloud.ifort-5.5.3-1-x86_64.pkg.tar.zst: 5.5.3+smokecloud.ifort/PKGBUILD
	cd 5.5.3+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.1.2+smokecloud.ifort-6.1.2-1-x86_64.pkg.tar.zst: 6.1.2+smokecloud.ifort/PKGBUILD
	cd 6.1.2+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.2.0+smokecloud.ifort-6.2.0-1-x86_64.pkg.tar.zst: 6.2.0+smokecloud.ifort/PKGBUILD
	cd 6.2.0+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.3.0+smokecloud.ifort-6.3.0-1-x86_64.pkg.tar.zst: 6.3.0+smokecloud.ifort/PKGBUILD
	cd 6.3.0+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.3.1+smokecloud.ifort-6.3.1-1-x86_64.pkg.tar.zst: 6.3.1+smokecloud.ifort/PKGBUILD
	cd 6.3.1+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.3.2+smokecloud.ifort-6.3.2-1-x86_64.pkg.tar.zst: 6.3.1+smokecloud.ifort/PKGBUILD
	cd 6.3.2+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.4.0+smokecloud.ifort-6.4.0-1-x86_64.pkg.tar.zst: 6.4.0+smokecloud.ifort/PKGBUILD
	cd 6.4.0+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.5.0+smokecloud.ifort-6.5.0-1-x86_64.pkg.tar.zst: 6.5.0+smokecloud.ifort/PKGBUILD
	cd 6.5.0+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.5.1+smokecloud.ifort-6.5.1-1-x86_64.pkg.tar.zst: 6.5.1+smokecloud.ifort/PKGBUILD
	cd 6.5.1+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.5.2+smokecloud.ifort-6.5.2-1-x86_64.pkg.tar.zst: 6.5.2+smokecloud.ifort/PKGBUILD
	cd 6.5.2+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.5.3+smokecloud.ifort-6.5.3-1-x86_64.pkg.tar.zst: 6.5.3+smokecloud.ifort/PKGBUILD
	cd 6.5.3+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.6.0+smokecloud.ifort-6.6.0-1-x86_64.pkg.tar.zst: 6.6.0+smokecloud.ifort/PKGBUILD
	cd 6.6.0+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.0+smokecloud.ifort-6.7.0-1-x86_64.pkg.tar.zst: 6.7.0+smokecloud.ifort/PKGBUILD
	cd 6.7.0+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.1+smokecloud.ifort-6.7.1-1-x86_64.pkg.tar.zst: 6.7.1+smokecloud.ifort/PKGBUILD
	cd 6.7.1+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.3+smokecloud.ifort-6.7.3-1-x86_64.pkg.tar.zst: 6.7.3+smokecloud.ifort/PKGBUILD
	cd 6.7.3+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.4+smokecloud.ifort-6.7.4-1-x86_64.pkg.tar.zst: 6.7.4+smokecloud.ifort/PKGBUILD
	cd 6.7.4+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.5+smokecloud.ifort-6.7.5-1-x86_64.pkg.tar.zst: 6.7.5+smokecloud.ifort/PKGBUILD
	cd 6.7.5+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.6+smokecloud.ifort-6.7.6-1-x86_64.pkg.tar.zst: 6.7.6+smokecloud.ifort/PKGBUILD
	cd 6.7.6+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.7+smokecloud.ifort-6.7.7-1-x86_64.pkg.tar.zst: 6.7.7+smokecloud.ifort/PKGBUILD
	cd 6.7.7+smokecloud.ifort && makepkg -f && cp $@ .. && cd ..
