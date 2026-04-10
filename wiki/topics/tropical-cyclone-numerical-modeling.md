---
title: "Tropical Cyclone Numerical Modeling"
page_type: "topic"
status: "active"
last_updated: "2026-04-10"
source_count: 11
---

# Definition

Tropical cyclone numerical modeling here refers to dynamical prediction systems and experiment frameworks used to simulate hurricane track, intensity, structure, waves, surge, and related transport processes, including fully coupled atmosphere-wave-ocean systems, stochastic predictability ensembles, global-nest FV3/HAFS-class systems, and global convection-permitting simulations used for process diagnosis.

# Current Synthesis

[Chen and Curcic (2016)](../papers/chen-curcic-2016-ocean-surface-waves-ike-sandy.md), [Curcic et al. (2016)](../papers/curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md), [Dietrich et al. (2018)](../papers/dietrich-et-al-2018-sensitivity-storm-surge-predictions-isaac.md), [Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md), and [Dobbelaere et al. (2022)](../papers/dobbelaere-curcic-lehenaff-hanert-2022-wave-induced-ocean-transport-irma.md) add a coupled atmosphere-wave-ocean/coastal-modeling branch. Across this chain, the wiki now has evidence that wave spectra, Stokes drift, surge forcing, and forecast uncertainty all change materially when the atmosphere, waves, currents, and coastal circulation are solved as a coupled system rather than as loosely connected post-processing steps.

[Chen and Curcic (2016)](../papers/chen-curcic-2016-ocean-surface-waves-ike-sandy.md) establish that a fully coupled system can predict open-ocean and near-landfall hurricane wave structure several days in advance, while also showing that coastal transformation makes the landfall problem more complex than the open-ocean one. [Curcic et al. (2016)](../papers/curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md) then show that this same coupled framework captures transport-relevant Stokes-drift effects seen by GLAD drifters in Isaac. [Dietrich et al. (2018)](../papers/dietrich-et-al-2018-sensitivity-storm-surge-predictions-isaac.md) extend the branch into surge prediction, where the key modeling issue becomes forcing fidelity. [Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md) extend it further into uncertainty quantification, separating internal-vortex sensitivity from stochastic environmental forcing. [Dobbelaere et al. (2022)](../papers/dobbelaere-curcic-lehenaff-hanert-2022-wave-induced-ocean-transport-irma.md) show that unstructured coupled wave-current systems can materially alter coastal transport pathways during Irma.

[Judt et al. (2016)](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md) and [Judt and Chen (2016)](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md) add a stochastic-ensemble branch using Hurricane Earl (2010). Together they show that high-resolution ensembles can separate fast convective error growth from slower mean-vortex uncertainty and can diagnose why RI onset timing remains hard to predict even when eventual major intensification is common across members.

[Judt et al. (2023)](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md) extend the modeling branch into a global convection-permitting framework, arguing that RI can proceed through both a symmetric "marathon" mode and an asymmetric burst-driven "sprint" mode. This is useful here because it turns part of the forecast problem into a mode-identification problem rather than just a resolution problem.

The Andrew-Hazelton-led three-paper chain adds the wiki's operational-development branch. [Hazelton et al. (2018)](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md) establishes a developmental FV3 high-resolution baseline in the 2017 Atlantic season, showing that track guidance can be competitive while intensity and size biases remain challenging, especially in RI and recurvature regimes. [Hazelton et al. (2020)](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md) then provides a process-level ensemble analysis for Hurricane Michael (2018), showing that lower vortex tilt and better upshear humidification separate stronger RI members from weaker members even when bulk shear is similar. [Hazelton et al. (2021)](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md) extends from case-centric research toward broader system verification by evaluating a global-nested HAFS prototype across the 2019 Atlantic season.

Inference for this wiki: these studies collectively support treating forecast-skill gains as architecture + physics + coupling + initialization + storm-structure + regime-identification problems, not just horizontal resolution upgrades.

# Evidence By Source

