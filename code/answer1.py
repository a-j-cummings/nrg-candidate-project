"""If an event has log-odds 3.2, what is the probability of this event?"""

import numpy as np

log_odds = 3.2
odds = np.exp(3.2)
prob = odds/(odds + 1)
print(prob)