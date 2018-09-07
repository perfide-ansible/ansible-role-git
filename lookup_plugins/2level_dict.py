#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright:
#   2018 Per H. <github.com/perfide>
# License:
#   BSD-3 https://opensource.org/licenses/BSD-3-Clause

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):
        items = []

        if isinstance(terms, list) and len(terms) == 1:
            terms = terms[0]

        for (key1, value1) in terms.items():
            for (key2, value2) in value1.items():
                item = [key1, key2, value2]
                items.append(item)

        return items

# [EOF]
