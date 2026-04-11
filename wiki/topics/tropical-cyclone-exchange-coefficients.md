---
title: "Tropical Cyclone Exchange Coefficients"
page_type: "topic"
status: "active"
last_updated: "2026-04-10"
source_count: 9
---

# Definition

Tropical cyclone exchange coefficients are the bulk momentum and enthalpy transfer coefficients used to relate near-surface wind, thermodynamic disequilibrium, and sea state to surface stress and air-sea energy fluxes. In this wiki, the key quantities are the drag coefficient (`CD`), the moisture or Dalton coefficient (`CE`), the enthalpy coefficient (`CK`), and the ratio `CK/CD`.

# Current Synthesis

The wiki previously had a strong drag-saturation branch through [Powell et al. (2003)](../papers/powell-vickery-reinhold-2003-reduced-drag-coefficient-high-wind-speeds.md), [Donelan et al. (2004)](../papers/donelan-et-al-2004-limiting-aerodynamic-roughness-ocean-very-strong-winds.md), [Holthuijsen et al. (2012)](../papers/holthuijsen-powell-pietrzak-2012-wind-and-waves-in-extreme-hurricanes.md), and [Curcic and Haus (2020)](../papers/curcic-haus-2020-revised-estimates-ocean-surface-drag-strong-winds.md). That branch argued that drag does not keep increasing monotonically through the highest winds and that wave state and data-processing choices matter.

The new CBLAST ingest fills the complementary humidity and enthalpy side of the problem. [French et al. (2007)](../papers/french-drennan-zhang-black-2007-hurricane-boundary-layer-momentum-flux.md) provide the first direct hurricane-boundary-layer momentum-flux measurements from Fabian and Isabel and report a drag-coefficient roll-off signal at 18-30 m s^-1, although with uncertain threshold and amplitude. [Drennan et al. (2007)](../papers/drennan-et-al-2007-hurricane-boundary-layer-latent-heat-flux.md) then report direct latent-heat-flux measurements from the same storms showing no evidence that the Dalton number increases with wind speed up to 30 m s^-1. [Zhang et al. (2008)](../papers/zhang-black-french-drennan-2008-direct-enthalpy-flux-cblast.md) extend that branch into combined enthalpy exchange and report a mean `CK/CD` significantly below earlier theoretical thresholds for hurricane development.

[Black et al. (2007)](../papers/black-et-al-2007-air-sea-exchange-cblast.md) tie the CBLAST results together. Their synthesis reports approximately invariant `CD` above about 23 m s^-1, approximately invariant `CE` up to 30 m s^-1, and an implied `CE/CD` near 0.7. The same paper also argues that roll vortices may augment boundary-layer moisture exchange and shows that upper-ocean cooling, inertial currents, and directional wave structure were measured simultaneously in Fabian and Frances, so the coefficient problem should not be treated as purely wind-speed dependent.

[Bell et al. (2012)](../papers/bell-montgomery-emanuel-2012-major-hurricane-exchange-coefficients-cblast.md) extend the evidence into the major-hurricane regime using budget constraints rather than direct turbulence sensors. Using six CBLAST missions in major hurricanes Fabian and Isabel, they report mean coefficients near `CD ~= 2.4 x 10^-3` and `CK ~= 1.0 x 10^-3` for 52-72 m s^-1 winds, with no significant increase in `CK/CD` above 50 m s^-1. Inference for this wiki: the direct-observation and budget-inference branches both support drag saturation or weak growth more strongly than they support a sharp increase in `CK/CD` with wind speed.

Taken together, the current wiki evidence suggests that exchange coefficients in hurricanes are state dependent but not in the simple way often assumed in older intensity arguments. Drag saturation appears robust. Large increases in enthalpy efficiency with wind speed do not. If major hurricanes require more net energy input than low-wind bulk formulas imply, the missing piece may involve spray, coherent structures such as rolls, ocean-state dependence, or theoretical reformulation rather than a monotonic `CK/CD` increase alone.

# Evidence By Source

- [Powell et al. (2003)](../papers/powell-vickery-reinhold-2003-reduced-drag-coefficient-high-wind-speeds.md) report reduced effective drag at high wind speeds relative to monotonic extrapolation from weaker winds.
- [Donelan et al. (2004)](../papers/donelan-et-al-2004-limiting-aerodynamic-roughness-ocean-very-strong-winds.md) report a limiting aerodynamic roughness regime consistent with drag saturation.
- [French et al. (2007)](../papers/french-drennan-zhang-black-2007-hurricane-boundary-layer-momentum-flux.md) provide the first direct hurricane-boundary-layer momentum-flux measurements and report a possible drag-coefficient roll-off.
- [Drennan et al. (2007)](../papers/drennan-et-al-2007-hurricane-boundary-layer-latent-heat-flux.md) report no significant increase in the Dalton number up to 30 m s^-1.
- [Zhang et al. (2008)](../papers/zhang-black-french-drennan-2008-direct-enthalpy-flux-cblast.md) report no statistically significant wind-speed dependence of the enthalpy coefficients in their observed range and find a mean `CK/CD` below earlier threshold estimates.
- [Black et al. (2007)](../papers/black-et-al-2007-air-sea-exchange-cblast.md) synthesize the direct CBLAST results and report `CE/CD` near 0.7, while also proposing roll-vortex enhancement and explicit ocean-state context.
- [Bell et al. (2012)](../papers/bell-montgomery-emanuel-2012-major-hurricane-exchange-coefficients-cblast.md) extend `CK`, `CD`, and `CK/CD` estimates into the major-hurricane regime and do not find significant `CK/CD` growth above 50 m s^-1.
- [Holthuijsen et al. (2012)](../papers/holthuijsen-powell-pietrzak-2012-wind-and-waves-in-extreme-hurricanes.md) emphasize that wave state must be part of exchange-coefficient interpretation in extreme hurricanes.
- [Curcic and Haus (2020)](../papers/curcic-haus-2020-revised-estimates-ocean-surface-drag-strong-winds.md) show that strong-wind drag estimates are sensitive to processing choices and revise some earlier high-wind values downward.

# Open Questions

- How much of the residual hurricane-maintenance problem should be attributed to sea spray, coherent rolls, foam, or unresolved wave-state effects rather than bulk-coefficient error alone?
- Are the modest `CK/CD` values from current direct and budget-based estimates representative across basins, storm sizes, and eyewall precipitation regimes?
- How should operational forecast systems encode state dependence from wave age, misalignment, rain, and ocean cooling without overfitting sparse observations?
- At what wind speed, if any, do enthalpy-transfer pathways depart fundamentally from the moderate-wind CBLAST behavior?
- Which parts of potential-intensity disagreement stem from coefficient uncertainty and which from broader structural assumptions in the theory?

# Related Pages

- [Air-Sea Interaction](air-sea-interaction.md)
- [Boundary-Layer Control](boundary-layer-control.md)
- [Potential Intensity](potential-intensity.md)
- [Tropical Cyclone Intensification](tropical-cyclone-intensification.md)
- [Tropical Cyclone Wave Coupling](tropical-cyclone-wave-coupling.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
