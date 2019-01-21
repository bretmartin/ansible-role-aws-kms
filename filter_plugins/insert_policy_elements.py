#!/usr/bin/env


def principal(statement, *args):
    statement['Principal']['AWS'] = args
    return statement


class FilterModule(object):
    def filters(self):
        return {
            "principal": principal,
        }
