python-ebird-wrapper
====================

This is a simple wrapper for the [eBird API version 1.1](https://confluence.cornell.edu/display/CLOISAPI/eBird+API+1.1)

The library also wraps the portion of the [avian knowledge API](https://confluence.cornell.edu/display/CLOISAPI/AKNAPIs) that is needed for the eBird API.

Usage
=====

```python
from ebird import AvianKnowledge
from ebird import EBird

ak = AvianKnowledge()

print ak.country_list()

ebird = EBird()

print ebird.species_reference()
```
