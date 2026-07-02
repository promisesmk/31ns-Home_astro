---
title: "Nordic 칩셋이 저전력 모드(Sleep Mode)에 진입했는데도 배터리 소모량이 예상보다 높은 원인은 무엇인가요?"
seoTitle: "nRF52 슬립모드(Sleep) 배터리 누수 해결: 플로팅 GPIO 전류 차단"
description: "Nordic nRF52 칩셋 저전력 슬립 모드에서 전류 소모가 비정상적으로 높은 원인인 미사용 GPIO 핀 플로팅 누설 전류 및 내부 DCDC 컨버터 비활성화 레지스터 확인법을 다룹니다."
category: "nordic-ble"
tags: ["nRF52저전력", "슬립모드전류", "GPIO플로팅", "배터리누수"]
date: 2026-07-02
lang: ko
slug: "nrf52-sleep-mode-high-battery-consumption"
---

사용하지 않는 GPIO 핀이 플로팅(Floating) 상태로 방치되어 누설 전류가 발생했거나, 내부 DC-DC 컨버터 대신 효율이 낮은 LDO 모드가 활성화되어 있는지 펌웨어 레지스터를 확인합니다.
