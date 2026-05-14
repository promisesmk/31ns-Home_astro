---
title: "nRF52805_BLE모듈_개발기술참고문서_이미지포함 (EN)"
description: "nRF52805 BLE module development technology reference document (for developers) GX805 / GX805C Series · Nordic Semiconductor nRF52805 WLCSP ⚠ Information on anonymization of sensitive information: Company name of the original..."
date: 2026-05-14
lang: "en"
tags: ["Astro", "Blog"]
---

**nRF52805 BLE 모듈 개발**기술 참고 문서 (개발자용)*GX805 / GX805C Series · Nordic Semiconductor nRF52805 WLCSP*



| ⚠ 민감정보 익명 처리 안내: 원본의 회사명·인명·연락처 등은 \[고객사], \[담당이사A], \[대표B], \[담당이사C], \[담당자D], \[외주RF튜닝업체], \[PCB제작업체A/B] 등으로 익명 처리하였습니다. |
| --- |

## **231127\_\[고객사]\_Module개발\_(1차미팅/복사)****2023년 11월 27일 월요일***오전 6:13***\[담당이사A], \[대표B], ,\[담당이사C]**

적용 Chip

PCB 사양/ 배치 및 회로배선고려

**Build\-up A, B, C**캔적용**기존 보유캔 스펙**

검토 또는 참고할 Ref Module type

모듈 Size

안테나 Type

**PCB size대비 Chip안테나로 설계 될 수 있음.**

안테나 파생

## **안테나 메칭****PCB 2층, 4층 기준설정 후 Build\-up 제작전에 안테나 패턴타입 설계**##**Buil\-up제작후 2차 안테나 메칭**

Sample제작 여부

RF단 튜닝

**개발검토 내용 전달****2023년 11월 30일 목요일***오전 10:03*

IC 및 모듈 Vendor를 검토한 결과 Pin out 개수가 적어서 2Layer로 설계가 가능해 보입니다.

다만, Pin배치, 부품 추가 등에 따라서 부득이하게 4Layer로 설계를 해야 하는 경우가 있을 수 있습니다.

**PCB 가격은(샘플,양산) 올라가게 됩니다.****I/O는 Chip 외곽으로 배치되어 있어서 모든 I/O를 뺄 수 있을 것 같습니다.****I/O개수를 줄인다고 해서 모들이 작아 지기에는 한계가 있습니다.**모듈설계 결정사항**32\.768KHz 크리스탈을 optional 처리 할지, 모듈에 넣을지.**개발 참고 대상은 \[담당이사A]님이 말씀 주신 것 외에,**Raytac에서 nRF52805로 개발된 모듈을 기준으로 하면 좋을 것 같습니다.****안테나도 거의 동일하게 설계 되어질 것으로 생각됩니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_01.webp" width="1063" height="411" loading="lazy" alt="Blog Image"  />

참고 이슈

**기존에 노르딕 Ref는 1005부품이 최소 Size 였습니다.****하지만 최근에는 IC도 작아진 만큼, 0603으로 대체(변경 가능한 용량들) 가 되어 부품들이****모두 작습니다. 따라서 모듈을 만들 때 작게 할 수 있습니다.*** → 생산 도급 시 다소 일반적인 부품이 아닙니다.* → RF튜닝시 별도로 부품을 구매해야 합니다.

**Nordic 레퍼런스의 BOM /부품 크기 참고/ inch 기준임.**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_02.webp" width="1081" height="354" loading="lazy" alt="Blog Image"  />**Inch è mm 참고**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_03.webp" width="704" height="445" loading="lazy" alt="Blog Image"  />

DK보드 제작 고려

*→ 향후 DK가 없으면 고객사 대응이 다소 어려울 것 같아서 Ratac 제품을 검토해 봤습니다.**아래 그림은 Raytac사의 DK 입니다.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_04.webp" width="1200" height="787" loading="lazy" alt="Blog Image"  />

향후 고려사항

**Module을 생산할 때 모듈을 개별로 시험할 수 있는 JIG 설계가 필요합니다.****기능적인 부분보다는 모듈각각의 Pin에 대해 솔더링을 하지 않고,****전기적 접촉을 할 수 있는 구조를 만드는 것이 중요해 보입니다.**

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

## **Module test****\-Function test : \[고객사]에서 test할 수 있도록 수작업배선.****/ DK 제작 전 작업.****\-RF 출력확인 : DTM F/W입수(\[고객사])후 출력측정 및 필요시 튜닝.**1. 11\)이후 2번째 Type 모듈 및 DK 개발.**보시고 궁금한 부분 있으시면 전화 주시면 고맙겠습니다.**##**Module\[고객사] 설계검토\_자료분석반영****2023년 11월 28일 화요일***오전 8:12***Raytac사의****MDBT42\-512KV2, \-P512KV2 모듈형태 참고하여 nRF52085를 사용한 모듈 개발.**개발컨셉 : CAN을 겸용으로 사용.* → nRF52805, nRF52832WLCSP

**따라서, 추후 nRF52832WLCSP로 모듈 개발시 위 모듈과 동일하게 설계할 경우****설계에 문제가 없을 것으로 판단하기 때문에 CAN설계를 동일하게 하고자 함.**위 모듈 검토사항**기존 nRF52805모듈을 검토한 내용에 추가적인 부분만 반영하여 설계하면 될 것으로 판단.****전체 높이 : 1\.8****가로 8\.8****세로 13\.8****CAN 높이 : 1\.0mm**설계적용 PCB : 0\.8T, 2Layer**안테나 싸이드 V\-cut, 그외 미싱홀 없음.\=\=\>PCB제작가능여부?**회로설계**RF test TP with GNT TP****52805 WLCLP****X\-tal 32Mhz : 1612size****LC 부품 : 0603 size****without DCDC and Xtal 32Khz****RF배치 : IC를 최대한 안테나 쪽으로 이동배치*** → IC 출력단 : Nordic REF참고반영* → ANT 메칭 : Pi메칭회로
*→ Raytac 모듈의 nRF52805 는 PCB가 작아서 RF단 출력이 많이 꺽임.**PCB size가 nRF52832WLCSP module로 적용할 수 있으므로****RF단 출력패턴을 대각선 일자로 배치하여 안테나 까지 유도하는 설계로 적용.**##**nrf52805 Ref\_Nordic사****Tuesday, December 19, 2023***7:59 AM***1.With DCDC**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_05.webp" width="900" height="537" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_06.webp" width="1200" height="1103" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_07.webp" width="1200" height="1157" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_08.webp" width="723" height="666" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_09.webp" width="1021" height="935" loading="lazy" alt="Blog Image"  />

