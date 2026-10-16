# 리딩 사다리 (Reading Ladder)

영어 원서 모임을 위해, 저작권이 만료된 영어 원서를 난이도 순서로 정리하고 워크북을 함께 제공하는 사이트입니다.

## 수록 작품

| 단계 | 작품 | 자료 | 분량 | 모임 |
|---|---|---|---|---|
| 1 | Ali Baba and the Forty Thieves (Andrew Lang, 1889) | 본문 + 워크북 | 3,601단어 | 1회 |
| 1 | Aladdin and the Wonderful Lamp (Andrew Lang, 1889) | 본문 + 워크북 | 5,326단어 | 2회 |
| 4 | Animal Farm (George Orwell, 1945) | 워크북 | 약 3만 단어 | 7회 |

제작 중: The Wonderful Wizard of Oz, Alice's Adventures in Wonderland, The Jungle Book

## 원칙

- **저작권이 만료된 작품만 올립니다.**
- **원문은 바꾸지 않습니다.** 옛 문체 작품은 원문의 문장과 줄거리를 그대로 두고, 지금 쓰지 않는 단어만 오늘의 영어로 바꿉니다. 바꾼 단어는 워크북의 "Words We Updated" 표에 모두 적어 둡니다.
- 대체할 말이 없는 옛 단어(†)와 옛 관용구(※)는 본문에 표시하고 워크북에서 설명합니다.
- *Animal Farm*은 한국에서는 저작권이 만료되었지만 미국 등에서는 아직 보호 중입니다. 그래서 워크북에는 책 본문이나 인용 없이, 새로 쓴 요약·예문·문제만 들어 있습니다.

## 읽기 시간 기준

- 영어 학습자는 보통 분당 약 100단어를 읽습니다(학습자 평균 80~120단어). → 1,000단어 ≈ 10분
- 워크북까지 하면 읽기 시간의 약 2배
- 모임 1회 ≈ 약 4,300단어 (The Giver 약 4만 3천 단어를 10회에 읽은 우리 모임의 속도)

## 폴더 구조

```
index.html              사이트 첫 페이지
workbooks/              내려받을 PDF (본문, 워크북)
src/lang-tales/         Lang 동화 원문(1889), 현대어 본문, 워크북 데이터, PDF 빌드 스크립트
src/animal-farm/        Animal Farm 워크북 데이터와 빌드 스크립트
```

## PDF 다시 만들기

Python 3와 Playwright(Chromium)가 필요합니다.

```
pip install playwright pypdfium2
python -m playwright install chromium
```

`src/lang-tales/build_story.py`와 `src/animal-farm/build_all.py`는 원래 작업 환경의 경로를 쓰고 있어서, 다시 빌드하려면 스크립트 안의 경로를 이 저장소 기준으로 바꿔야 합니다.

## 출처

- Andrew Lang, *The Blue Fairy Book* (1889) — 공개 저작물
- 읽기 속도: Beglar, Hunt & Kite 외, 외국어 학습자 읽기 속도 연구 (*Reading in a Foreign Language*)
