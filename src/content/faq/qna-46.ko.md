---
title: "양산 후 시장에 배포된 무선 제품의 펌웨어를 원격 업데이트(OTA)할 때 전원 차단 등으로 인한 하드웨어 벽돌(Brick) 현상 방지 방안은?"
seoTitle: "BLE 원격 펌웨어 업데이트(OTA) 중 중단 시 벽돌 방지용 듀얼 뱅크 설계"
description: "소비자 사용 중 무선 펌웨어 업데이트(OTA)를 진행하다 배터리 방전이나 전원 차단이 발생해 기기가 영구 오작동(벽돌)하는 것을 막기 위한 Dual-Bank Bootloader(듀얼뱅크 부트로더) 설계 공학입니다."
category: "production"
tags: ["OTA업데이트", "벽돌방지", "듀얼뱅크", "부트로더"]
date: 2026-07-02
lang: ko
slug: "ota-firmware-update-dual-bank-flash-fail-safe"
---

듀얼 뱅크(Dual Bank) 플래시 메모리 구조를 적용하여, 새로운 펌웨어 다운로드가 100% 완료되고 무결성이 검증된 후에만 기존 부팅 이미지를 교체하도록 Fail-safe 안전장치를 설계합니다.
