FROM lscr.io/linuxserver/code-server:latest

USER root

COPY packages.txt /tmp/packages.txt

RUN apt-get update && \
	grep -vE '^\s*#|^\s*$' /tmp/packages.txt | xargs apt-get install -y --no-install-recommends && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/packages.txt

USER abc
