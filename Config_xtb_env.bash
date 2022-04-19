#***************************************
# SHELL SCRIPT PARA CONFIGURAR O XTB

#!/usr/bin/env bash
# requirements: $XTBHOME is set to `xtb` root directory
# otherwise the script will find the location of itself here:
if [ -z "${XTBHOME}" ]; then
	   XTBHOME="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi

# set up path for xtb, using the xtb directory and the users home directory
XTBPATH=${XTBHOME}/share/xtb:${XTBHOME}:${HOME}

# to include the documentation we include our man pages in the users manpath
MANPATH=${MANPATH}:${XTBHOME}/share/man

# finally we have to make the binaries and scripts accessable
PATH=${PATH}:${XTBHOME}/bin
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${XTBHOME}/lib
PYTHONPATH=${PYTHONPATH}:${XTBHOME}/python

export PATH XTBPATH MANPATH LD_LIBRARY_PATH PYTHONPATH
#******************************************************
