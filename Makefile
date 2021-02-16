#default: 5.5.3 6.1.2 6.2.0 6.3.0 6.3.1 6.3.2 6.4.0 6.5.0 6.5.1 6.5.3
.PHONY: default

default: fds-5.5.3+nist.ifort-5.5.3-1-x86_64.pkg.tar.zst \
	fds-6.1.2+nist.ifort-6.1.2-1-x86_64.pkg.tar.zst \
	fds-6.2.0+nist.ifort-6.2.0-1-x86_64.pkg.tar.zst \
	fds-6.3.0+nist.ifort-6.3.0-1-x86_64.pkg.tar.zst \
	fds-6.3.1+nist.ifort-6.3.1-1-x86_64.pkg.tar.zst \
	fds-6.3.2+nist.ifort-6.3.2-1-x86_64.pkg.tar.zst \
	fds-6.4.0+nist.ifort-6.4.0-1-x86_64.pkg.tar.zst \
	fds-6.5.0+nist.ifort-6.5.0-1-x86_64.pkg.tar.zst \
	fds-6.5.1+nist.ifort-6.5.1-1-x86_64.pkg.tar.zst \
	fds-6.5.2+nist.ifort-6.5.2-1-x86_64.pkg.tar.zst \
	fds-6.5.3+nist.ifort-6.5.3-1-x86_64.pkg.tar.zst \
	fds-6.6.0+nist.ifort-6.6.0-1-x86_64.pkg.tar.zst \
	fds-6.7.0+nist.ifort-6.7.0-1-x86_64.pkg.tar.zst \
	fds-6.7.1+nist.ifort-6.7.1-1-x86_64.pkg.tar.zst \
	fds-6.7.3+nist.ifort-6.7.3-1-x86_64.pkg.tar.zst \
	fds-6.7.4+nist.ifort-6.7.4-1-x86_64.pkg.tar.zst \
	fds-6.7.4+smokecloud.gnu-6.7.4-1-x86_64.pkg.tar.zst \
	fds-6.7.5+nist.ifort-6.7.5-1-x86_64.pkg.tar.zst \
	fds-6.7.5+smokecloud.gnu-6.7.5-1-x86_64.pkg.tar.zst 

install: default
	pacman -U fds-6.7.5+nist.ifort-6.7.5-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.5+smokecloud.gnu-6.7.5-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.4+nist.ifort-6.7.4-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.4+smokecloud.gnu-6.7.4-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.3+nist.ifort-6.7.3-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.1+nist.ifort-6.7.1-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.7.0+nist.ifort-6.7.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.6.0+nist.ifort-6.6.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.5.3+nist.ifort-6.5.3-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.5.2+nist.ifort-6.5.2-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.5.1+nist.ifort-6.5.1-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.5.0+nist.ifort-6.5.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.4.0+nist.ifort-6.4.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.3.2+nist.ifort-6.3.2-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.3.1+nist.ifort-6.3.1-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.3.0+nist.ifort-6.3.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.2.0+nist.ifort-6.2.0-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-6.1.2+nist.ifort-6.1.2-1-x86_64.pkg.tar.zst --noconfirm
	pacman -U fds-5.5.3+nist.ifort-5.5.3-1-x86_64.pkg.tar.zst --noconfirm



#%.o: %.c $(DEPS)
#		$(CC) -c -o $@ $< $(CFLAGS)
fds-5.5.3+nist.ifort-5.5.3-1-x86_64.pkg.tar.zst: 5.5.3+nist.ifort/PKGBUILD
	cd 5.5.3+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.1.2+nist.ifort-6.1.2-1-x86_64.pkg.tar.zst: 6.1.2+nist.ifort/PKGBUILD
	cd 6.1.2+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.2.0+nist.ifort-6.2.0-1-x86_64.pkg.tar.zst: 6.2.0+nist.ifort/PKGBUILD
	cd 6.2.0+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.3.0+nist.ifort-6.3.0-1-x86_64.pkg.tar.zst: 6.3.0+nist.ifort/PKGBUILD
	cd 6.3.0+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.3.1+nist.ifort-6.3.1-1-x86_64.pkg.tar.zst: 6.3.1+nist.ifort/PKGBUILD
	cd 6.3.1+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.3.2+nist.ifort-6.3.2-1-x86_64.pkg.tar.zst: 6.3.2+nist.ifort/PKGBUILD
	cd 6.3.2+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.4.0+nist.ifort-6.4.0-1-x86_64.pkg.tar.zst: 6.4.0+nist.ifort/PKGBUILD
	cd 6.4.0+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.5.0+nist.ifort-6.5.0-1-x86_64.pkg.tar.zst: 6.5.0+nist.ifort/PKGBUILD
	cd 6.5.0+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.5.1+nist.ifort-6.5.1-1-x86_64.pkg.tar.zst: 6.5.1+nist.ifort/PKGBUILD
	cd 6.5.1+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.5.2+nist.ifort-6.5.2-1-x86_64.pkg.tar.zst: 6.5.2+nist.ifort/PKGBUILD
	cd 6.5.2+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.5.3+nist.ifort-6.5.3-1-x86_64.pkg.tar.zst: 6.5.3+nist.ifort/PKGBUILD
	cd 6.5.3+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.6.0+nist.ifort-6.6.0-1-x86_64.pkg.tar.zst: 6.6.0+nist.ifort/PKGBUILD
	cd 6.6.0+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.0+nist.ifort-6.7.0-1-x86_64.pkg.tar.zst: 6.7.0+nist.ifort/PKGBUILD
	cd 6.7.0+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.1+nist.ifort-6.7.1-1-x86_64.pkg.tar.zst: 6.7.1+nist.ifort/PKGBUILD
	cd 6.7.1+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.3+nist.ifort-6.7.3-1-x86_64.pkg.tar.zst: 6.7.3+nist.ifort/PKGBUILD
	cd 6.7.3+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.4+nist.ifort-6.7.4-1-x86_64.pkg.tar.zst: 6.7.4+nist.ifort/PKGBUILD
	cd 6.7.4+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.4+smokecloud.gnu-6.7.4-1-x86_64.pkg.tar.zst: 6.7.4+smokecloud.gnu/PKGBUILD
	cd 6.7.4+smokecloud.gnu && makepkg -f && cp $@ .. && cd ..
fds-6.7.5+nist.ifort-6.7.5-1-x86_64.pkg.tar.zst: 6.7.5+nist.ifort/PKGBUILD
	cd 6.7.5+nist.ifort && makepkg -f && cp $@ .. && cd ..
fds-6.7.5+smokecloud.gnu-6.7.5-1-x86_64.pkg.tar.zst: 6.7.5+smokecloud.gnu/PKGBUILD
	cd 6.7.5+smokecloud.gnu && makepkg -f && cp $@ .. && cd ..
