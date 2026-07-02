---
title: "BLE 통신 거리(Range)를 기존 대비 2배 이상 연장하기 위한 하드웨어 튜닝 기법은 무엇이 있나요?"
seoTitle: "블루투스 BLE 송수신 거리 2배 늘리기: Coded PHY 및 FEM 적용"
description: "BLE 통신 커버리지를 연장하기 위해 외장 송수신 증폭기(FEM) 회로 설계 적용 및 노르딕 칩셋이 지원하는 BLE Long Range(Coded PHY 125kbps/500kbps) 튜닝 기법을 소개합니다."
category: "nordic-ble"
tags: ["BLE통신거리", "FEM증폭기", "CodedPHY", "LongRange"]
date: 2026-07-02
lang: ko
slug: "ble-communication-range-extension-fem-coded-phy"
---

정밀한 RF 매칭 회로 최적화를 기본으로, 하드웨어에 별도의 FEM(PA/LNA 증폭기) 칩을 추가하거나 Nordic 칩셋이 지원하는 Coded PHY(Long Range) 모드를 소프트웨어적으로 활성화합니다.
