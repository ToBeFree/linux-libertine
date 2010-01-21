#!/usr/bin/env fontforge
# -*- coding: utf-8 -*-
#
# erstellt die shadow Version des Libertine-Font
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
import libertine

if len(sys.argv) < 3:
    sys.exit(sys.argv[0] + ' <sfd-file> <output-dir>')
if not os.path.isdir(sys.argv[2]):
    sys.exit(sys.argv[2] + ' is not a valid dir!')
if not os.path.isfile(sys.argv[1]):
    sys.exit(sys.argv[1] + ' is not a valid file!')

fnt = fontforge.open(sys.argv[1])

print "### " + sys.argv[1]

if libertine.fonts.has_key(fnt.fontname) == False:
   print "### Fontname " + fnt.fontname + " unknown";
   sys.exit(0);

fontnames = libertine.fonts[fnt.fontname];
version = fnt.version

if fontnames.has_key("shfilename") == False:
   print "### Fontname " + fnt.fontname + " no shadow";
   sys.exit(0);

fnt.close();

filename = fontnames["shfilename"];
fontname = fontnames["shfontname"];
familyname = fontnames["shfamilyname"];
fullname = fontnames["shfullname"];
weight = fontnames["shweight"];

# $1 sfd-file
# $2 out-dir
# $3 filename
# $4 fontname
# $5 familyname
# $6 fullname
# $7 weight
cmd = 'fontforge -script script/createShadow.pe ' \
	+ sys.argv[1] + ' ' \
	+ sys.argv[2] + ' ' \
	+ filename + ' ' \
	+ '"' + fontname + '" ' \
	+ '"' + familyname + '" ' \
	+ '"' + fullname + '" ' \
	+ '"' + weight + '" ' \
	+ '"' + version + '"'
print "### system: " + cmd
os.system(cmd)
