---
title: "BLE Antenna Impedance Matching and RF Optimization Guide"
description: "Everything about BLE antenna matching and optimization A complete guide to VNA tuning from PCB design errors for beginners Figure 1. BLE antenna system overview — 50Ω impedance matching path compared to poor design The Invisible Pipeline RF signal is 2.4 GHz..."
date: 2026-05-15
lang: "en"
tags: ["Hardware", "BLE", "RF", "Embedded"]
draft: false
slug: "en/ble-antenna-matching-optimization"
---

## **Everything about BLE antenna matching and optimization**

Complete guide to VNA tuning from PCB design errors for beginners

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_01.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 1\. BLE Antenna System Overview — 50Ω Impedance Matched Path Versus Bad Design*

## **The Invisible Pipeline**

RF signals are sensitive energies that oscillate at 2\.4 GHz (wavelength approximately 12\.5 cm).

### **The Danger of Reflection**

If the chipset, pattern, and antenna do not all meet the standard of '50 ohms (Ω)', the energy cannot be radiated and is reflected back to the chip, reducing the reception distance and causing heat generation. (Increased VSWR and Return Loss)

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_02.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 2\. Comparison of matched state (Matched 50Ω) vs. impedance mismatched (Mismatched)*# **Find the antenna that’s right for you**##**Inverted\-F (IFA) — Inverted F pattern antenna*** Space: 15 × 25 mm* Efficiency: 70% \~ 80%
*Cost: Zero (no additional parts)* Most recommended standard method (smart sensor, beacon)

### **Ceramic Chip — Ceramic Chip Antenna*** Space: 3 × 2 mm* Efficiency: 20% \~ 50%
*Cost: Medium* Suitable for ultra-small wearable devices, but low efficiency

### **Wire \& Monopole — External whip antenna*** Space: 31 mm length* Efficiency: 80% \~ 90%
*Cost: Low* Ideal for high-performance industrial equipment without space constraints

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_03.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 3\. IFA / Ceramic Chip / External Whip Antenna Comparison*# **Anatomy of a failed BLE design**

We dissect the critical design errors that destroy RF performance.

### **Major Design Error Types*** Antenna Placement Error: Antenna placed inside the board or placed close to metal parts* Wiring and accessibility errors (Routing \& Access): RF wiring not maintaining 50Ω impedance
* Noise Coupling: Place high-noise elements such as switching regulators near the RF path.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_04.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 4\. BLE design failure cases — antenna placement, wiring, and noise coupling errors*# **Antenna placement and separation distance (Placement \& Keep\-Out)**

Copper must be removed from all layers around and below the antenna.

A continuous ground plane of sufficient size (minimum 25 × 35 mm) is essential.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_05.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 5\. Antenna Keep\-Out Area — BAD (copper present below antenna) vs GOOD (copper removed and placed on top)*# **50Ω Matching Pattern (The 50Ω Trace \& RF Access)**

Impedance cannot be roughly guessed. Accurate calculation of trace width (W), separation distance (G), substrate thickness (H), and dielectric constant (εr) is required.

CPWG (Coplanar Waveguide with Ground) method is advantageous in blocking noise.

**💡 Pro Tip:** During the development stage, be sure to place a pad (RF Access Point) for a U.FL connector or coaxial cable. Without this, the VNA will be 'blind', unable to make measurements.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_06.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 6\. Coplanar Waveguide (CPWG) cross-sectional structure — W (line width), G (separation), H (substrate thickness)*# **The Missing Network**

A Pi\-Network type matching network pad is required between the BLE SoC output and the antenna.

### **Notes on component selection*** Self-resonant frequency (SRF) must be over 3 GHz* The capacitor uses a C0G (NP0\) dielectric that is resistant to temperature changes.
* Inductor uses High\-Q Wirewound type to minimize insertion loss

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_07.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 7\. BLE SoC → Pi\-Network Pads → Antenna connection circuit diagram*# **VNA (The Tool of Truth)**

Measure return loss (S11\) using a VNA.

A deep skeleton (V\-shape) where the S11 waveform drops below \-10 dB must be located at the center of the target frequency (2\.44 GHz) for a perfect match.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_08.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 8\. VNA screen — V\-shape skeleton centered at 2\.44 GHz in S11 waveform with ideal matching*# **Absolute Principle: SOLT Calibration (The Golden Rule of Calibration)**

A VNA without calibration cannot be trusted. System errors of the 12\-term error model, such as directionality (e00\), source matching (e11\), and reflection tracking (e10·e01\), must be removed.

By connecting the Short, Open, Load, and Thru standard kits, the measurement accuracy is ‘on point’.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_09.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 9\. SOLT Calibration Kit — Short / Open / Load / Thru Standard Connectors*# **Moving the Reference Plane: Port Expansion (Moving the Reference Plane)**

The Dilemma: Calibration ends at the end of the cable, but the matching network on the PCB is where we measure.

The Fix: To compensate for the phase delay caused by the coaxial cable, the VNA's 'Port Extension' function must be used to accurately move the reference plane to the antenna feed point.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_10.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 10\. Calibration Plane → Measurement Plane movement concept (Port Extension)*# **Demystifying the Smith Chart**

Approach it as an ‘impedance treasure map’ rather than mathematics.

The exact center of the chart (50 ohms) is the perfect match we need to achieve. Visually determine how off center the current antenna's impedance (R \+ jX) is.

*50Ω (Target): Right center of Smith chart — ideal matching target* Current Impedance: Currently measured antenna impedance location

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_11.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 11\. Smith Chart — 50Ω Target and Current Impedance Location*# **Steering to the Center**

The inductor (L) and capacitor (C) act as arrow keys on the Smith chart. Use the simulator to find the optimal component combination and place it in the center.

### **Direction of movement of Smith chart by component*** Parallel inductor (Shunt L): counterclockwise top movement* Series inductor (Series L): clockwise upward movement
*Parallel capacitor (Shunt C): clockwise downward movement* Series Capacitor (Series C): Move bottom counterclockwise

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_12.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 12\. Smith Chart Component Navigation — L/C combination to reach 50Ω center*# **Enclosure Detuning*** The plastic case acts as a dielectric and lowers the antenna's resonant frequency by about 50\~100 MHz (Detuning).* Be sure to perform VNA measurements with the actual production case on, and if necessary, trim the ends of the antenna pattern and raise the frequency.

### **Bare PCB vs Encased PCB Comparison*** Bare PCB: 2\.44 GHz — Ideal Resonance* Encased PCB: 2\.35 GHz — Detuning occurs, correction required by trimming

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_13.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 13\. Comparison of S11 waveforms before and after device assembly — resonance frequency shift when case is mounted*# **The BLE Success Checklist**

If you follow these rules, you can more than double the communication distance.

### **Layout (Design)*** Antenna is placed at the edge of the board* Securing perfect separation area (keep\-out) up, down, left and right
* Maintain calculated impedance 50Ω RF pattern

### **Hardware*** U.FL connector must be added for debugging* Secure 3 0402 pads for Pi\-matching network
* Continuous ground of at least 25 × 35 mm

### **Tuning*** VNA cable phase delay compensation (Port Extension)* 50Ω matching using Smith chart
* Be sure to measure with the final equipment (enclosure) on

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_14.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />

*Figure 14\. BLE antenna success checklist — Layout / Hardware / Tuning 3 steps*# **Q\&A — BLE Antenna Matching and Optimization**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/BLE_안테나_정합과_최적화_기술자료/img_15.webp" width="1200" height="669" loading="lazy" alt="Blog Image" />*Figure 15\. BLE antenna matching and optimization*