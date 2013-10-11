# -*- coding: utf-8 -*-
__author__ = 'Jet'

import base64
from openerp.tools.translate import _
from openerp import tools
from openerp import SUPERUSER_ID
from openerp.osv import osv, fields


class mail_message_sms(osv.Model):
    """ Update mail.message to add sms support """
    _name = "mail.message"
    _inherit = "mail.message"
    _columns = {'type': fields.selection([
                                             ('email', 'Email'),
                                             ('sms', 'Sms'), # extend type options
                                             ('comment', 'Comment'),
                                             ('notification', 'System notification'),
                                             ], 'Type',
                                         help="Message type: email for email message, notification for system " \
                                              "message, comment for other messages such as user replies"),
                }

class res_partner_mail_sms(osv.Model):
    """ Update partner to add sms support """
    _name = "res.partner"
    _inherit = ['res.partner', 'mail.thread']
    #_mail_flat_thread = False

    def message_post(self, cr, uid, thread_id, **kwargs):
        # handle sms sending
        if kwargs.get('type') == 'sms':
            id = kwargs['context']['default_res_id']
            read = self.read(cr, uid, id, ['mobile'], kwargs.get('context', None))
            if read['mobile']:
                ctx = {'sms_no': read['mobile'], 'sms_msg': kwargs['body']}
                res = self.pool.get('sim.card').send_sms(cr, uid, [], ctx)
                if not res:
                    raise osv.except_osv('Error:', 'Sending Error.')

        return super(res_partner_mail_sms, self).message_post(cr, uid, thread_id, **kwargs)

