# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2013 L.S. Advanced Software (<http://www.lsweb.it>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Priorità sui task",
    "version" : "1.0",
    "author" : "L.S. Advanced Software Srl",
    "category" : "Generic Modules/Project",
    'description': """
This module adds a priority field for each task item calculated by multiplying urgency and importance factors.
""",
    "depends" : ['project'],
    "init_xml" : [],
    "data" : ["task_priority.xml",],
    'auto_install': False,
    'installable': True,
}