---
title: "노르딕 칩셋 내장 DC-DC 컨버터 사용 시 발생하는 노이즈가 RF 송수신에 미치는 영향은?"
seoTitle: "Nordic 내장 DC-DC 스위칭 노이즈로 인한 RF 수신감도 저하 해결"
description: "nRF52 시리즈 내장 DCDC 레귤레이터 사용 시 인덕터에서 발생하는 고주파 스위칭 노이즈가 RF 라인 및 안테나 성능에 미치는 악영향을 최소화하는 레이아웃 배치 방안을 다룹니다."
category: "nordic-ble"
tags: ["DC-DC노이즈", "스위칭인덕터", "RF수신감도", "노르딕회로"]
date: 2026-07-02
lang: ko
slug: "nordic-dcdc-converter-switching-noise-rf"
---

인덕터 주변의 스위칭 노이즈가 안테나나 RF 입력단으로 유입되면 수신 감도가 급락하므로, 노이즈가 적은 권장 규격의 인덕터 사용 및 RF 트레이스와의 이격 배치가 매우 중요합니다.
