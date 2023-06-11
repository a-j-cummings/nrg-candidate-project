"""Fit a model on time to event data found in the survival_data.csv file. 
Explain how different variables (var1, var2, and var3) might influence hazards.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import CoxPHFitter

survival_data = pd.read_csv('../candidate_project/survival_data.csv')
# minor EDA to check for obvious singularities
survival_data.corr()

# model fit
cph = CoxPHFitter()
cph.fit(survival_data, # fit method fits for right censored data
        duration_col='T',
        event_col='E',
        formula='var1 + var2 + var3')

# diagnostics (influential observations)
d_resids = cph.compute_residuals(survival_data, kind='deviance')
sns.regplot(x=d_resids.index, y=d_resids.deviance)
plt.show() # nothing concerning

# assumptions
#   Proportional Hazards
cph.check_assumptions(survival_data, show_plots=True)
plt.show() # don't love the look of var 3, but it is not egregious
#   Linearity
m_resids = cph.compute_residuals(survival_data, kind='martingale')
fig, axs = plt.subplots(ncols=3)
sns.regplot(x=survival_data.var1, y=m_resids.martingale, lowess=True, ax=axs[0])
sns.regplot(x=survival_data.var2, y=m_resids.martingale, lowess=True, ax=axs[1])
sns.regplot(x=survival_data.var3, y=m_resids.martingale, lowess=True, ax=axs[2])
plt.show() # a little wiggle on var3, but also not egregious

# model summary
cph.print_summary()