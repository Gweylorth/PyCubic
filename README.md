# PyCubic

A Python interface for cubic graphs manipulation.

## Run the application

	$ python run.py

## Prerequisites and installation

* [Python 2.7+](http://www.python.org/download/releases/2.7.5/)
(should already be installed under Unix)
* [nauty and Traces programs](http://cs.anu.edu.au/~bdm/nauty/)
* [graph-tool library](http://projects.skewed.de/graph-tool/)

Example for Debian, `DISTRIBUTION` being replaced by `squeeze` or `sid`:

	$ apt-get install nauty
    $ vim /etc/apt/sources.list
    
	# Add the following lines, replacing `DISTRIBUTION`:

    deb http://downloads.skewed.de/apt/DISTRIBUTION DISTRIBUTION main
    deb-src http://downloads.skewed.de/apt/DISTRIBUTION DISTRIBUTION main
    
	# Save sources.list

    $ apt-get update
    $ apt-get install python-graph-tool

Example for Ubuntu, `DISTRIBUTION` being replaced by `raring`, `quantal`,
`precise`, `oneiric`, `natty` or `maverick`:

    $ apt-get install nauty
    $ vim /etc/apt/sources.list
    
    # Add the following lines, replacing DISTRIBUTION
    
    deb http://downloads.skewed.de/apt/DISTRIBUTION DISTRIBUTION universe
    deb-src http://downloads.skewed.de/apt/DISTRIBUTION DISTRIBUTION universe
    
    # Save sources.list
    
    $ apt-get update
    $ apt-get install python-graph-tool
    
    
## Documentation

Technical documentation in HTML format will be available through `doc/index.html`
after running `release.sh` or `cd sphinx && make html`.

    
## Authors
* Gwenegan HUDIN
* Nicolas BUSSENEAU


## Legal mentions

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

Copyright 2013, Gwenegan HUDIN and Nicolas BUSSENEAU
