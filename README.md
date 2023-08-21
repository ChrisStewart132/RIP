# cosc364 rip simulation


https://github.com/ChrisStewart132/RIP/assets/30304173/1b7c396f-2e2c-4d6d-a73f-62e5212ff06b


cmd: python3 ripd.py tests/1/config1.txt

Implementation of a “routing daemon” as a normal userspace program under Linux.
Instead of sending its routing packets over real network interfaces, it communicates
with its peer daemons (which run in parallel on the same machine) through local sockets.
	- reads a configuration file specifying the simulated network
	- creates UDP sockets for each of its input ports
	- loops reaction to incoming events
	- follows parts of: G. Malkin. RIP Version 2. RFC 2453, 1998
