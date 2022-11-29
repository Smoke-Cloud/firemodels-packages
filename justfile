make-fedora version:
	mkdir -p dist
	cd {{version}} && bash ../makerpm.sh
	cp {{version}}/rpmbuild/RPMS/*.rpm ../dist

install-fedora version:
	dnf install -y dist/fds{{version}}*

make-fedora-all: (make-fedora "5.5.3") (make-fedora "6.1.2") (make-fedora "6.2.0") (make-fedora "6.3.0") (make-fedora "6.3.1") (make-fedora "6.3.2") (make-fedora "6.4.0") (make-fedora "6.5.0") (make-fedora "6.5.1") (make-fedora "6.5.2") (make-fedora "6.5.3") (make-fedora "6.6.0") (make-fedora "6.7.0") (make-fedora "6.7.1") (make-fedora "6.7.3") (make-fedora "6.7.4") (make-fedora "6.7.5") (make-fedora "6.7.6") (make-fedora "6.7.7") (make-fedora "6.7.8") (make-fedora "6.7.9")

install-fedora-all: (install-fedora "5.5.3") (install-fedora "6.1.2") (install-fedora "6.2.0") (install-fedora "6.3.0") (install-fedora "6.3.1") (install-fedora "6.3.2") (install-fedora "6.4.0") (install-fedora "6.5.0") (install-fedora "6.5.1") (install-fedora "6.5.2") (install-fedora "6.5.3") (install-fedora "6.6.0") (install-fedora "6.7.0") (install-fedora "6.7.1") (install-fedora "6.7.3") (install-fedora "6.7.4") (install-fedora "6.7.5") (install-fedora "6.7.6") (install-fedora "6.7.7") (install-fedora "6.7.8") (install-fedora "6.7.9")

test-all:
	bash run-tests.sh
