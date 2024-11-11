##
## This file is part of the libsigrokdecode project.
##
## Copyright (C) 2024 Ciaran Roche <ciaranderoiste123@gmail.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

'''
OPEN Alliance 10BASE-T1x MAC-PHY Serial Interface describes a serial interface between a MAC-PHY and a
station control unit e.g. a microcontroller. 

https://opensig.org/wp-content/uploads/2023/12/OPEN_Alliance_10BASET1x_MAC-PHY_Serial_Interface_V1.1.pdf

'''

from .pd import Decoder