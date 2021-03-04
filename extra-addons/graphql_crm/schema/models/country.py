# Copyright 2021 Isabelle RICHARD
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene

from odoo.addons.graphql_base import OdooObjectType


class Country(OdooObjectType):
    code = graphene.String(required=True)
    name = graphene.String(required=True)
