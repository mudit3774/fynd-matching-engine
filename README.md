# fynd-matching-engine
Matching Engine for fynd

# Usage 
'''
from fynd import Preferences
from fynd import MatchingEngine

pref_1 = Preferences(19.107554, 72.896517, 10, 'time')
pref_2 = Preferences(19.107554, 72.896517, 10, 'time')
m = MatchingEngine()
suggestions = m.get_suggestions([pref_1, pref_2])
print suggestions
'''
