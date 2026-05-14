---
title: "nRF52805_BLE모듈_개발기술참고문서_이미지포함"
description: "nRF52805 BLE 모듈 개발 기술 참고 문서 (개발자용) GX805 / GX805C Series · Nordic Semiconductor nRF52805 WLCSP ⚠ 민감정보 익명 처리 안내: 원본의 회사명·인명·연락처 등은 [고객사], [담당이사A], [대표B], [담당이..."
date: 2026-05-14
lang: "ko"
tags: ["Hardware", "BLE", "RF", "Embedded"]
draft: false
---

**nRF52805 BLE 모듈 개발**

기술 참고 문서 (개발자용)

*GX805 / GX805C Series · Nordic Semiconductor nRF52805 WLCSP*



| ⚠ 민감정보 익명 처리 안내: 원본의 회사명·인명·연락처 등은 \[고객사], \[담당이사A], \[대표B], \[담당이사C], \[담당자D], \[외주RF튜닝업체], \[PCB제작업체A/B] 등으로 익명 처리하였습니다. |
| --- |

## **231127\_\[고객사]\_Module개발\_(1차미팅/복사)**

**2023년 11월 27일 월요일**

*오전 6:13*

**\[담당이사A], \[대표B], ,\[담당이사C]**

적용 Chip

PCB 사양/ 배치 및 회로배선고려

**Build\-up A, B, C**

캔적용

**기존 보유캔 스펙**

검토 또는 참고할 Ref Module type

모듈 Size

안테나 Type

**PCB size대비 Chip안테나로 설계 될 수 있음.**

안테나 파생

## **안테나 메칭**

**PCB 2층, 4층 기준설정 후 Build\-up 제작전에 안테나 패턴타입 설계**

## **Buil\-up제작후 2차 안테나 메칭**

Sample제작 여부

RF단 튜닝

**개발검토 내용 전달**

**2023년 11월 30일 목요일**

*오전 10:03*

IC 및 모듈 Vendor를 검토한 결과 Pin out 개수가 적어서 2Layer로 설계가 가능해 보입니다.

다만, Pin배치, 부품 추가 등에 따라서 부득이하게 4Layer로 설계를 해야 하는 경우가 있을 수 있습니다.

**PCB 가격은(샘플,양산) 올라가게 됩니다.**

**I/O는 Chip 외곽으로 배치되어 있어서 모든 I/O를 뺄 수 있을 것 같습니다.**

**I/O개수를 줄인다고 해서 모들이 작아 지기에는 한계가 있습니다.**

모듈설계 결정사항

**32\.768KHz 크리스탈을 optional 처리 할지, 모듈에 넣을지.**

개발 참고 대상은 \[담당이사A]님이 말씀 주신 것 외에,

**Raytac에서 nRF52805로 개발된 모듈을 기준으로 하면 좋을 것 같습니다.**

**안테나도 거의 동일하게 설계 되어질 것으로 생각됩니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_01.webp" width="1063" height="411" loading="lazy" alt="Blog Image" />

참고 이슈

**기존에 노르딕 Ref는 1005부품이 최소 Size 였습니다.**

**하지만 최근에는 IC도 작아진 만큼, 0603으로 대체(변경 가능한 용량들) 가 되어 부품들이**

**모두 작습니다. 따라서 모듈을 만들 때 작게 할 수 있습니다.**

* → 생산 도급 시 다소 일반적인 부품이 아닙니다.
* → RF튜닝시 별도로 부품을 구매해야 합니다.

**Nordic 레퍼런스의 BOM /부품 크기 참고/ inch 기준임.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_02.webp" width="1081" height="354" loading="lazy" alt="Blog Image" />

**Inch è mm 참고**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_03.webp" width="704" height="445" loading="lazy" alt="Blog Image" />

DK보드 제작 고려

* → 향후 DK가 없으면 고객사 대응이 다소 어려울 것 같아서 Ratac 제품을 검토해 봤습니다.

**아래 그림은 Raytac사의 DK 입니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_04.webp" width="1200" height="787" loading="lazy" alt="Blog Image" />

향후 고려사항

**Module을 생산할 때 모듈을 개별로 시험할 수 있는 JIG 설계가 필요합니다.**

**기능적인 부분보다는 모듈각각의 Pin에 대해 솔더링을 하지 않고,**

**전기적 접촉을 할 수 있는 구조를 만드는 것이 중요해 보입니다.**

개발을 진행 할 경우 간략히 아래와 같습니다.

경쟁사외 모듈 제품 분석, Nordic 52805 Ref 설계 분석

Raytac사 모듈 구입 : 설계특이사항 분석

회로설계 완료

CAD설계 진행 및 설계 컨펌.

## **안테나 설계 사전 검토/ 안테나 메칭업체**

PCB제작

## **안테나 메칭/ Bare Board Level**

부품수급: 사급(\[고객사]) 또는 구매

SMT의뢰

## **Module test**

**\-Function test : \[고객사]에서 test할 수 있도록 수작업배선.**

**/ DK 제작 전 작업.**

**\-RF 출력확인 : DTM F/W입수(\[고객사])후 출력측정 및 필요시 튜닝.**

1. 11\)이후 2번째 Type 모듈 및 DK 개발.

**보시고 궁금한 부분 있으시면 전화 주시면 고맙겠습니다.**

## **Module\[고객사] 설계검토\_자료분석반영**

**2023년 11월 28일 화요일**

*오전 8:12*

**Raytac사의**

**MDBT42\-512KV2, \-P512KV2 모듈형태 참고하여 nRF52085를 사용한 모듈 개발.**

개발컨셉 : CAN을 겸용으로 사용.

* → nRF52805, nRF52832WLCSP

**따라서, 추후 nRF52832WLCSP로 모듈 개발시 위 모듈과 동일하게 설계할 경우**

**설계에 문제가 없을 것으로 판단하기 때문에 CAN설계를 동일하게 하고자 함.**

위 모듈 검토사항

**기존 nRF52805모듈을 검토한 내용에 추가적인 부분만 반영하여 설계하면 될 것으로 판단.**

**전체 높이 : 1\.8**

**가로 8\.8**

**세로 13\.8**

**CAN 높이 : 1\.0mm**

설계적용 PCB : 0\.8T, 2Layer

**안테나 싸이드 V\-cut, 그외 미싱홀 없음.\=\=\>PCB제작가능여부?**

회로설계

**RF test TP with GNT TP**

**52805 WLCLP**

**X\-tal 32Mhz : 1612size**

**LC 부품 : 0603 size**

**without DCDC and Xtal 32Khz**

**RF배치 : IC를 최대한 안테나 쪽으로 이동배치**

