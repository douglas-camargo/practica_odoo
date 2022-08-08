# -*- coding: utf-8 -*-

{
    "name": "Odoo Academy",
    
    "summary": "Academy app to manage Training",
    
    "description": "courses",
    
    "author": "douglas camargo",

    "website": "https://wwww.odoo.com",

    "category": "Training",

    "version": "0.1",

    "depends": ["base"],

    "data":[
      'security/academy_security.xml',
      'security/ir.model.access.csv',
      'views/academy_menuitems.xml',
    ],
    
}