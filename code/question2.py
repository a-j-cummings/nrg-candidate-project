"""Fit a model to the height_data.csv file. For every 10 units of increase in 
weight, how much taller does the model predict a person gets?
"""
# To estimate uncertainty in the above question, a prediction interval will be
# needed.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

height = pd.read_csv('../candidate_project/height_data.csv')

# EDA
sns.pairplot(height, hue='male')
plt.show()
# age has an obvious effect while an individual is growing, consider splines
# heteroskedasticity in height as a function of weight is evident
#   ^ not uncommon for biological data
# height-weight looks nonlinear, likely due to the effect of age, check for it
# There appears to be a relationship between age and weight that is stronger and
#   shaped like the relationship between age and height
# Interactions with gender are worth considering
# Interestingly, relationship between height and age may be a survivorship bias;
#   many studies have found correlations between small body size (specifically 
#   being short) and longevity. I would want to learn more about how the data
#   was collected as this could introduce a confounding source of bias.
# THIS TYPE OF REGRESSION IS, FRANKLY, BETTER DONE IN R
#   I am not aware of Python packages that handle structure in the residuals,
#   (I think statsmodels is close, but not quite enough). I've spent some good 
#   time looking too.

height.describe()
height.isna().sum()