* → IC 출력단 : Nordic REF참고반영
* → ANT 메칭 : Pi메칭회로
* → Raytac 모듈의 nRF52805 는 PCB가 작아서 RF단 출력이 많이 꺽임.

**PCB size가 nRF52832WLCSP module로 적용할 수 있으므로**

**RF단 출력패턴을 대각선 일자로 배치하여 안테나 까지 유도하는 설계로 적용.**

## **nrf52805 Ref\_Nordic사**

**2023년 12월 19일 화요일**

*오전 7:59*

**1 .With DCDC**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_05.webp" width="900" height="537" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_06.webp" width="1200" height="1103" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_07.webp" width="1200" height="1157" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_08.webp" width="723" height="666" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_09.webp" width="1021" height="935" loading="lazy" alt="Blog Image" />

Without DCDC

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_10.webp" width="1200" height="772" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_11.webp" width="1200" height="1108" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_12.webp" width="1177" height="1169" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_13.webp" width="1200" height="1102" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_14.webp" width="1035" height="944" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_15.webp" width="871" height="859" loading="lazy" alt="Blog Image" />

PCB 설계 레퍼런스

**아래 RF 출력단 임피던스 확인**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_16.webp" width="863" height="785" loading="lazy" alt="Blog Image" />

**실질적으로 모듈 설계시 아래 S값은 적용이 어려움.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_17.webp" width="590" height="552" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_18.webp" width="1100" height="162" loading="lazy" alt="Blog Image" />

**주의 : IC nrf52805 \<\=\=\> 안테나까지**

**아래와 같이 메칭 안맞음./ 부품크기고려하여 PCB패턴 메칭하지 않은 것으로 보임.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_19.webp" width="501" height="405" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_20.webp" width="587" height="500" loading="lazy" alt="Blog Image" />

부품 Size

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_21.webp" width="1008" height="351" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_22.webp" width="649" height="566" loading="lazy" alt="Blog Image" />

## **참고모듈\_Raytac MDBT42T /섹션결과**

**2023년 11월 28일 화요일**

*오전 10:44*

**온라인구매**

https://www.digikey.com/en/products/filter/rf\-transceiver\-modules\-and\-modems/872?s\=N4IgTCBcDaILIBEBCAVALGALiAugXyA

**https://www.raytac.com/product/ins.php?index\_id\=107**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_23.webp" width="1086" height="1076" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_24.webp" width="809" height="956" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_25.webp" width="598" height="677" loading="lazy" alt="Blog Image" />

**No 32\.768K, No DCDC parts**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_26.webp" width="886" height="1223" loading="lazy" alt="Blog Image" />

**1\.CAN : 0\.2T, 1\.05mm (height from PCB top), 5\.8mm x 7\.0mm**

**2\.PCB : 0\.8T 4layer**

**3\.X\-tal : 1612사용**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_27.webp" width="634" height="463" loading="lazy" alt="Blog Image" />

**3\.Half Hole**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_28.webp" width="633" height="452" loading="lazy" alt="Blog Image" />

**3\.Via BPL and PSR**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_29.webp" width="645" height="480" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_30.webp" width="779" height="571" loading="lazy" alt="Blog Image" />

**4\.배치 및 ANT 형상**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_31.webp" width="293" height="426" loading="lazy" alt="Blog Image" />

배치컨셉

**안테나메칭단 : Pi구성**

**IC를 최대한 안테나 쪽으로 이동배치**

**IC 출력 튜닝단은 nRF52805 REF 배치 설계 적용.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_32.webp" width="631" height="470" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_33.webp" width="640" height="475" loading="lazy" alt="Blog Image" />

부품크기

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_34.webp" width="520" height="383" loading="lazy" alt="Blog Image" />

1. 7\. 1005 대체 검토

문제점 : Size가 커짐에 따라 튜닝이 용이해 지지만 래퍼런스를 따지지 않으므로 튜닝이슈는 커지게 됨 .

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_35.webp" width="641" height="489" loading="lazy" alt="Blog Image" />

**240117 : \[PCB제작업체A]\-**

섹션결과 0\.7T, H/H oz, 양면같으나, 0\.7T자재는 없으며 0\.8T, H/H oz로 작업시 최종두께 0\.9T예상됩니다.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_36.webp" width="1105" height="770" loading="lazy" alt="Blog Image" />

## **참고모듈\_Raytac MDBT42**

**2023년 12월 22일 금요일**

*오후 12:24*

**https://www.raytac.com/product/ins.php?index\_id\=33**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_37.webp" width="1200" height="621" loading="lazy" alt="Blog Image" />

**위 MDBT42\-512KV2, \-P512KV2 모듈형태 참고하여 nRF52085를 사용한 모듈 개발.**

주목적 : CAN을 겸용으로 사용.

* → nRF52805, nRF52832WLCSP

**따라서, 추후 nRF52832WLCSP로 모듈 개발시 위 모듈과 동일하게 설계할 경우**

**설계에 문제가 없을 것으로 판단하기 때문에 CAN설계를 동일하게 하고자 함.**

위 모듈 검토사항

**기존 nRF52805모듈을 검토한 내용에 추가적인 부분만 반영하여 설계하면 될 것으로 판단.**

**전체 높이 : 1\.8**

**가로 8\.8**

**세로 13\.8**

**CAN 높이 : 1\.0mm**

CAN

**좌, 우측면 모서리는 두께만큼 단차 적용**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_38.webp" width="481" height="371" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_39.webp" width="641" height="481" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_40.webp" width="691" height="832" loading="lazy" alt="Blog Image" />

## **Raytac DK with Half hole module**

**2023년 11월 28일 화요일**

*오후 1:32*

**https://www.raytac.com/product/ins.php?index\_id\=114**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_41.webp" width="1200" height="811" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_42.webp" width="1200" height="794" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_43.webp" width="1200" height="791" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_44.webp" width="1200" height="827" loading="lazy" alt="Blog Image" />

## **Raytac DK with SMD module**

**2023년 11월 28일 화요일**

*오후 1:35*

**https://www.raytac.com/product/ins.php?index\_id\=130**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_45.webp" width="1200" height="789" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_46.webp" width="1200" height="807" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_47.webp" width="1200" height="786" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_48.webp" width="1200" height="807" loading="lazy" alt="Blog Image" />

## **튜닝부품 키트**

**2023년 11월 28일 화요일**

*오후 2:21*

**https://www.devicemart.co.kr/goods/view?no\=1313419**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_49.webp" width="1200" height="543" loading="lazy" alt="Blog Image" />

**https://www.devicemart.co.kr/goods/view?no\=1313427**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_50.webp" width="1200" height="551" loading="lazy" alt="Blog Image" />

**Module test/모듈테스트**

**2023년 11월 29일 수요일**

*오전 9:35*

