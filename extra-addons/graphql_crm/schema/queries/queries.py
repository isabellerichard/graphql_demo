# Copyright 2021 Isabelle RICHARD
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene

from odoo import _
from odoo.exceptions import UserError

from ..models.opportunity import Opportunity
from ..models.partner import Partner


class Query(graphene.ObjectType):
    all_partners = graphene.List(
        graphene.NonNull(Partner),
        required=True,
        companies_only=graphene.Boolean(),
        limit=graphene.Int(),
        offset=graphene.Int(),
    )

    all_opportunities = graphene.List(
        graphene.NonNull(Opportunity),
        required=True,
        tag_color=graphene.Int(),
        only_with_contact=graphene.Boolean(),
        limit=graphene.Int(),
        offset=graphene.Int(),
        description="Get all opportunities and bound contact",
    )

    reverse = graphene.String(
        required=True,
        description="Reverse a string",
        word=graphene.String(required=True),
    )

    error_example = graphene.String()

    @staticmethod
    def resolve_all_partners(
            root, info, companies_only=False, limit=None, offset=None):
        domain = []
        if companies_only:
            domain.append(("is_company", "=", True))
        return info.context["env"]["res.partner"].search(
            domain, limit=limit, offset=offset
        )

    @staticmethod
    def resolve_all_opportunities(
            root, info, tag_color=None, only_with_contact=False,
            limit=None, offset=None):
        model = "crm.lead"
        if model not in info.context["env"]:
            raise UserError(_("Please install CRM application!"))
        domain = [('type', '=', 'opportunity')]
        if tag_color:
            domain.append(("tag_ids.color", "=", tag_color))
        if only_with_contact:
            domain.append(("partner_id", "!=", False))
        return info.context["env"][model].search(
            domain, limit=limit, offset=offset
        )

    @staticmethod
    def resolve_reverse(root, info, word):
        return word[::-1]

    @staticmethod
    def resolve_error_example(root, info):
        raise UserError(_("UserError example"))
