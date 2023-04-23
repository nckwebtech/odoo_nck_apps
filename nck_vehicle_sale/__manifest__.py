{
    'name': 'Pre Owned Vehicles',
    'version': '15.0.1.0.0',
    'summary': 'Pre Owned Vehicles',
    'sequence': 10,
    'description': """This app helps to Sale Pre Owned Vehicles usinf website.""",
    'author': 'Zillo Tech',
    'company': 'Zillo WebTech',
    'maintainer': 'Zillo WebTech',
    'website': 'https://www.nckwebtech.com/',
    'images': ['static/description/banner.png'],
    'depends': ['account', 'product', 'base', 'sale_management', 'website', 'stock', 'website_sale'],
    'data': ['security/ir.model.access.csv',
             'data/used_vehicle_data.xml',
             'report/inventory_product_report.xml',
             'report/inventory_product_template.xml',
             'views/vehicle_form.xml',
             'views/used_vehicle_brand_views.xml',
             'views/product_template_vehicle_views.xml',
             'views/website_downpayment_option.xml',
             ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