**http://www.jig\-hitech.co.kr/page/product01\_02\.php**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_51.webp" width="850" height="1040" loading="lazy" alt="Blog Image" />

https://www.indiamart.com/proddetail/esp8266\-burner\-fixture\-test\-board\-development\-board\-for\-esp\-12s\-12f\-12e\-07s\-07\-series\-module\-23199561897\.html

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_52.webp" width="1034" height="936" loading="lazy" alt="Blog Image" />

https://www.instructables.com/DIY\-ESP8266\-ESP\-12\-Socket\-Snap\-Fit\-Breadboard\-Frie/

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_53.webp" width="696" height="773" loading="lazy" alt="Blog Image" />

https://ko.aliexpress.com/i/32802723152\.html?gatewayAdapt\=glo2kor

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_54.webp" width="582" height="555" loading="lazy" alt="Blog Image" />

https://hackaday.com/2022/03/07/flexypins\-might\-help\-with\-those\-pesky\-castellated\-modules/

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_55.webp" width="815" height="467" loading="lazy" alt="Blog Image" />

https://www.espressif.com/en/products/equipment/production\-testing\-equipment/overview

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_56.webp" width="824" height="686" loading="lazy" alt="Blog Image" />

https://forum.contextualelectronics.com/t/test\-jig\-for\-esp8266\-modules/4637

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_57.webp" width="991" height="688" loading="lazy" alt="Blog Image" />

## **231214\_모듈개발 2차 미팅.**

**2023년 12월 11일 월요일**

*오후 3:07*

**개발고려**

개발품목 : 모듈 2종과 EVB 2종 중

개발자료 : 회로도 PDF, 거버파일, PCB DXF파일

지그개발 방향, 난이도/외주?

기존캔 사용 : 기 Datasheet를 참고하여 모듈 설계

모듈설계하면서(Ratac사 모듈검토) 캔 납땜 위치제공\=\=\> CAN제작

모듈샘플구매

**231222**

**\[대표B]님 통화**

**모듈 컨셉**

**모듈의 크기는**

Raytac사의 MDBT42\-512KV2 또는 MDBT42\-P512KV2 크기/Half hole 참고하여 설계.

**위 모듈은 nRF52832 WLCSP 기준으로 설계되어 있으나**

**우선 개발모듈은 nRF52805를 위 모듈의 크기에 맞춰서 설계하고**

**차후 nRF52832 WLCP를 적용해서 모듈을 추가로 개발할 때 동일한 CAN을 사용하고자 함.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_58.webp" width="1200" height="640" loading="lazy" alt="Blog Image" />

**회로설계 결정사항**

Module

**PCB Size : 8\.8 x 13\.8**

**PCB T : 0\.8T**

**PCB Layer : 2L**

**RF IC :nRF52805**

**With out : 32\.768Khz,DCDC inductor**

**Ant : pattern and chip**

**32Mhz : 1612 / 차후 nRF52832WLCP모듈 공용**

**L , C : nRF52805 Ref from Nordic**

EVB

## **CAN Dimension\_PPT**

**2023년 12월 27일 수요일**

*오전 11:29*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_59.webp" width="1200" height="675" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_60.webp" width="1200" height="675" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_61.webp" width="1200" height="674" loading="lazy" alt="Blog Image" />

## **For CAD\_PPT**

**2023년 12월 27일 수요일**

*오후 2:52*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_62.webp" width="1200" height="668" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_63.webp" width="1200" height="671" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_64.webp" width="1200" height="667" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_65.webp" width="1200" height="672" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_66.webp" width="1200" height="675" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_67.webp" width="1200" height="527" loading="lazy" alt="Blog Image" />

## **EVB배치 참고**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_68.webp" width="1200" height="794" loading="lazy" alt="Blog Image" />

## **240109\_모듈개발 3차 미팅.**

**2024년 1월 9일 화요일**

*오후 12:08*

## **J\-link Pin out**

**2024년 1월 31일 수요일**

*오전 11:08*

**https://wiki.segger.com/20\-pin\_J\-Link\_Connector**

**Pinout for JTAG**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_69.webp" width="414" height="348" loading="lazy" alt="Blog Image" />

**https://www.devicemart.co.kr/goods/view?no\=1179243**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_70.webp" width="1200" height="667" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_71.webp" width="892" height="607" loading="lazy" alt="Blog Image" />

**https://ko.aliexpress.com/i/32428874079\.html**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_72.webp" width="1082" height="832" loading="lazy" alt="Blog Image" />

## **CAD 검토1**

**2024년 1월 29일 월요일**

*오전 5:29*

**Module**

쉴드캔 부품기구

**쉴드캔 데이터올림, 두께표시**

쉴드캔 고정패트

**Non plate 적용**

**J8: 왼쪽으로 조금이동,**

**홀작음 \=\=\>**

**R값?**

쉴드캔 납땜패드

**노출**

안테나 폭, 길이

BOTTOM PAD size1

## **CAD검토2**

**2024년 1월 29일 월요일**

*오후 1:54*

**Module**

Bottom면 pad size 크기 작음.

TP3, TP4 추가/회로도 변경함.

* → Bottom면에 1파이 Pad추가

**For Cad.pdf 3, 4page 참고**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_73.webp" width="380" height="279" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_74.webp" width="548" height="323" loading="lazy" alt="Blog Image" />

**SILK**

1. 1\. Module

**\-Pattern 안테나 Bottom 영역 : GW\_MHP52805\_V1\.0**

**\-Chip 안테나 Bottom 영역 : GW\_MHC52805\_V1\.0**

Main

**GW\_EVB\_MHP52805\_V1\.0**

**회로도에 있는 각 초록색에 대한 SILK 표기 부탁드립니다.**

## **CAD 검토3**

**2024년 1월 30일 화요일**

*오전 5:48*

**Module**

쉴드캔

**J8은 쉴드캔 센터라인에 배치, J8하단부 GND copper도 J8라인과 일치.**

**J8의 센터점과 쉴드캔 아랫쪽 과의 거리가 3\.8\-0\.75\=3\.05 인데, 2\.949정도로 다소 짧음.**

**쉴드캔 납땜패트 노출.**

배치 / 미리 말씀을 드려야 했는데.. 죄송합니다.

* → RF단 구간 최소화해서 Loss를 없게 해야 될 거 같습니다.

**아래 처럼 일자로 꼭 되지 않더라도 아무래도 수정을 좀 해 봐야 될 거 같아요..**

**U2배치를 최대한 위쪽으로 이동 배치를 해서 RF단과 5,6 pad 연결배선을 좀 수정해야 될거 같아요.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_75.webp" width="531" height="250" loading="lazy" alt="Blog Image" />

