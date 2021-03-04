# Copyright 2021 Isabelle RICHARD
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene

from odoo.addons.graphql_base import OdooObjectType

from .opportunity_tag import OpportunityTag
from .partner import Partner


class Opportunity(OdooObjectType):
    name = graphene.String(required=True)
    contact = graphene.Field(Partner)
    date_deadline = graphene.DateTime()
    tags = graphene.List(
        graphene.NonNull(lambda: OpportunityTag), required=True)

    @staticmethod
    def resolve_contact(root, info):
        return root.partner_id or None

    @staticmethod
    def resolve_tags(root, info):
        return root.tag_ids
