import requests

import EBirdException

class EBird(object):

  def __init__(self, options={}):
    self.base_api_url = 'http://ebird.org/ws1.1'

  def handle_response(self, response):
    if response.status_code != 200:
      raise EBirdException.EBirdException(response.status_code, response.text)
    else:
      return response.json()

  def recent_observations_geo(self, lat, lng, options={}):
    params = {'lat': lat, 'lng': lng, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/obs/geo/recent', params=params))

  def recent_species_observations_geo(self, lat, lng, sci, options={}):
    params = {'lat': lat, 'lng': lng, 'sci': sci, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/obs/geo_spp/recent', params=params))

  def recent_observations_hotspot(self, r, options={}):
    params = {'r': r, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/obs/hotspot/recent', params=params))


  def recent_species_observations_hotspot(self, r, sci, options={}):
    params = {'r': r, 'sci': sci, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/obs/hotspot_spp/recent', params=params))


  def recent_observations_location(self, r, options={}):
    params = {'r': r, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/obs/loc/recent', params=params))


  def recent_species_observations_location(self, r, sci, options={}):
    params = {'r': r, 'sci': sci, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/obs/loc_spp/recent', params=params))


  def recent_observations_region(self, rtype, r, options={}):
    params = {'r': r, 'rtype': rtype, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/obs/region/recent', params=params))


  def recent_species_observations_region(self, rtype, r, sci, options={}):
    params = {'r': r, 'rtype': rtype, 'sci': sci, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/obs/region_spp/recent', params=params))


  def recent_notable_observations_geo(self, lat, lng, options={}):
    params = {'lat': lat, 'lng': lng, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/notable/geo/recent', params=params))


  def recent_notable_observations_hotspot(self, r, options={}):
    params = {'r': r, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/notable/hotspot/recent', params=params))


  def recent_notable_observations_location(self, r, options={}):
    params = {'r': r, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/notable/loc/recent', params=params))


  def recent_notable_observations_region(self, rtype, r, options={}):
    params = {'r': r, 'rtype': rtype, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/notable/region/recent', params=params))


  def nearest_species_observation_location(self, lat, lng, sci, options={}):
    params = {'lat': lat, 'lng': lng, 'sci': sci, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/data/nearest/geo_spp/recent', params=params))

  def recent_observations(self, r, options={}):
    params = {'r': r, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/product/obs/hotspot/recent', params=params))


  def species_reference(self, options={}):
    params = {'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/ref/taxa/ebird', params=params))


  def hotspot_reference(self, rtype, r, options={}):
    params = {'rtype': rtype, 'r': r, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/ref/hotspot/region', params=params))


  def hotspot_geo(self, lat, lng, options={}):
    params = {'lat': lat, 'lng': lng, 'fmt': 'json'}
    params.update(options)
    return self.handle_response(requests.get(self.base_api_url + '/ref/hotspot/geo', params=params))
