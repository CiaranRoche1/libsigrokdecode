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

import sigrokdecode as srd
from collections import namedtuple

class Decoder(srd.Decoder):
    api_version = 3
    id = 'oaspi'
    name = 'OA-SPI'
    longname = 'OPEN Alliance Serial Peripheral Interface'
    desc = 'OPEN Alliance Compilant Serial Peripheral Interface'
    license = 'gplv2+'
    inputs = ['logic']
    outputs = ['spi']
    tags = ['Embedded/automotive']
    channels = (
        {'id': 'sck', 'name': 'SCK', 'desc': 'Clock'},
        {'id': 'miso', 'name': 'MISO', 'desc': 'Master in, slave out'},
        {'id': 'mosi', 'name': 'MOSI', 'desc': 'Master out, slave in'},
        {'id': 'cs', 'name': 'CSn', 'desc': 'Chip-select (Active Low)'},
        {'id': 'irq', 'name': 'IRQn', 'desc': 'MAC-PHY Interrupt Request (Active Low)'},
    )
    options = (
        {'id': 'chunk_sz', 'desc': 'Chuck Size'}
    )
    annotations = (
        ('miso-data', 'MISO data'),
        ('mosi-data', 'MOSI data'),
        ('miso-bit', 'MISO bit'),
        ('mosi-bit', 'MOSI bit'),
        ('warning', 'Warning'),
        ('miso-transfer', 'MISO transfer'),
        ('mosi-transfer', 'MOSI transfer'),
    )
    annotation_rows = (
        ('miso-bits', 'MISO bits', (2,)),
        ('miso-data-vals', 'MISO data', (0,)),
        ('miso-transfers', 'MISO transfers', (5,)),
        ('mosi-bits', 'MOSI bits', (3,)),
        ('mosi-data-vals', 'MOSI data', (1,)),
        ('mosi-transfers', 'MOSI transfers', (6,)),
        ('other', 'Other', (4,)),
    )
    binary = (
        ('miso', 'MISO'),
        ('mosi', 'MOSI'),
    )

    def __init__(self):
        self.reset()

    def reset(self):
        self.samplerate = None

    def start(self):
        self.out_python = self.register(srd.OUTPUT_PYTHON)
        self.out_ann = self.register(srd.OUTPUT_ANN)
        self.out_binary = self.register(srd.OUTPUT_BINARY)
        self.out_bitrate = self.register(srd.OUTPUT_META,
                meta=(int, 'Bitrate', 'Bitrate from Start bit to Stop bit'))
        
    def metadata(self, key, value):
        if key == srd.SRD_CONF_SAMPLERATE:
            self.samplerate = value
        
    