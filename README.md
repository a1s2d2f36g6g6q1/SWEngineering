# SWEngineering

## 1. Collaborators

1. 서동우 (https://github.com/a1s2d2f36g6g6q1)
2. 이동규 (https://github.com/LDeHa)
3. 이재승 (https://github.com/LJS0328)

## 2. Project

주식예보
AI 기반 주식 예측 모델 활용 웹 사이트

## 3. Install

원활한 사용, 또는 개발을 위해 필요한 라이브러리를 설치해야 합니다.

1. 현재 프로젝트를 클론 한 후, 해당 프로젝트 폴더로 이동합니다.
2. 해당 폴더에서 Terminal / CMD 를 실행합니다.
3. Terminal / CMD 에서 가상 환경을 생성하고 실행합니다.

```
Windows :
1. python -m venv venv
2. venv\Scripts\activate
```

```
macOS / Linux :
1. python3 -m venv venv
2. source venv/bin/activate

---
(참고 : 가상 환경을 종료하려면 deactivate 를 입력)
```

4. 명령어 앞에 (venv) 가 표시되는지 확인합니다
5. 요구 라이브러리를 설치하기 위해 다음 명령어를 실행합니다.

```
pip install -r requirements.txt
(pip install --upgrade pip 으로 pip 업그레이드 후, 다시 requirements.txt 설치)
```

6. 다음 명령어를 실행하여 서버를 마이그레이션 한 후 실행합니다.
```
[Win]
python manage.py migrate
python manage.py runserver

[macOS / Linux]
python3 manage.py migrate
python3 manage.py runserver
---
(참고 : 서버를 종료하려면 Ctrl + C 를 입력)
```

## 4. Dependencies

- IDE : PyCharm
- Language : Python
- Framework : Django
- HTML

## 5. How to use

---

## 6. License

```
Copyright (c) 2019-present NAVER Corp.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

```
Select market data provided by ICE Data Services
© 2023 TradingView, Inc.
```

```
COPYRIGHT© DAOL Investment & Securities Co., Ltd. ALL RIGHTS RESERVED
```

---

추가 사항 ->
네이버 크롤링 코드 / 트레이딩뷰 API / 다올 API

requirements.txt 수정해야함...