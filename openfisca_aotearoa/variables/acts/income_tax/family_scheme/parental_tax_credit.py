# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class family_scheme__qualifies_for_parental_tax_credit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person is qualified as eligible for the parental tax credit'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518484.html"

    def formula(persons, period, parameters):
        base_qualifies = persons("family_scheme__base_qualifies", period)
        received_tested_benefit = persons('social_security__received_income_tested_benefit', period.this_year)

        return base_qualifies * not_(received_tested_benefit)


class family_scheme__parental_tax_credit_entitlement(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = u'The parental tax credit entitlement a person has under the family scheme'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518546.html#DLM1518546"

    def formula(persons, period, parameters):
        # TODO
        return persons
