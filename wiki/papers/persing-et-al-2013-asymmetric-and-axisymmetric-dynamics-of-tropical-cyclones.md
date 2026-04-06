---
title: "Asymmetric and Axisymmetric Dynamics of Tropical Cyclones"
page_type: "paper"
status: "active"
last_updated: "2026-04-06"
source_count: 1
---

# Citation

Persing, J., M. T. Montgomery, J. C. McWilliams, and R. K. Smith, 2013: *Asymmetric and axisymmetric dynamics of tropical cyclones*. *Atmospheric Chemistry and Physics*, 13, 12299-12341. DOI: [10.5194/acp-13-12299-2013](https://doi.org/10.5194/acp-13-12299-2013).

Accessed text source: [ACP article page](https://acp.copernicus.org/articles/13/12299/2013/) and [ACP PDF](https://acp.copernicus.org/articles/13/12299/2013/acp-13-12299-2013.pdf).

Peer-review status: Peer-reviewed primary research article.

# Research Question

Persing et al. (2013) ask how tropical cyclone evolution differs between fully three-dimensional and strictly axisymmetric model configurations for the prototype intensification problem, and what those differences imply for spin-up, convective organization, eddy momentum transport, and mature intensity theory.

# Data And Methods

- Study type: Idealized numerical modeling study comparing matched three-dimensional and axisymmetric simulations.
- Model framework: CM1 version 14 run in 3-D and axisymmetric configurations.
- Spatial scope: Prototype tropical cyclone intensification problem on an f plane at 20 degrees N over a warm ocean; not basin-specific.
- Initial state: Initially cloud-free, unsaturated, axisymmetric baroclinic vortex in gradient-wind balance with zero initial radial and vertical velocity and maximum initial tangential wind of 13 m s-1 at the surface near 100 km radius.
- Environmental and physical setup: Nearly moist-neutral sounding, sea-surface temperature of 299.3 K, simple Newtonian cooling, no ice microphysics, and no dissipative heating.
- Numerical configuration: The control comparison uses a 3-D simulation with 3 km interior horizontal grid spacing and 40 vertical levels to 25 km, together with an axisymmetric simulation with 3 km radial spacing. Both use the same subgrid turbulence formulation with prescribed mixing lengths of 700 m horizontally and 50 m vertically.
- Surface-exchange setup: Control enthalpy exchange coefficient Ck = 1.29 x 10-3 and drag coefficient CD = 2.58 x 10-3, with additional experiments varying drag.
- Diagnostics analyzed: Azimuthally averaged wind fields, heating, spin-up function, tangential-momentum budgets, resolved and subgrid eddy momentum fluxes, gradient Richardson number, maximum tangential wind, and radius of maximum wind.
- Ensemble sensitivity: The paper includes additional perturbed realizations and drag-coefficient sensitivity experiments to sample stochastic convective variability and test robustness of the 3-D versus axisymmetric contrast.

# Findings

- Persing et al. (2013) find that the mature vortex in the 3-D control simulation is weaker than in the corresponding axisymmetric simulation, consistent with earlier work, but they argue this difference should not be interpreted simply as downgradient mixing by asymmetries.
- The paper shows that during key spin-up periods the resolved 3-D eddy momentum fluxes above the boundary layer are counter-gradient rather than purely diffusive. These eddies support contraction and intensification of the maximum tangential winds.
- The authors attribute much of the 3-D versus axisymmetric contrast to differences in convective organization. In the 3-D simulation, differential angular rotation strains convection tangentially and delays organization into annular rings, so azimuthally averaged heating and its radial gradient are weaker than in the axisymmetric model for much of the spin-up period.
- Even so, the 3-D vortex can temporarily intensify faster than the axisymmetric vortex. During those episodes, local convection in the 3-D model becomes more intense and quasi ring-like, and the associated vertical eddy momentum flux contributes significantly to azimuthal-mean spin-up.
- The paper argues that vortical plume structures assist intensification by helping contract the radius of maximum wind and extend tangential winds upward through the troposphere.
- The authors find that resolved eddy momentum-flux structure above the boundary layer differs substantially from the subgrid parameterizations used in both the 3-D and axisymmetric models, implying that strict down-gradient closures are not an adequate representation of the asymmetric eddies diagnosed here.
- Tangential-momentum-budget analysis shows that the spin-up of the azimuthally averaged maximum tangential wind occurs within the frictional boundary layer in both model configurations.
- In the 3-D model, surface drag plays an important dynamical role by helping organize convection in azimuth. The paper shows a radical difference between 3-D and axisymmetric drag sensitivity when the drag coefficient is reduced or increased from realistic control values.
- The paper does not support a then-recent hypothesis that small-scale vertical mixing in the upper-tropospheric outflow is the controlling mechanism for intensification in this prototype problem.
- More broadly, Persing et al. (2013) conclude that representing convection as concentric rings and assuming down-gradient eddy momentum fluxes are both important limitations of strict axisymmetric theory and modeling.

# Limitations

- The study is an idealized model comparison, not an observational analysis or real-storm hindcast.
- The prototype problem omits several processes important in nature, including environmental shear, storm translation, negative ocean feedback from cold-wake formation, and detailed cloud-radiative feedbacks.
- The experiments use prescribed subgrid turbulence closures, constant control exchange coefficients, simple warm-rain microphysics, and no ice microphysics, so some sensitivities remain model-dependent.
- The 3-D simulation uses 3 km inner-grid spacing, which permits asymmetric convection but does not resolve all turbulent and cloud-microphysical scales explicitly.
- Inference for this wiki: the paper gives strong primary support for the importance of 3-D convective organization and eddy fluxes in the prototype problem, but it does not by itself establish how these mechanisms behave in fully realistic, sheared, or coupled tropical cyclones.

# Referenced Papers

This is a curated ingest queue, not a dump of the full bibliography. It lists the cited papers that are currently most useful for expanding the existing wiki pages. As these papers are ingested, replace the plain citations below with direct links to their wiki paper pages.

- `Prototype problem precursor:` Nguyen, V. S., R. K. Smith, and M. T. Montgomery, 2008: *Tropical-cyclone intensification and predictability in three dimensions*. *Quarterly Journal of the Royal Meteorological Society*, 134, 563-582.
- `3-D axisymmetric precursor:` Smith, R. K., M. T. Montgomery, and S. V. Nguyen, 2008: *Axisymmetric dynamics of tropical cyclone intensification in a three-dimensional model*. *Quarterly Journal of the Royal Meteorological Society*, 134, 337-351.
- `Spin-up mechanism:` Smith, R. K., M. T. Montgomery, and S. V. Nguyen, 2009: *Tropical cyclone spin-up revisited*. *Quarterly Journal of the Royal Meteorological Society*, 135, 1321-1335.
- `WISHE test:` Montgomery, M. T., S. V. Nguyen, J. Persing, and R. K. Smith, 2009: *Do tropical cyclones intensify by WISHE?* *Quarterly Journal of the Royal Meteorological Society*, 135, 1697-1714.
- `Drag sensitivity:` Montgomery, M. T., R. K. Smith, and S. V. Nguyen, 2010: *Sensitivity of tropical cyclone models to the surface drag coefficient*. *Quarterly Journal of the Royal Meteorological Society*, 136, 1945-1953.
- `Potential-intensity contrast:` Yang, B., Y. Wang, and B. Wang, 2007: *The effects of internally generated asymmetries on tropical cyclone potential intensity*. *Journal of the Atmospheric Sciences*, 64, 1165-1188.

# Linked Pages

- [Tropical Cyclone Intensification](../topics/tropical-cyclone-intensification.md)
- [Rotating Convection Paradigm](../topics/rotating-convection-paradigm.md)
- [Boundary-Layer Control](../topics/boundary-layer-control.md)
- [Potential Intensity](../topics/potential-intensity.md)
- [Prototype Intensification Problem](../methods/prototype-intensification-problem.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
