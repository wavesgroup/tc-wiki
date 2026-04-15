---
title: "Reduced Drag Coefficient for High Wind Speeds in Tropical Cyclones"
page_type: "paper"
status: "active"
last_updated: "2026-04-15"
source_count: 2
---

# Citation

Powell, M. D., P. J. Vickery, and T. A. Reinhold, 2003: *Reduced drag coefficient for high wind speeds in tropical cyclones*. *Nature*, 422, 279-283. DOI: [10.1038/nature01481](https://doi.org/10.1038/nature01481).

Accessed text sources: [DocsLib mirror of the full article](https://docslib.org/doc/4367979/reduced-drag-coefficient-for-high-wind-speeds-in-tropical-cyclones) and [DOI landing page](https://doi.org/10.1038/nature01481).

Peer-review status: Peer-reviewed primary research article.

# Research Question

Powell et al. (2003) ask how the air-sea momentum drag coefficient behaves at very high tropical-cyclone wind speeds, where many operational parameterizations had previously assumed monotonic drag increase.

# Data And Methods

- Study type: Observational analysis in tropical-cyclone conditions.
- Core data stream: Hurricane wind-profile observations using aircraft-based measurements and dropwindsonde-era datasets reported for high-wind marine boundary-layer conditions.
- Primary diagnostic: Neutral drag coefficient behavior as a function of near-surface wind speed.

# Key Equations

Powell et al. (2003) diagnose high-wind drag from the near-surface logarithmic wind profile

```math
U = \frac{U_*}{\kappa}\ln\left(\frac{Z}{Z_0}\right),
```

where $U$ is mean wind speed at height $Z$, $U_*$ is friction velocity, $\kappa \approx 0.4$ is the von Karman constant, and $Z_0$ is aerodynamic roughness length.

They then relate friction velocity, stress, and neutral 10-m drag with

```math
\tau = \rho U_*^2 = \rho C_D U_{10}^2,
```

which is the paper's key bridge from GPS-sonde wind profiles to the drag coefficient $C_D$.

The roughness closure used in the paper is the Charnock relation

```math
Z_0 = \alpha \frac{U_*^2}{g},
```

with $\alpha$ a roughness constant and $g$ gravity. Together, these equations define the retrieval chain behind the paper's central result that momentum flux levels off instead of increasing indefinitely at hurricane-force winds.

# Findings

- The paper reports that drag-coefficient behavior in extreme winds is lower than expected from simple monotonic extrapolation of moderate-wind bulk formulas.
- The result introduced a high-impact constraint on hurricane air-sea momentum exchange: drag increase with wind speed is not indefinite.
- This finding became a key benchmark for later laboratory, wave-state-aware, and reanalysis studies of high-wind surface exchange.

# Limitations

- The drag retrieval depends on neutral-stability and log-layer assumptions applied to storm-inner-core GPS-sonde profiles.
- High-wind observational sampling in tropical cyclones is sparse and condition-dependent, which complicates universal parameterization.
- The paper focuses on momentum exchange; enthalpy-flux implications require separate evidence.

# Referenced Papers

This is a curated ingest queue, not a full bibliography.

- `High-wind roughness laboratory follow-up:` [On the Limiting Aerodynamic Roughness of the Ocean in Very Strong Winds](donelan-et-al-2004-limiting-aerodynamic-roughness-ocean-very-strong-winds.md).
- `Wave-state and extreme-sea context:` [Wind and Waves in Extreme Hurricanes](holthuijsen-powell-pietrzak-2012-wind-and-waves-in-extreme-hurricanes.md).
- `Correction and updated drag threshold:` [Revised Estimates of Ocean Surface Drag in Strong Winds](curcic-haus-2020-revised-estimates-ocean-surface-drag-strong-winds.md).

# Linked Pages

- [Boundary-Layer Control](../topics/boundary-layer-control.md)
- [Potential Intensity](../topics/potential-intensity.md)
- [Tropical Cyclone Intensification](../topics/tropical-cyclone-intensification.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
