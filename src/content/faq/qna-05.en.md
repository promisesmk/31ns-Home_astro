---
title: "What layout tips minimize SMPS switching noise interference on 2.4GHz RF receiver sensitivity (RSSI)?"
seoTitle: "Reducing SMPS Switching Noise Impact on RF Receiver RSSI"
description: "Layout recommendations to protect RF transceiver sensitivity from SMPS high-frequency switching noise, including ground partitioning and decoupling capacitor placement."
category: "rf-tuning"
tags: ["SMPSNoise", "RSSI", "GNDIsolation", "DecouplingCapacitors"]
date: 2026-07-02
lang: en
slug: "en/smps-switching-noise-rf-rssi-layout"
---

Isolate the RF ground plane from the power supply ground plane, connecting them at a single point via a ferrite bead. Place decoupling capacitors as close to the RF IC power pins as possible to filter high-frequency switching ripples.