Without DCDC

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_10.webp" width="1200" height="772" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_11.webp" width="1200" height="1108" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_12.webp" width="1177" height="1169" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_13.webp" width="1200" height="1102" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_14.webp" width="1035" height="944" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_15.webp" width="871" height="859" loading="lazy" alt="Blog Image"  />

PCB Design Reference

**Check the RF output terminal impedance below**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_16.webp" width="863" height="785" loading="lazy" alt="Blog Image"  />**In practice, the S values below are difficult to apply when designing modules.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_17.webp" width="590" height="552" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_18.webp" width="1100" height="162" loading="lazy" alt="Blog Image"  />

**Caution: IC nrf52805 \<\=\=\> up to antenna****Matching does not match as shown below. / It appears that the PCB pattern was not matched considering the part size.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_19.webp" width="501" height="405" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_20.webp" width="587" height="500" loading="lazy" alt="Blog Image"  />

Part Size

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_21.webp" width="1008" height="351" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_22.webp" width="649" height="566" loading="lazy" alt="Blog Image"  />

## **Reference module\_Raytac MDBT42T /Section results****Tuesday, November 28, 2023***10:44 AM***Online Purchase**https://www.digikey.com/en/products/filter/rf\-transceiver\-modules\-and\-modems/872?s\=N4IgTCBcDaILIBEBCAVALGALiAugXyA**https://www.raytac.com/product/ins.php?index\_id\=107**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_23.webp" width="1086" height="1076" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_24.webp" width="809" height="956" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_25.webp" width="598" height="677" loading="lazy" alt="Blog Image"  />

**No 32\.768K, No DCDC parts**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_26.webp" width="886" height="1223" loading="lazy" alt="Blog Image"  />**1\.CAN : 0\.2T, 1\.05mm (height from PCB top), 5\.8mm x 7\.0mm****2\.PCB: 0\.8T 4layer****3\.X\-tal: Use 1612**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_27.webp" width="634" height="463" loading="lazy" alt="Blog Image"  />**3\.Half Hole**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_28.webp" width="633" height="452" loading="lazy" alt="Blog Image"  />**3\.Via BPL and PSR**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_29.webp" width="645" height="480" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_30.webp" width="779" height="571" loading="lazy" alt="Blog Image"  />

**4\.Placement and ANT Geometry**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_31.webp" width="293" height="426" loading="lazy" alt="Blog Image"  />

Placement concept

**Antenna matching stage: Pi configuration****Move the IC as close to the antenna as possible****IC output tuning stage adopts nRF52805 REF arrangement design.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_32.webp" width="631" height="470" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_33.webp" width="640" height="475" loading="lazy" alt="Blog Image"  />

Part size

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_34.webp" width="520" height="383" loading="lazy" alt="Blog Image"  />

1. 7\. 1005 Alternative Review

Problem: Tuning becomes easier as the size increases, but tuning issues increase because references are not considered.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_35.webp" width="641" height="489" loading="lazy" alt="Blog Image"  />

**240117 : \[PCB Manufacturer A]\-**

The section result is 0\.7T, H/H oz, both sides are the same, but there is no 0\.7T material, and when working with 0\.8T, H/H oz, the final thickness is expected to be 0\.9T.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_36.webp" width="1105" height="770" loading="lazy" alt="Blog Image"  />

## **Reference module\_Raytac MDBT42****Friday, December 22, 2023***12:24 PM***https://www.raytac.com/product/ins.php?index\_id\=33**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_37.webp" width="1200" height="621" loading="lazy" alt="Blog Image"  />**Module development using nRF52085, referring to the above MDBT42\-512KV2, \-P512KV2 module types.**Main purpose: Combined use of CAN.* → nRF52805, nRF52832WLCSP

**Therefore, when developing a module with nRF52832WLCSP in the future, if it is designed the same as the above module****We plan to make the CAN design the same because we believe there will be no problems with the design.**Above module review**It is judged that the design should only reflect additional aspects of the review of the existing nRF52805 module.****Total height: 1\.8****Horizontal 8\.8****Height 13\.8****CAN height: 1\.0mm**CAN**Left and right edges have a step equal to the thickness**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_38.webp" width="481" height="371" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_39.webp" width="641" height="481" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_40.webp" width="691" height="832" loading="lazy" alt="Blog Image"  />

## **Raytac DK with Half hole module****Tuesday, November 28, 2023***1:32 PM***https://www.raytac.com/product/ins.php?index\_id\=114**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_41.webp" width="1200" height="811" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_42.webp" width="1200" height="794" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_43.webp" width="1200" height="791" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_44.webp" width="1200" height="827" loading="lazy" alt="Blog Image"  />

## **Raytac DK with SMD module****Tuesday, November 28, 2023***1:35 PM***https://www.raytac.com/product/ins.php?index\_id\=130**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_45.webp" width="1200" height="789" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_46.webp" width="1200" height="807" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_47.webp" width="1200" height="786" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_48.webp" width="1200" height="807" loading="lazy" alt="Blog Image"  />

