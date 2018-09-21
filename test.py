import cerberus
import datetime
import yaml


member = {
    'id': {
        'openstates': '12345',
        'imaginary': '23423432',
        'fec': ['asdfa', 'asdfasdfa'],
    },
    'name': {
        'full': 'john j test III',
        'first': 'john',
        'middle': 'jay',
        'middle_initial': 'j',
        'nickname': 'jj3',
        'suffixes': 'III',
        'aliases': ['johnny mustache'],
    },
    'social': {
        'facebook': 'johntest',
        'instagram_id': '23423423'
    },
    'bio': {
        'born': datetime.date.today(),
        'died': '2015-01-01',
        'gender': 'R',
    },
    'positions': [
        {
            'name': 'UT House District 1',
            'ocd_division': 'state:ut',
            'party': "Democrat",
            'type': 'state-rep',
        }
    ]
}

subtypes = [
    'bio',
    'contact',
    'id',
    'name',
    'role',
    'social'
]

for subtype in subtypes:
    path = 'schema/{}.yaml'.format(subtype)
    with open(path, 'r') as stream:
        schema = yaml.load(stream)
    cerberus.schema_registry.add(subtype, schema)

representative = {
    'id': {'schema': 'id'},
    'bio': {'schema': 'bio'},
    'contacts': {'type':'list', 'schema': 'contact'},
    'name': {'schema': 'name'},
    'jobs': {'type': 'list', 'schema': 'role'},
    'social': {'schema': 'social'}
}

v = cerberus.Validator(representative)
# print(v.schema.validate())
print(v.validate(member))
print(v.errors)
