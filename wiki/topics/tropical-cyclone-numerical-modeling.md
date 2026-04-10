---
title: "Tropical Cyclone Numerical Modeling"
page_type: "topic"
status: "active"
last_updated: "2026-04-10"
source_count: 6
---

# Definition

Tropical cyclone numerical modeling here refers to dynamical prediction systems and experiment frameworks used to simulate hurricane track, intensity, and structure, including stochastic predictability ensembles, global-nest FV3/HAFS-class systems, and global convection-permitting simulations used for process diagnosis.

# Current Synthesis

[Judt et al. (2016)](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md) and [Judt and Chen (2016)](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md) add a stochastic-ensemble branch using Hurricane Earl (2010). Together they show that high-resolution ensembles can separate fast convective error growth from slower mean-vortex uncertainty and can diagnose why RI onset timing remains hard to predict even when eventual major intensification is common across members.

[Judt et al. (2023)](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md) extend the modeling branch into a global convection-permitting framework, arguing that RI can proceed through both a symmetric "marathon" mode and an asymmetric burst-driven "sprint" mode. This is useful here because it turns part of the forecast problem into a mode-identification problem rather than just a resolution problem.

The Andrew-Hazelton-led three-paper chain adds the wiki's operational-development branch. [Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md) establishes a developmental FV3 high-resolution baseline in the 2017 Atlantic season, showing that track guidance can be competitive while intensity and size biases remain challenging, especially in RI and recurvature regimes. [Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md) then provides a process-level ensemble analysis for Hurricane Michael (2018), showing that lower vortex tilt and better upshear humidification separate stronger RI members from weaker members even when bulk shear is similar. [Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) extends from case-centric research toward broader system verification by evaluating a global-nested HAFS prototype across the 2019 Atlantic season.

Inference for this wiki: these studies collectively support treating forecast-skill gains as architecture + physics + initialization + storm-structure + regime-identification problems, not just horizontal resolution upgrades.

# Evidence By Source

- [Judt et al. (2016)](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md) show that the mean vortex and dominant asymmetry can remain predictable much longer than convective details in high-resolution Hurricane Earl ensembles.
- [Judt and Chen (2016)](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md) show that RI timing uncertainty persists even in a forecast set where most members still become major hurricanes.
- [Judt et al. (2023)](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md) argue from a global convection-permitting simulation that RI can occur through distinct structural modes with different environmental and vortex signatures.
- [Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md) show that a high-resolution FV3 nest can deliver useful seasonal track/intensity performance and realistic structure evolution in many cases.
- The same paper reports that wind radii tended to be too large and that RI periods still produced major negative intensity errors in some storms.
- [Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md) show in a sheared RI case that vortex tilt and moistening pathways discriminate strong and weak ensemble outcomes better than bulk-shear magnitude alone.
- [Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) provide system-level seasonal verification for a global-nested HAFS prototype and document improvement signals plus remaining RI/transition failure modes.

# Open Questions

- Which model ingredients most reduce RI timing error: inner-core initialization, moist physics, ocean coupling, stochastic perturbations, or vortex-scale data assimilation?
- How stable are these FV3/HAFS lessons across basins, slower storms, and land-interaction regimes?
- Can structural predictors like tilt, upshear moistening, and RI mode classification be operationalized to diagnose when model RI forecasts are physically credible?

# Related Pages

- [Tropical Cyclone Intensification](tropical-cyclone-intensification.md)
- [Tropical Cyclone Predictability](tropical-cyclone-predictability.md)
- [Rapid Intensification](rapid-intensification.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
- [Predictability of Tropical Cyclone Intensity: Scale-Dependent Forecast Error Growth in High-Resolution Stochastic Kinetic-Energy Backscatter Ensembles](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md)
- [Predictability and Dynamics of Tropical Cyclone Rapid Intensification Deduced from High-Resolution Stochastic Ensembles](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md)
- [Marathon vs. Sprint: Two Modes of Tropical Cyclone Rapid Intensification in a Global Convection-Permitting Simulation](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md)
- [2017 Atlantic Hurricane Forecasts from a High-Resolution Version of the GFDL fvGFS Model: Evaluation of Track, Intensity, and Structure](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md)
- [High-Resolution Ensemble HFV3 Forecasts of Hurricane Michael (2018): Rapid Intensification in Shear](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md)
- [2019 Atlantic Hurricane Forecasts from the Global-Nested Hurricane Analysis and Forecast System: Composite Statistics and Key Events](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md)
