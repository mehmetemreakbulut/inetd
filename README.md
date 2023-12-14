# inetd

#Basic internet service demon with Python

In recent years, due to security limitations in the original inetd design, it has been replaced with xinetd, rlinetd, ucspi-tcp and others on many systems. In particular, GNU/Linux distributions offer many options and macOS (starting from the 10.2 release) uses xinetd . As of Mac OS

The services provided by inetd are not vital, and can be disabled completely. This practice is becoming increasingly common on machines dedicated to a single function. For example, an HTTP server could be configured to simply run httpd , keeping all other ports closed. A dedicated firewall may not start any services.
