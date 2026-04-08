---
title: "Tropical Cyclone Numerical Modeling"
page_type: "topic"
status: "active"
last_updated: "2026-04-08"
source_count: 3
---

# Definition

Tropical cyclone numerical modeling here refers to dynamical prediction systems and experiment frameworks used to simulate hurricane track, intensity, and structure, including global-nest FV3/HAFS-class systems and high-resolution ensembles used for process diagnosis.

# Current Synthesis

A new Andrew-Hazelton-led three-paper chain adds a first dedicated numerical-modeling track to this wiki. [Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md) establishes a developmental FV3 high-resolution baseline in the 2017 Atlantic season, showing that track guidance can be competitive while intensity and size biases remain challenging, especially in RI and recurvature regimes.

[Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md) then provides a process-level ensemble analysis for Hurricane Michael (2018), showing that lower vortex tilt and better upshear humidification separate stronger RI members from weaker members even when bulk shear is similar. This offers a modeling bridge between environmental forcing and inner-core structural control.

[Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) extends from case-centric research toward broader system verification by evaluating a global-nested HAFS prototype across the 2019 Atlantic season. The paper indicates progress in track/intensity skill while preserving the caution that RI timing and transition regimes remain difficult.

Inference for this wiki: these studies collectively support treating forecast-skill gains as architecture + physics + initialization + storm-structure problems, not just horizontal resolution upgrades.

# Evidence By Source

- [Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md) show that a high-resolution FV3 nest can deliver useful seasonal track/intensity performance and realistic structure evolution in many cases.
- The same paper reports that wind radii tended to be too large and that RI periods still produced major negative intensity errors in some storms.
- [Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md) show in a sheared RI case that vortex tilt and moistening pathways discriminate strong and weak ensemble outcomes better than bulk-shear magnitude alone.
- [Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) provide system-level seasonal verification for a global-nested HAFS prototype and document improvement signals plus remaining RI/transition failure modes.

# Open Questions

- Which model ingredients most reduce RI timing error: inner-core initialization, moist physics, ocean coupling, or vortex-scale data assimilation?
- How stable are these FV3/HAFS lessons across basins, slower storms, and land-interaction regimes?
- Can structural predictors like tilt and upshear moistening be operationalized to diagnose when model RI forecasts are physically credible?

# Related Pages

- [Tropical Cyclone Intensification](tropical-cyclone-intensification.md)
- [Rapid Intensification](rapid-intensification.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
- [2017 Atlantic Hurricane Forecasts from a High-Resolution Version of the GFDL fvGFS Model: Evaluation of Track, Intensity, and Structure](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md)
- [High-Resolution Ensemble HFV3 Forecasts of Hurricane Michael (2018): Rapid Intensification in Shear](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md)
- [2019 Atlantic Hurricane Forecasts from the Global-Nested Hurricane Analysis and Forecast System: Composite Statistics and Key Events](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md)
