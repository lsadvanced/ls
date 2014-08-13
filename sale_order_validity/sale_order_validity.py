# -*- encoding: utf-8 -*-
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

# Purpose of the module: allow better order handling by improving and automating the order validity terms
#
# How it works:
#
# It will add two new fileds. Order validity and type of validity
# By default, order validity is 30 days from SO creation and that is reflected in the selection field and in the order date field (normally hidden)
# By selecting a new validity type (10 days, 15 days, ecc) the validity date will be adjusted. 
# By selecting an empty validity type the validity date field will be unhidden - this to allow a specific date now hardcoded in the selection field
#
# Update: 10 Dec 2013


from openerp.osv import osv, fields
import datetime

class sale_order_validity(osv.osv):

    _inherit = 'sale.order'
    
    def compute_expiration(self, cr, uid, context=None):
        res={}
        sale_order_line = {}
         
        sale_orders=self.pool.get('sale.order')
        ids = sale_orders.search(cr, uid, [])
        
        for sale_order_line in self.browse(cr, uid, ids, context=context):
            if ((datetime.datetime.strptime(sale_order_line.date_validity,'%Y-%m-%d')<datetime.datetime.today()) and sale_order_line.state=='draft'):           
                self.write(cr, uid, [sale_order_line.id], {'order_expired' : True}, context=context)
        return res
    
    _columns = {
		'mode_validity': fields.selection([('10 Days','10 Days'),('15 Days','15 Days'),('30 Days','30 Days'),('60 Days','60 Days')]),
        'date_validity': fields.date('Deadline Date'),
        'order_expired': fields.boolean('Order expired'),
    }
    _defaults = {  
    	'mode_validity' : lambda *a: '30 Giorni',
        'order_expired' : lambda *b: False,
    }

    def on_change_date_type(self, cr, uid, ids, type, order_date_str, context=None):
        vals= {}
        new_date= None
        order_date=datetime.datetime.strptime(order_date_str, '%Y-%m-%d')
        if type == '10 Days':
           date_ahead=order_date+datetime.timedelta(days=10)
           new_date=date_ahead.strftime('%Y-%m-%d %H:%M:%S')
           vals = {'date_validity': new_date}
        if type == '15 Days':
           date_ahead=order_date+datetime.timedelta(days=15)
           new_date=date_ahead.strftime('%Y-%m-%d %H:%M:%S')
           vals = {'date_validity': new_date}
        if type == '30 Days':
           date_ahead=order_date+datetime.timedelta(days=30)
           new_date=date_ahead.strftime('%Y-%m-%d %H:%M:%S')
           vals = {'date_validity': new_date}  
        if type == '60 Days':
           date_ahead=order_date+datetime.timedelta(days=60)
           new_date=date_ahead.strftime('%Y-%m-%d %H:%M:%S')
           vals = {'date_validity': new_date}  
            
        if (new_date and (datetime.datetime.strptime(new_date,'%Y-%m-%d %H:%M:%S')>datetime.datetime.today())):
           vals['order_expired'] = False 
        else:
           vals['order_expired'] = True
               
        return {'value': vals}



