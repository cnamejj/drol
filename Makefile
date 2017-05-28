#drol: Makefile
#Written by Bradley Sadowsky, MIT License <bradley.sadowsky@gmail.com>
#11/24/2016

all: drol.py drol.1.gz
	install drol.py /bin
	install -g 0 -o 0 -m 0644 drol.1.gz /usr/share/man/man1

noop-install: drol.py drol.1.gz # Installs without any options passed to install
	install drol.py /bin
	install drol.1.gz /usr/share/man/man1

mac-install: drol.py drol.1.gz # Installs to a mac with security features
	install drol.py /usr/local/bin
	install drol.1.gz /usr/share/man/man1
