# -*- coding: iso-8859-1 -*-
# Copyright (C) 2009 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from PyQt4 import QtCore, QtGui
from .linkchecker_ui_options import Ui_Options

class LinkCheckerOptions (QtGui.QDialog, Ui_Options):
    """Hold options for current URL to check."""

    def __init__ (self, parent=None):
        super(LinkCheckerOptions, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.resetButton, QtCore.SIGNAL("clicked()"), self.reset)
        self.connect(self.closeButton, QtCore.SIGNAL("clicked()"), self.close)

    def reset (self):
        """Reset options to default values."""
        self.recursionlevel.setValue(-1)
        self.verbose.setChecked(False)
        self.threads.setValue(10)
        self.timeout.setValue(60)