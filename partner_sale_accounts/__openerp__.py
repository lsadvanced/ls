# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 L.S. Advanced Software srl
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
    'name': 'Partner Sales Accounts',
    'version': '1.0',
    'category': 'Sales',
    'description': """
This module let's you add a list of sales people following this customer.
""",
    'author': 'L.S. Advanced Software',
    'website': 'http://www.lsweb.it',
    'summary': 'Partner Sales Accounts',
    'depends': ['partner_department'],
    'data': [
        'partner_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}