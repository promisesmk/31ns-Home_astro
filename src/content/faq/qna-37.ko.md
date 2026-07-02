---
title: "2.4GHz 대역폭 내에서 채널별 송신 출력(Tx Power) 편차가 심할 때 인증 통과에 미치는 영향은?"
seoTitle: "2.4GHz 채널별 송신 출력(Tx) 편차 수정 및 무선 인증 통과 대책"
description: "블루투스나 무선 채널(CH 0~39) 전 대역에서 신호 출력이 균일하지 못해 특정 주파수에서 한계 스펙을 이탈하여 인증이 실패하는 것을 막는 펌웨어 캘리브레이션 보정 기법을 소개합니다."
category: "certification"
tags: ["송신출력편차", "채널캘리브레이션", "펌웨어보정", "인증통과"]
date: 2026-07-02
lang: ko
slug: "ble-tx-power-channel-flatness-calibration-for-certification"
---

채널별 출력 편차가 커서 특정 채널이 규격 한계치를 초과하거나 미달하면 인증 통과가 불가능하므로, 펌웨어 단에서 채널별 보정 값(Calibration)을 적용하여 출력을 평탄하게 맞추어야 합니다.
