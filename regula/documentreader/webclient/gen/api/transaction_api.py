# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from regula.documentreader.webclient.gen.api_client import ApiClient
from regula.documentreader.webclient.gen.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TransactionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_tag_tag_id_delete(self, tag_id, **kwargs):  # noqa: E501
        """Delete Reprocess transactions by tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_tag_tag_id_delete(tag_id, async_req=True)
        >>> result = thread.get()

        :param tag_id: Tag id (required)
        :type tag_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v2_tag_tag_id_delete_with_http_info(tag_id, **kwargs)  # noqa: E501

    def api_v2_tag_tag_id_delete_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Delete Reprocess transactions by tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_tag_tag_id_delete_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param tag_id: Tag id (required)
        :type tag_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'tag_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_tag_tag_id_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_id' is set
        if self.api_client.client_side_validation and ('tag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['tag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tag_id` when calling `api_v2_tag_tag_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in local_var_params:
            path_params['tagId'] = local_var_params['tag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            204: "object",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            '/api/v2/tag/{tagId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_v2_tag_tag_id_transactions_get(self, tag_id, **kwargs):  # noqa: E501
        """Get transactions by tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_tag_tag_id_transactions_get(tag_id, async_req=True)
        >>> result = thread.get()

        :param tag_id: Tag id (required)
        :type tag_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListTransactionsByTagResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v2_tag_tag_id_transactions_get_with_http_info(tag_id, **kwargs)  # noqa: E501

    def api_v2_tag_tag_id_transactions_get_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Get transactions by tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_tag_tag_id_transactions_get_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param tag_id: Tag id (required)
        :type tag_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListTransactionsByTagResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'tag_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_tag_tag_id_transactions_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_id' is set
        if self.api_client.client_side_validation and ('tag_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['tag_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tag_id` when calling `api_v2_tag_tag_id_transactions_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in local_var_params:
            path_params['tagId'] = local_var_params['tag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "ListTransactionsByTagResponse",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            '/api/v2/tag/{tagId}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_v2_transaction_transaction_id_file_get(self, transaction_id, name, **kwargs):  # noqa: E501
        """Get Reprocess transaction file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_transaction_transaction_id_file_get(transaction_id, name, async_req=True)
        >>> result = thread.get()

        :param transaction_id: Transaction id (required)
        :type transaction_id: int
        :param name: File name (required)
        :type name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: file
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v2_transaction_transaction_id_file_get_with_http_info(transaction_id, name, **kwargs)  # noqa: E501

    def api_v2_transaction_transaction_id_file_get_with_http_info(self, transaction_id, name, **kwargs):  # noqa: E501
        """Get Reprocess transaction file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_transaction_transaction_id_file_get_with_http_info(transaction_id, name, async_req=True)
        >>> result = thread.get()

        :param transaction_id: Transaction id (required)
        :type transaction_id: int
        :param name: File name (required)
        :type name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(file, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'transaction_id',
            'name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_transaction_transaction_id_file_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_id' is set
        if self.api_client.client_side_validation and ('transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_id` when calling `api_v2_transaction_transaction_id_file_get`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `api_v2_transaction_transaction_id_file_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_id' in local_var_params:
            path_params['transactionId'] = local_var_params['transaction_id']  # noqa: E501

        query_params = []
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "file",
            404: None,
        }

        return self.api_client.call_api(
            '/api/v2/transaction/{transactionId}/file', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_v2_transaction_transaction_id_get(self, transaction_id, **kwargs):  # noqa: E501
        """Get Reprocess transaction data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_transaction_transaction_id_get(transaction_id, async_req=True)
        >>> result = thread.get()

        :param transaction_id: Transaction id (required)
        :type transaction_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TransactionProcessGetResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v2_transaction_transaction_id_get_with_http_info(transaction_id, **kwargs)  # noqa: E501

    def api_v2_transaction_transaction_id_get_with_http_info(self, transaction_id, **kwargs):  # noqa: E501
        """Get Reprocess transaction data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_transaction_transaction_id_get_with_http_info(transaction_id, async_req=True)
        >>> result = thread.get()

        :param transaction_id: Transaction id (required)
        :type transaction_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TransactionProcessGetResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'transaction_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_transaction_transaction_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_id' is set
        if self.api_client.client_side_validation and ('transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_id` when calling `api_v2_transaction_transaction_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_id' in local_var_params:
            path_params['transactionId'] = local_var_params['transaction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "TransactionProcessGetResponse",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            '/api/v2/transaction/{transactionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_v2_transaction_transaction_id_process_post(self, transaction_id, transaction_process_request, **kwargs):  # noqa: E501
        """Reprocess  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_transaction_transaction_id_process_post(transaction_id, transaction_process_request, async_req=True)
        >>> result = thread.get()

        :param transaction_id: Transaction id (required)
        :type transaction_id: int
        :param transaction_process_request: (required)
        :type transaction_process_request: TransactionProcessRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TransactionProcessResult
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v2_transaction_transaction_id_process_post_with_http_info(transaction_id, transaction_process_request, **kwargs)  # noqa: E501

    def api_v2_transaction_transaction_id_process_post_with_http_info(self, transaction_id, transaction_process_request, **kwargs):  # noqa: E501
        """Reprocess  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_transaction_transaction_id_process_post_with_http_info(transaction_id, transaction_process_request, async_req=True)
        >>> result = thread.get()

        :param transaction_id: Transaction id (required)
        :type transaction_id: int
        :param transaction_process_request: (required)
        :type transaction_process_request: TransactionProcessRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TransactionProcessResult, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'transaction_id',
            'transaction_process_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_transaction_transaction_id_process_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_id' is set
        if self.api_client.client_side_validation and ('transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_id` when calling `api_v2_transaction_transaction_id_process_post`")  # noqa: E501
        # verify the required parameter 'transaction_process_request' is set
        if self.api_client.client_side_validation and ('transaction_process_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_process_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_process_request` when calling `api_v2_transaction_transaction_id_process_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_id' in local_var_params:
            path_params['transactionId'] = local_var_params['transaction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_process_request' in local_var_params:
            body_params = local_var_params['transaction_process_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "TransactionProcessResult",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            '/api/v2/transaction/{transactionId}/process', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_v2_transaction_transaction_id_results_get(self, transaction_id, **kwargs):  # noqa: E501
        """Get Reprocess transaction result  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_transaction_transaction_id_results_get(transaction_id, async_req=True)
        >>> result = thread.get()

        :param transaction_id: Transaction id (required)
        :type transaction_id: int
        :param with_images: With base64 images or url
        :type with_images: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TransactionProcessResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v2_transaction_transaction_id_results_get_with_http_info(transaction_id, **kwargs)  # noqa: E501

    def api_v2_transaction_transaction_id_results_get_with_http_info(self, transaction_id, **kwargs):  # noqa: E501
        """Get Reprocess transaction result  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_transaction_transaction_id_results_get_with_http_info(transaction_id, async_req=True)
        >>> result = thread.get()

        :param transaction_id: Transaction id (required)
        :type transaction_id: int
        :param with_images: With base64 images or url
        :type with_images: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TransactionProcessResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'transaction_id',
            'with_images'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_transaction_transaction_id_results_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_id' is set
        if self.api_client.client_side_validation and ('transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_id` when calling `api_v2_transaction_transaction_id_results_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_id' in local_var_params:
            path_params['transactionId'] = local_var_params['transaction_id']  # noqa: E501

        query_params = []
        if 'with_images' in local_var_params and local_var_params['with_images'] is not None:  # noqa: E501
            query_params.append(('withImages', local_var_params['with_images']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "TransactionProcessResponse",
            400: None,
            403: None,
        }

        return self.api_client.call_api(
            '/api/v2/transaction/{transactionId}/results', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
