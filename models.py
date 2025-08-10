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
                Field('integerfield' 'integer'),
                Field('booleanfield','boolean'),
                Field('datetimefield','datetime'),
                Field('datefield','date'),
                Field('uploadfield'),
                Field('passwordfield')
                )

db.define_table('child',
                Field('stringfield'),
                Field('parentid','reference parent'),
                Field('textfield','text'),
                Field('quantity','integer'),
                Field('price','decimal(10,2'),
                Field('booleanfield','boolean') )

## always commit your models to avoid problems later
db.commit()
#
