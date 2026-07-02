---
title: "전원부(SMPS) 스위칭 노이즈가 2.4GHz RF 수신 감도(RSSI)에 미치는 영향을 최소화하는 레이아웃 팁은?"
seoTitle: "SMPS 전원 노이즈로 인한 RF 수신감도(RSSI) 저하 방지 레이아웃"
description: "전원부(SMPS)의 스위칭 고주파 노이즈가 RF 회로에 유입되어 RSSI 및 수신감도를 떨어뜨리는 현상을 해결하는 GND 분할 설계 및 바이패스 디커플링 캡 배치 팁입니다."
category: "rf-tuning"
tags: ["SMPS노이즈", "수신감도RSSI", "GND분할", "디커플링콘덴서"]
date: 2026-07-02
lang: ko
slug: "smps-switching-noise-rf-rssi-layout"
---

RF 단과 전원 단의 GND 영역을 분할한 뒤 페라이트 비드를 통해 한 점에서 연결하고, 디커플링 커패시터를 RF IC 전원 핀에 최대한 가깝게 배치하여 고주파 노이즈 유입을 차단합니다.
