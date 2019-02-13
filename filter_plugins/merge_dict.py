#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright:
#   2018 Per H. <github.com/perfide>
# License:
#   BSD-3 https://opensource.org/licenses/BSD-3-Clause

def merge_dict(dict1, dict2):
    """Recursive dict.update
    :param dict1: rezessive target which gets overridden
    :param dict2: source with most imortance
    :return: merged dict
    """
    dict1 = dict1.copy()
    dict2 = dict2.copy()
    for key, value in dict2.items():
        if key in dict1:
            if (isinstance(dict1[key], dict) and isinstance(dict2[key], dict)):
                dict1[key] = merge_dict(dict1[key], dict2[key])
            elif (isinstance(dict1[key], dict) ^ isinstance(dict2[key], dict)):
                raise KeyError('incompatible structure: {} vs. {}'.format(
                    dict1[key], dict2[key]))
            else:
                dict1[key] = dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1
# end def merge_dict


class FilterModule(object):
    """get source names by type from chain definition"""

    def filters(self):
        return {'merge_dict': merge_dict}
    # end def filters
# end class FilterModule

# [EOF]
