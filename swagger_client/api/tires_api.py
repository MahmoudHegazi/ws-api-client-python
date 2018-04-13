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


class TiresApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tires_list(self, **kwargs):  # noqa: E501
        """Returns a list of tires  # noqa: E501

        Get a list of tires with a number of matching model modifications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tires_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param float width: Tire width, mm (e.g. `195`)
        :param float width_min: Lower bound for tire width, mm (e.g. `165`)
        :param float width_max: Upper bound for tire width, mm (e.g. `200`)
        :param float aspect_ratio: Aspect ratio, % (e.g. `50`)
        :param float aspect_ratio_min: Lower bound for aspect ratio, % (e.g. `30`)
        :param float aspect_ratio_max: Upper bound for aspect ratio, % (e.g. `70`)
        :param float rim_diameter: Rim diameter, in (e.g. `16`)
        :param float rim_diameter_min: Lower bound for rim diameter, in (e.g. `13`)
        :param float rim_diameter_max: Upper bound for rim diameter, in (e.g. `20`)
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[Tire]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tires_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tires_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def tires_list_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of tires  # noqa: E501

        Get a list of tires with a number of matching model modifications  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tires_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param float width: Tire width, mm (e.g. `195`)
        :param float width_min: Lower bound for tire width, mm (e.g. `165`)
        :param float width_max: Upper bound for tire width, mm (e.g. `200`)
        :param float aspect_ratio: Aspect ratio, % (e.g. `50`)
        :param float aspect_ratio_min: Lower bound for aspect ratio, % (e.g. `30`)
        :param float aspect_ratio_max: Upper bound for aspect ratio, % (e.g. `70`)
        :param float rim_diameter: Rim diameter, in (e.g. `16`)
        :param float rim_diameter_min: Lower bound for rim diameter, in (e.g. `13`)
        :param float rim_diameter_max: Upper bound for rim diameter, in (e.g. `20`)
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[Tire]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['width', 'width_min', 'width_max', 'aspect_ratio', 'aspect_ratio_min', 'aspect_ratio_max', 'rim_diameter', 'rim_diameter_min', 'rim_diameter_max', 'brands', 'brands_exclude', 'countries', 'countries_exclude']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tires_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'width_min' in params:
            query_params.append(('width_min', params['width_min']))  # noqa: E501
        if 'width_max' in params:
            query_params.append(('width_max', params['width_max']))  # noqa: E501
        if 'aspect_ratio' in params:
            query_params.append(('aspect_ratio', params['aspect_ratio']))  # noqa: E501
        if 'aspect_ratio_min' in params:
            query_params.append(('aspect_ratio_min', params['aspect_ratio_min']))  # noqa: E501
        if 'aspect_ratio_max' in params:
            query_params.append(('aspect_ratio_max', params['aspect_ratio_max']))  # noqa: E501
        if 'rim_diameter' in params:
            query_params.append(('rim_diameter', params['rim_diameter']))  # noqa: E501
        if 'rim_diameter_min' in params:
            query_params.append(('rim_diameter_min', params['rim_diameter_min']))  # noqa: E501
        if 'rim_diameter_max' in params:
            query_params.append(('rim_diameter_max', params['rim_diameter_max']))  # noqa: E501
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
            '/tires/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Tire]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tires_read(self, tire, **kwargs):  # noqa: E501
        """Model modifications matching given tire  # noqa: E501

        Get a list of model modifications by tire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tires_read(tire, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tire: Formatted tire size. Use _**`GET /tires/`**_ to get possible values (e.g. `195/50R15`) (required)
        :param float width: Tire width, mm (e.g. `195`)
        :param float width_min: Lower bound for tire width, mm (e.g. `165`)
        :param float width_max: Upper bound for tire width, mm (e.g. `200`)
        :param float aspect_ratio: Aspect ratio, % (e.g. `50`)
        :param float aspect_ratio_min: Lower bound for aspect ratio, % (e.g. `30`)
        :param float aspect_ratio_max: Upper bound for aspect ratio, % (e.g. `70`)
        :param float rim_diameter: Rim diameter, in (e.g. `16`)
        :param float rim_diameter_min: Lower bound for rim diameter, in (e.g. `13`)
        :param float rim_diameter_max: Upper bound for rim diameter, in (e.g. `20`)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
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
            return self.tires_read_with_http_info(tire, **kwargs)  # noqa: E501
        else:
            (data) = self.tires_read_with_http_info(tire, **kwargs)  # noqa: E501
            return data

    def tires_read_with_http_info(self, tire, **kwargs):  # noqa: E501
        """Model modifications matching given tire  # noqa: E501

        Get a list of model modifications by tire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tires_read_with_http_info(tire, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tire: Formatted tire size. Use _**`GET /tires/`**_ to get possible values (e.g. `195/50R15`) (required)
        :param float width: Tire width, mm (e.g. `195`)
        :param float width_min: Lower bound for tire width, mm (e.g. `165`)
        :param float width_max: Upper bound for tire width, mm (e.g. `200`)
        :param float aspect_ratio: Aspect ratio, % (e.g. `50`)
        :param float aspect_ratio_min: Lower bound for aspect ratio, % (e.g. `30`)
        :param float aspect_ratio_max: Upper bound for aspect ratio, % (e.g. `70`)
        :param float rim_diameter: Rim diameter, in (e.g. `16`)
        :param float rim_diameter_min: Lower bound for rim diameter, in (e.g. `13`)
        :param float rim_diameter_max: Upper bound for rim diameter, in (e.g. `20`)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tire', 'width', 'width_min', 'width_max', 'aspect_ratio', 'aspect_ratio_min', 'aspect_ratio_max', 'rim_diameter', 'rim_diameter_min', 'rim_diameter_max', 'lang', 'brands', 'brands_exclude', 'countries', 'countries_exclude']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tires_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tire' is set
        if ('tire' not in params or
                params['tire'] is None):
            raise ValueError("Missing the required parameter `tire` when calling `tires_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tire' in params:
            path_params['tire'] = params['tire']  # noqa: E501

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'width_min' in params:
            query_params.append(('width_min', params['width_min']))  # noqa: E501
        if 'width_max' in params:
            query_params.append(('width_max', params['width_max']))  # noqa: E501
        if 'aspect_ratio' in params:
            query_params.append(('aspect_ratio', params['aspect_ratio']))  # noqa: E501
        if 'aspect_ratio_min' in params:
            query_params.append(('aspect_ratio_min', params['aspect_ratio_min']))  # noqa: E501
        if 'aspect_ratio_max' in params:
            query_params.append(('aspect_ratio_max', params['aspect_ratio_max']))  # noqa: E501
        if 'rim_diameter' in params:
            query_params.append(('rim_diameter', params['rim_diameter']))  # noqa: E501
        if 'rim_diameter_min' in params:
            query_params.append(('rim_diameter_min', params['rim_diameter_min']))  # noqa: E501
        if 'rim_diameter_max' in params:
            query_params.append(('rim_diameter_max', params['rim_diameter_max']))  # noqa: E501
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
            '/tires/{tire}/', 'GET',
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
