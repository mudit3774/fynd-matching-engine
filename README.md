# Fynd Matching Engine
Matching Engine for finding the best area to live in given different set of preferences.
Preferences are basically lat, lon, travel mode and acceptable travel time from home.

# Usage 

Use fynd to create an arrray of preferences and use MatchingEngine.get_suggestions([]) 
to get are recommendation/polygon.

```
from fynd import Preferences
from fynd import MatchingEngine

pref_1 = Preferences(19.107554, 72.896517, 10, 'time')
pref_2 = Preferences(19.107554, 72.896517, 10, 'time')
m = MatchingEngine()
suggestions = m.get_suggestions([pref_1, pref_2])
print suggestions
```
