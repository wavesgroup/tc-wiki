---
title: "A Statistical/Dynamical Model for North Atlantic Seasonal Hurricane Prediction"
page_type: "paper"
status: "active"
last_updated: "2026-04-17"
source_count: 1
---

# Citation

Klotzbach, P. J., L.-P. Caron, and M. M. Bell, 2020: *A statistical/dynamical model for North Atlantic seasonal hurricane prediction*. *Geophysical Research Letters*, 47, e2020GL089357. DOI: [10.1029/2020GL089357](https://doi.org/10.1029/2020GL089357).

Accessed text source: [Colorado State University publication summary and abstract](https://tropical.colostate.edu/pub/Klotzbach_Caron_2020_GRL.html).

Peer-review status: Peer-reviewed primary research article.

# Research Question

Klotzbach et al. (2020) ask whether a hybrid statistical/dynamical framework using ECMWF SEAS5 forecasts of key Atlantic predictors can improve North Atlantic seasonal hurricane prediction skill relative to traditional statistical schemes alone.

# Data And Methods

- Study type: Seasonal forecast-model development and cross-validated hindcast evaluation.
- Forecast target: Seasonal North Atlantic accumulated cyclone energy (ACE).
- Predictive framework: The ECMWF SEAS5 seasonal forecast system is used to predict the three July large-scale predictors in Colorado State University's early August statistical hurricane forecast model.
- Training and evaluation period: 1982-2019.
- Lead times: Initializations as early as 1 March, with later May and June initializations also evaluated for the April, June, and July seasonal outlook cycle.
- Verification approach: Cross-validated correlations between hindcast ACE and observed seasonal ACE, with the hybrid model also combined with CSU's existing statistical forecasts.

# Findings

- Klotzbach et al. (2020) find that SEAS5 shows useful skill in forecasting all three July predictor fields from as early as 1 March.
- When those predicted fields are regressed against seasonal ACE, the resulting statistical/dynamical model achieves a cross-validated correlation of 0.60 for 1 March initialization and 0.67 for 1 June initialization over 1982-2019.
- The combined statistical plus statistical/dynamical framework outperforms either component alone for the early April, June, and July outlooks.
- The most notable improvement occurs in the earliest outlook, which is important because lead-time is usually where traditional seasonal forecast skill is weakest.
- Inference for this wiki: the paper shows how Klotzbach's climate-controls research can be operationalized. It does not replace the statistical predictor logic; it improves the forecast pipeline by letting a dynamical model estimate the predictors earlier and more skillfully.

# Limitations

- The forecast target is basinwide seasonal ACE, so the model does not predict storm count distribution, landfall probabilities, or rapid-intensification timing directly.
- Skill is demonstrated in cross-validated hindcasts rather than a long independent real-time test set, so the operational value should be treated as promising rather than fully settled.
- The system depends on one dynamical model family and on three established CSU predictors, so it does not test whether a broader predictor pool or different seasonal models would perform better.
- Current ingest is abstract-constrained rather than full-text extracted, so detailed predictor definitions and calibration choices should be revisited in a later pass if this topic expands.

# Referenced Papers

This is a curated ingest queue, not a full bibliography.

- `Seasonal predictor mechanism:` [Tropical and Subtropical North Atlantic Vertical Wind Shear and Seasonal Tropical Cyclone Activity](jones-bell-klotzbach-2020-na-atlantic-vws-seasonal-tc-activity.md).
- `Foundational Atlantic ENSO context:` [El Niño-Southern Oscillation's Impact on Atlantic Basin Hurricanes and U.S. Landfalls](klotzbach-2011-enso-atlantic-hurricanes-us-landfalls.md).
- `Intraseasonal complement to seasonal prediction:` [On the Madden-Julian Oscillation-Atlantic Hurricane Relationship](klotzbach-2010-mjo-atlantic-hurricane-relationship.md).
- `Program-level review context:` Klotzbach, P. J., E. Blake, J. Camp, L.-P. Caron, J. C. L. Chan, N.-Y. Kang, Y. Kuleshov, S.-M. Lee, H. Murakami, M. Saunders, Y. Takaya, F. Vitart, and R. Zhan, 2019: *Seasonal tropical cyclone forecasting*. *Tropical Cyclone Research and Review*, 8, 134-149. DOI: [10.6057/2019TCRR03.03](https://doi.org/10.6057/2019TCRR03.03).

# Linked Pages

- [Atlantic Hurricane Climate Controls and Seasonal Forecasting](../topics/atlantic-hurricane-climate-controls-and-seasonal-forecasting.md)
- [Tropical Cyclone Predictability](../topics/tropical-cyclone-predictability.md)
- [Tropical and Subtropical North Atlantic Vertical Wind Shear and Seasonal Tropical Cyclone Activity](jones-bell-klotzbach-2020-na-atlantic-vws-seasonal-tc-activity.md)
- [El Niño-Southern Oscillation's Impact on Atlantic Basin Hurricanes and U.S. Landfalls](klotzbach-2011-enso-atlantic-hurricanes-us-landfalls.md)