## **Tuning Parts Kit****Tuesday, November 28, 2023***2:21 PM***https://www.devicemart.co.kr/goods/view?no\=1313419**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_49.webp" width="1200" height="543" loading="lazy" alt="Blog Image"  />**https://www.devicemart.co.kr/goods/view?no\=1313427**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_50.webp" width="1200" height="551" loading="lazy" alt="Blog Image"  />**Module test/module test****Wednesday, November 29, 2023***9:35 AM***http://www.jig\-hitech.co.kr/page/product01\_02\.php**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_51.webp" width="850" height="1040" loading="lazy" alt="Blog Image"  />

https://www.indiamart.com/proddetail/esp8266\-burner\-fixture\-test\-board\-development\-board\-for\-esp\-12s\-12f\-12e\-07s\-07\-series\-module\-23199561897\.html

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_52.webp" width="1034" height="936" loading="lazy" alt="Blog Image"  />

https://www.instructables.com/DIY\-ESP8266\-ESP\-12\-Socket\-Snap\-Fit\-Breadboard\-Frie/

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_53.webp" width="696" height="773" loading="lazy" alt="Blog Image"  />

https://ko.aliexpress.com/i/32802723152\.html?gatewayAdapt\=glo2kor

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_54.webp" width="582" height="555" loading="lazy" alt="Blog Image"  />

https://hackaday.com/2022/03/07/flexypins\-might\-help\-with\-those\-pesky\-castellated\-modules/

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_55.webp" width="815" height="467" loading="lazy" alt="Blog Image"  />

https://www.espressif.com/en/products/equipment/production\-testing\-equipment/overview

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_56.webp" width="824" height="686" loading="lazy" alt="Blog Image"  />

https://forum.contextualelectronics.com/t/test\-jig\-for\-esp8266\-modules/4637

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_57.webp" width="991" height="688" loading="lazy" alt="Blog Image"  />

## **231214\_모듈개발 2차 미팅.****2023년 12월 11일 월요일***오후 3:07***개발고려**

개발품목 : 모듈 2종과 EVB 2종 중

개발자료 : 회로도 PDF, 거버파일, PCB DXF파일

지그개발 방향, 난이도/외주?

기존캔 사용 : 기 Datasheet를 참고하여 모듈 설계

모듈설계하면서(Ratac사 모듈검토) 캔 납땜 위치제공\=\=\> CAN제작

모듈샘플구매

**231222****\[대표B]님 통화****모듈 컨셉****모듈의 크기는**Raytac사의 MDBT42\-512KV2 또는 MDBT42\-P512KV2 크기/Half hole 참고하여 설계.**위 모듈은 nRF52832 WLCSP 기준으로 설계되어 있으나****우선 개발모듈은 nRF52805를 위 모듈의 크기에 맞춰서 설계하고****차후 nRF52832 WLCP를 적용해서 모듈을 추가로 개발할 때 동일한 CAN을 사용하고자 함.**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_58.webp" width="1200" height="640" loading="lazy" alt="Blog Image"  />**회로설계 결정사항**Module**PCB Size : 8\.8 x 13\.8****PCB T : 0\.8T****PCB Layer : 2L****RF IC :nRF52805****With out : 32\.768Khz,DCDC inductor****Ant : pattern and chip****32Mhz : 1612 / 차후 nRF52832WLCP모듈 공용****L , C : nRF52805 Ref from Nordic**

EVB

## **CAN Dimension\_PPT****2023년 12월 27일 수요일***오전 11:29*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_59.webp" width="1200" height="675" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_60.webp" width="1200" height="675" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_61.webp" width="1200" height="674" loading="lazy" alt="Blog Image"  />

## **For CAD\_PPT****2023년 12월 27일 수요일***오후 2:52*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_62.webp" width="1200" height="668" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_63.webp" width="1200" height="671" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_64.webp" width="1200" height="667" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_65.webp" width="1200" height="672" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_66.webp" width="1200" height="675" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_67.webp" width="1200" height="527" loading="lazy" alt="Blog Image"  />

## **EVB배치 참고**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_68.webp" width="1200" height="794" loading="lazy" alt="Blog Image"  />

## **240109\_모듈개발 3차 미팅.****2024년 1월 9일 화요일***오후 12:08*##**J\-link Pin out****2024년 1월 31일 수요일***오전 11:08***https://wiki.segger.com/20\-pin\_J\-Link\_Connector****Pinout for JTAG**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_69.webp" width="414" height="348" loading="lazy" alt="Blog Image"  />**https://www.devicemart.co.kr/goods/view?no\=1179243**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_70.webp" width="1200" height="667" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_71.webp" width="892" height="607" loading="lazy" alt="Blog Image"  />

**https://ko.aliexpress.com/i/32428874079\.html**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_72.webp" width="1082" height="832" loading="lazy" alt="Blog Image"  />

## **CAD 검토1****2024년 1월 29일 월요일***오전 5:29***Module**쉴드캔 부품기구**쉴드캔 데이터올림, 두께표시**쉴드캔 고정패트**Non plate 적용****J8: 왼쪽으로 조금이동,****홀작음 \=\=\>****R값?**쉴드캔 납땜패드**노출**

안테나 폭, 길이

BOTTOM PAD size1

## **CAD검토2****2024년 1월 29일 월요일***오후 1:54***Module**

Bottom면 pad size 크기 작음.

TP3, TP4 추가/회로도 변경함.

*→ Bottom면에 1파이 Pad추가**For Cad.pdf 3, 4page 참고**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_73.webp" width="380" height="279" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_74.webp" width="548" height="323" loading="lazy" alt="Blog Image"  />