* → 5,6pad로 연결되는 패턴 길이를 최대한 줄여서 GND공간확보

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_76.webp" width="637" height="469" loading="lazy" alt="Blog Image" />

배선

**11pin via 없이 top에서 패턴연결**

**15pin으로 연결되는 via 위쪽으로 이동, C10 위치 이동.**

안테나

**안테나를 위,아래 우측 PCB외곽에 최대한 붙여서 배치.**

* → 안테나와 GND 간격이격
* → 시작점도 위쪽으로 같이 이동.
* → x축 가로방향 길이 반영은 시작점에서 우측으로 연결되는 길이만 증가.
* → Y축 양측(위,아래)로 늘어난 길이는 증간 3단 웨이브의 세로길이만 균등배분

Pin 간격

**0\.9mm/전체적용**

* → 기준 9pin\-\-\-\-\>2pin / 1pin고정
* → 10pin\~16pin : 왼쪽 면 센터기준으로 0\.9mm간격
* → 17pin\~19pin : 위쪽 9pin과 라인정렬 및 0\.9mm간격 / 19pin고정

Pad size

**Bottom 에 있는 pad : 0\.4 x0\.8**

**단, 1pin : 길이만 1\.2mm , 19pin : 유지**

PAD GND 연결 및 Copper보강

**Top : 10,16 : copper보강**

**Bottom의 10, 16, 1, 19pin도 GND 연결 및 copper 보강**

U2 GND via

**가운데에 Via 적용 /52805데이터시티 참고**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_77.webp" width="851" height="850" loading="lazy" alt="Blog Image" />

**Nordic datasheet**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_78.webp" width="560" height="963" loading="lazy" alt="Blog Image" />

U2 pin 간격

**G1\~G2간 간격 안맞음.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_79.webp" width="626" height="410" loading="lazy" alt="Blog Image" />

**Main**

Conn영역 제거

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_80.webp" width="440" height="850" loading="lazy" alt="Blog Image" />

**SILK**

1. 1\. Module

**\-Pattern 안테나 Bottom 영역 : GW\_MHP52805\_V1\.0**

**\-Chip 안테나 Bottom 영역 : GW\_MHC52805\_V1\.0**

1. 2\. Main

**GW\_EVB\_MHP52805\_V1\.0**

**회로도에 있는 각 초록색에 대한 SILK 표기 부탁드립니다.**

## **CAD 검토4**

**2024년 1월 31일 수요일**

*오전 8:01*

**Module**

19pin top, Bottom Pad 확장 \=\=\> CAN홀 까지

* → CAN도 GND이므로 쇼트문제 없음.

Y1 90도 시계방향회전

**배선 짧게유지**

TP3, TP4 silk 위치 오버랩?

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_81.webp" width="481" height="411" loading="lazy" alt="Blog Image" />

안테나 끝선 웨이브라인에 맞춰서 잘라내 주세요.

**EVB**

Module 납땜 pad 위치 안맞는거 같은데요? 일치 또는 조금 더 커야 할거 같은데요.

**Module의 Pad들이 EVB GND Copper 닿을 것으로 보임.**

CONN1

**A5,B5 pad size 조정**

## **CAD 검토5**

**2024년 1월 31일 수요일**

*오전 10:36*

**Module**

Y1 GND 이격이유?

J8 센터와 쉴드켄 아랫쪽과의 거리 2\.949mm \=\=\>3\.05mm

Via 포함하여 copper보강

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_82.webp" width="553" height="354" loading="lazy" alt="Blog Image" />

**Main**

2\~9 Pad좌우 Copper와 이격 좀만 더해 줘요.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_83.webp" width="1132" height="507" loading="lazy" alt="Blog Image" />

**18, 17 Pad 좌우도 이격 좀만 더 해줘요.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_84.webp" width="371" height="442" loading="lazy" alt="Blog Image" />

J9 핀넘버 실크

**1,2,9,10번 4개만 써 주세요.**

**아랫쪽에 All GPIO도 넣어 주세요.**

J7번 우치

**c17라인 위치정도로 내려 주세요.**

J5, J2 네모박스안에 좀 넣어 주세요. 그리고 J\-Link라고 좀 넣어 주세요.

## **CAD 검토6**

**2024년 2월 1일 목요일**

*오전 7:19*

**Module**

**EVB**

모듈과 납땜되는 패드에서 라인 안쪽으로의 길이가 1\.4mm입니다.

**이 길이를 유지하려면 모듈의 GND 공간도 좀더 좁혀야 되는데**

**그렇게는 안하는게 좋겠습니다.**

**그냥, 모듈의 Pad 길이 처럼 1\.2mm와 동일하게 해 주세요. GND copper는 그냥 두시구요.**

**어차피 pad size가 납땜에는 문제가 안되니까요.**

J\-Link Silk 박스 들어 간거 같긴한데… 흰색으로 안보이네요?

J7 위치는 좋구요.

**Current 글씨는 J7 아래쪽에 넣어 주세요.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_85.webp" width="1067" height="875" loading="lazy" alt="Blog Image" />

TP1, TP2를 반시계방향으로 90도 돌려주세요.

**납땜해서 쓰는 Pad인데 가로 배치가 더 좋을 것 같습니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_86.webp" width="280" height="257" loading="lazy" alt="Blog Image" />

회로도에 C21 \=\=\> NC/1005로 변경 좀 해 주세요.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_87.webp" width="400" height="241" loading="lazy" alt="Blog Image" />

## **CAD 검토7**

**2024년 2월 5일 월요일**

*오전 7:18*

**L7을 C7 라인에 맞춰 주세요.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_88.webp" width="456" height="811" loading="lazy" alt="Blog Image" />

**쉴드캔 왼쪽상단 : 모서리에서 가로방향은 납땜이 되어야 하고**

**세로방향은 납땜 부위가 없는데**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_89.webp" width="442" height="435" loading="lazy" alt="Blog Image" />

**마스크 확인**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_90.webp" width="928" height="574" loading="lazy" alt="Blog Image" />

## **CAD 검토7 최종\_\[고객사]공유**

**2024년 2월 2일 금요일**

*오후 2:25*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_91.webp" width="681" height="689" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_92.webp" width="706" height="582" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_93.webp" width="1200" height="983" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_94.webp" width="1137" height="777" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_95.webp" width="1138" height="788" loading="lazy" alt="Blog Image" />

## **패턴안테나 메칭 /형상추가검토**

**2024년 2월 15일 목요일**

*오후 12:38*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_96.webp" width="470" height="418" loading="lazy" alt="Blog Image" />

**Pattern과 Chip안테나 겸용 회로이므로 패턴안테나 E1에 대해**

**L3, C7, L4(0603size)로 메칭이 필요합니다.**

