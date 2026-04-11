---
title: "Tropical Cyclone Wave Coupling"
page_type: "topic"
status: "active"
last_updated: "2026-04-10"
source_count: 9
---

# Definition

Tropical cyclone wave coupling refers here to the two-way interaction between storm winds, surface waves, currents, surge, and wave-driven transport processes, especially where Stokes drift, radiation-stress gradients, coastal transformation, and wind-wave misalignment materially affect hazards or model behavior.

# Current Synthesis

The wiki now has a coherent wave-coupling branch that links older directional-spectrum observations to newer coupled-model transport and surge studies. [Wright et al. (2001)](../papers/wright-et-al-2001-hurricane-directional-wave-spectrum-open-ocean.md), [Walsh et al. (2002)](../papers/walsh-et-al-2002-hurricane-directional-wave-spectrum-landfall.md), and [Walsh et al. (2021)](../papers/walsh-fairall-popstefanija-2021-in-the-eye-of-the-storm.md) establish the observational base: hurricane wave fields are strongly asymmetric, directionally structured, and increasingly measurable in storm-relative coordinates. [Black et al. (2007)](../papers/black-et-al-2007-air-sea-exchange-cblast.md) bridge that base to a fully coupled field-program context by combining aircraft-measured directional spectra with drifters and floats deployed ahead of Fabian and Frances, including observed significant waves near 11 m during Frances.

[Chen and Curcic (2016)](../papers/chen-curcic-2016-ocean-surface-waves-ike-sandy.md) extend that base with a fully coupled-model view of two landfalling storms. Their Ike and Sandy results show that near-landfall wave spectra become broader and more complex than open-ocean spectra because shoaling, dissipation, refraction, and opposing swell reshape both wave geometry and the effective surface-stress environment. Inference for this wiki: wave coupling near landfall is not a minor post-processing detail; it changes the surface boundary condition the atmosphere and coastal ocean actually feel.

[Curcic et al. (2016)](../papers/curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md) and [Dobbelaere et al. (2022)](../papers/dobbelaere-curcic-lehenaff-hanert-2022-wave-induced-ocean-transport-irma.md) show that wave-driven transport effects are large enough to matter directly for hazard applications. In Isaac, Stokes drift contributed about one-fifth of the average near-surface Lagrangian velocity and substantially enhanced lateral dispersion. In Irma, radiation-stress gradients and especially Stokes drift produced kilometer-scale trajectory differences for coastal drifters and debris analogs, with the Stokes-drift effect dominating wave-induced transport.

[Dietrich et al. (2018)](../papers/dietrich-et-al-2018-sensitivity-storm-surge-predictions-isaac.md) and [Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md) add the forecast-system and uncertainty dimension. Dietrich et al. show that surge forecasts in Isaac were sensitive to whether the coastal model was forced by a parametric vortex or by a full-physics coupled atmosphere-wave-ocean model. Li et al. show that, in a coupled Earl forecast system, internal-vortex uncertainty strongly affects intensity and RI likelihood while stochastic environmental forcing dominates track spread. Together these studies imply that coupled wave-aware forecast systems matter both because of the physics they carry and because they redistribute forecast uncertainty across different storm outcomes.

# Evidence By Source

- [Wright et al. (2001)](../papers/wright-et-al-2001-hurricane-directional-wave-spectrum-open-ocean.md) provide the early observational benchmark that hurricane directional spectra vary strongly with storm-relative position in the open ocean.
- [Walsh et al. (2002)](../papers/walsh-et-al-2002-hurricane-directional-wave-spectrum-landfall.md) extend that benchmark into the landfall regime, where fetch and coastal proximity further complicate wave geometry.
- [Walsh et al. (2021)](../papers/walsh-fairall-popstefanija-2021-in-the-eye-of-the-storm.md) show that NOAA WSRA can map these directional-spectrum asymmetries densely enough for modern reconnaissance use.
- [Black et al. (2007)](../papers/black-et-al-2007-air-sea-exchange-cblast.md) show that CBLAST paired directional wave observations with simultaneous upper-ocean and atmospheric measurements, including 11-m significant waves in Frances.
- [Chen and Curcic (2016)](../papers/chen-curcic-2016-ocean-surface-waves-ike-sandy.md) show that shallow-water transformation broadens hurricane wave spectra near landfall and that wind-wave misalignment plus opposing swell can increase modeled drag materially.
- [Curcic et al. (2016)](../papers/curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md) show that hurricane-induced Stokes drift contributes about 20% of the near-surface Lagrangian velocity in Isaac and helps produce much larger relative diffusivity than under prestorm conditions.
- [Dietrich et al. (2018)](../papers/dietrich-et-al-2018-sensitivity-storm-surge-predictions-isaac.md) show that surge guidance in Isaac depends strongly on atmospheric-forcing choice, with full-physics coupled forcing outperforming advisory-driven parametric forcing in that case.
- [Li et al. (2019)](../papers/li-et-al-2019-uncertainty-propagation-coupled-atmosphere-wave-ocean-earl.md) show that coupled forecast uncertainty can be partitioned into internal-vortex and stochastic-environmental contributions, with RI sensitivity and track sensitivity responding to different perturbation classes.
- [Dobbelaere et al. (2022)](../papers/dobbelaere-curcic-lehenaff-hanert-2022-wave-induced-ocean-transport-irma.md) show that coastal wave-current coupling during Irma changed currents by up to about 1 m s^-1 and caused kilometer-scale differences in transported material.

# Open Questions

- Which parts of hurricane surge and debris-transport error come mainly from atmospheric forcing, which from wave-current coupling, and which from coastal bathymetric/topographic uncertainty?
- How should operational systems represent Stokes drift and wave radiation stress when computational constraints still favor simpler forcing pipelines?
- How general are the large transport impacts seen in Isaac and Irma across basins, shelf geometries, and fast-moving storms?
- Can directional-spectrum observations now dense enough for reconnaissance be assimilated directly into coupled hurricane forecast systems?

# Related Pages

- [Air-Sea Interaction](air-sea-interaction.md)
- [Boundary-Layer Control](boundary-layer-control.md)
- [Tropical Cyclone Numerical Modeling](tropical-cyclone-numerical-modeling.md)
- [Tropical Cyclone Predictability](tropical-cyclone-predictability.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