**SILK**1. 1\. Module**\-Pattern 안테나 Bottom 영역 : GW\_MHP52805\_V1\.0****\-Chip 안테나 Bottom 영역 : GW\_MHC52805\_V1\.0**Main**GW\_EVB\_MHP52805\_V1\.0****회로도에 있는 각 초록색에 대한 SILK 표기 부탁드립니다.**##**CAD 검토3****2024년 1월 30일 화요일***오전 5:48***Module**쉴드캔**J8은 쉴드캔 센터라인에 배치, J8하단부 GND copper도 J8라인과 일치.****J8의 센터점과 쉴드캔 아랫쪽 과의 거리가 3\.8\-0\.75\=3\.05 인데, 2\.949정도로 다소 짧음.****쉴드캔 납땜패트 노출.**배치 / 미리 말씀을 드려야 했는데.. 죄송합니다.* → RF단 구간 최소화해서 Loss를 없게 해야 될 거 같습니다.

**아래 처럼 일자로 꼭 되지 않더라도 아무래도 수정을 좀 해 봐야 될 거 같아요..****U2배치를 최대한 위쪽으로 이동 배치를 해서 RF단과 5,6 pad 연결배선을 좀 수정해야 될거 같아요.**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_75.webp" width="531" height="250" loading="lazy" alt="Blog Image"  />* → 5,6pad로 연결되는 패턴 길이를 최대한 줄여서 GND공간확보

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_76.webp" width="637" height="469" loading="lazy" alt="Blog Image"  />

배선

**11pin via 없이 top에서 패턴연결****15pin으로 연결되는 via 위쪽으로 이동, C10 위치 이동.**안테나**안테나를 위,아래 우측 PCB외곽에 최대한 붙여서 배치.*** → 안테나와 GND 간격이격* → 시작점도 위쪽으로 같이 이동.
*→ x축 가로방향 길이 반영은 시작점에서 우측으로 연결되는 길이만 증가.* → Y축 양측(위,아래)로 늘어난 길이는 증간 3단 웨이브의 세로길이만 균등배분

Pin 간격

**0\.9mm/전체적용*** → Standard 9pin\-\-\-\-\>2pin / 1pin fixed* → 10pin\~16pin: 0\.9mm interval based on the left center
* → 17pin\~19pin: Line alignment with the upper 9pin and 0\.9mm interval / 19pin fixed

pad size

**Pad at Bottom: 0\.4 x0\.8****However, 1pin: length only 1\.2mm, 19pin: maintained**PAD GND connection and copper reinforcement**Top: 10,16: copper reinforcement****Bottom pins 10, 16, 1, and 19 are also connected to GND and reinforced with copper**U2 GND via**Apply Via in the center / Refer to 52805 Data City**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_77.webp" width="851" height="850" loading="lazy" alt="Blog Image"  />**Nordic datasheet**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_78.webp" width="560" height="963" loading="lazy" alt="Blog Image"  />

U2 pin spacing

**Space between G1\~G2 does not match.**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_79.webp" width="626" height="410" loading="lazy" alt="Blog Image"  />**Main**

Remove Conn area

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_80.webp" width="440" height="850" loading="lazy" alt="Blog Image"  />

**SILK**1. 1\. Module**\-Pattern Antenna Bottom Area: GW\_MHP52805\_V1\.0****\-Chip Antenna Bottom Area: GW\_MHC52805\_V1\.0**1. 2\. Main**GW\_EVB\_MHP52805\_V1\.0****Please indicate SILK for each green color in the circuit diagram.**##**CAD Review4****Wednesday, January 31, 2024***8:01 AM***Module**19pin top, bottom pad expansion \=\=\> to CAN hole* → CAN is also GND, so there is no short circuit problem.

Y1 90 degree clockwise rotation

**Keep the wiring short**

TP3, TP4 silk position overlap?

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_81.webp" width="481" height="411" loading="lazy" alt="Blog Image"  />

Cut it according to the wave line at the end of the antenna.

**EVB**I think the module soldering pad is not in the right position? I think it should match or be a little bigger.**Module pads appear to touch EVB GND Copper.**CONN1**A5,B5 pad size adjustment**##**CAD Review5****Wednesday, January 31, 2024***10:36 AM***Module**

Reason for Y1 GND separation?

Distance between J8 center and the bottom of the shield 2\.949mm \=\=\>3\.05mm

Copper reinforcement including vias

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_82.webp" width="553" height="354" loading="lazy" alt="Blog Image"  />

**Main**

2\~9 Add a little more space between the left and right copper of the pad.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_83.webp" width="1132" height="507" loading="lazy" alt="Blog Image"  />

**18, 17 Please leave a little more space between the left and right pads.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_84.webp" width="371" height="442" loading="lazy" alt="Blog Image"  />

J9 pin number silk

**Please write only 4 numbers: 1, 2, 9, and 10.****Please also include All GPIO at the bottom.**J7 Uchi**Please lower it to about line c17.**

Please put them in the J5 and J2 square boxes. And please add J\-Link.

## **CAD Review6****Thursday, February 1, 2024***7:19 AM***Module****EVB**The length from the pad soldered to the module to the inside of the line is 1\.4mm.**To maintain this length, the GND space of the module must be narrowed further****It would be better not to do that.****Just make it equal to 1\.2mm like the pad length of the module. Leave the GND copper alone.****Pad size is not a problem for soldering anyway.**

It looks like it came in a J\-Link Silk box... It doesn't look white?

J7 location is good.

**Please put Current text at the bottom of J7.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_85.webp" width="1067" height="875" loading="lazy" alt="Blog Image"  />

Turn TP1 and TP2 90 degrees counterclockwise.

**This is a pad that is used by soldering, so I think it would be better to place it horizontally.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_86.webp" width="280" height="257" loading="lazy" alt="Blog Image"  />

Please change C21 \=\=\> to NC/1005 in the circuit diagram.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_87.webp" width="400" height="241" loading="lazy" alt="Blog Image"  />

## **CAD Review7****Monday, February 5, 2024***7:18 AM***Align L7 to C7 line.**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_88.webp" width="456" height="811" loading="lazy" alt="Blog Image"  />**Shield can top left: The horizontal direction from the corner must be soldered****There is no soldering area in the vertical direction**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_89.webp" width="442" height="435" loading="lazy" alt="Blog Image"  />**Check mask**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_90.webp" width="928" height="574" loading="lazy" alt="Blog Image"  />

