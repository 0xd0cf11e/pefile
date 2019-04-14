#!/usr/bin/python
"""
Output all the export function names of a PE file.

Suweera De Souza <0xd0cf11e@gmail.com>
"""

import sys
import pefile

if len(sys.argv) == 2:
    print("Running script on %s ..." % sys.argv[1])
    pe = pefile.PE(sys.argv[1])
    if pe.is_dll():
        for export in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            print export.name
    else:
        print "File is not a DLL. Aborting."
else:
    print "Run script on a DLL file"
