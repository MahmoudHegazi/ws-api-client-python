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

from ws_api_client.api_client import ApiClient


class BoltPatternsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bolt_patterns_list(self, **kwargs):  # noqa: E501
        """Get list of bolt patterns  # noqa: E501

        A list of possible bolt patterns with the number of matching model modifications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bolt_patterns_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param float stud: Number of stud holes (e.g. `5`)
        :param float stud_min: Lower bound for number of stud holes (e.g. `4`)
        :param float stud_max: Upper bound for number of stud holes (e.g. `7`)
        :param float pcd: Pitch circle diameter, mm (e.g. `115`)
        :param float pcd_min: Lower bound for pitch circle diameter, mm (e.g. `105`)
        :param float pcd_max: Upper bound for pitch circle diameter, mm (e.g. `135`)
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[BoltPattern]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.bolt_patterns_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bolt_patterns_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def bolt_patterns_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of bolt patterns  # noqa: E501

        A list of possible bolt patterns with the number of matching model modifications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bolt_patterns_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param float stud: Number of stud holes (e.g. `5`)
        :param float stud_min: Lower bound for number of stud holes (e.g. `4`)
        :param float stud_max: Upper bound for number of stud holes (e.g. `7`)
        :param float pcd: Pitch circle diameter, mm (e.g. `115`)
        :param float pcd_min: Lower bound for pitch circle diameter, mm (e.g. `105`)
        :param float pcd_max: Upper bound for pitch circle diameter, mm (e.g. `135`)
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[BoltPattern]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stud', 'stud_min', 'stud_max', 'pcd', 'pcd_min', 'pcd_max', 'brands', 'brands_exclude', 'countries', 'countries_exclude']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bolt_patterns_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'stud' in params:
            query_params.append(('stud', params['stud']))  # noqa: E501
        if 'stud_min' in params:
            query_params.append(('stud_min', params['stud_min']))  # noqa: E501
        if 'stud_max' in params:
            query_params.append(('stud_max', params['stud_max']))  # noqa: E501
        if 'pcd' in params:
            query_params.append(('pcd', params['pcd']))  # noqa: E501
        if 'pcd_min' in params:
            query_params.append(('pcd_min', params['pcd_min']))  # noqa: E501
        if 'pcd_max' in params:
            query_params.append(('pcd_max', params['pcd_max']))  # noqa: E501
        if 'brands' in params:
            query_params.append(('brands', params['brands']))  # noqa: E501
        if 'brands_exclude' in params:
            query_params.append(('brands_exclude', params['brands_exclude']))  # noqa: E501
        if 'countries' in params:
            query_params.append(('countries', params['countries']))  # noqa: E501
        if 'countries_exclude' in params:
            query_params.append(('countries_exclude', params['countries_exclude']))  # noqa: E501

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
            '/bolt-patterns/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BoltPattern]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bolt_patterns_read(self, bolt_pattern, **kwargs):  # noqa: E501
        """Model modifications by bolt pattern  # noqa: E501

        Get a list of model modifications matching to the given bolt pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bolt_patterns_read(bolt_pattern, async=True)
        >>> result = thread.get()

        :param async bool
        :param str bolt_pattern: Bolt pattern combines number of stud holes and pitch circle diameter. Use _**`GET /bolt-patterns/`**_ to get possible values (e.g. `5x105`) (required)
        :param float rim_diameter: Rim diameter, in (e.g. `16`)
        :param float rim_width: Rim width, in (e.g. `7`)
        :param float offset: Rim offset, mm (e.g. `40`)
        :param float offset_min: Lower bound for rim offset, mm (e.g. `35`)
        :param float offset_max: Upper bound for rim offset, mm (e.g. `45`)
        :param float cb: Centre bore value, mm (e.g. `60`)
        :param float cb_min: Lower bound for centre bore value, mm (e.g. `55`)
        :param float cb_max: Upper bound for centre bore value, mm (e.g. `65`)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn,zh-tw`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.bolt_patterns_read_with_http_info(bolt_pattern, **kwargs)  # noqa: E501
        else:
            (data) = self.bolt_patterns_read_with_http_info(bolt_pattern, **kwargs)  # noqa: E501
            return data

    def bolt_patterns_read_with_http_info(self, bolt_pattern, **kwargs):  # noqa: E501
        """Model modifications by bolt pattern  # noqa: E501

        Get a list of model modifications matching to the given bolt pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bolt_patterns_read_with_http_info(bolt_pattern, async=True)
        >>> result = thread.get()

        :param async bool
        :param str bolt_pattern: Bolt pattern combines number of stud holes and pitch circle diameter. Use _**`GET /bolt-patterns/`**_ to get possible values (e.g. `5x105`) (required)
        :param float rim_diameter: Rim diameter, in (e.g. `16`)
        :param float rim_width: Rim width, in (e.g. `7`)
        :param float offset: Rim offset, mm (e.g. `40`)
        :param float offset_min: Lower bound for rim offset, mm (e.g. `35`)
        :param float offset_max: Upper bound for rim offset, mm (e.g. `45`)
        :param float cb: Centre bore value, mm (e.g. `60`)
        :param float cb_min: Lower bound for centre bore value, mm (e.g. `55`)
        :param float cb_max: Upper bound for centre bore value, mm (e.g. `65`)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn,zh-tw`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bolt_pattern', 'rim_diameter', 'rim_width', 'offset', 'offset_min', 'offset_max', 'cb', 'cb_min', 'cb_max', 'lang', 'brands', 'brands_exclude', 'countries', 'countries_exclude']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bolt_patterns_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bolt_pattern' is set
        if ('bolt_pattern' not in params or
                params['bolt_pattern'] is None):
            raise ValueError("Missing the required parameter `bolt_pattern` when calling `bolt_patterns_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bolt_pattern' in params:
            path_params['bolt_pattern'] = params['bolt_pattern']  # noqa: E501

        query_params = []
        if 'rim_diameter' in params:
            query_params.append(('rim_diameter', params['rim_diameter']))  # noqa: E501
        if 'rim_width' in params:
            query_params.append(('rim_width', params['rim_width']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'offset_min' in params:
            query_params.append(('offset_min', params['offset_min']))  # noqa: E501
        if 'offset_max' in params:
            query_params.append(('offset_max', params['offset_max']))  # noqa: E501
        if 'cb' in params:
            query_params.append(('cb', params['cb']))  # noqa: E501
        if 'cb_min' in params:
            query_params.append(('cb_min', params['cb_min']))  # noqa: E501
        if 'cb_max' in params:
            query_params.append(('cb_max', params['cb_max']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'brands' in params:
            query_params.append(('brands', params['brands']))  # noqa: E501
        if 'brands_exclude' in params:
            query_params.append(('brands_exclude', params['brands_exclude']))  # noqa: E501
        if 'countries' in params:
            query_params.append(('countries', params['countries']))  # noqa: E501
        if 'countries_exclude' in params:
            query_params.append(('countries_exclude', params['countries_exclude']))  # noqa: E501

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
            '/bolt-patterns/{bolt_pattern}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MakeWithModels]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
