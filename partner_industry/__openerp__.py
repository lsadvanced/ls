# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 L.S. Advanced Software (<http://www.lsweb.it>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Partner Industry Sector',
    'version': '0.1',
    'depends': ['base'],
    'author': 'L.S. Advanced Software',
    'website': 'http://www.lsweb.it',
    'description': """
     Partner's industry sector classification
    """,
    'license': 'AGPL-3',
    'category': 'Sales',
    'data': [
        'security/ir.model.access.csv',
        'partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
