---
title: "Why is the sleep mode current consumption of a Nordic SoC higher than specified in the datasheet?"
seoTitle: "Resolving High Sleep Current and Leakage in nRF52 Boards"
description: "Learn to fix low-power state leakage by configuring unused GPIO pins to pull-up/pull-down states and verifying register settings for internal DC-DC converters."
category: "nordic-ble"
tags: ["nRF52LowPower", "SleepCurrent", "FloatingGPIO", "BatteryLeakage"]
date: 2026-07-02
lang: en
slug: "en/nrf52-sleep-mode-high-battery-consumption"
---

Unused GPIO pins left in a floating state cause leakage current. Additionally, check firmware configuration to ensure the internal DC-DC converter is enabled rather than defaulting to the less efficient LDO mode.
