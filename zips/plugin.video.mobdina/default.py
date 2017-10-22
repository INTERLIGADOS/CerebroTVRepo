#!/usr/bin/python
# -*- coding: UTF-8 -*-
#/*  ==== Author :: _beastMaster [ SweetWork Copyright (C) 2017 ] ==============
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# *  ===========================================================================
# *  
# */

import sys

from resources.lib.common import control

from resources.main import SwampAddon

################################################################################
#  Plugin Entry Point
################################################################################

if __name__ == "__main__":
    try: result = SwampAddon(sys.argv).execute()
    except KeyboardInterrupt: sys.exit(-1)
    else:
        if result is not None: control.infoDialog(control.lang(30492))
        sys.exit(result)
