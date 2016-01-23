#!/usr/bin/env python

"""
Copyright (c) 2016, Guy Bowerman
Description: Azure Resource Manager Python library
License: MIT (see LICENSE file for details)
"""

# subnfs - place to store azurerm functions related to subscriptions

from .settings import azure_rm_endpoint, BASE_API
from .restfns import do_get

# list_subscriptions(access_token)
# list the available Azure subscriptions for this user/service principle
def list_subscriptions(access_token):
    endpoint = ''.join([azure_rm_endpoint, 
	                    '/subscriptions/', 
			            '?api-version=', BASE_API]) 
    return do_get(endpoint, access_token)