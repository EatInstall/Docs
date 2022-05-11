#!/usr/bin/env python3
# SPDX-License-Identifer: GPL-3.0-or-later
#######################################################################################################

import os, sys
from glob import glob
print("------------- Eat Docs Page List Generator -------------")
if sys.version_info.major < 3:
  print("Error: You must run Python 3 or later to run this script. (Example: Python 2.7 is not supported. 3.10 is supported.)")
  exit(1)
print("VERBose: Checking for documentation entries...")
files = []
print("----------- ENTRIES ------------------------------------")
print("Entries are:")
for i in glob(os.getcwd() + "/*.html"):
  print("   * " + os.path.basename(i).replace(".html",""))
  files.append(i)
print("----------- LIST BUILD ---------------------------------")
print("Starting generation...")
for i in files:
  with open(os.getcwd() + "/index.html", "a") as f:
    f.write("\n<li><a href='" + os.path.basename(i) + "'>" + os.path.basename(i).replace(".html", "") + "</a></li>")
print("Done, exiting successfully! ✅")
exit(0)
