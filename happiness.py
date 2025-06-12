#!/usr/bin/env python3
import os
import sys
os.execv(sys.executable, ['python'] + sys.argv)
