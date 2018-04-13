# coding: utf-8

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TrimsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def trims_list(self, make, model, year, **kwargs):  # noqa: E501
        """Model modifications  # noqa: E501

        List of model modifications matching given manufacturer, model and year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trims_list(make, model, year, async=True)
        >>> result = thread.get()

        :param async bool
        :param str make: Manufacturer slug name, use _**`GET /makes/`**_ to get possible values (e.g. `mitsubishi`) (required)
        :param str model: Model slug name, use _**`GET /models/`**_ to get possible values (e.g. `outlander`) (required)
        :param int year: You can use _**`GET /years/`**_ to get possible years (e.g. `2015`) (required)
        :return: list[Trim]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.trims_list_with_http_info(make, model, year, **kwargs)  # noqa: E501
        else:
            (data) = self.trims_list_with_http_info(make, model, year, **kwargs)  # noqa: E501
            return data

    def trims_list_with_http_info(self, make, model, year, **kwargs):  # noqa: E501
        """Model modifications  # noqa: E501

        List of model modifications matching given manufacturer, model and year  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trims_list_with_http_info(make, model, year, async=True)
        >>> result = thread.get()

        :param async bool
        :param str make: Manufacturer slug name, use _**`GET /makes/`**_ to get possible values (e.g. `mitsubishi`) (required)
        :param str model: Model slug name, use _**`GET /models/`**_ to get possible values (e.g. `outlander`) (required)
        :param int year: You can use _**`GET /years/`**_ to get possible years (e.g. `2015`) (required)
        :return: list[Trim]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['make', 'model', 'year']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trims_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'make' is set
        if ('make' not in params or
                params['make'] is None):
            raise ValueError("Missing the required parameter `make` when calling `trims_list`")  # noqa: E501
        # verify the required parameter 'model' is set
        if ('model' not in params or
                params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `trims_list`")  # noqa: E501
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `trims_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'make' in params:
            query_params.append(('make', params['make']))  # noqa: E501
        if 'model' in params:
            query_params.append(('model', params['model']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user_key']  # noqa: E501

        return self.api_client.call_api(
            '/trims/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Trim]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
