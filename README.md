# cosc364 rip simulation

cmd: python3 ripd.py tests/1/config1.txt

Implementation of a “routing daemon” as a normal userspace program under Linux.
Instead of sending its routing packets over real network interfaces, it communicates
with its peer daemons (which run in parallel on the same machine) through local sockets.
	- reads a configuration file specifying the simulated network
	- creates UDP sockets for each of its input ports
	- loops reaction to incoming events
	- follows parts of: G. Malkin. RIP Version 2. RFC 2453, 1998