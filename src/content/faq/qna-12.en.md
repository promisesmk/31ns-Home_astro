---
title: "When BLE connection drops are frequent, what RF hardware parameters should be investigated first?"
seoTitle: "Troubleshooting BLE Connection Drops via Crystal ppm Tuning"
description: "Diagnose bluetooth connection reliability issues by addressing RTC sleep clock inaccuracy (drift) and optimizing antenna impedance mismatches."
category: "nordic-ble"
tags: ["BLEDisconnect", "RTCCrystal", "ppmError", "RFDebugging"]
date: 2026-07-02
lang: en
slug: "en/ble-connection-drop-hardware-troubleshooting"
---

Inspect the frequency tolerance (ppm) of the 32.768kHz RTC crystal to prevent sleep-wake timing drifts, and verify if antenna return loss is causing the signal strength to dip below the link-budget threshold.
