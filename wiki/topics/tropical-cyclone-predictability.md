---
title: "Tropical Cyclone Predictability"
page_type: "topic"
status: "active"
last_updated: "2026-04-17"
source_count: 18
---

# Definition

Tropical cyclone predictability here refers to how far ahead storm intensity, structure, and rapid-intensification timing can be forecast before uncertainty from the environment, internal vortex dynamics, and convection becomes too large.

# Current Synthesis

The wiki now has a first dedicated predictability branch anchored by two Judt-led Hurricane Earl ensemble studies, plus links to the existing FV3/HAFS numerical-modeling pages. [Judt et al. (2016)](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md) show that intensity predictability is strongly scale dependent: convective-scale details lose predictability within hours, rainband-scale structure within days, but the azimuthal-mean vortex and wave number-1 asymmetry can remain predictable for at least a week when the large-scale environment is well constrained.

[Judt and Chen (2016)](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md) then narrow the problem to rapid intensification (RI). In their Earl ensembles, most members eventually undergo RI and become major hurricanes, yet the onset timing remains weakly predictable and partly stochastic. This separates the predictability of *whether* RI happens from the predictability of *when* it begins.

[Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md) add a second Earl branch inside a fully coupled atmosphere-wave-ocean framework. Rather than using only stochastic perturbations, they parameterize uncertainty in initial vortex strength, size, and asymmetry, then show that RI sensitivity is tied most strongly to azimuthally averaged maximum wind speed and asymmetry orientation within the tested range. When SKEBS forcing is added, however, track spread responds much more strongly than it did to internal-vortex perturbations alone. This sharpens the wiki's current distinction between internal-vortex uncertainty, RI-pathway uncertainty, and environment-driven track uncertainty.

[Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md), [Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md), and [Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) add an operational-modeling branch showing that even advanced FV3/HAFS-class systems still concentrate large errors in RI timing, storm structure, and transition regimes. [Judt et al. (2023)](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md) provide one explanation for why those failures are hard to eliminate: RI itself can occur through structurally different modes, including a low-shear symmetric "marathon" mode and a burst-driven, center-reforming "sprint" mode under less favorable environments.


Reasor-centered shear-resilience papers extend this branch beyond stochastic-ensemble diagnostics. [Reasor et al. (2004)](../papers/reasor-montgomery-grasso-2004-vortex-resiliency-vertical-shear.md) and [Reasor and Montgomery (2015)](../papers/reasor-montgomery-2015-heuristic-model-tc-resilience.md) provide mechanism-oriented resilience framing, while [Reasor and Eastin (2009)](../papers/reasor-eastin-2009-ri-guillermo-part-i-low-wavenumber-structure.md), [Reasor and Eastin (2012)](../papers/reasor-eastin-2012-ri-guillermo-part-ii-resiliency-in-shear.md), and [Reasor et al. (2013)](../papers/reasor-rogers-lorsolo-2013-environmental-flow-impacts-on-tc-structure.md) show that forecast-relevant RI behavior in shear depends strongly on evolving inner-core structure and environmental-flow regime.

The new Klotzbach-centered Atlantic climate-controls branch extends predictability to longer leads and coarser scales. [Klotzbach (2010)](../papers/klotzbach-2010-mjo-atlantic-hurricane-relationship.md) shows that Atlantic genesis, intensification, and U.S. landfalls are materially modulated by MJO phase on roughly 2-week time scales, while [Klotzbach (2011)](../papers/klotzbach-2011-enso-atlantic-hurricanes-us-landfalls.md) shows that ENSO shifts the seasonal Atlantic background for hurricane activity and landfall probabilities. [Klotzbach (2012)](../papers/klotzbach-2012-enso-mjo-atlantic-ri.md) then extends that logic to RI itself, showing that favorable subseasonal and seasonal climate states increase RI odds. [Jones et al. (2020)](../papers/jones-bell-klotzbach-2020-na-atlantic-vws-seasonal-tc-activity.md) and [Klotzbach et al. (2020)](../papers/klotzbach-caron-bell-2020-statistical-dynamical-north-atlantic-seasonal-hurricane-prediction.md) show how this longer-lead predictability can be interpreted and partly operationalized through seasonal environmental predictors, especially Atlantic vertical-wind-shear modes and hybrid statistical/dynamical forecast systems.

