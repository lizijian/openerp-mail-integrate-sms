# -*- coding: utf-8 -*-
{
    'name': 'Crm(mail) integrate Sms',
    'description': """
Crm(mail) integrate Sms
""",
    'author': 'Jet',
    'version': '0.1',
    'category': 'Customer Relationship Management',
    'installable': True,
    'auto_install': False,
    'depends': [
        'crm',
        'mail',
        'android_sms',
    ],
    'data': [
        #'crm_data.xml',
    ],
    'js': ['static/src/js/mail_sms.js'],
    'qweb': ['static/src/xml/mail_sms.xml'],
    'application': True,
    'bootstrap': True,
    #'images': ['images/crm_dashboard.png', 'images/customers.png','images/leads.png','images/opportunities_kanban.png','images/opportunities_form.png','images/opportunities_calendar.png','images/opportunities_graph.png','images/logged_calls.png','images/scheduled_calls.png','images/stages.png'],
}
