---
title: "BLE 기기의 방사 스퓨리어스(Radiated Spurious Emission) 기준 초과 시 하드웨어 디버깅 절차는?"
seoTitle: "무선 인증 방사 스퓨리어스 불합격 시 하모닉스 필터(LPF) 디버깅"
description: "국가 인증 챔버 테스트에서 2.4GHz의 고조파(4.8GHz, 7.2GHz 등 Harmonics) 대역 스퓨리어스가 기준을 초과할 때 스펙트럼 분석기를 활용한 LPF 필터 소자 매칭 튜닝법을 제시합니다."
category: "certification"
tags: ["스퓨리어스디버깅", "스펙트럼분석기", "하모닉스", "LPF필터"]
date: 2026-07-02
lang: ko
slug: "radiated-spurious-emission-harmonics-filter-debugging"
---

스펙트럼 분석기로 초과되는 하모닉(고조파) 주파수 대역을 정확히 확인한 후, RF 매칭단에 Low Pass Filter(LPF) 소자를 추가하여 불요파를 감쇄시킵니다.
