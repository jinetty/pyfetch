SCRIPT= pyfetch.py
EXEC= pyfetch
SHORTEXEC = pyf

# paths
PREFIX = /usr/local
MANPREFIX = $(PREFIX)/share/man

install:
	mkdir -p $(PREFIX)/bin
	cp -f $(SCRIPT) $(PREFIX)/bin/$(EXEC)
	chmod 755 $(PREFIX)/bin/$(EXEC)
	ln -s $(PREFIX)/bin/$(EXEC) $(PREFIX)/bin/$(SHORTEXEC)

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/$(EXEC)
	rm -f $(DESTDIR)$(PREFIX)/bin/$(SHORTEXEC)

reinstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/$(EXEC)
	rm -f $(DESTDIR)$(PREFIX)/bin/$(SHORTEXEC)
	mkdir -p $(PREFIX)/bin
	cp -f $(SCRIPT) $(PREFIX)/bin/$(EXEC)
	chmod 755 $(PREFIX)/bin/$(EXEC)
	ln -s $(PREFIX)/bin/$(EXEC) $(PREFIX)/bin/$(SHORTEXEC)

.PHONY: install uninstall reinstall
