from __future__ import unicode_literals
from frappe import _

def get_data():

    return {
        'fieldname': 'travel_request',

        'transactions': [
            {
                'label': _('Reference'),
                'items': ['Employee Advance']
            },
        ]
    }