## **CAD Review 7 Final\_\[Client] Share****Friday, February 2, 2024***2:25 PM*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_91.webp" width="681" height="689" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_92.webp" width="706" height="582" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_93.webp" width="1200" height="983" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_94.webp" width="1137" height="777" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_95.webp" width="1138" height="788" loading="lazy" alt="Blog Image"  />

## **Pattern antenna matching/additional review of shape****Thursday, February 15, 2024***12:38 PM*<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_96.webp" width="470" height="418" loading="lazy" alt="Blog Image"  />**As it is a circuit for both pattern and chip antennas, about pattern antenna E1****Matching is required with L3, C7, L4 (0603size).**##**However, we request antenna matching while the Module PCB is soldered to the Main BD.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_97.webp" width="1157" height="724" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_98.webp" width="436" height="447" loading="lazy" alt="Blog Image"  />

**Review Matters****\Has [Customer] ever tested the RF range among the RF characteristics of the Raytac module?****\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=**##**First pattern antenna matching request**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_99.webp" width="584" height="802" loading="lazy" alt="Blog Image"  />**1\.Issue: Gain is currently too small.****The gap between the antenna wave part and PCB GND is narrow, so the characteristics deteriorate due to the C value****Measurement after 1st matching**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_100.webp" width="1200" height="590" loading="lazy" alt="Blog Image"  />**Measurement after 2nd matching**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_101.webp" width="1200" height="581" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_102.webp" width="1200" height="384" loading="lazy" alt="Blog Image"  />

Compare Raytac modules/same size

**Raytac module characteristics/datasheet****Peak gain is low and there is no significant difference (chamber error) from the characteristics of the [client] module.****In addition, the gain characteristics appear to have been copied directly from Peak EIRP data.****Gain must be a 360-degree interval average, so it must show a much lower measurement value than Peak.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_103.webp" width="467" height="105" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_104.webp" width="1200" height="199" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_105.webp" width="1200" height="203" loading="lazy" alt="Blog Image"  />

**\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=**Antenna Considerations**Design Board**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_106.webp" width="1097" height="786" loading="lazy" alt="Blog Image"  />**Raytac Board**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_107.webp" width="525" height="323" loading="lazy" alt="Blog Image"  />

Performance improvement plan/Gain

**GND separation, antenna width reduction****Review 1\) Below is similar to the USB dongle design data / secondary measurement of the module.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_108.webp" width="1004" height="543" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_109.webp" width="1200" height="553" loading="lazy" alt="Blog Image"  />

**Review 2\)****The antenna shape does not take a wave even if the length is short as shown below****Consideration on antenna shape: phone call\_240226**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_110.webp" width="1200" height="900" loading="lazy" alt="Blog Image"  />

## **Chip antenna matching****Thursday, February 15, 2024***12:47 PM*<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_111.webp" width="470" height="418" loading="lazy" alt="Blog Image"  />**It is a circuit for both pattern and chip antennas, and the PCB is manufactured individually with only the antennas different.****Matching to L3, C7, L4, L7 (0603 size) is required for chip antenna E2.**##**It would be better to do antenna matching while the Module PCB is soldered to the Main BD.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_112.webp" width="1200" height="789" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_113.webp" width="993" height="942" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_114.webp" width="1200" height="781" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_115.webp" width="1200" height="836" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_116.webp" width="1200" height="884" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_117.webp" width="1200" height="844" loading="lazy" alt="Blog Image"  />

## **PCB 1st shipment****Monday, February 19, 2024***10:51 AM*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_118.webp" width="783" height="654" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_119.webp" width="759" height="589" loading="lazy" alt="Blog Image"  />

**Module land formation problem**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_120.webp" width="648" height="481" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_121.webp" width="639" height="486" loading="lazy" alt="Blog Image"  />

**CAN seated status**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_122.webp" width="643" height="477" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_123.webp" width="643" height="490" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_124.webp" width="638" height="480" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_125.webp" width="646" height="483" loading="lazy" alt="Blog Image"  />

## **PCB 2nd arrival\_module****Thursday, February 29, 2024***7:16 AM***Reference when making Half Hole.****\[PCB Manufacturer B] Based on Half Hole specifications****Half hole drill: 0\.4****Half hole pad: 0\.6****Half hole drill: regulation is 0\.8, minimum value: 0\.4 / routing drill is 1\.0****If you use a smaller half hole, the hole will collapse.****Half Hole Pad: In the panel plating method to preserve the plating of the half hole****Considering the characteristics of dry film, the hole is 0\.1mm or more on the left and right****PAD must be inserted.****Depending on the nickname method, correction is required during the process when creating a half hole.****nickname**

1. 1\)Panel plating: Use of dry film / Currently common method
2. 2\)Pattern plating: Use of lead / Old method, seems to have been used by Raytac module.

**Exactly how it was manufactured because the HPL process was applied****Difficult to understand.****Metal Gerber No. 1**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_126.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_127.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_128.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_129.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

**Metal Gerber No. 2****Half hole drill: 0\.4 / Minimum value reflected in production process****PAD design: 0\.4,****PAD correction: Minimum value is 0\.6 based on 0\.45 / 0\.4 drill*** → Plating disappears when nicknamed.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_130.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_131.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_132.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_133.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

**Metal Gerber No. 3**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_134.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_135.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_136.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_137.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

**Comparison of PAD size between Metal Gerber No. 1 (Half Hole not plated) and reference product**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_138.webp" width="1200" height="890" loading="lazy" alt="Blog Image"  />**Comparison of Metal Gerber No. 2 (minimum specifications: 0\.4 drill, modified in CAM with 0\.6pad) and reference product’s PAD and spacing**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_139.webp" width="1200" height="897" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_140.webp" width="641" height="481" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_141.webp" width="645" height="485" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_142.webp" width="644" height="479" loading="lazy" alt="Blog Image"  />