## **단, Main BD에 Module PCB가 납땜된 상태에서 안테나 메칭을 요청 드립니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_97.webp" width="1157" height="724" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_98.webp" width="436" height="447" loading="lazy" alt="Blog Image" />

**검토사항**

**\[고객사]는 Raytac모듈의 RF특성중 RF도달 거리가 어느정도인지 시험해 본 적이 있는지?**

**\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=**

## **1차 패턴안테나 메칭의뢰**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_99.webp" width="584" height="802" loading="lazy" alt="Blog Image" />

**1\.이슈 : Gain이 현재 너무작은 상태.**

**안테나 wave부분과 PCB GND간의 간격이 협소하여 C값에 의해 특성열화**

**1차 메칭 후 측정**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_100.webp" width="1200" height="590" loading="lazy" alt="Blog Image" />

**2차 메칭 후 측정**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_101.webp" width="1200" height="581" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_102.webp" width="1200" height="384" loading="lazy" alt="Blog Image" />

비교 Raytac 모듈 /동일 크기

**Raytac모듈 특성 /datasheet**

**Peak gain 낮으며 \[고객사]모듈의 특성과 큰 차이(챔버오차) 없음.**

**또한, Gain특성은 Peak EIRP데이터를 그대로 복사하여 사용한 것으로 보임.**

**Gain은 360도 구간 평균이어야 함으로 더 낮게 Peak보다 훨씬 낮은 측정치를 보여야 함.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_103.webp" width="467" height="105" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_104.webp" width="1200" height="199" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_105.webp" width="1200" height="203" loading="lazy" alt="Blog Image" />

**\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=**

안테나 고찰

**설계보드**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_106.webp" width="1097" height="786" loading="lazy" alt="Blog Image" />

**Raytac보드**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_107.webp" width="525" height="323" loading="lazy" alt="Blog Image" />

성능개선안/ Gain

**GND 이격, 안테나 폭 축소**

**검토1\) 아래는 USB 동글 설계자료 / 모듈의 2차 측정과 비슷함.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_108.webp" width="1004" height="543" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_109.webp" width="1200" height="553" loading="lazy" alt="Blog Image" />

**검토2\)**

**안테나 형상은 아래와 같이 길이가 짧더라도 wave를 취하지 않는 형태**

**안테나 형상에 대한 고찰 : 전화통화함\_240226**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_110.webp" width="1200" height="900" loading="lazy" alt="Blog Image" />

## **Chip안테나 메칭**

**2024년 2월 15일 목요일**

*오후 12:47*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_111.webp" width="470" height="418" loading="lazy" alt="Blog Image" />

**Pattern과 Chip안테나 겸용 회로이며, 안테나만 다르게 하여 개별로 PCB가 제작됩니다.**

**칩안테나 E2에 대해 L3, C7, L4, L7(0603size)로 메칭이 필요합니다.**

## **Main BD에 Module PCB가 납땜된 상태에서 안테나 메칭을 하는 것이 좋을 것 같습니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_112.webp" width="1200" height="789" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_113.webp" width="993" height="942" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_114.webp" width="1200" height="781" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_115.webp" width="1200" height="836" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_116.webp" width="1200" height="884" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_117.webp" width="1200" height="844" loading="lazy" alt="Blog Image" />

## **PCB 1차입고**

**2024년 2월 19일 월요일**

*오전 10:51*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_118.webp" width="783" height="654" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_119.webp" width="759" height="589" loading="lazy" alt="Blog Image" />

**모듈 랜드형성 문제**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_120.webp" width="648" height="481" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_121.webp" width="639" height="486" loading="lazy" alt="Blog Image" />

**CAN 안착상태**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_122.webp" width="643" height="477" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_123.webp" width="643" height="490" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_124.webp" width="638" height="480" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_125.webp" width="646" height="483" loading="lazy" alt="Blog Image" />

## **PCB 2차 입고\_모듈**

**2024년 2월 29일 목요일**

*오전 7:16*

**Half Hole 제작시 참고.**

**\[PCB제작업체B] Half Hole사양기준**

**Half hole 드릴 : 0\.4**

**Half hole pad : 0\.6**

**Half Hole 드릴 : 규정은 0\.8, 최소치 : 0\.4 / 라우팅드릴이 1\.0이므로**

**하프홀을 더 작게 사용하면 홀이 붕괴됨.**

**Half Hole패드 : Half hole의 도금을 살리기 위해 판넬도금방식에서는**

**드라이필름의 특성을 고려하여 Hole좌,우로 0\.1mm 이상**

**PAD를 넣어줘야 함.**

**애칭공법에 따라서 Half Hole생성시 공정상 보정이 필요함.**

**애칭**

1. 1\)판넬도금 : 드라이필름사용 / 현재 일반적인 공법
2. 2\)패턴도금 : 납사용 / 예전공법, Raytac모듈이 사용했을 것으로 보이나

**HPL공정을 적용했기 때문에 정확히 어떤방법으로 제조했는지**

**파악이 어려움.**

**메탈거버 1번**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_126.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_127.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_128.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_129.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

**메탈거버 2번**

**Half hole 드릴 :0\.4 / 생산공정반영 최소치**

**PAD 설계 : 0\.4,**

**PAD보정 : 0\.45 / 0\.4드릴기준 0\.6이 최소치**

* → 애칭시 도금 없어짐.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_130.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_131.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_132.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_133.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

**메탈거버 3번**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_134.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_135.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_136.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_137.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

**메탈거버 1번(Half Hole 도금안됨)과 참고 제품의 PAD 크기 비교**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_138.webp" width="1200" height="890" loading="lazy" alt="Blog Image" />

**메탈거버 2번(최소사양 : 0\.4드릴, 0\.6pad로 CAM에서 수정) 과 참고제품의 PAD, 간격비교**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_139.webp" width="1200" height="897" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_140.webp" width="641" height="481" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_141.webp" width="645" height="485" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_142.webp" width="644" height="479" loading="lazy" alt="Blog Image" />

## **PCB 3차 입고\_모듈**

**2024년 3월 8일 금요일**

*오전 5:10*

Half Hole 형성/ 도금상태

**Half Hole : 0\.6pad, 0\.3 dril 로 보정해봄/ 원본 : 0\.4pad, 0\.3 dril**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_143.webp" width="1200" height="895" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_144.webp" width="1200" height="881" loading="lazy" alt="Blog Image" />

Half Hole형성/ Burr 제거가 아닌 방지

**라우팅전에 Half Hole 왼쪽에 1차 드릴처리.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_145.webp" width="695" height="527" loading="lazy" alt="Blog Image" />

## **RF 튜닝결과**

**2024년 3월 18일 월요일**

