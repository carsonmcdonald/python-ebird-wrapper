import requests
import csv
import re

import EBirdException

class AvianKnowledge(object):

  def __init__(self, options={}):
    self.base_api_url = 'http://www.avianknowledge.net/ws1.0'

  def handle_response(self, response):
    if response.status_code != 200:
      raise EBirdException.EBirdException(response.status_code, response.text)
    else:
      data = re.sub(r',\n', ',', response.text)
      resp = []
      for row in csv.reader(self.utf_8_encoder(data.split('\n'))):
        if len(row) > 0:
          resp.append(row)
      return resp

  def utf_8_encoder(self, unicode_csv_data):
    for line in unicode_csv_data:
      yield line.encode('utf-8')

  def country_list(self):
    params = {'format': 'csv'}
    return self.handle_response(requests.get(self.base_api_url + '/ref/country/list', params=params))

  def subnational1_list(self, options={}):
    params = {'format': 'csv'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/ref/subnational1/list', params=params))
