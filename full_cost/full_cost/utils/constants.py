from typing import Iterable
from enum import StrEnum
from dataclasses import dataclass

"""
CEMES organisation
People enter their working units per activity => one database per activity
Admins make an invoice per facturation => one bill use entries possibly from various databases or an inset of databases
"""
CNRS_PERCENTAGE = 6

class BaseEnum(StrEnum):

    @classmethod
    def names(cls):
        return (elt.name for elt in cls)

    @classmethod
    def values(cls):
        return (elt.value for elt in cls)

    @classmethod
    def to_dict(cls):
        return {elt.name: elt.value for elt in cls}


class PriceCategory(BaseEnum):
    T1 = 'CNRS Interne'
    T2 ='CNRS Externe'
    T3 = 'Private'


@dataclass()
class Entity:
    """ A class describing "something" related to a price in the full cost project"""
    name: str
    short: str
    prices: dict[PriceCategory, float]


class EntityCategory(BaseEnum):
    MET_C = 'Conventionnal TEM'
    MET_A = 'Advanced TEM'

    PREPA = 'Preparation for MET and MEB'
    PREPA_SOFT = 'Soft Matter Preparation'

    FIB_MEB = 'FIB Preparation and MEB'


    SPECTRO = 'Optical Spectroscopy'
    SPECTRO_CHEMISTRY = 'Optical Spectroscopy for Chemistry'
    MAGNET = 'Magnetic Properties'

    MEBA = 'Advanced MEB'

    MATC = 'Material Caracterisation'

    CLEANR = 'Clean Room Processes'
    NEARF = 'Near-field microscopy'
    FIB_LITHO = 'Lithography using the ZEISS'

    UHVI = 'UHV Imagery'
    DUFG = 'Growth DUF'
    LT4 = 'LT-UHV 4 tips'

    GROWTH = 'Growth'
    IMPLANT = 'Ionic Implantation'

    MECA = 'Mechanic Service'
    ELEC = 'Electronic Service'

    def to_entity(self, prices: dict[PriceCategory, float]) -> Entity:
        return Entity(self.name, self.value, prices)


entities = {
    EntityCategory.MET_C:
        EntityCategory.MET_C.to_entity(
            {PriceCategory.T1: 247.,
             PriceCategory.T2: 1066.,
             PriceCategory.T3: 1333.,}
        ),
    EntityCategory.MET_A:
        EntityCategory.MET_A.to_entity(
            {PriceCategory.T1: 81.,
             PriceCategory.T2: 976.,
             PriceCategory.T3: 1121., }
        ),
    EntityCategory.PREPA:
        EntityCategory.PREPA.to_entity(
            {PriceCategory.T1: 119.,
             PriceCategory.T2: 1366.,
             PriceCategory.T3: 1708., }
        ),
    EntityCategory.PREPA_SOFT:
        EntityCategory.PREPA_SOFT.to_entity(
            {PriceCategory.T1: 119.,
             PriceCategory.T2: 1366.,
             PriceCategory.T3: 1708., }
        ),
    EntityCategory.FIB_MEB:
        EntityCategory.FIB_MEB.to_entity(
            {PriceCategory.T1: 202.,
             PriceCategory.T2: 341.,
             PriceCategory.T3: 426., }
        ),
    EntityCategory.SPECTRO:
        EntityCategory.SPECTRO.to_entity(
            {PriceCategory.T1: 130.,
             PriceCategory.T2: 419.,
             PriceCategory.T3: 524., }
        ),
    EntityCategory.SPECTRO_CHEMISTRY:
        EntityCategory.SPECTRO_CHEMISTRY.to_entity(
            {PriceCategory.T1: 130.,
             PriceCategory.T2: 419.,
             PriceCategory.T3: 524., }
        ),
    EntityCategory.MAGNET:
        EntityCategory.MAGNET.to_entity(
            {PriceCategory.T1: 130.,
             PriceCategory.T2: 419.,
             PriceCategory.T3: 524., }
        ),
    EntityCategory.MATC:
        EntityCategory.MATC.to_entity(
            {PriceCategory.T1: 66.,
             PriceCategory.T2: 358.,
             PriceCategory.T3: 448., }
        ),
    EntityCategory.CLEANR:
        EntityCategory.CLEANR.to_entity(
            {PriceCategory.T1: 281.,
             PriceCategory.T2: 652.,
             PriceCategory.T3: 815., }
        ),
    EntityCategory.NEARF:
        EntityCategory.NEARF.to_entity(
            {PriceCategory.T1: 281.,
             PriceCategory.T2: 652.,
             PriceCategory.T3: 815., }
        ),
    EntityCategory.FIB_LITHO:
        EntityCategory.CLEANR.to_entity(
            {PriceCategory.T1: 281.,
             PriceCategory.T2: 652.,
             PriceCategory.T3: 815., }
        ),

}