*오전 8:51*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_146.webp" width="794" height="1165" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_147.webp" width="798" height="873" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_148.webp" width="787" height="1154" loading="lazy" alt="Blog Image" />

**1차 개발 SMD후 전반내용점검**

**2024년 3월 8일 금요일**

*오전 5:20*

RF

## **튜닝전과 튜닝 후 결과참고 및 안테나 메칭결과 /raytac 특성비교\_칩, 패턴, Raytac**

**모듈 to 모듈간 통신시 거리확인**

**모듈 to 휴대폰간 통신시 거리확인**

## **안테나 특성개선 추가검토/패턴안테나 메칭 정리내용의 마지막 성능개선안참고**

PCB제작

**Half Hole 설계**

* → 과정과 설계수정

**Half hole 형성 룰에 따른 Pad size 및 드릴 치수 CAD설계변경, Burr 발생방지,**

개선검토 /2차샘플 또는 최종자료에 적용

1. 1\) Half Hole : Pad 및 드릴 치수수정 0\.4/0\.3\=\=\>0\.6/0\.4(PCB공정)

**GND보강 : 측면 GND Half hole 추가여부, 변경시 EVB도같이 GND 추가**

1. 2\) EVB

**U4 수납땜시 핀헤더간섭**

* → J6, J4, J1을 1608 0ohm으로 변경여부
* → J9, J10 오른쪽으로 이동
1. 3\) 모듈 ANT 특성 / 추가설계검토여부

**현재 안테나 특성결과 비교 3종\_패턴, 칩, Raytac**

1. 4\)) 쉴드캔 CAN 릴패킹시 릴포캣이 유격이 커서 부품이 일정하게 안착되지 않음(SMT공정)

모듈 Kit Array 배치

1. 1\) JIG 제작업체와 협의된 사항 있는지?

**전체 모듈 개수, JIG에서 필요한 어레이배치 등.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_149.webp" width="360" height="848" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_150.webp" width="653" height="1012" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_151.webp" width="892" height="1073" loading="lazy" alt="Blog Image" />

## **1차 개발 SMT 후 CAD수정요청**

**2024년 3월 22일 금요일**

*오전 11:09*

수정

**모듈 2종 및 EVB**

**EVB에 모듈회로제거함**

수정내용

**\-쉴드캔과 간섭우려 : C10, L2, C7**

* → 쉴드캔이 고정된 상태로 부품전체를 아래쪽으로 0\.2mm 이동배치.
* → 안테나는 이동없이 고정.
* 측면 Half Hole : PCB 가공상 여러 이유에 의해 기본룰 적용.
* → 드릴 : 0\.4mm, PAD size : 0\.6mm,
* → 1, 19pin도 동일하게 적용.

메인보드

* → 모듈 Pad에 맞게 수정.
* → R16,R17 풀업추가

**U4 수납땜시 핀헤더간섭**

* → J6, J4, J1을 1608 0ohm으로 변경/R18,R19,R20추가
* → J9, J10 오른쪽으로 이동

Half Hole 참고 이미지

**아래이미지 4장은 Half Hole이 정상이며,**

**기존 CAD설계데이터에서 CAM작업하면서 보정값 반영한 경우**

**의 이미지이며, 정상으로 Via가 형성됨. 그 값이 0\.4/0\.6임.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_152.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_153.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_154.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_155.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

**아래 이미지는 4장은 Half Hole의 불량품 이미지 이며**

**기존 데이터 그대로 제작시 Via Hole이 에칭시 형성을 시키지 못한거라고함.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_156.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_157.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_158.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_159.webp" width="1101" height="822" loading="lazy" alt="Blog Image" />

**따라서, CAD수정을 하는 이유는 PCB가 문제없이 제작되는 보정값을 적용했을때**

**Half Hole 쪽 PAD가 이형적인 모양으로 만들어 지므로, 보기가 좋지 않을뿐더러**

**제품제공시 또다른 이슈거리가 발생될 수 있어서 근본적으로 PAD크기를 일률적으로**

**하기 위함.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_160.webp" width="497" height="328" loading="lazy" alt="Blog Image" />

## **모듈설계 H/W 차별화**

**2024년 2월 15일 목요일**

*오후 12:57*

**1\.측면 Half Hole PAD에 Via를 적용하여 Main B/D와의 연결성을 강화함.**

**Half Hole 측면이 기타 이유에 의해 손상되어도 Pad on Via에 의해 연결성이 확보됨.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_161.webp" width="1200" height="777" loading="lazy" alt="Blog Image" />

모든 Via에 대해 HPL 적용

**Via에서 생성되는 GAS가 없기 때문에 RF IC 및 주변 부품이 GAS에 의한**

**냉납 발생을 막아 줌.**

**또한 Main B/D와 밀착납땜시 주변 패턴과의 간섭을 차단함.**

X\-Tal 주변 Copper 분리를 통해 주변 Noise에 의해 영향을 적게 받음.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_162.webp" width="367" height="463" loading="lazy" alt="Blog Image" />

## **모듈생산지그관련**

**2024년 4월 29일 월요일**

*오전 10:29*

**모듈 지그 문의/방문**

**1\.테스트블럭의 재질/RF 시험관련**

**2\.메인보드와 핀연결방식(듀얼,싱글)/장단점**

**3\.Pin 간격 0\.9mm**

* → 최소간격??/차후 설계시

회로부 제작 검토

**\-지그샘플확인, 모듈테스트 시나리오에 따른 지그회설계검토.**

**\-테스트 블럭 케이스안에 메인보드 장착여부/ 외부 별도 케이스적용여부**

**\-전원공급연결구성**

**\-프로그램핀연결구성**

F/W 프로그래밍

## **\-Module test FW , Module 제품 FW 프로그래밍**

* → 테스트용과 판매용 펌웨어를 하나로 구성하여

**프로그래밍을 한 번만 할지….??**

테스트시나리오

1. 1\) RF 주파수
2. 2\) RF 출력레벨
3. 3\) I/O테스트

**쇼트, 오픈**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_163.webp" width="704" height="545" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_164.webp" width="694" height="538" loading="lazy" alt="Blog Image" />

**\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=**

**H/W 설계검토 안**

**물리적연결 테스트**

I/O test 1

IC, Pad에서 I/O간 쇼트,

**모든 I/O는 Pull\-up상태(외부 Pull\-up)**

**소프트웨어로 특정 I/O에 대해 Out mode, Low출력 설정 후**

**나머지 I/O는 Input mode로 설정한 상태에서 High상태를 확인하고**

**(GND쇼트확인, 연결오픈확인)**

**Low 입력이 되는 I/O가 있는지.**

**(I/O간 쇼트확인)**

**모든 I/O에 대해 순차적으로 반복확인.**

**임의의 I/O는 테스트모드진입 및 다음테스트항목 이동**

