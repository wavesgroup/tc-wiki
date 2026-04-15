---
title: "Air-Sea Enthalpy and Momentum Exchange at Major Hurricane Wind Speeds Observed During CBLAST"
page_type: "paper"
status: "active"
last_updated: "2026-04-15"
source_count: 2
---

# Citation

Bell, Michael M., Michael T. Montgomery, and Kerry A. Emanuel, 2012: *Air-Sea Enthalpy and Momentum Exchange at Major Hurricane Wind Speeds Observed During CBLAST*. *Journal of the Atmospheric Sciences*, 69(11), 3197-3222. DOI: [10.1175/JAS-D-11-0276.1](https://doi.org/10.1175/JAS-D-11-0276.1).

Accessed text sources: [DocsLib mirror of the full article](https://docslib.org/doc/4546383/air-sea-enthalpy-and-momentum-exchange-at-major-hurricane-wind-speeds-observed-during-cblast) and the [CoLab article record](https://colab.ws/articles/10.1175%2Fjas-d-11-0276.1).

Peer-review status: Peer-reviewed primary research article.

# Research Question

Bell et al. (2012) ask what the bulk momentum and enthalpy exchange coefficients are in the major-hurricane regime, where direct turbulent flux measurements are extremely difficult and existing theory is weakly constrained.

# Data And Methods

- Study type: Budget-based observational inference, not direct eddy-covariance flux measurement.
- Storm sample: Six missions from the 2003 CBLAST field program in major hurricanes Fabian and Isabel.
- Wind regime: Major-hurricane winds between about 52 and 72 m s^-1.
- Method: Deduce momentum and enthalpy fluxes from absolute angular momentum and total energy budgets using a variational technique, with explicit error analysis for unresolved budget terms and observational errors.

# Key Equations

Bell et al. (2012) center their analysis on the bulk exchange-coefficient ratio that enters potential-intensity arguments,

```math
\frac{C_K}{C_D},
```

where $C_D$ is the drag coefficient and $C_K$ is the enthalpy exchange coefficient.

Using the paper's reported mean retrievals for major-hurricane conditions gives the representative coefficient pair

```math
C_D \approx 2.4 \times 10^{-3},
\qquad
C_K \approx 1.0 \times 10^{-3},
```

for winds between about $52$ and $72~\mathrm{m\,s^{-1}}$.

A wiki restatement of the bulk formulas that the paper's angular-momentum and total-energy budgets are designed to constrain is

```math
|\tau| = \rho C_D U_{10}^2,
\qquad
F_K = \rho C_K U_{10}(k_0^* - k_{10}),
```

where $|\tau|$ is surface-stress magnitude, $F_K$ is enthalpy flux, and $k_0^* - k_{10}$ is the air-sea enthalpy disequilibrium. From the reported mean coefficients, the implied representative ratio is

```math
\frac{C_K}{C_D} \approx 0.42,
```

which is a wiki calculation from the paper's reported averages rather than a separately quoted Bell et al. equation.

# Findings

- Bell et al. (2012) report a near-surface mean drag coefficient CD of about 2.4 x 10^-3 with a 46% standard deviation for winds between 52 and 72 m s^-1.
- The paper reports a mean enthalpy coefficient CK of about 1.0 x 10^-3 with a 40% standard deviation over the same wind range.
- These are reported as the first known estimates of CK and CK/CD in major hurricanes.
- The authors find no significant change in the magnitude of the bulk exchange coefficients relative to minimal-hurricane conditions, and no significant increase in CK/CD above 50 m s^-1.
- Inference for this wiki: the major-hurricane branch of CBLAST does not support a simple picture in which CK/CD rises sharply with wind speed to solve hurricane-maintenance constraints.

# Limitations

- The coefficients are inferred indirectly from budget closures rather than measured directly with turbulence sensors at these wind speeds.
- The sample is limited to two storms and six missions, so uncertainty remains large.
- The reported standard deviations and explicit error analysis show that unresolved budget terms and observational error remain an important caveat.

# Referenced Papers

This is a curated ingest queue, not a full bibliography.

- `Program synthesis:` [Air-Sea Exchange in Hurricanes: Synthesis of Observations from the Coupled Boundary Layer Air-Sea Transfer Experiment](black-et-al-2007-air-sea-exchange-cblast.md).
- `Direct momentum-flux precursor:` [Turbulent Fluxes in the Hurricane Boundary Layer. Part I: Momentum Flux](french-drennan-zhang-black-2007-hurricane-boundary-layer-momentum-flux.md).
- `Direct latent-heat-flux precursor:` [Turbulent Fluxes in the Hurricane Boundary Layer. Part II: Latent Heat Flux](drennan-et-al-2007-hurricane-boundary-layer-latent-heat-flux.md).
- `Direct enthalpy-flux precursor:` [First Direct Measurements of Enthalpy Flux in the Hurricane Boundary Layer: The CBLAST Results](zhang-black-french-drennan-2008-direct-enthalpy-flux-cblast.md).

# Linked Pages

- [Air-Sea Interaction](../topics/air-sea-interaction.md)
- [Tropical Cyclone Exchange Coefficients](../topics/tropical-cyclone-exchange-coefficients.md)
- [Potential Intensity](../topics/potential-intensity.md)
- [Tropical Cyclone Intensification](../topics/tropical-cyclone-intensification.md)
- [Boundary-Layer Control](../topics/boundary-layer-control.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
