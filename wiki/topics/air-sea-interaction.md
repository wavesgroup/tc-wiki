---
title: "Air-Sea Interaction"
page_type: "topic"
status: "active"
last_updated: "2026-04-10"
source_count: 14
---

# Definition

Air-sea interaction in tropical cyclones is the two-way coupling between the storm and ocean surface layer: atmospheric winds and fluxes force ocean mixing/cooling, while evolving SST, mixed-layer structure, and wave state feed back on momentum and enthalpy fluxes that control intensity change.

# Current Synthesis

The wiki's new cold-wake ingest adds a focused feedback chain spanning process theory, coupled modeling, and observations. [Price (1981)](../papers/price-1981-upper-ocean-response-to-a-hurricane.md) provides the mechanistic base: hurricane forcing can rapidly cool the upper ocean via mixing/entrainment with pronounced storm-relative asymmetry. [Schade and Emanuel (1999)](../papers/schade-emanuel-1999-oceans-effect-on-intensity.md) and [Chan et al. (2001)](../papers/chan-duan-shay-2001-intensity-change-simple-coupled-model.md) show that this cooling can weaken subsequent intensification in coupled frameworks, especially when ocean stratification and translation speed favor strong wake formation.

[Bender and Ginis (2000)](../papers/bender-ginis-2000-real-case-hurricane-ocean-interaction.md) extend this into real-case forecasting, showing that explicit coupling and cold-wake representation can reduce intensity forecast error when uncoupled models over-intensify storms traversing cooled water. [Cione and Uhlhorn (2003)](../papers/cione-uhlhorn-2003-sst-variability-hurricanes.md) add observational context that storm-relative SST structure is heterogeneous enough to matter for intensity-change interpretation.

This cold-wake branch complements the existing high-wind exchange branch from [Powell et al. (2003)](../papers/powell-vickery-reinhold-2003-reduced-drag-coefficient-high-wind-speeds.md), [Donelan et al. (2004)](../papers/donelan-et-al-2004-limiting-aerodynamic-roughness-ocean-very-strong-winds.md), [Holthuijsen et al. (2012)](../papers/holthuijsen-powell-pietrzak-2012-wind-and-waves-in-extreme-hurricanes.md), and [Curcic and Haus (2020)](../papers/curcic-haus-2020-revised-estimates-ocean-surface-drag-strong-winds.md), which constrain how momentum exchange behaves at extreme wind speeds. Together, the two branches imply that intensity prediction errors can arise both from under-resolved ocean cooling and from imperfect strong-wind flux parameterizations.

The new ingest extends this page into explicit wave-current-surge coupling. [Curcic et al. (2016)](../papers/curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md) show from Hurricane Isaac drifters and a coupled model that hurricane-induced Stokes drift can account for about one-fifth of the near-surface Lagrangian flow and sharply increase lateral dispersion. [Chen and Curcic (2016)](../papers/chen-curcic-2016-ocean-surface-waves-ike-sandy.md) then show in Ike and Sandy that shoaling, refraction, and opposing swell broaden landfall wave spectra and materially alter the wind-wave stress environment. [Dietrich et al. (2018)](../papers/dietrich-et-al-2018-sensitivity-storm-surge-predictions-isaac.md) show that coastal surge forecasts during Isaac were sensitive to atmospheric-forcing choice and improved when a full-physics coupled atmosphere-wave-ocean model supplied that forcing. [Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md) add a predictability result within a coupled system: RI sensitivity and track sensitivity do not respond to the same uncertainty sources. [Dobbelaere et al. (2022)](../papers/dobbelaere-curcic-lehenaff-hanert-2022-wave-induced-ocean-transport-irma.md) extend the branch into Florida Reef Tract transport during Irma, showing that wave radiation stress and especially Stokes drift can change coastal trajectories by kilometers to tens of kilometers. Inference for this wiki: air-sea interaction in hurricanes should not be treated only as SST feedback plus bulk flux coefficients; wave-mediated transport and coastal response are part of the coupled problem.

# Evidence By Source

- [Price (1981)](../papers/price-1981-upper-ocean-response-to-a-hurricane.md) established core upper-ocean cold-wake mechanisms beneath moving hurricanes.
- [Schade and Emanuel (1999)](../papers/schade-emanuel-1999-oceans-effect-on-intensity.md) demonstrated that coupling-induced cooling can materially reduce simulated intensity.
- [Chan et al. (2001)](../papers/chan-duan-shay-2001-intensity-change-simple-coupled-model.md) showed that reduced-order coupled models can still capture first-order intensity damping from SST cooling.
- [Bender and Ginis (2000)](../papers/bender-ginis-2000-real-case-hurricane-ocean-interaction.md) reported real-case forecast improvement when coupled cold-wake effects were represented.
- [Cione and Uhlhorn (2003)](../papers/cione-uhlhorn-2003-sst-variability-hurricanes.md) documented hurricane-environment SST variability relevant to short-term intensity tendencies.
- [Powell et al. (2003)](../papers/powell-vickery-reinhold-2003-reduced-drag-coefficient-high-wind-speeds.md) and [Donelan et al. (2004)](../papers/donelan-et-al-2004-limiting-aerodynamic-roughness-ocean-very-strong-winds.md) indicate drag-saturation behavior at high wind speeds.
- [Holthuijsen et al. (2012)](../papers/holthuijsen-powell-pietrzak-2012-wind-and-waves-in-extreme-hurricanes.md) and [Curcic and Haus (2020)](../papers/curcic-haus-2020-revised-estimates-ocean-surface-drag-strong-winds.md) reinforce wave-state and processing sensitivity in strong-wind flux estimation.
- [Curcic et al. (2016)](../papers/curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md) show that Stokes drift materially alters hurricane-forced near-surface transport and dispersion.
- [Chen and Curcic (2016)](../papers/chen-curcic-2016-ocean-surface-waves-ike-sandy.md) show that near-landfall wave transformation can change directional spectra and increase modeled drag through wind-wave misalignment and shallow-water effects.
- [Dietrich et al. (2018)](../papers/dietrich-et-al-2018-sensitivity-storm-surge-predictions-isaac.md) show that coastal surge forecasts can improve when forced by a full-physics coupled atmosphere-wave-ocean model instead of simpler advisory-based forcing.
- [Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md) show that different uncertainty sources inside a coupled forecast system project differently onto RI likelihood and track spread.
- [Dobbelaere et al. (2022)](../papers/dobbelaere-curcic-lehenaff-hanert-2022-wave-induced-ocean-transport-irma.md) show that radiation-stress gradients and Stokes drift can materially alter coastal transport pathways during a major hurricane.

# Open Questions

- Which operational intensity models capture cold-wake penalties most robustly across basins and translation-speed regimes?
- How much forecast error is attributable to upper-ocean initial-condition error versus atmospheric structural error?
- How should operational systems jointly constrain drag saturation and enthalpy exchange in very strong winds?
- What storm-relative SST sampling strategy is most predictive of 6-24 h intensity change?
- When do wave-driven transport and surge errors become as important as cold-wake intensity penalties in coupled forecast systems?

# Related Pages

- [Tropical Cyclone Intensification](tropical-cyclone-intensification.md)
- [Tropical Cyclone Wave Coupling](tropical-cyclone-wave-coupling.md)
- [Potential Intensity](potential-intensity.md)
- [Boundary-Layer Control](boundary-layer-control.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