**임의의 I/O 1개를 결과표시용으로 사용.(LED 및 부저)**

모드용 및 표시용 LED를 제외하고 나머지 I/O에 LED를 연결하여

**LED의 순차점등 동작을 육안으로 확인하여 I/O의 연결상태를 확인한다.**

**RF Signal 확인**

1. 1\. Gain 확인

**JIG의 버튼에 의해 Becon mode로 진입 / 또는 APP에서 Signal 확인 되는 모드.**

* nRF Tool / phone APP

**RSS값확인**

주파수확인

**JIG의 버튼에 의해 특정 RF ch 출력/ DTM모드의 constant carrier**

**\-스팩트럼아날라이져로 주파수 In range 확인.**

**100EA 단위로 Sampling test.**

## **모듈 소켓 설계도면**

**2024년 6월 4일 화요일**

*오후 4:04*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_165.webp" width="1200" height="954" loading="lazy" alt="Blog Image" />

**DDDF**

## **모듈생산지그용 보드설계**

**2024년 5월 16일 목요일**

*오전 8:14*

EVB 회로도

\<\<PCA10040\_Schematic\_And\_PCB\-nskim.pdf\>\>

설계구성 컨셉

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_166.webp" width="862" height="420" loading="lazy" alt="Blog Image" />

모듈소켓설계건 문의사항

**모듈이 안착되는 PCB Layout**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_167.webp" width="761" height="616" loading="lazy" alt="Blog Image" />

모듈과 PCB Layout에 있는 18EA pad간의 연결은 납땜이 아닌 스프링핀 접촉인지요?

소켓의 재질?

**PCB에 닿는 부분 중 메탈소재?**

## **\=\=\>소켓이 소켓보드와 접촉되는 영역 실크적용 및 절연지**

**모듈회로도**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_168.webp" width="908" height="719" loading="lazy" alt="Blog Image" />

**소켓GPIO pin 구성**

**전원부 5V인가 옵션처리??: 안함.**

**전원용 콘덴서 추가**

**EVB의 커넥터 P1,2,3,4,6 사용하여 보드설계,**

**모듈의 모든 PAD의 PIN이 회로구성이 되도록 설계.**

**\-P0\.01, P0\.00은 I/O로 확인할지, 32\.768K X\-tal 연결하여 확인할지?**

* → 32\.768K 디폴트구성, 옵션으로 I/O구성

## **\-DCC, DEC4는 소켓보드의 DCDC회로구성, 구성에 따라 소프트웨어로 설정여부?**

**\-나머지 I/O는 EVB의 U1(nRF52832\) AIN0\~7 로 연결구성.(위 빨간 점 I/O)**

**전원은 VIO\=VDD\=VDD\_nRF 같으며 P1의 1,2 pin(VIO), 6,7(GND)를 사용.**

**Shield detect pin 사용여부?**

* → 사용한다면 pin 처리 방안은?

**PCA10040의 SB18을 납땜하여 GND인가.**

## **(소켓보드에서 처리시 소켓보드와의 커넥터연결성이 좋지 않음)**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_169.webp" width="552" height="941" loading="lazy" alt="Blog Image" />

**Programming**

## **P20 커넥터 활용\=\=\>소켓보드와 연결?**

## **Select pin 별도로 회로구성 : 소켓보드에서 High 처리?**

* → shield select pin헤더처리 필요.

**P20이 8pin은 GND detect pin인데, PCB에서 패턴으로 연결된 곳이 없음.**

* → 하지만 P20의 8pin GND 디텍터 사용하여 J\-link 또는 EVB 를 선택하여

**프로그래밍 할 수 있는 pin헤더를 넣어 놓을 것.**

* →

**P20커넥터는 사용하지 않고, J\-Link만 사용하기로 함.**

**P20사용시 연결이 불안정한 경우가 있음.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_170.webp" width="1185" height="440" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_171.webp" width="927" height="239" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_172.webp" width="650" height="485" loading="lazy" alt="Blog Image" />

**전원 및 USB to serial**

**https://sheep\-thrills.net/FT230X\_SMD\_module.html**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_173.webp" width="948" height="801" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_174.webp" width="809" height="961" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_175.webp" width="1200" height="274" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_176.webp" width="1200" height="755" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_177.webp" width="1200" height="865" loading="lazy" alt="Blog Image" />

\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

## **1차 소켓보드 컨셉**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_178.webp" width="1200" height="580" loading="lazy" alt="Blog Image" />

## **2차 소켓보드 컨셉**

**JIG보드설계는 아래 그림 참고**

**핀헤더 소켓은 dip type으로 적용하여 안정성 확보**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_179.webp" width="707" height="942" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_180.webp" width="1200" height="650" loading="lazy" alt="Blog Image" />

https://devzone.nordicsemi.com/f/nordic\-q\-a/27786/flashing\-external\-board\-using\-nrfgo\-studio

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_181.webp" width="784" height="594" loading="lazy" alt="Blog Image" />

**J\-link 참고**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_182.webp" width="1200" height="352" loading="lazy" alt="Blog Image" />

**20\-pin J\-Link Connector**

**https://wiki.segger.com/20\-pin\_J\-Link\_Connector**

**SWD 인터페이스 기준으로 Pin 구성할것**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_183.webp" width="1200" height="714" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_184.webp" width="1200" height="229" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_185.webp" width="876" height="1117" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_186.webp" width="11" height="11" loading="lazy" alt="Blog Image" />

## **모듈데이터시트 리뷰**

**2024년 6월 4일 화요일**

*오전 7:12*

GX805C

**추후 양산용 쉴드캔적용하여 사진 변경이 되면 좋을 것 같습니다.**

**또한 모듈의 Pad도 Half Hole을 사용하지 않기로 했기 때문에**

**추후 변경된 PCB로 SMT이후 사진을 적용하는게 좋겠습니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_187.webp" width="331" height="433" loading="lazy" alt="Blog Image" />

GX805는 패턴안테나모듈의 모델명 이므로

**(모듈명 확정시 처음부터 Chip안테나는 "C" 가 붙었고, 패턴안테나는 붙는게 없습니다)**

**아래와 같이 GX805는공통이름으로 쓰였지만 2모듈의 공통이름이라고 보기는 어려워서**

**사용자가 주문할때 다소 헛갈릴 수 있겠습니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_188.webp" width="915" height="306" loading="lazy" alt="Blog Image" />

## **모듈 및 DK PCB설계변경**

**2024년 6월 7일 금요일**

*오후 1:39*

\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

**모듈 설계변경 검토 /\[고객사] 미팅시 공유**

Half Hole 제거 및 Silk 변경에 따라 RF 특성에 영향에 대한 문의.

