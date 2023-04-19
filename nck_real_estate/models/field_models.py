from odoo import fields, models


class RealEstateFieldFeatureModels(models.Model):
    _name = 'lot.feature'
    _rec_name = 'feature_name'

    feature_name = fields.Char('Lot Feature')


class RealEstateFieldHCModels(models.Model):
    _name = 'heating.cooling'
    _rec_name = 'heating_cooling_type'

    heating_cooling_type = fields.Char('Heating and Cooling')


class RealEstateFieldIAModels(models.Model):
    _name = 'indoor.amenities'
    _rec_name = 'indoor_amenities_type'

    indoor_amenities_type = fields.Char('Indoor Amenities')


class RealEstateFieldOAModels(models.Model):
    _name = 'outdoor.amenities'
    _rec_name = 'outdoor_amenities_type'

    outdoor_amenities_type = fields.Char('Outdoor Amenities')