@dataclass()
class Activity:
    activity_short: str
    activity_long: str
    entities: Iterable[Entity]


class ActivityCategory(BaseEnum):

    MET = 'Transmission Electron Microscopy Platform'
    PREPA = 'Sample Preparation Service'
    FIB_MEB = 'Focused Ion Beam and MEB'
    OSM = 'Optical Spectroscopy and Magnetism'
    CARAC = 'Material Characterisation'
    CLEANR = 'Clean Room'
    CHEM = 'Chemistry'
    GROWTH_IMP = 'Growth and Implantation'
    STM_AFM = 'UHV Imagery'
    ENGINEERING = 'Engineering'

ACTIVITIES = (
    Activity(ActivityCategory.MET.name,
             ActivityCategory.MET.value,
             entities=(EntityCategory.MET_C.to_entity(),
                       EntityCategory.MET_A.to_entity(),
                       ),
             ),
)


ACTIVITIES = {OSM.activity_short: {'activity_short': OSM.activity_short.value,
                     'activity_long': OSM.activity_long.value,
                     'sub_billings': [('SPEC','Optical Spectroscopy'),
                                      ],
                     'related_entities': {'SPEC': 'SPECTRO',
                                          'PREPF': 'PREPA'}},

             'met': {'activity_short': 'met',
                     'activity_long': 'Transmission Electron Microscopy Platform',
                     'sub_billings': [('METC','Conventionnal TEM'),
                                      ('META', 'Advanced TEM')],
                     'related_entities': {'META': 'TEM',
                                          'METC': 'TEM'}},

             'prepa': {'activity_short': 'prepa',
                       'activity_long': 'Sample Preparation Service',
                       'sub_billings': [('PREPC','Conventionnal Preparation'),
                                        ('FIBp','FIB preparation')],
                     'related_entities': {'PREPC': 'PREPA',}},

             'fib': {'activity_short': 'fib',
                     'activity_long': 'Focused Ion Beam',
                     'sub_billings':
                         [('FIBp','FIB preparation'),
                          ('MEBA','Advanced MEB'),
                          ('FIBc','FIB Clean Room'),],
                     'related_entities': {'FIBp': 'PREPA', 'MEBA': 'MEBA', 'FIBc': 'FIBCR', }},

             'mphys': {'activity_short': 'mphys',
                       'activity_long': 'PS2I',
                       'sub_billings':
                           [('MAG', 'Magnetic Measurement'),
                            ('MATC', 'Material Caracterisation')],
                    'related_entities':
                           {'MAG': 'MAGNETIC',
                            'MATC': 'MATCARAC'}},
            'chem':{'activity_short': 'chem',
                    'activity_long': 'Chemistry',
                    'sub_billings': [('CHEM', 'Chemistry'),],
                     'related_entities': {'CHEM': 'CHEM'}},

            'imag': {'activity_short': 'imag', 'activity_long': 'STM/AFM - UHV Growth',
                     'sub_billings': [('UHVI', 'UHV Imagery'),
                                      ('DUFG', 'Growth DUF'),
                                      ('LT4', 'LT-UHV 4 tips'),
                                      ('NEARF', 'Near-field microscopy'),],
                      'related_entities':
                         {'UHVI': 'UHVI',
                          'LT4': 'LT4',
                          'NEARF':'NEARF'}},
            'fab': {'activity_short': 'fab',
                    'activity_long': 'Nanomaterial Fabrication',
                    'sub_billings': [
                        ('CLEANR', 'Clean Room Processes'),
                        ('GROWTH', 'Growth'),],
                      'related_entities':
                        {'CLEANR': 'CLEANR',
                         'DUFG': 'DUFG',
                         'GROWTH': 'GROWTHIMP',
                         'IMPLANT': 'GROWTHIMP'}},
             'implant': {'activity_short': 'implant', 'activity_long': 'Implantation and growth',
                     'sub_billings': [('GROWTH', 'Growth'),
                                      ('IMPLANT', 'Ionic Implantation')],
                     'related_entities': {'GROWTH': 'GROWTHIMP', 'IMPLANT': 'GROWTHIMP'}},
             'engi': {'activity_short': 'engi', 'activity_long': 'Engineering Platform',
                     'sub_billings': [('MECA', 'Mechanic Service'),
                                      ('ELEC', 'Electronic Service'),],
                     'related_entities': {'MECA': 'MECA', 'ELEC': 'ELEC',}},
             }