**답변(안테나설계업체) : 방사특성에 있어서 충분히 달라질 수 있다.**

**이유는 모듈이 작기 때문에 PAD의 납땜량이 GND 조건에**

**영향을 미칠 수 있고 Silk에 의해 Main B'D 밀착되는부분의 유전율이**

**차이가 있어서 작게나마 영향이 있을 수 있다.**

* → 튜닝단과 안테나메칭단 특성 확인작업 필요.

PCB를 신규로 제작하여 SMT후 특성확인을 하기로 준비하고 있으나

**PCB를 제작하기 전에 PCB수정을 통해 GND 조건을 최대한 추가로 보상하는 방법.**

* → 패드추가 하여 진행 검토. (기존에는 패턴을 일부 배선고려)
* → KC인증 전에 수정사항 반영

**Main\_TOP**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_189.webp" width="660" height="455" loading="lazy" alt="Blog Image" />

**Module\_BOT**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_190.webp" width="704" height="476" loading="lazy" alt="Blog Image" />

진행

* → SUB, Main 모두 CAD 수정 : 외부업체
* → PCB발주 및 부품 : \[고객사]
* → SMT : \[고객사]
* → 튜닝 : \[외주RF튜닝업체]
* → 메칭확인 : 외부업체

**외부업체 건은 일부비용이 발생됩니다.**

**CAD수정 : 모듈 2종 EVB 1종**

* → Module 의 GND Pad는 3 Point 추가.
* → EVB의 PAD는 데이터시트 기반으로 Main Board PAD 형성.

\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

## **\[담당자D]공유**

Module

**GND pad 추가**

**안테나 형상 1종 추가 : 파일명은 "\-1" 추가되어서 다르게 구분하지만 Silk는 GX805와 동일함.**

* → 모듈 총 3종

EVB

**GND Pad추가 및 전체 Pad size 조정**

**실크변경 : GW\_EVB\_MHP\&C52805\_V1\.1\=\=\> GW\_EVB\_GX805\_V1\.0**

공통사항

**설계명 변경 : 파일명 참고하여 도면에 표시명 변경 부탁드려요..**

수정관련 참고 내용

**GND Pad 추가**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_191.webp" width="1049" height="786" loading="lazy" alt="Blog Image" />

**안테나 형상 추가 관련**

**정해진 길이 없음: 안테나 부품메칭으로 보상, 길이는17mm예상, 폭은 0\.3mm,**

**(GND pad추가는 위와 동일하게 적용)**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_192.webp" width="1026" height="717" loading="lazy" alt="Blog Image" />

**EVB**

**모듈에 추가된 패드와 동일한 위치에 PAD추가**

**PAD size는 아래 그림을 참고하여 size 조정**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_193.webp" width="800" height="929" loading="lazy" alt="Blog Image" />

**\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=**

## **CAD 검토**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_194.webp" width="574" height="128" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_195.webp" width="979" height="626" loading="lazy" alt="Blog Image" />

## **패턴안테나 메칭의뢰/2차**

**2024년 7월 16일 화요일**

*오전 6:10*

**회로도/ 안테나 2종 동일**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_196.webp" width="639" height="456" loading="lazy" alt="Blog Image" />

모노폴웨이브 안테나

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_197.webp" width="1066" height="682" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_198.webp" width="398" height="706" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_199.webp" width="567" height="596" loading="lazy" alt="Blog Image" />

1. 2\)모노폴안테나

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_200.webp" width="1062" height="687" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_201.webp" width="389" height="694" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_202.webp" width="520" height="614" loading="lazy" alt="Blog Image" />

## **Chip안테나 메칭/2차**

**2024년 7월 19일 금요일**

*오전 10:31*

**\[고객사]에서 \[담당이사A]에게 모듈 PCB 및 EVB 전달하기로 함.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_203.webp" width="1200" height="886" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_204.webp" width="1200" height="887" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_205.webp" width="1200" height="888" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_206.webp" width="1200" height="888" loading="lazy" alt="Blog Image" />

## **240828\_미팅**

**2024년 8월 28일 수요일**

*오후 1:50*

## **1\.대만 안테나 메칭 이후 미팅**

* 안건 : 1\)효율때문에 PAD설계 변경 또는 유지에 관련된 내용.
1. 2\)회신 주신 칩 안테나(CW804\) 로 재설계를 해야 하는지에 대한 내용.
2. 3\)메칭 검토 10페이지 BOM 반영 관련 내용
3. 4\)기타 사항
* → Chip 안테나 변경하여 PCB 설계변경.

## **소켓보드 : 회로에서 USB \-c 커넥터 제거**

**T**

**s**

## **CAD 검토\_소켓보드**

**2024년 10월 8일 화요일**

*오전 8:08*

SW1

**ON, OFF의 실크 위치를 서로 바꿔서 배치.**

**(스위치를 오른쪽으로 당기면 1\-2간 연결되어 ON되므로 ON 실크를 스위치 오른쪽에 배치)**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_207.webp" width="432" height="330" loading="lazy" alt="Blog Image" />

회로도 수정을 좀 했습니다.

**아래 2곳 입니다.**

**TX를 \=\=\>RX로, RX를 \=\=\>TX로 변경.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_208.webp" width="629" height="321" loading="lazy" alt="Blog Image" />

* → 변경

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_209.webp" width="726" height="343" loading="lazy" alt="Blog Image" />

**R17 GND를 아래와 같이 변경했습니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_210.webp" width="462" height="197" loading="lazy" alt="Blog Image" />

아래 영역에 있는 TP 및 부품을 모두 Bottom에 배치해야 될 것 같습니다.

**검토하다 보니 소켓기구가 PCB에 완전 밀착이 되더라구요..**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_211.webp" width="463" height="478" loading="lazy" alt="Blog Image" />

## **소켓보드 전류 제한**

**2025년 1월 17일 금요일**

*오전 8:45*

## **소켓보드를 사용하여 Module을 시험하는 과정에서 모듈이 열이 발생하는 경우**

**전원을 차단하고자 함.**

모듈이 모든시험에서 정상적으로 동작함에도 불구하고 어딘가 쇼트현상에 의해 전류를 과다하게 소모하고 있고, 이때 모듈에서 열이 발생함.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_212.webp" width="1007" height="600" loading="lazy" alt="Blog Image" />

\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

**Fixed current and low price**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_213.webp" width="1200" height="188" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_214.webp" width="1026" height="244" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_215.webp" width="1200" height="449" loading="lazy" alt="Blog Image" />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_216.webp" width="1200" height="542" loading="lazy" alt="Blog Image" />

## **모듈 발열불량 분석**

**2025년 3월 15일 토요일**

*오전 6:42*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_217.webp" width="1200" height="643" loading="lazy" alt="Blog Image" />