## **3rd arrival of PCB\_module****Friday, March 8, 2024***5:10 AM*Half Hole Formation/Plating Status**Half Hole: Correction with 0\.6pad, 0\.3 dril/ Original: 0\.4pad, 0\.3 dril**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_143.webp" width="1200" height="895" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_144.webp" width="1200" height="881" loading="lazy" alt="Blog Image"  />

Half hole formation/prevention of burrs rather than removal

**First drill on the left side of the Half Hole before routing.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_145.webp" width="695" height="527" loading="lazy" alt="Blog Image"  />

## **RF tuning result****Monday, March 18, 2024***8:51 AM*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_146.webp" width="794" height="1165" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_147.webp" width="798" height="873" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_148.webp" width="787" height="1154" loading="lazy" alt="Blog Image"  />

**Inspection of overall contents after 1st development SMD****Friday, March 8, 2024***5:20 AM*

RF

## **Reference to results before and after tuning and comparison of antenna matching results/raytac characteristics\_Chip, pattern, Raytac****Check distance when communicating between modules****Check distance when communicating between module and mobile phone**##**Refer to the last performance improvement plan in the additional review of antenna characteristic improvement/pattern antenna matching summary**PCB production**Half Hole Design*** → Process and design modifications**Change in CAD design of pad size and drill dimensions according to half hole formation rules, prevent burrs,**

Review for improvement / apply to secondary sample or final data

1. 1\) Half Hole: Pad and drill dimension modification 0\.4/0\.3\=\=\>0\.6/0\.4 (PCB process)

**GND reinforcement: Whether to add GND half hole on the side, when changing, add GND as well as EVB**1. 2\) EVB**Pin header interference when storing U4*** → Whether to change J6, J4, J1 to 1608 0ohm* → J9, J10 move to the right
1. 3\) Module ANT characteristics / additional design review

**Comparison of current antenna characteristic results of 3 types\_pattern, chip, Raytac**

1. 4\)) During shield can CAN reel packing, the parts are not seated uniformly due to the large gap in the reel pocket (SMT process)

Module Kit Array Placement

1. 1\) Has anything been discussed with the JIG manufacturer?

**Total number of modules, array placement required in JIG, etc.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_149.webp" width="360" height="848" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_150.webp" width="653" height="1012" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_151.webp" width="892" height="1073" loading="lazy" alt="Blog Image"  />

## **Request for CAD modification after 1st development SMT****Friday, March 22, 2024***11:09 AM*Edit**2 types of modules and EVB****Module circuit removed from EVB**Edit contents**\-Concerns of interference with shield cans: C10, L2, C7*** → With the shield can fixed, move the entire part downward by 0\.2mm.* → The antenna is fixed without moving.
*Side Half Hole: Basic rules applied due to various reasons in PCB processing.* → Drill: 0\.4mm, PAD size: 0\.6mm,
* → The same applies to 1 and 19 pins.

motherboard

*→ Modified to fit the module pad.* → R16, R17 pull-ups added

**Pin header interference when storing U4*** → Change J6, J4, J1 to 1608 0ohm/add R18, R19, R20* → J9, J10 move to the right

Half Hole Reference Image

**The 4 images below show a normal Half Hole,****When correction values are reflected during CAM work on existing CAD design data**This is an image of**, and a via is formed normally. The value is 0\.4/0\.6.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_152.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_153.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_154.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_155.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

**The four images below are images of half hole defective products****It is said that when manufactured according to the existing data, the Via Hole was not formed during etching.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_156.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_157.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_158.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_159.webp" width="1101" height="822" loading="lazy" alt="Blog Image"  />

**Therefore, the reason for CAD correction is when the correction value is applied so that the PCB is produced without problems****Because the PAD on the half hole side is made in an unusual shape, it not only looks bad****Because other issues may arise when providing the product, the PAD size is fundamentally uniform****To.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_160.webp" width="497" height="328" loading="lazy" alt="Blog Image"  />

## **Module design H/W differentiation****Thursday, February 15, 2024***12:57 PM***1\. Via is applied to the side half hole PAD to strengthen the connection with the main B/D.****Connectivity is secured by Pad on Via even if the half hole side is damaged for other reasons.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_161.webp" width="1200" height="777" loading="lazy" alt="Blog Image"  />

HPL applied to all vias

**Because there is no GAS generated from the via, the RF IC and surrounding components are not affected by GAS****Prevents cold soldering.****Also, when soldering closely to the main B/D, interference with surrounding patterns is blocked.**

Less affected by surrounding noise through separation of copper around X\-Tal.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_162.webp" width="367" height="463" loading="lazy" alt="Blog Image"  />

## **Module production jig related****Monday, April 29, 2024***10:29 AM***Module jig inquiry/visit****1\.Test block material/RF test related****2\.Mainboard and pin connection method (dual, single)/Advantages and disadvantages****3\.Pin spacing 0\.9mm*** → Minimum spacing??/During future design

Circuit manufacturing review

**\-Jig sample confirmation, jig design review according to module test scenario.****\-Whether the motherboard is installed in the test block case/whether a separate external case is applied****\-Power supply connection configuration****\-Program pin connection configuration**

F/W programming

## **\-Module test FW, Module product FW programming*** → Configure test and sales firmware into one**Should I just program it once? .??**

Test scenario

1. 1\) RF frequency
2. 2\) RF output level
3. 3\) I/O test

**Short, open**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_163.webp" width="704" height="545" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_164.webp" width="694" height="538" loading="lazy" alt="Blog Image"  />

**\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=****H/W design review not included****Physical connection test**

I/O test 1

Short circuit between IC and Pad to I/O,

