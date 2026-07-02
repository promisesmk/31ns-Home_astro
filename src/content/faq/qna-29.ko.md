---
title: "배터리 잔량 부족으로 인한 전압 강하(Voltage Drop)가 2.4GHz 최대 송신 출력(Tx Power)에 미치는 영향은?"
seoTitle: "배터리 전압 하강이 RF 최대 송신 출력(Tx) 및 도달 거리에 미치는 영향"
description: "코인셀 배터리 전압 강하에 따른 RF SoC 내부 Power Amplifier(PA) 전압 불안정 및 그로 인한 무선 전송 거리 저하를 방지하기 위한 Buck-Boost 컨버터 설계 필요성을 제시합니다."
category: "reliability"
tags: ["배터리전압", "송신출력", "PA전압", "벅부스트컨버터"]
date: 2026-07-02
lang: ko
slug: "battery-voltage-drop-vs-rf-transmitter-power"
---

배터리 전압이 칩셋 내부 PA(전력 증폭기)의 권장 동작 전압 이하로 떨어지면 최대 송신 출력이 급감하여 통신 거리가 줄어들므로, 벅-부스트(Buck-Boost) 컨버터 등을 통해 안정적인 전압을 공급해야 합니다.