activities_choices = [(k, ACTIVITIES[k]['activity_long'],) for k in ACTIVITIES.keys()]

BILLINGS = [dict(entity=('SPECTRO', 'Optical Spectroscopy'),
                 activities=('osm',),
                 related_subbillings=[dict(short='SPEC',
                                           long='Optical Spectroscopy')]),
            dict(entity=('TEM', 'Electronic Microscopy'),
                 activities=('met',),
                 related_subbillings=[dict(short='META',
                                           long='Advanced TEM'),
                                      dict(short='METC',
                                           long='Conventionnal TEM')],),
                dict(entity=('PREPA', 'Sample Preparation'),
                     activities=('prepa', 'fib'),
                     related_subbillings=[dict(short='PREPC',
                                               long='Conventionnal Preparation'),
                                          dict(short='FIBp',
                                               long='FIB preparation')],),
                dict(entity=('MEBA', 'Advanced MEB'),
                     activities=('fib',),
                     related_subbillings=[dict(short='MEBA',
                                               long='Advanced MEB')],),
                dict(entity=('FIBCR', 'FIB Clean Room'),
                     activities=('fib',),
                     related_subbillings=[dict(short='FIBc',
                                               long='FIB Clean Room')],),
                dict(entity=('SOFT', 'Soft Matter'),
                     activities=('osm',),
                     related_subbillings=[dict(short='SOFT',
                                               long='Soft Matter')],),
                dict(entity=('MATCARAC', 'PS2I'),
                     activities=('mphys',),
                      related_subbillings=[dict(short='MATC',
                                                long='Material Caracterisation')],),
                dict(entity=('MAGNETIC', 'Magnetic Measurement'),
                     activities=('mphys',),
                      related_subbillings=[dict(short='MAG',
                                                long='Magnetic Measurement')],),
                dict(entity=('CHEM', 'Chemistry'),
                     activities=('chem',),
                     related_subbillings=[dict(short='CHEM',
                                               long='Chemistry')],),
                dict(entity=('CLEANR', 'Clean Room Processes'),
                     activities=('fab',),
                      related_subbillings=[dict(short='CLEANR',
                                                long='Clean Room Processes')],),
                dict(entity=('UHVI', 'UHV Imagery'),
                     activities=('imag',),
                      related_subbillings=[dict(short='UHVI',
                                                long='UHV Imagery')],),
                dict(entity=('LT4', 'LT-UHV 4 tips'),
                     activities=('imag',),
                      related_subbillings=[dict(short='LT4',
                                                long='LT-UHV 4 tips')],),
                dict(entity=('DUFG', 'Growth DUF'),
                     activities=('imag',),
                     related_subbillings=[dict(short='DUFG',
                                               long='Growth DUF')],),
                dict(entity=('NEARF', 'Near-field microscopy'),
                     activities=('imag',),
                      related_subbillings=[dict(short='NEARF',
                                                long='Near-field microscopy')],),
                dict(entity=('GROWTHIMP', 'Growth and Implantation'),
                     activities=('implant',),
                      related_subbillings=[dict(short='GROWTH',
                                                long='Growth'),
                                           dict(short='IMPLANT',
                                                long='Ionic Implantation')],),
                dict(entity=('MECA', 'Mechanic Service'),
                     activities=('engi',),
                     related_subbillings=[dict(short='MECA',
                                               long='Mechanic Service')], ),
                dict(entity=('ELEC', 'Electronic Service'),
                     activities=('engi',),
                     related_subbillings=[dict(short='ELEC',
                                               long='Electronic Service')], ),
                ]

def get_activities_from_entity(entity):
    if entity == '':
        return list(ACTIVITIES.keys())
    else:
        billings = [d['entity'][0] for d in BILLINGS]
        ind = billings.index(entity)
        return BILLINGS[ind]['activities']

def get_entity_long(entity):
    billings = [d['entity'][0] for d in BILLINGS]
    ind = billings.index(entity)
    return BILLINGS[ind]['entity'][1]

def get_subbillings_from_entity_short(entity):
    billings = [d['entity'][0] for d in BILLINGS]
    ind = billings.index(entity)
    return [d['short'] for d in BILLINGS[ind]['related_subbillings']]

def get_subbillings_from_entity_long(entity):
    billings = [d['entity'][0] for d in BILLINGS]
    ind = billings.index(entity)
    return [d['long'] for d in BILLINGS[ind]['related_subbillings']]

def get_billings_from_activity(activity):
    billings = []
    for bill in BILLINGS:
        if activity in bill['activities']:
            billings.append(activity)

def get_billing_entities_as_list():
    return [bill['entity'] for bill in BILLINGS]