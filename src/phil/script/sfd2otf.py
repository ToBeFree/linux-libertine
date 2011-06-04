#!/usr/bin/env fontforge
# -*- coding: utf-8 -*-
#
# wandelt sfd in otf/svg um
#
# $1 sfd-file
# $2 output-dir
#
# $Id$
#
# Michael Niedermair m.g.n@gmx.de
#
import fontforge
import psMat
import sys
import os
import re
import math

if len(sys.argv) < 3:
    sys.exit(sys.argv[0] + ' <sfd-file> <output-dir>')
if not os.path.isdir(sys.argv[2]):
    sys.exit(sys.argv[2] + ' is not a valid dir!')
if not os.path.isfile(sys.argv[1]):
    sys.exit(sys.argv[1] + ' is not a valid file!')


fnt = fontforge.open(sys.argv[1])

print "### " + sys.argv[1]

basename = os.path.basename(sys.argv[1])
filename = re.sub('(?P<name>.*)\.sfd', '\g<name>', basename)
outname = sys.argv[2] + "/" + filename + ".otf"
print "    generate " + outname
fnt.generate(outname)

outname = sys.argv[2] + "/" + filename + ".svg"
print "    generate " + outname
fnt.generate(outname)