**All I/Os are in Pull\-up state (external Pull\-up)****After setting Out mode and Low output for specific I/O using software****Check High status with the remaining I/O set to Input mode****(Check GND short, check connection open)****Is there any I/O with low input?****(Check short circuit between I/O)****Repeatedly check all I/Os sequentially.****Random I/O enters test mode and moves to the next test item****Use one random I/O to display results. (LED and buzzer)**Except for mode and display LEDs, connect LEDs to the remaining I/O.**Check the I/O connection status by visually checking the sequential lighting operation of the LED.****Check RF Signal**1. 1\. Check Gain**Enter into Becon mode by pressing the JIG button / or signal confirmation mode in the APP.***nRF Tool/phone APP**Check RSS value**Frequency check**Specific RF ch output by JIG button/constant carrier in DTM mode****\-Check frequency in range with spectrum analyzer.****Sampling test in 100EA units.**##**Module socket design drawing****Tuesday, June 4, 2024***4:04 PM*<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_165.webp" width="1200" height="954" loading="lazy" alt="Blog Image"  />**DDDF**##**Board design for module production jig****Thursday, May 16, 2024***8:14 AM*

EVB circuit diagram

\<\<PCA10040\_Schematic\_And\_PCB\-nskim.pdf\>\>

Design composition concept

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_166.webp" width="862" height="420" loading="lazy" alt="Blog Image"  />

Inquiry regarding module socket design

**PCB Layout where the module is seated**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_167.webp" width="761" height="616" loading="lazy" alt="Blog Image"  />

Is the connection between the module and the 18EA pad in the PCB layout a spring pin contact rather than soldering?

What material is the socket made of?

**Metal material among the parts touching the PCB?**##**\=\=\>Area where the socket is in contact with the socket board. Silk applied and insulating paper****Module circuit diagram**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_168.webp" width="908" height="719" loading="lazy" alt="Blog Image"  />**Socket GPIO pin configuration****Is the power supply 5V or option processing??: No.****Added condenser for power****Board design using EVB connectors P1,2,3,4,6,****Designed so that the PIN of all PADs of the module is configured as a circuit.****\-P0\.01, Should P0\.00 be checked through I/O or by connecting to 32\.768K X\-tal?*** → 32\.768K default configuration, optional I/O configuration

## **\-DCC and DEC4 are configured by software depending on the DCDC circuit configuration of the socket board?****\-The remaining I/O is connected to EVB's U1 (nRF52832\) AIN0\~7. (Red dot I/O above)****Power is the same as VIO\=VDD\=VDD\_nRF and uses 1,2 pins (VIO) and 6,7 (GND) of P1.****Shield detect pin used?*** → If used, what is the pin handling plan?**Is it GND by soldering SB18 of PCA10040?**##**(When processing on the socket board, connector connectivity with the socket board is not good)**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_169.webp" width="552" height="941" loading="lazy" alt="Blog Image"  />**Programming**##**Use P20 connector\=\=\>Connect with socket board?**##**Select pin separate circuit configuration: High processing on socket board?*** → shield select pin header processing required.**P20's 8 pin is a GND detect pin, but there is no pattern connection on the PCB.*** → However, by selecting J\-link or EVB using the 8pin GND detector of P20,**Insert a pin header that can be programmed.*** →**P20 connector will not be used, only J\-Link will be used.****Connection may be unstable when using P20.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_170.webp" width="1185" height="440" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_171.webp" width="927" height="239" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_172.webp" width="650" height="485" loading="lazy" alt="Blog Image"  />

**Power and USB to serial****https://sheep\-thrills.net/FT230X\_SMD\_module.html**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_173.webp" width="948" height="801" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_174.webp" width="809" height="961" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_175.webp" width="1200" height="274" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_176.webp" width="1200" height="755" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_177.webp" width="1200" height="865" loading="lazy" alt="Blog Image"  />

\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\= \=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

## **First socket board concept**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_178.webp" width="1200" height="580" loading="lazy" alt="Blog Image"  />

## **Secondary socket board concept****Refer to the picture below for JIG board design****Pin header socket is dip type to ensure stability**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_179.webp" width="707" height="942" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_180.webp" width="1200" height="650" loading="lazy" alt="Blog Image"  />

https://devzone.nordicsemi.com/f/nordic\-q\-a/27786/flashing\-external\-board\-using\-nrfgo\-studio

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_181.webp" width="784" height="594" loading="lazy" alt="Blog Image"  />

**Refer to J\-link**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_182.webp" width="1200" height="352" loading="lazy" alt="Blog Image"  />**20\-pin J\-Link Connector****https://wiki.segger.com/20\-pin\_J\-Link\_Connector****Pin configuration based on SWD interface**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_183.webp" width="1200" height="714" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_184.webp" width="1200" height="229" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_185.webp" width="876" height="1117" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_186.webp" width="11" height="11" loading="lazy" alt="Blog Image"  />

## **Module data sheet review****Tuesday, June 4, 2024***7:12 AM*GX805C**It would be nice to change the photo in the future by applying shield cans for mass production.****Also, because we decided not to use half holes for the module pad****It would be better to apply the photo after SMT to the changed PCB in the future.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_187.webp" width="331" height="433" loading="lazy" alt="Blog Image"  />

GX805 is the model name of the pattern antenna module.

**(When confirming the module name, "C" is attached to the chip antenna from the beginning, and there is no attached pattern antenna)****As shown below, GX805 is used as a common name, but it is difficult to see it as a common name for 2 modules****Users may be a bit confused when ordering.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_188.webp" width="915" height="306" loading="lazy" alt="Blog Image"  />

## **Module and DK PCB design change****Friday, June 7, 2024***1:39 PM*\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\= \=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=**Review of module design changes /\Share during [client] meeting**Inquiry regarding the effect on RF characteristics due to half hole removal and silk change.**Answer (antenna design company): Radiation characteristics can vary significantly.****The reason is that the module is small, so the soldering amount of PAD is less than GND condition****It can affect the dielectric constant of the part that is closely attached to the main B'D by silk****There may be a small effect due to differences.*** → Need to check the characteristics of the tuning stage and antenna matching stage.

