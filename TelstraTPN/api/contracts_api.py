# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.4.2
    Contact: pnapi-support@team.telstra.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from TelstraTPN.api_client import ApiClient


class ContractsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def inventory_links_contract(self, linkid, **kwargs):  # noqa: E501
        """Create new Contract on specified link  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_links_contract(linkid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str linkid: Unique identifier representing a specific link (required)
        :param Createcontractrequest createcontractrequest:
        :return: SuccessFragment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_links_contract_with_http_info(linkid, **kwargs)  # noqa: E501
        else:
            (data) = self.inventory_links_contract_with_http_info(linkid, **kwargs)  # noqa: E501
            return data

    def inventory_links_contract_with_http_info(self, linkid, **kwargs):  # noqa: E501
        """Create new Contract on specified link  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_links_contract_with_http_info(linkid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str linkid: Unique identifier representing a specific link (required)
        :param Createcontractrequest createcontractrequest:
        :return: SuccessFragment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['linkid', 'createcontractrequest']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_links_contract" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'linkid' is set
        if ('linkid' not in local_var_params or
                local_var_params['linkid'] is None):
            raise ValueError("Missing the required parameter `linkid` when calling `inventory_links_contract`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'linkid' in local_var_params:
            path_params['linkid'] = local_var_params['linkid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'createcontractrequest' in local_var_params:
            body_params = local_var_params['createcontractrequest']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/1.0.0/inventory/links/{linkid}/contract', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessFragment',  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inventory_links_contract_get(self, linkid, contractid, **kwargs):  # noqa: E501
        """Get active Contract by ContractID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_links_contract_get(linkid, contractid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str linkid: Unique identifier representing a specific link (required)
        :param str contractid: Unique identifier representing a specific contract (required)
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_links_contract_get_with_http_info(linkid, contractid, **kwargs)  # noqa: E501
        else:
            (data) = self.inventory_links_contract_get_with_http_info(linkid, contractid, **kwargs)  # noqa: E501
            return data

    def inventory_links_contract_get_with_http_info(self, linkid, contractid, **kwargs):  # noqa: E501
        """Get active Contract by ContractID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_links_contract_get_with_http_info(linkid, contractid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str linkid: Unique identifier representing a specific link (required)
        :param str contractid: Unique identifier representing a specific contract (required)
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['linkid', 'contractid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_links_contract_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'linkid' is set
        if ('linkid' not in local_var_params or
                local_var_params['linkid'] is None):
            raise ValueError("Missing the required parameter `linkid` when calling `inventory_links_contract_get`")  # noqa: E501
        # verify the required parameter 'contractid' is set
        if ('contractid' not in local_var_params or
                local_var_params['contractid'] is None):
            raise ValueError("Missing the required parameter `contractid` when calling `inventory_links_contract_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'linkid' in local_var_params:
            path_params['linkid'] = local_var_params['linkid']  # noqa: E501
        if 'contractid' in local_var_params:
            path_params['contractid'] = local_var_params['contractid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/1.0.0/inventory/links/{linkid}/contract/{contractid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inventory_links_contract_put(self, linkid, contractid, **kwargs):  # noqa: E501
        """Update active Contract by ContractID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_links_contract_put(linkid, contractid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str linkid: Unique identifier representing a specific link (required)
        :param str contractid: Unique identifier representing a specific contract (required)
        :param Body body:
        :return: SuccessFragment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_links_contract_put_with_http_info(linkid, contractid, **kwargs)  # noqa: E501
        else:
            (data) = self.inventory_links_contract_put_with_http_info(linkid, contractid, **kwargs)  # noqa: E501
            return data

    def inventory_links_contract_put_with_http_info(self, linkid, contractid, **kwargs):  # noqa: E501
        """Update active Contract by ContractID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_links_contract_put_with_http_info(linkid, contractid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str linkid: Unique identifier representing a specific link (required)
        :param str contractid: Unique identifier representing a specific contract (required)
        :param Body body:
        :return: SuccessFragment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['linkid', 'contractid', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_links_contract_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'linkid' is set
        if ('linkid' not in local_var_params or
                local_var_params['linkid'] is None):
            raise ValueError("Missing the required parameter `linkid` when calling `inventory_links_contract_put`")  # noqa: E501
        # verify the required parameter 'contractid' is set
        if ('contractid' not in local_var_params or
                local_var_params['contractid'] is None):
            raise ValueError("Missing the required parameter `contractid` when calling `inventory_links_contract_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'linkid' in local_var_params:
            path_params['linkid'] = local_var_params['linkid']  # noqa: E501
        if 'contractid' in local_var_params:
            path_params['contractid'] = local_var_params['contractid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/1.0.0/inventory/links/{linkid}/contract/{contractid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessFragment',  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
