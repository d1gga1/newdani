# -*- coding: utf-8 -*-
"""Raccoglie i pacchetti lingua delle landing page per paese."""
from seo_l_west import L as _W
from seo_l_east import L as _E
from seo_l_north import L as _N

LANGS = {}
for _d in (_W, _E, _N):
    LANGS.update(_d)
