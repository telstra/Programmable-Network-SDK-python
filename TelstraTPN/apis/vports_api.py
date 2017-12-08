# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

    OpenAPI spec version: 2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class VportsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_v_port_for_physical_endpoint(self, **kwargs):
        """
        Create VPort for physical endpoint
        Create VPort representing a VLAN on a Physical Ethernet Port
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_v_port_for_physical_endpoint(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Model100InventoryRegularvportRequest body: 
        :return: Model100InventoryRegularvportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_v_port_for_physical_endpoint_with_http_info(**kwargs)
        else:
            (data) = self.create_v_port_for_physical_endpoint_with_http_info(**kwargs)
            return data

    def create_v_port_for_physical_endpoint_with_http_info(self, **kwargs):
        """
        Create VPort for physical endpoint
        Create VPort representing a VLAN on a Physical Ethernet Port
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_v_port_for_physical_endpoint_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Model100InventoryRegularvportRequest body: 
        :return: Model100InventoryRegularvportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_v_port_for_physical_endpoint" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['auth']

        return self.api_client.call_api('/1.0.0/inventory/regularvport', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Model100InventoryRegularvportResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_vnf_v_port(self, **kwargs):
        """
        Create VNF VPort
        Create VNF VPort
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_vnf_v_port(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Model100InventoryVnfVportRequest body: 
        :return: Model100InventoryVnfVportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_vnf_v_port_with_http_info(**kwargs)
        else:
            (data) = self.create_vnf_v_port_with_http_info(**kwargs)
            return data

    def create_vnf_v_port_with_http_info(self, **kwargs):
        """
        Create VNF VPort
        Create VNF VPort
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_vnf_v_port_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Model100InventoryVnfVportRequest body: 
        :return: Model100InventoryVnfVportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_vnf_v_port" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['auth']

        return self.api_client.call_api('/1.0.0/inventory/vnf/vport', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Model100InventoryVnfVportResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_information_about_the_specified_v_port(self, vportuuid, **kwargs):
        """
        Get information about the specified VPort
        Get information about the specified VPort
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_information_about_the_specified_v_port(vportuuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str vportuuid: Unique identifier representing a specific virtual port (required)
        :return: EndpointPort
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_information_about_the_specified_v_port_with_http_info(vportuuid, **kwargs)
        else:
            (data) = self.get_information_about_the_specified_v_port_with_http_info(vportuuid, **kwargs)
            return data

    def get_information_about_the_specified_v_port_with_http_info(self, vportuuid, **kwargs):
        """
        Get information about the specified VPort
        Get information about the specified VPort
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_information_about_the_specified_v_port_with_http_info(vportuuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str vportuuid: Unique identifier representing a specific virtual port (required)
        :return: EndpointPort
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vportuuid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_information_about_the_specified_v_port" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vportuuid' is set
        if ('vportuuid' not in params) or (params['vportuuid'] is None):
            raise ValueError("Missing the required parameter `vportuuid` when calling `get_information_about_the_specified_v_port`")


        collection_formats = {}

        path_params = {}
        if 'vportuuid' in params:
            path_params['vportuuid'] = params['vportuuid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['auth']

        return self.api_client.call_api('/1.0.0/inventory/vport/{vportuuid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EndpointPort',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