Inference for this wiki: tropical-cyclone predictability should be treated as scale dependent and regime dependent, but also as climate conditioned. Large-scale modes such as the MJO and ENSO place probabilistic bounds on genesis geography, RI likelihood, and seasonal activity, while internal convective reorganization and structural mode transitions still sharply limit practical predictability of RI onset and short-term intensity change.

[Aberson (2011)](../papers/aberson-2011-impact-of-dropwindsonde-data-on-tc-forecasts-gfs.md) adds an adaptive-observing branch: targeted dropwindsonde assimilation in the GFS produced case-dependent but measurable tropical-cyclone forecast improvements. Inference for this wiki: intrinsic predictability limits and observing-network design must be interpreted together, because targeted sampling can recover skill in some sensitive flow configurations.

# Evidence By Source

- [Reasor et al. (2004)](../papers/reasor-montgomery-grasso-2004-vortex-resiliency-vertical-shear.md) show via idealized dynamics that resilience in shear depends on intrinsic alignment behavior, implying regime-dependent forecast sensitivity to vortex structure.
- [Reasor and Eastin (2009)](../papers/reasor-eastin-2009-ri-guillermo-part-i-low-wavenumber-structure.md) diagnose low-wavenumber structural evolution in Guillermo RI, supporting a structured predictability problem rather than random convective noise alone.
- [Reasor and Eastin (2012)](../papers/reasor-eastin-2012-ri-guillermo-part-ii-resiliency-in-shear.md) show that RI can proceed under shear when resilience pathways are active, sharpening the distinction between bulk-shear and effective-shear impacts.
- [Reasor et al. (2013)](../papers/reasor-rogers-lorsolo-2013-environmental-flow-impacts-on-tc-structure.md) provide multi-case airborne-radar evidence that environmental flow regimes map onto systematic inner-core structural differences.
- [Reasor and Montgomery (2015)](../papers/reasor-montgomery-2015-heuristic-model-tc-resilience.md) provide a reduced resilience framework that helps interpret why similar shear magnitudes can yield different intensity outcomes.
- [Judt et al. (2016)](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md) show that small-scale asymmetric errors saturate within roughly 6-12 h, while rainband-scale structure remains predictable on roughly 1-5-day horizons.
- The same paper finds that the azimuthal-mean vortex and wave number-1 asymmetry remain predictable for at least 7 days in Hurricane Earl, with uncertainty strongly tied to large-scale environmental and boundary-condition perturbations.
- [Judt and Chen (2016)](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md) show that RI likelihood can be comparatively predictable even when exact RI timing is not.
- The same paper identifies early- and late-RI pathways, implying that timing uncertainty is partly tied to different structural routes to maturity.
- [Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md) show that RI in Earl was more sensitive to initial mean-vortex strength and asymmetry orientation than to storm size or asymmetry magnitude within their tested uncertainty range.
- The same paper shows that stochastic environmental forcing widened the track envelope much more than internal-vortex perturbations alone, even when both produced substantial intensity spread.
- [Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md) show that an early high-resolution FV3 system produced useful track guidance while still missing selected RI episodes badly.
- [Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md) show that member-to-member RI outcomes in Hurricane Michael depend strongly on tilt reduction and upshear moistening even when bulk shear is similar.
- [Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) provide system-scale evidence that RI and transition regimes remain concentrated forecast-failure modes in a prototype HAFS configuration.
- [Judt et al. (2023)](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md) argue that structurally distinct RI modes help explain why forecast skill and scientific consensus break down most sharply around RI onset.
- [Klotzbach (2010)](../papers/klotzbach-2010-mjo-atlantic-hurricane-relationship.md) shows that Atlantic TC activity and even U.S. landfalls are materially modulated by MJO phase, implying meaningful subseasonal predictability in basinwide probabilities.
- [Klotzbach (2011)](../papers/klotzbach-2011-enso-atlantic-hurricanes-us-landfalls.md) shows that ENSO materially shifts Atlantic hurricane frequency, major-hurricane probability, and regional landfall likelihood on seasonal time scales.
- [Klotzbach (2012)](../papers/klotzbach-2012-enso-mjo-atlantic-ri.md) shows that RI probability itself is climate conditioned, with more Atlantic RI in La Niña years and in favorable MJO phases.
- [Jones et al. (2020)](../papers/jones-bell-klotzbach-2020-na-atlantic-vws-seasonal-tc-activity.md) show that seasonal Atlantic vertical-wind-shear predictability depends on both tropical and subtropical climate modes, including anticyclonic Rossby wave breaking.
- [Klotzbach et al. (2020)](../papers/klotzbach-caron-bell-2020-statistical-dynamical-north-atlantic-seasonal-hurricane-prediction.md) show that predicting environmental controls directly with a seasonal dynamical model can improve seasonal ACE outlook skill.

