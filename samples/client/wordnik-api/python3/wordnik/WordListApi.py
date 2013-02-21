#!/usr/bin/env python
"""
WordAPI.py
Copyright 2012 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from .models import *


class WordListApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def updateWordList(self, permalink, auth_token, **kwargs):
        """Updates an existing WordList

        Args:
            permalink, str: permalink of WordList to update (required)
            body, WordList: Updated WordList (optional)
            auth_token, str: The auth token of the logged-in user, obtained by calling /account.{format}/authenticate/{username} (described above) (required)
            
        Returns: 
        """

        allParams = ['permalink', 'body', 'auth_token']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateWordList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wordList.{format}/{permalink}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        if ('auth_token' in params):
            headerParams['auth_token'] = params['auth_token']
        if ('permalink' in params):
            replacement = str(self.apiClient.toPathValue(params['permalink']))
            resourcePath = resourcePath.replace('{' + 'permalink' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        
    def deleteWordList(self, permalink, auth_token, **kwargs):
        """Deletes an existing WordList

        Args:
            permalink, str: ID of WordList to delete (required)
            auth_token, str: The auth token of the logged-in user, obtained by calling /account.{format}/authenticate/{username} (described above) (required)
            
        Returns: 
        """

        allParams = ['permalink', 'auth_token']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteWordList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wordList.{format}/{permalink}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        if ('auth_token' in params):
            headerParams['auth_token'] = params['auth_token']
        if ('permalink' in params):
            replacement = str(self.apiClient.toPathValue(params['permalink']))
            resourcePath = resourcePath.replace('{' + 'permalink' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        
    def getWordListByPermalink(self, permalink, auth_token, **kwargs):
        """Fetches a WordList by ID

        Args:
            permalink, str: permalink of WordList to fetch (required)
            auth_token, str: The auth token of the logged-in user, obtained by calling /account.{format}/authenticate/{username} (described above) (required)
            
        Returns: WordList
        """

        allParams = ['permalink', 'auth_token']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getWordListByPermalink" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wordList.{format}/{permalink}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('auth_token' in params):
            headerParams['auth_token'] = params['auth_token']
        if ('permalink' in params):
            replacement = str(self.apiClient.toPathValue(params['permalink']))
            resourcePath = resourcePath.replace('{' + 'permalink' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'WordList')
        return responseObject
        
        
    def addWordsToWordList(self, permalink, auth_token, **kwargs):
        """Adds words to a WordList

        Args:
            permalink, str: permalink of WordList to user (required)
            body, list[StringValue]: Array of words to add to WordList (optional)
            auth_token, str: The auth token of the logged-in user, obtained by calling /account.{format}/authenticate/{username} (described above) (required)
            
        Returns: 
        """

        allParams = ['permalink', 'body', 'auth_token']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addWordsToWordList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wordList.{format}/{permalink}/words'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('auth_token' in params):
            headerParams['auth_token'] = params['auth_token']
        if ('permalink' in params):
            replacement = str(self.apiClient.toPathValue(params['permalink']))
            resourcePath = resourcePath.replace('{' + 'permalink' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        
    def getWordListWords(self, permalink, auth_token, **kwargs):
        """Fetches words in a WordList

        Args:
            permalink, str: ID of WordList to use (required)
            auth_token, str: The auth token of the logged-in user, obtained by calling /account.{format}/authenticate/{username} (described above) (required)
            sortBy, str: Field to sort by (optional)
            sortOrder, str: Direction to sort (optional)
            skip, int: Results to skip (optional)
            limit, int: Maximum number of results to return (optional)
            
        Returns: list[WordListWord]
        """

        allParams = ['permalink', 'auth_token', 'sortBy', 'sortOrder', 'skip', 'limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getWordListWords" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wordList.{format}/{permalink}/words'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])
        if ('sortOrder' in params):
            queryParams['sortOrder'] = self.apiClient.toPathValue(params['sortOrder'])
        if ('skip' in params):
            queryParams['skip'] = self.apiClient.toPathValue(params['skip'])
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        if ('auth_token' in params):
            headerParams['auth_token'] = params['auth_token']
        if ('permalink' in params):
            replacement = str(self.apiClient.toPathValue(params['permalink']))
            resourcePath = resourcePath.replace('{' + 'permalink' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[WordListWord]')
        return responseObject
        
        
    def deleteWordsFromWordList(self, permalink, auth_token, **kwargs):
        """Removes words from a WordList

        Args:
            permalink, str: permalink of WordList to use (required)
            body, list[StringValue]: Words to remove from WordList (optional)
            auth_token, str: The auth token of the logged-in user, obtained by calling /account.{format}/authenticate/{username} (described above) (required)
            
        Returns: 
        """

        allParams = ['permalink', 'body', 'auth_token']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteWordsFromWordList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/wordList.{format}/{permalink}/deleteWords'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('auth_token' in params):
            headerParams['auth_token'] = params['auth_token']
        if ('permalink' in params):
            replacement = str(self.apiClient.toPathValue(params['permalink']))
            resourcePath = resourcePath.replace('{' + 'permalink' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        
    


