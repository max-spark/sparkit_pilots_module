# -*- coding: utf-8 -*-
{
    'name': "SparkIt Pilots Module",

    'summary': """
        Optional Addon module to SparkIt allowing to create pilot objects and
        pilot udpate forms""",

    'description': """
        This module allows the user to create, manage, and track pilot programs.
        In each pilot, you can add communities, add a Pilot Learning Plan, and
        track up to 10 indicators and qualitative data on pilot progress through
        pilot update forms, which are accessible via normal visit report forms.
    """,

    'author': "Spark MicroGrants",
    'website': "http://www.sparkmicrogrants.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sparkit'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pilot_views.xml',
        'views/sparkit_community_views.xml',
        'views/sparkit_vrf_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
