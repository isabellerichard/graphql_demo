# Copyright 2021 Isabelle RICHARD
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene

from .mutations import Mutation
from .queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
