"""
This file defines the database models
"""

from pydal.validators import *

from .common import Field, db

### Define your table below
#
db.define_table('parent',
                Field('stringfield'),
                Field('textfield','text'),
                Field('integerfield', 'integer'),
                Field('booleanfield','boolean'),
                Field('datetimefield','datetime'),
                Field('datefield','date'),
                Field('uploadfield'),
                Field('passwordfield'),
                Field.Virtual('virtualfield', lambda r: r['integerfield'] * 2),
                format='%(stringfield)s'
                )

db.parent.virtualfield2 = Field.Virtual(lambda r: r['integerfield'] * 2)

db.define_table('child',
                Field('stringfield'),
                Field('parentid','reference parent', notnull=True),
                Field('textfield','text'),
                Field('quantity','integer'),
                Field('price','decimal(10,2)'),
                Field('booleanfield','boolean'),
                Field('total_comp_price', compute = lambda r: r['price'] * r['quantity']),
                Field.Virtual('total_virtual_price', lambda r: r['price'] * r['quantity']))

db.child.total_virtual_price2 = Field.Virtual(lambda r: r.child.price * r.child.quantity)

db.child.parentid.requires = IS_IN_DB(db, 'parent.id')

## always commit your models to avoid problems later
db.commit()
#
