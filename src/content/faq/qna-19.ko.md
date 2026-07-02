---
title: "외부 32.768kHz 크리스탈(RTC)의 주파수 편차(ppm)가 BLE 연결 안정성에 미치는 영향은?"
seoTitle: "32.768kHz RTC 크리스탈 오차(ppm)와 BLE 무선 연결 안정성"
description: "외부 슬립 크리스탈(RTC 오실레이터) 주파수 오차(ppm)가 BLE 무선 통신 기기의 슬립 상태 해제 시 타이밍 윈도우 불일치 및 패킷 드롭에 미치는 기전을 분석합니다."
category: "nordic-ble"
tags: ["RTC크리스탈", "ppm오차", "패킷손실", "연결안정성"]
date: 2026-07-02
lang: ko
slug: "rtc-crystal-frequency-deviation-ppm-ble-stability"
---

주파수 편차가 크면 저전력 모드에서 깨어날 때 마스터와 슬레이브 간의 통신 타이밍 윈도우가 어긋나게 되어 패킷 손실률이 급증하고 잦은 연결 끊김 현상이 발생합니다.
