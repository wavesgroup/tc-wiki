---
title: "Potential Intensity"
page_type: "topic"
status: "active"
last_updated: "2026-04-07"
source_count: 8
---

# Definition

Potential intensity (PI) is the theoretical upper bound on tropical cyclone intensity in a given environment, commonly framed through an axisymmetric dissipative heat-engine model.

# Current Synthesis

[Montgomery and Smith (2017)](../papers/montgomery-smith-2017-fluid-dynamics-of-tropical-cyclones.md) treat PI as a major mature-intensity framework but not as a complete description of storm intensity. The review notes that an upper bound should exist on energetic grounds, yet it also emphasizes that both original and revised PI formulations have important limitations.

The paper highlights several issues. Some arguments depend on approximate gradient balance in the boundary layer, even though unbalanced boundary-layer flow appears important for eyewall dynamics. The review also notes sensitivity to exchange coefficients, dissipative-heating assumptions, turbulence formulations, and the difference between axisymmetric and 3D behavior.

[Smith and Montgomery (2010)](../papers/smith-montgomery-2010-hurricane-boundary-layer-theory.md) is not itself a PI paper, but it strengthens one of these caveats. The paper argues that steady boundary-layer formulations with standard zero-gradient upper-boundary conditions do not directly determine unbalanced flow above the layer. By implication, PI arguments that depend on steady, approximately balanced boundary-layer control need to be interpreted carefully.

[Persing et al. (2013)](../papers/persing-et-al-2013-asymmetric-and-axisymmetric-dynamics-of-tropical-cyclones.md) sharpen a related caveat from the modeling side. In disputing an earlier PI-style interpretation of why 3-D simulated storms are weaker than axisymmetric ones, the authors argue that such explanations can miss the roles of unbalanced boundary-layer dynamics, convective organization, and resolved eddy momentum fluxes.

[Nolan et al. (2025)](../papers/nolan-fischer-oneill-2025-mass-and-condensate-sources-for-tropical-cyclone-outflow.md) add a structural caveat from the outflow side. In their simulations, the outflow layer between roughly 100 and 300 km radius is not fed mainly by an isolated eyewall exhaust: rainbands supply a large share of the dry-air mass flux and an even larger share of condensate, while convective and mesoscale ascent repeatedly disrupt the layer. The paper therefore argues that PI interpretations relying on a smooth, self-contained outflow layer or internally set outflow temperature should be treated cautiously.

A complementary caveat comes from the high-wind air-sea exchange literature. [Powell et al. (2003)](../papers/powell-vickery-reinhold-2003-reduced-drag-coefficient-high-wind-speeds.md), [Donelan et al. (2004)](../papers/donelan-et-al-2004-limiting-aerodynamic-roughness-ocean-very-strong-winds.md), [Holthuijsen et al. (2012)](../papers/holthuijsen-powell-pietrzak-2012-wind-and-waves-in-extreme-hurricanes.md), and [Curcic and Haus (2020)](../papers/curcic-haus-2020-revised-estimates-ocean-surface-drag-strong-winds.md) collectively indicate that momentum drag behavior in severe winds is not a simple monotonic function of wind speed. Because PI frameworks depend on exchange-coefficient assumptions (directly or indirectly in practical implementations), this chain strengthens the wiki's existing warning that PI skill can be sensitive to uncertain surface-layer physics.

# Evidence By Source

- Montgomery and Smith (2017) summarize PI as a prediction of the maximum possible intensity in a given environment, usually in terms of maximum gradient wind.
- The review notes criticism of the dissipative heat-engine interpretation and points to uncertainty in how dissipative heating should be represented.
- The paper discusses an extended analytical theory in which unbalanced flow can contribute significantly to maximum intensity, but the authors note that this is no longer a purely environmental PI estimate because it requires storm-structure inputs.
- The review summarizes a revised PI theory based on outflow stratification set internally by the vortex, then argues that the revised theory still has limitations and should be tested more carefully against observations and 3D simulations.
- Montgomery and Smith (2017) conclude that 3D effects need to be accounted for properly in a consistent formulation of the maximum-intensity problem.
- Smith and Montgomery (2010) show analytically that a steady continuous boundary-layer model with negligible friction near its top and zero vertical wind gradients there cannot directly determine the flow above it when that flow departs from gradient balance.
- Inference for this wiki: that result helps explain why PI theories tied to steady boundary-layer control can miss supergradient amplification and other unbalanced inner-core dynamics.
- [Persing et al. (2013)](../papers/persing-et-al-2013-asymmetric-and-axisymmetric-dynamics-of-tropical-cyclones.md) explicitly question a previous explanation of 3-D versus axisymmetric intensity differences based mainly on Emanuel-style PI arguments, arguing that it neglects known PI weaknesses, unbalanced boundary-layer dynamics, and differences in convective organization.
- [Nolan et al. (2025)](../papers/nolan-fischer-oneill-2025-mass-and-condensate-sources-for-tropical-cyclone-outflow.md) find that rainbands contribute roughly one-third to two-thirds of the outflow dry-air mass flux and most of the condensate in the cirrus shield in their two mature-hurricane simulations.
- The same paper argues that such repeated rainband and mesoscale injections are difficult to reconcile with PI interpretations that assume outflow temperature or self-stratification is set within a largely self-contained outflow layer.
- [Powell et al. (2003)](../papers/powell-vickery-reinhold-2003-reduced-drag-coefficient-high-wind-speeds.md) report reduced effective drag at very high tropical-cyclone wind speeds relative to simple extrapolation from moderate winds.
- [Donelan et al. (2004)](../papers/donelan-et-al-2004-limiting-aerodynamic-roughness-ocean-very-strong-winds.md) report a limiting aerodynamic roughness regime in very strong winds, supporting drag saturation behavior.
- [Holthuijsen et al. (2012)](../papers/holthuijsen-powell-pietrzak-2012-wind-and-waves-in-extreme-hurricanes.md) emphasize explicit wind-wave coupling in extreme hurricanes, implying that fixed exchange curves can miss state dependence.
- [Curcic and Haus (2020)](../papers/curcic-haus-2020-revised-estimates-ocean-surface-drag-strong-winds.md) revise strong-wind drag estimates and report saturation near Cd ~2.6 x 10^-3 around U10 ~25 m s^-1 in corrected processing.

# Open Questions

- Which PI assumptions fail most seriously in observed major hurricanes?
- How should boundary-layer imbalance and 3D turbulence be incorporated into future intensity-limit theories?
- How should rainband-fed, intermittently mixed outflow alter current outflow-temperature assumptions in PI theory?
- When PI agrees with observed or simulated intensity, is that agreement physically informative or partly compensating error?
- How should PI-related maximum-intensity estimation evolve when high-wind momentum drag is saturating and wave-state dependent?

# Related Pages

- [Tropical Cyclone Intensification](tropical-cyclone-intensification.md)
- [Tropical Cyclone Outflow](tropical-cyclone-outflow.md)
- [Boundary-Layer Control](boundary-layer-control.md)
- [Hurricane Boundary-Layer Models](../methods/hurricane-boundary-layer-models.md)
- [Steady-State Tropical Cyclones](steady-state-tropical-cyclones.md)
- [Tropical Cyclone Fluid Dynamics](../syntheses/tropical-cyclone-fluid-dynamics.md)
