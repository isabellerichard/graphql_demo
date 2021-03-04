# Copyright 2021 Isabelle RICHARD
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene

from odoo.addons.graphql_base import OdooObjectType


class OpportunityTag(OdooObjectType):
    name = graphene.String(required=True)
    color = graphene.Int()
