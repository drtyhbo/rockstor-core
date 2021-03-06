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

from rest_framework.response import Response
from storageadmin.util import handle_exception
from system.services import (toggle_auth_service, systemctl)
from django.db import transaction
from base_service import BaseServiceDetailView
from smart_manager.models import Service

import logging
logger = logging.getLogger(__name__)


class WinbindServiceView(BaseServiceDetailView):

    @transaction.atomic
    def post(self, request, command):
        """
        execute a command on the service
        """
        service = Service.objects.get(name='winbind')
        if (command == 'config'):
            try:
                config = request.data['config']
                toggle_auth_service('winbind', 'start', config)
                logger.info('authconfig executed')
                self._save_config(service, config)
            except Exception, e:
                logger.exception(e)
                e_msg = ('Winbind could not be configured. Try again')
                handle_exception(Exception(e_msg), request)

        else:
            try:
                toggle_auth_service('winbind', command,
                                    config=self._get_config(service))
                logger.info('authconfig executed')
                if (command == 'stop'):
                    systemctl('winbind', 'disable')
                else:
                    systemctl('winbind', 'enable')
                systemctl('winbind', command)
                logger.info('winbind altered')
            except Exception, e:
                logger.exception(e)
                e_msg = ('Failed to %s winbind service due to system error.' %
                         command)
                handle_exception(Exception(e_msg), request)

        return Response()