We are preparing to manufacture a new PCB and check its characteristics after SMT.

**How to additionally compensate for the GND condition as much as possible by modifying the PCB before manufacturing the PCB.*** → Add pad and review progress. (Previously, some wiring was considered for the pattern)* → Modifications reflected before KC certification

**Main\_TOP**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_189.webp" width="660" height="455" loading="lazy" alt="Blog Image"  />**Module\_BOT**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_190.webp" width="704" height="476" loading="lazy" alt="Blog Image"  />

progress

*→ CAD modification for both SUB and Main: External company* → PCB ordering and parts: \[Customer]
*→ SMT : \[Customer]* → Tuning: \[Outsourced RF Tuning Company]
*→ Matching confirmation: External company**Some costs may apply for cases involving external companies.****CAD modification: 2 types of modules, 1 type of EVB*** → 3 points are added to the GND pad of the module.* → EVB's PAD is formed as Main Board PAD based on the data sheet.

\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\= \=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

## **\[Person in Charge D] Share**Module**Add GND pad****Added 1 type of antenna shape: “\-1” is added to the file name to distinguish it differently, but Silk is the same as GX805.*** → Total of 3 types of modules

EVB

**Add GND Pad and adjust overall pad size****Silk change: GW\_EVB\_MHP\&C52805\_V1\.1\=\=\> GW\_EVB\_GX805\_V1\.0**Common features**Change design name: Please refer to the file name and change the display name on the drawing.**Notes on modifications**Add GND Pad**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_191.webp" width="1049" height="786" loading="lazy" alt="Blog Image"  />**Regarding addition of antenna shape****No fixed length: Compensated by matching antenna parts, length expected to be 17mm, width 0\.3mm,****(GND pad addition applies the same as above)**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_192.webp" width="1026" height="717" loading="lazy" alt="Blog Image"  />**EVB****Add PAD in the same location as the pad added to the module****Pad size can be adjusted by referring to the picture below**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_193.webp" width="800" height="929" loading="lazy" alt="Blog Image"  />**\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=**##**CAD Review**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_194.webp" width="574" height="128" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_195.webp" width="979" height="626" loading="lazy" alt="Blog Image"  />

## **Pattern antenna matching request/2nd****Tuesday, July 16, 2024***6:10 AM***Circuit diagram/2 types of antennas are the same**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_196.webp" width="639" height="456" loading="lazy" alt="Blog Image"  />

monopole wave antenna

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_197.webp" width="1066" height="682" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_198.webp" width="398" height="706" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_199.webp" width="567" height="596" loading="lazy" alt="Blog Image"  />

1. 2\)Monopole antenna

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_200.webp" width="1062" height="687" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_201.webp" width="389" height="694" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_202.webp" width="520" height="614" loading="lazy" alt="Blog Image"  />

## **Chip antenna matching/secondary****Friday, July 19, 2024***10:31 AM***\[Customer] decided to deliver the module PCB and EVB to \[Director A].**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_203.webp" width="1200" height="886" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_204.webp" width="1200" height="887" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_205.webp" width="1200" height="888" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_206.webp" width="1200" height="888" loading="lazy" alt="Blog Image"  />

## **240828\_Meeting****Wednesday, August 28, 2024***1:50 PM*##**1\.Meeting after Taiwanese antenna matching***Agenda: 1\)Contents related to changing or maintaining PAD design due to efficiency.
1. 2\)Content on whether redesign is necessary with the chip antenna (CW804\) you replied to.
2. 3\)Matching review page 10 BOM reflection related content
3. 4\)Other matters
* → Change the PCB design by changing the chip antenna.

## **Socket board: Remove USB\-c connector from circuit****T****s**##**CAD Review\_Socket Board****Tuesday, October 8, 2024***8:08 AM*SW1**Silk positions of ON and OFF are swapped.****(When the switch is pulled to the right, 1\-2 are connected and turned ON, so place the ON silk on the right side of the switch)**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_207.webp" width="432" height="330" loading="lazy" alt="Blog Image"  />

I made some modifications to the circuit diagram.

**There are two locations below.****Change TX to \=\=\>RX and RX to \=\=\>TX.**<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_208.webp" width="629" height="321" loading="lazy" alt="Blog Image"  />* → change

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_209.webp" width="726" height="343" loading="lazy" alt="Blog Image"  />

**R17 GND was changed as shown below.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_210.webp" width="462" height="197" loading="lazy" alt="Blog Image"  />

I think all TP and parts in the area below should be placed at the bottom.

**After reviewing, I found that the socket mechanism was completely adhered to the PCB.**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_211.webp" width="463" height="478" loading="lazy" alt="Blog Image"  />

## **Socket Board Current Limit****Friday, January 17, 2025***8:45 AM*##**If the module generates heat while testing the module using the socket board****Intent to cut off power.**

Even though the module operates normally in all tests, it is consuming excessive current due to a short circuit somewhere, and at this time, heat is generated in the module.

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_212.webp" width="1007" height="600" loading="lazy" alt="Blog Image"  />

\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\= \=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=

**Fixed current and low price**

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_213.webp" width="1200" height="188" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_214.webp" width="1026" height="244" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_215.webp" width="1200" height="449" loading="lazy" alt="Blog Image"  />

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_216.webp" width="1200" height="542" loading="lazy" alt="Blog Image"  />

## **Module heat failure analysis****Saturday, March 15, 2025***6:42 AM*

<img src="https://cdn.jsdelivr.net/gh/promisesmk/31ns-Home-blog-assets@main/nRF52805_BLE모듈_개발기술참고문서_이미지포함/img_217.webp" width="1200" height="643" loading="lazy" alt="Blog Image"  />