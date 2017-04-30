#!/usr/bin/env python


def sort_key_policy(policy):
    if type(policy) == dict:
        return sort_key_policy_dict(policy)
    elif type(policy) == list:
        return sort_key_policy_list(policy)
    else:
        return policy


def sort_key_policy_dict(policy_dict):
    sorted_policy_dict = {}
    for key, value in policy_dict.items():
        if type(value) == dict:
            sorted_policy_dict[key] = sort_key_policy_dict(value)
        elif type(value) == list:
            sorted_policy_dict[key] = sort_key_policy_list(value)
        else:
            sorted_policy_dict[key] = value
    return sorted_policy_dict


def sort_key_policy_list(policy_list):
    list_item_types = []
    sorted_policy_list = []
    for item in policy_list:
        if type(item) == dict:
            list_item_types.append('dict')
            sorted_policy_list.append(sort_key_policy_dict(item))
        elif type(item) == list:
            list_item_types.append('list')
            sorted_policy_list.append(sort_key_policy_list(item))
        else:
            list_item_types.append('other')
            sorted_policy_list.append(item)
    if set(list_item_types) != set(['dict']):
        sorted_policy_list.sort()
    return sorted_policy_list


class FilterModule(object):
    def filters(self):
        return {
            "sort_key_policy": sort_key_policy,
        }