- [Chen and Curcic (2016)](../papers/chen-curcic-2016-ocean-surface-waves-ike-sandy.md) show that fully coupled atmosphere-wave-ocean modeling can reproduce observed hurricane wave structure in both open-ocean and near-landfall settings while also exposing where simple wave parameterizations break down.
- [Curcic et al. (2016)](../papers/curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md) show that coupled wave-aware simulations are needed to reproduce the near-surface transport actually measured by drifters in Isaac.
- [Dietrich et al. (2018)](../papers/dietrich-et-al-2018-sensitivity-storm-surge-predictions-isaac.md) show that surge forecasts during Isaac were sensitive to atmospheric-forcing construction and improved when a full-physics coupled model supplied the forcing.
- [Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md) show that surrogate-based uncertainty analysis can separate which initial-vortex parameters most affect RI likelihood inside a coupled forecast system.
- [Dobbelaere et al. (2022)](../papers/dobbelaere-curcic-lehenaff-hanert-2022-wave-induced-ocean-transport-irma.md) show that unstructured wave-current coupling materially alters modeled currents and transport pathways in a hurricane-struck coastal reef system.
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
- Which coastal-hazard forecast errors disappear only when explicit wave-current coupling and Stokes-drift effects are carried through the model system?

# Related Pages

- [Tropical Cyclone Intensification](tropical-cyclone-intensification.md)
- [Tropical Cyclone Predictability](tropical-cyclone-predictability.md)
- [Tropical Cyclone Wave Coupling](tropical-cyclone-wave-coupling.md)
- [Rapid Intensification](rapid-intensification.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
- [Ocean surface waves in Hurricane Ike (2008) and Superstorm Sandy (2012): Coupled model predictions and observations](../papers/chen-curcic-2016-ocean-surface-waves-ike-sandy.md)
- [Hurricane-induced ocean waves and stokes drift and their impacts on surface transport and dispersion in the Gulf of Mexico](../papers/curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md)
- [Sensitivity of Storm Surge Predictions to Atmospheric Forcing during Hurricane Isaac](../papers/dietrich-et-al-2018-sensitivity-storm-surge-predictions-isaac.md)
- [Uncertainty Propagation in Coupled Atmosphere-Wave-Ocean Prediction System: A Study of Hurricane Earl (2010)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md)
- [Impacts of Hurricane Irma (2017) on wave-induced ocean transport processes](../papers/dobbelaere-curcic-lehenaff-hanert-2022-wave-induced-ocean-transport-irma.md)
- [Predictability of Tropical Cyclone Intensity: Scale-Dependent Forecast Error Growth in High-Resolution Stochastic Kinetic-Energy Backscatter Ensembles](../papers/judt-chen-berner-2016-intensity-predictability-scale-dependent-error-growth.md)
- [Predictability and Dynamics of Tropical Cyclone Rapid Intensification Deduced from High-Resolution Stochastic Ensembles](../papers/judt-chen-2016-ri-predictability-stochastic-ensembles.md)
- [Marathon vs. Sprint: Two Modes of Tropical Cyclone Rapid Intensification in a Global Convection-Permitting Simulation](../papers/judt-rios-berrios-bryan-2023-marathon-vs-sprint-ri-modes.md)
- [2017 Atlantic Hurricane Forecasts from a High-Resolution Version of the GFDL fvGFS Model: Evaluation of Track, Intensity, and Structure](../papers/hazelton-et-al-2018-2017-atlantic-hurricane-forecasts-high-resolution-fvgfs.md)
- [High-Resolution Ensemble HFV3 Forecasts of Hurricane Michael (2018): Rapid Intensification in Shear](../papers/hazelton-et-al-2020-high-resolution-ensemble-hfv3-hurricane-michael-ri-shear.md)
- [2019 Atlantic Hurricane Forecasts from the Global-Nested Hurricane Analysis and Forecast System: Composite Statistics and Key Events](../papers/hazelton-et-al-2021-2019-atlantic-hurricane-forecasts-global-nested-hafs.md)
