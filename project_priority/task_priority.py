# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields

class task_priority(osv.osv):

    _name = 'project.task'
    _inherit = 'project.task'
    _columns = {
		'urgency'   : fields.integer('Urgenza'),
        'importance': fields.integer('Importanza'),
        'comp_priority': fields.integer('Priorità'),
        'difficulty': fields.integer('Difficoltà'),         
    }
    _order = 'comp_priority desc'   
    _defaults = {
    	'urgency' : lambda *a: 2,
    	'importance' : lambda *a: 2,
        'comp_priority': lambda *a: 4,
        'difficulty': lambda *a: 3,
    }

    def project_task_onchange(self, cr, uid, ids, urgency, importance, context=None):

        _comp_priority= urgency * importance
        vals = {'comp_priority': _comp_priority}        
        return {'value': vals}
 