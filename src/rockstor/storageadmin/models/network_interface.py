"""
Copyright (c) 2012-2013 RockStor, Inc. <http://rockstor.com>
This file is part of RockStor.

RockStor is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.

RockStor is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from django.db import models


class NetworkInterface(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, null=True)
    mac = models.CharField(max_length=100)
    boot_proto = models.CharField(max_length=100, null=True)
    onboot = models.CharField(max_length=100, null=True)
    network = models.CharField(max_length=100, null=True)
    netmask = models.CharField(max_length=100, null=True)
    ipaddr = models.CharField(max_length=100, null=True)
    itype = models.CharField(max_length=100, default='io')
    gateway = models.CharField(max_length=100, null=True)
    dns_servers = models.CharField(max_length=1024, null=True)
    domain = models.CharField(max_length=1024, null=True)

    class Meta:
        app_label = 'storageadmin'