# Open Questions

- Which aspects of RI timing are intrinsically unpredictable, and which are still limited mainly by initialization or model physics?
- How often do forecast busts arise from missing the correct RI mode rather than from mean-state environmental error?
- Can large-scale predictability of the mean vortex be translated into useful probabilistic bounds on short-term intensity change?
- How much useful RI predictability comes from climate-mode conditioning versus storm-scale structural initialization?
- Which structural precursors are robust enough to improve operational ensemble calibration for RI?

# Related Pages

- [Rapid Intensification](rapid-intensification.md)
- [Tropical Cyclone Observing Systems and Adaptive Sampling](tropical-cyclone-observing-systems-and-adaptive-sampling.md)
- [Atlantic Hurricane Climate Controls and Seasonal Forecasting](atlantic-hurricane-climate-controls-and-seasonal-forecasting.md)
- [Tropical Cyclone Intensification](tropical-cyclone-intensification.md)
- [Tropical Cyclone Numerical Modeling](tropical-cyclone-numerical-modeling.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
- [On the Madden-Julian Oscillation-Atlantic Hurricane Relationship](../papers/klotzbach-2010-mjo-atlantic-hurricane-relationship.md)
- [El Niño-Southern Oscillation's Impact on Atlantic Basin Hurricanes and U.S. Landfalls](../papers/klotzbach-2011-enso-atlantic-hurricanes-us-landfalls.md)
- [El Niño-Southern Oscillation, the Madden-Julian Oscillation and Atlantic Basin Tropical Cyclone Rapid Intensification](../papers/klotzbach-2012-enso-mjo-atlantic-ri.md)
- [Tropical and Subtropical North Atlantic Vertical Wind Shear and Seasonal Tropical Cyclone Activity](../papers/jones-bell-klotzbach-2020-na-atlantic-vws-seasonal-tc-activity.md)
- [A Statistical/Dynamical Model for North Atlantic Seasonal Hurricane Prediction](../papers/klotzbach-caron-bell-2020-statistical-dynamical-north-atlantic-seasonal-hurricane-prediction.md)
- [Predictability of Tropical Cyclone Intensity: Scale-Dependent Forecast Error Growth in High-Resolution Stochastic Kinetic-Energy Backscatter Ensembles](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md)
- [Predictability and Dynamics of Tropical Cyclone Rapid Intensification Deduced from High-Resolution Stochastic Ensembles](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md)
- [Uncertainty Propagation in Coupled Atmosphere-Wave-Ocean Prediction System: A Study of Hurricane Earl (2010)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md)
- [Marathon vs. Sprint: Two Modes of Tropical Cyclone Rapid Intensification in a Global Convection-Permitting Simulation](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md)
- [High-Resolution Ensemble HFV3 Forecasts of Hurricane Michael (2018): Rapid Intensification in Shear](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md)
- [A New Look at the Problem of Tropical Cyclones in Vertical Shear Flow: Vortex Resiliency](../papers/reasor-montgomery-grasso-2004-vortex-resiliency-vertical-shear.md)
- [Rapidly Intensifying Hurricane Guillermo (1997). Part I: Low-Wavenumber Structure and Evolution](../papers/reasor-eastin-2009-ri-guillermo-part-i-low-wavenumber-structure.md)
- [Rapidly Intensifying Hurricane Guillermo (1997), Part II: Resiliency in Shear](../papers/reasor-eastin-2012-ri-guillermo-part-ii-resiliency-in-shear.md)
- [Environmental Flow Impacts on Tropical Cyclone Structure Diagnosed from Airborne Doppler Radar Composites](../papers/reasor-rogers-lorsolo-2013-environmental-flow-impacts-on-tc-structure.md)
- [Evaluation of a Heuristic Model for Tropical Cyclone Resilience](../papers/reasor-montgomery-2015-heuristic-model-tc-resilience.md)
