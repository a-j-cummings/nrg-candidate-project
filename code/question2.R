library(tidyverse)
library(nlme)
library(splines)

# See question2.py for the context of this script (lines 14-28)
height <- read_csv('../candidate_project/height_data.csv')

mod <- gls(height ~ bs(age, knots=c(3,8,16), degree=1)*male + weight, 
           weights = varExp(form = ~ weight),
           data = height)
summary(mod)
# With the parameterization of the fixed terms of the model, the variance 
# weighting is almost reduced to matter of principle. I think the analysis 
# without it loses some of its defensibility.
# The parameterization the model uses is fitting linear splines with knots at
# ages of significant changes in physical human development. These splines are
# estimated twice, once for each sex, to account for sex-age differences in 
# development. Though there are better ways to account for the effect of weight
# on height if high fidelity prediction is the goal, but for this analysis 
# leaving a single term for weight unencumbered by interaction effects is
# very useful for inference.

# Assumptions
#   Linearity + Equal variance (after accounting for heteroskedasticity)
ggplot() + 
  geom_point(aes(x=fitted(mod), y=resid(mod, type='pearson'))) + 
  labs(x='Fitted values', y='Standardized (Pearson) Residuals')
#   looks good to me!

#   Normality
ggplot(mapping = aes(sample=resid(mod))) + 
  stat_qq() + 
  stat_qq_line()
#   Given the challenges of accounting for fairly complex interactions, I am
#   pretty satisfied with this QQ plot. There still are some heavy tails, but 
#   I would be comfortable defending this assumption being met.

#   Without more information on the data collection I cannot comment on the 
#   independence of the data, but I am comfortable with it given the context of
#   this analysis.

#   I would certify this model as valid. Inference can proceed without caveat.

# Model summary
mod$coefficients['weight']
confint(mod)['weight',]
