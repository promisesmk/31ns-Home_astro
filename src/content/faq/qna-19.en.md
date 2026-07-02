---
title: "How does external 32.768kHz RTC crystal clock drift (ppm) impact BLE connection stability?"
seoTitle: "How 32.768kHz RTC ppm Drift Degrades BLE Connection Stability"
description: "A technical breakdown of sleep clock accuracy (SCA) requirements in Bluetooth, detailing clock drift calculations and ppm tolerances."
category: "nordic-ble"
tags: ["RTCCrystal", "ppmTolerance", "PacketLoss", "LinkStability"]
date: 2026-07-02
lang: en
slug: "en/rtc-crystal-frequency-deviation-ppm-ble-stability"
---

High clock drift causes timing window offset deviations when the peripheral wakes from sleep. This clock mismatch leads to packet misses, latency spikes, and eventual connection timeouts.
