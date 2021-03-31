SCRIPT= pyfetch
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
	mkdir -p $(PREFIX)/bin
	cp -f $(SCRIPT) $(PREFIX)/bin/$(EXEC)
	chmod 755 $(PREFIX)/bin/$(EXEC)
	ln -s $(PREFIX)/bin/$(EXEC) $(PREFIX)/bin/$(SHORTEXEC)
	rm -f $(DESTDIR)$(PREFIX)/bin/$(EXEC)
	rm -f $(DESTDIR)$(PREFIX)/bin/$(SHORTEXEC)

.PHONY: install uninstall reinstall
