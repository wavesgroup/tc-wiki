---
title: "Tropical Cyclone Predictability"
page_type: "topic"
status: "active"
last_updated: "2026-04-10"
source_count: 6
---

# Definition

Tropical cyclone predictability here refers to how far ahead storm intensity, structure, and rapid-intensification timing can be forecast before uncertainty from the environment, internal vortex dynamics, and convection becomes too large.

# Current Synthesis

The wiki now has a first dedicated predictability branch anchored by two Judt-led Hurricane Earl ensemble studies, plus links to the existing FV3/HAFS numerical-modeling pages. [Judt et al. (2016)](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md) show that intensity predictability is strongly scale dependent: convective-scale details lose predictability within hours, rainband-scale structure within days, but the azimuthal-mean vortex and wave number-1 asymmetry can remain predictable for at least a week when the large-scale environment is well constrained.

[Judt and Chen (2016)](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md) then narrow the problem to rapid intensification (RI). In their Earl ensembles, most members eventually undergo RI and become major hurricanes, yet the onset timing remains weakly predictable and partly stochastic. This separates the predictability of *whether* RI happens from the predictability of *when* it begins.

[Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md), [Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md), and [Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) add an operational-modeling branch showing that even advanced FV3/HAFS-class systems still concentrate large errors in RI timing, storm structure, and transition regimes. [Judt et al. (2023)](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md) provide one explanation for why those failures are hard to eliminate: RI itself can occur through structurally different modes, including a low-shear symmetric "marathon" mode and a burst-driven, center-reforming "sprint" mode under less favorable environments.

Inference for this wiki: tropical-cyclone predictability should be treated as scale dependent and regime dependent. Large-scale flow places longer-lived bounds on vortex evolution, but internal convective reorganization and structural mode transitions strongly limit practical predictability of RI onset and short-term intensity change.

# Evidence By Source

- [Judt et al. (2016)](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md) show that small-scale asymmetric errors saturate within roughly 6-12 h, while rainband-scale structure remains predictable on roughly 1-5-day horizons.
- The same paper finds that the azimuthal-mean vortex and wave number-1 asymmetry remain predictable for at least 7 days in Hurricane Earl, with uncertainty strongly tied to large-scale environmental and boundary-condition perturbations.
- [Judt and Chen (2016)](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md) show that RI likelihood can be comparatively predictable even when exact RI timing is not.
- The same paper identifies early- and late-RI pathways, implying that timing uncertainty is partly tied to different structural routes to maturity.
- [Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md) show that an early high-resolution FV3 system produced useful track guidance while still missing selected RI episodes badly.
- [Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md) show that member-to-member RI outcomes in Hurricane Michael depend strongly on tilt reduction and upshear moistening even when bulk shear is similar.
- [Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) provide system-scale evidence that RI and transition regimes remain concentrated forecast-failure modes in a prototype HAFS configuration.
- [Judt et al. (2023)](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md) argue that structurally distinct RI modes help explain why forecast skill and scientific consensus break down most sharply around RI onset.

# Open Questions

- Which aspects of RI timing are intrinsically unpredictable, and which are still limited mainly by initialization or model physics?
- How often do forecast busts arise from missing the correct RI mode rather than from mean-state environmental error?
- Can large-scale predictability of the mean vortex be translated into useful probabilistic bounds on short-term intensity change?
- Which structural precursors are robust enough to improve operational ensemble calibration for RI?

# Related Pages

- [Rapid Intensification](rapid-intensification.md)
- [Tropical Cyclone Intensification](tropical-cyclone-intensification.md)
- [Tropical Cyclone Numerical Modeling](tropical-cyclone-numerical-modeling.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
- [Predictability of Tropical Cyclone Intensity: Scale-Dependent Forecast Error Growth in High-Resolution Stochastic Kinetic-Energy Backscatter Ensembles](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md)
- [Predictability and Dynamics of Tropical Cyclone Rapid Intensification Deduced from High-Resolution Stochastic Ensembles](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md)
- [Marathon vs. Sprint: Two Modes of Tropical Cyclone Rapid Intensification in a Global Convection-Permitting Simulation](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md)
- [High-Resolution Ensemble HFV3 Forecasts of Hurricane Michael (2018): Rapid Intensification in Shear](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md)
