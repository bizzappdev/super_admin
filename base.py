# -*- coding: utf-8 -*-
from osv import osv
from openerp import SUPERUSER_ID

def name_selection_groups(ids): return 'sel_groups_' + '_'.join(map(str, ids))
def name_boolean_group(id): return 'in_group_' + str(id)

class res_users(osv.osv):
    _inherit = 'res.users'

    def init(self, cr):
        for app, kind, gs in self.pool.get('res.groups').get_groups_by_application(cr, 1):
            try:
                if kind == 'selection':
                    self.write(cr, 1 , [SUPERUSER_ID],{name_selection_groups(map(int, gs)):gs[-1].id})
                else:
                    for g in gs:
                        self.write(cr, 1 , [SUPERUSER_ID],{name_boolean_group(g.id):True})
            except:
                continue



res_users()


class module(osv.osv):
    _inherit = "ir.module.module"
    
    def button_immediate_install(self, cr, uid, ids, context=None):
        print "999999999999999999999999999999999(((("
        res = super(module, self).button_immediate_install(cr, uid, ids, context=context)
        
        for app, kind, gs in self.pool.get('res.groups').get_groups_by_application(cr, SUPERUSER_ID):
            try:
                if kind == 'selection':
                    self.pool.get('res.users').write(cr, SUPERUSER_ID , [SUPERUSER_ID],{name_selection_groups(map(int, gs)):gs[-1].id})
                else:
                    for g in gs:
                        self.pool.get('res.users').write(cr, SUPERUSER_ID , [SUPERUSER_ID],{name_boolean_group(g.id):True})
            except :
             
                continue
        return res
