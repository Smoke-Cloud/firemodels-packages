#default: 5.5.3 6.1.2 6.2.0 6.3.0 6.3.1 6.3.2 6.4.0 6.5.0 6.5.1 6.5.3
.PHONY: default

default: fds-5.5.3-5.5.3-1-x86_64.pkg.tar.xz \
	fds-6.1.2-6.1.2-1-x86_64.pkg.tar.xz \
	fds-6.2.0-6.2.0-1-x86_64.pkg.tar.xz \
	fds-6.3.0-6.3.0-1-x86_64.pkg.tar.xz \
	fds-6.3.1-6.3.1-1-x86_64.pkg.tar.xz \
	fds-6.3.2-6.3.2-1-x86_64.pkg.tar.xz \
	fds-6.4.0-6.4.0-1-x86_64.pkg.tar.xz \
	fds-6.5.0-6.5.0-1-x86_64.pkg.tar.xz \
	fds-6.5.1-6.5.1-1-x86_64.pkg.tar.xz \
	fds-6.5.3-6.5.3-1-x86_64.pkg.tar.xz \
	fds-6.6.0-6.6.0-1-x86_64.pkg.tar.xz \
	fds-6.7.0-6.7.0-1-x86_64.pkg.tar.xz \
	fds-6.7.1-6.7.1-1-x86_64.pkg.tar.xz \
	fds-6.7.3-6.7.3-1-x86_64.pkg.tar.xz \
	fds-6.7.4-6.7.4-1-x86_64.pkg.tar.xz 

install: default
	pacman -U fds-5.5.3-5.5.3-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.1.2-6.1.2-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.2.0-6.2.0-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.3.0-6.3.0-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.3.1-6.3.1-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.3.2-6.3.2-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.4.0-6.4.0-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.5.0-6.5.0-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.5.1-6.5.1-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.5.3-6.5.3-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.6.0-6.6.0-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.7.0-6.7.0-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.7.1-6.7.1-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.7.3-6.7.3-1-x86_64.pkg.tar.xz --noconfirm
	pacman -U fds-6.7.4-6.7.4-1-x86_64.pkg.tar.xz --noconfirm



#%.o: %.c $(DEPS)
#		$(CC) -c -o $@ $< $(CFLAGS)
fds-5.5.3-5.5.3-1-x86_64.pkg.tar.xz: 
	cd 5.5.3 && makepkg -f && cp $@ .. && cd ..
fds-6.1.2-6.1.2-1-x86_64.pkg.tar.xz:
	cd 6.1.2 && makepkg -f && cp $@ .. && cd ..
fds-6.2.0-6.2.0-1-x86_64.pkg.tar.xz:
	cd 6.2.0 && makepkg -f && cp $@ .. && cd ..
fds-6.3.0-6.3.0-1-x86_64.pkg.tar.xz:
	cd 6.3.0 && makepkg -f && cp $@ .. && cd ..
fds-6.3.1-6.3.1-1-x86_64.pkg.tar.xz:
	cd 6.3.1 && makepkg -f && cp $@ .. && cd ..
fds-6.3.2-6.3.2-1-x86_64.pkg.tar.xz:
	cd 6.3.2 && makepkg -f && cp $@ .. && cd ..
fds-6.4.0-6.4.0-1-x86_64.pkg.tar.xz:
	cd 6.4.0 && makepkg -f && cp $@ .. && cd ..
fds-6.5.0-6.5.0-1-x86_64.pkg.tar.xz:
	cd 6.5.0 && makepkg -f && cp $@ .. && cd ..
fds-6.5.1-6.5.1-1-x86_64.pkg.tar.xz:
	cd 6.5.1 && makepkg -f && cp $@ .. && cd ..
fds-6.5.3-6.5.3-1-x86_64.pkg.tar.xz:
	cd 6.5.3 && makepkg -f && cp $@ .. && cd ..
fds-6.6.0-6.6.0-1-x86_64.pkg.tar.xz:
	cd 6.6.0 && makepkg -f && cp $@ .. && cd ..
fds-6.7.0-6.7.0-1-x86_64.pkg.tar.xz:
	cd 6.7.0 && makepkg -f && cp $@ .. && cd ..
fds-6.7.1-6.7.1-1-x86_64.pkg.tar.xz:
	cd 6.7.1 && makepkg -f && cp $@ .. && cd ..
fds-6.7.3-6.7.3-1-x86_64.pkg.tar.xz:
	cd 6.7.3 && makepkg -f && cp $@ .. && cd ..
fds-6.7.4-6.7.4-1-x86_64.pkg.tar.xz:
	cd 6.7.4 && makepkg -f && cp $@ .. && cd ..
