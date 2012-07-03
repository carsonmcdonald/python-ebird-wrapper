from ebird import AvianKnowledge
from ebird import EBird

ak = AvianKnowledge()

#print ak.country_list()

#print ak.subnational1_list()
#print ak.subnational1_list({'countryCode': 'US'})

ebird = EBird()

#print ebird.species_reference()
#print ebird.species_reference({'locale': 'fr_CA'})
#print ebird.species_reference({'cat': 'hybrid'})

#print ebird.hotspot_reference('subnational1', 'US-KY')

#print ebird.hotspot_geo(38, -85)

#print ebird.recent_observations('L99381')

#print ebird.recent_observations_geo(38, -85)

#print ebird.recent_species_observations_geo(42.46, -76.51, 'branta canadensis')

#print ebird.recent_observations_hotspot('L99381')

#print ebird.recent_species_observations_hotspot('L99381', 'Hirundo rustica')

#print ebird.recent_observations_location('L99381')

#print ebird.recent_species_observations_location('L99381', 'Hirundo rustica')

#print ebird.recent_observations_region('subnational1', 'US-KY')

#print ebird.recent_species_observations_region('subnational1', 'US-KY', 'Hirundo rustica')

#print ebird.recent_notable_observations_geo(38, -85)

#print ebird.recent_notable_observations_hotspot('L149830')

#print ebird.recent_notable_observations_location('L149830')

#print ebird.recent_notable_observations_region('subnational1', 'US-KY')

#print ebird.nearest_species_observation_location(38, -85, 'Hirundo rustica')
