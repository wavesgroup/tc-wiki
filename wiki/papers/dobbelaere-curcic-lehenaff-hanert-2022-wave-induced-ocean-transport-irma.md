---
title: "Impacts of Hurricane Irma (2017) on wave-induced ocean transport processes"
page_type: "paper"
status: "active"
last_updated: "2026-04-15"
source_count: 2
---

# Citation

Dobbelaere, Thomas, Milan Curcic, Matthieu Le Henaff, and Emmanuel Hanert, 2022: *Impacts of Hurricane Irma (2017) on wave-induced ocean transport processes*. *Ocean Modelling*, 171, 101947. DOI: [10.1016/j.ocemod.2022.101947](https://doi.org/10.1016/j.ocemod.2022.101947).

Accessed text sources: [NOAA Institutional Repository accepted-manuscript PDF](https://repository.library.noaa.gov/view/noaa/35794/noaa_35794_DS1.pdf) and [DOI landing page](https://doi.org/10.1016/j.ocemod.2022.101947).

Peer-review status: Peer-reviewed primary coupled wave-current coastal transport study.

# Research Question

Dobbelaere et al. (2022) ask how wave-current interactions, especially radiation-stress gradients and Stokes drift, modify coastal transport during Hurricane Irma (2017) in the Florida Reef Tract.

# Data And Methods

- Study type: Coupled coastal wave-current modeling and passive-drifter transport study.
- Case: Hurricane Irma (2017) in the Florida Reef Tract and adjacent shelf.
- Model framework: The unstructured-mesh coastal ocean model SLIM coupled to the SWAN spectral wave model.
- Validation: Comparisons to observed waves, storm surge, and currents during Irma.
- Transport diagnostics: Passive-drifter simulations comparing coupled versus uncoupled radiation-stress and Stokes-drift effects.

# Key Equations

Dobbelaere et al. (2022) evolve the coastal circulation with conservative shallow-water equations:

```math
\frac{\partial H}{\partial t} + \nabla \cdot \mathbf{U} = 0,
```

```math
\frac{\partial \mathbf{U}}{\partial t}
+ \nabla \cdot \left(\frac{\mathbf{U}\mathbf{U}}{H}\right)
+ f \mathbf{e}_z \times \mathbf{U}
= \alpha g H \nabla(H-h)
- \frac{1}{\rho}\nabla p_{\mathrm{atm}}
+ \frac{1}{\rho}\boldsymbol{\tau}_s
+ \nabla \cdot (\nu \nabla \mathbf{U})
- \frac{C_b}{H^2}|\mathbf{U}|\mathbf{U}
+ \gamma(\mathbf{U}_{\mathrm{ref}}-\mathbf{U}).
```

Here $H$ is water-column height and $\mathbf{U}$ is depth-averaged transport. This is the hydrodynamic backbone for the transport experiments.

The coupled wave field is advanced with the SWAN action-balance equation

```math
\frac{\partial N}{\partial t}
+ \nabla_x \cdot [(\mathbf{c}_g + \mathbf{u})N]
+ \frac{\partial (c_\theta N)}{\partial \theta}
+ \frac{\partial (c_\sigma N)}{\partial \sigma}
= \frac{S_{\mathrm{in}} + S_{\mathrm{ds}} + S_{\mathrm{nl}}}{\sigma},
\qquad
N = \frac{E}{\sigma},
```

which is the paper's compact statement of wave advection, refraction, frequency shifting, and source-sink balance.

The wave-induced transport piece is then diagnosed with

```math
\mathbf{u}_s
= \int_0^{2\pi} \int_0^{\infty}
\frac{\sigma^3}{h \tanh(2kh)} E(\sigma,\theta)(\cos\theta,\sin\theta)\, d\sigma\, d\theta,
```

and coupling closes through $\boldsymbol{\tau}_s = \boldsymbol{\tau}_{\mathrm{wind}} + \boldsymbol{\tau}_{\mathrm{wave}}$ once SWAN returns the radiation-stress forcing to SLIM.

# Findings

- Dobbelaere et al. (2022) found that the coupled model reproduced Irma's coastal waves, surge, and currents credibly enough to support transport diagnosis.
- The wave radiation-stress gradient alone altered modeled currents by up to about 1 m s^-1, with the largest effects over the shelf break and reef zones.
- Radiation stress alone could shift drifting material by up to about 5 km during the hurricane, while Stokes drift caused much larger deflections, up to about 20 km, and dominated wave-induced transport by roughly a factor of four.
- The paper also shows that neglecting wave-current coupling when computing Stokes drift changes predicted trajectories by up to about 5 km, so wave coupling is not just a small correction in heavy-wind coastal transport.

# Limitations

- The circulation model is depth averaged and barotropic, so it does not resolve full 3-D ocean structure or explicit air-sea heat-flux feedbacks.
- This is a single-region coastal study, and the magnitude of the transport response depends on local shelf, reef, and current structure.
- The authors note that their momentum-flux treatment can still overestimate atmosphere-to-ocean momentum transfer under hurricane conditions because momentum carried away by waves is not fully removed.

# Referenced Papers

This is a curated ingest queue, not a full bibliography.

- `Open-ocean hurricane Stokes-drift predecessor cited in this paper:` [Hurricane-induced ocean waves and stokes drift and their impacts on surface transport and dispersion in the Gulf of Mexico](curcic-chen-ozgokmen-2016-hurricane-induced-ocean-waves-stokes-drift.md).
- `Strong-wind drag context cited in this paper:` [Revised Estimates of Ocean Surface Drag in Strong Winds](curcic-haus-2020-revised-estimates-ocean-surface-drag-strong-winds.md).

# Linked Pages

- [Air-Sea Interaction](../topics/air-sea-interaction.md)
- [Tropical Cyclone Wave Coupling](../topics/tropical-cyclone-wave-coupling.md)
- [Tropical Cyclone Numerical Modeling](../topics/tropical-cyclone-numerical-modeling.md)
