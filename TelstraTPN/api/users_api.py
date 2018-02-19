# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.3.3
    Contact: pnapi-support@team.telstra.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from TelstraTPN.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def accountcustomeruuiduserget(self, customeruuid, **kwargs):  # noqa: E501
        """List users  # noqa: E501

        List all users associated with the specified customer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.accountcustomeruuiduserget(customeruuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customeruuid: Unique identifier representing a specific customer (required)
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.accountcustomeruuiduserget_with_http_info(customeruuid, **kwargs)  # noqa: E501
        else:
            (data) = self.accountcustomeruuiduserget_with_http_info(customeruuid, **kwargs)  # noqa: E501
            return data

    def accountcustomeruuiduserget_with_http_info(self, customeruuid, **kwargs):  # noqa: E501
        """List users  # noqa: E501

        List all users associated with the specified customer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.accountcustomeruuiduserget_with_http_info(customeruuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customeruuid: Unique identifier representing a specific customer (required)
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customeruuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accountcustomeruuiduserget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customeruuid' is set
        if ('customeruuid' not in params or
                params['customeruuid'] is None):
            raise ValueError("Missing the required parameter `customeruuid` when calling `accountcustomeruuiduserget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customeruuid' in params:
            path_params['customeruuid'] = params['customeruuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/1.0.0/account/{customeruuid}/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[User]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
