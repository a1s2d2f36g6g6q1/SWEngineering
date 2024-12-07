from django.shortcuts import render, HttpResponse
import matplotlib
matplotlib.use('Agg')  # GUI 백엔드 대신 Agg 백엔드 사용 (이미지 저장용)
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
import requests
import os
import json
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from io import BytesIO
import base64

# 종목 데이터 크롤링
def market_crawler(market):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize=30&page=1"
    response = requests.get(url)
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("No data to decode")
        data = {}
    market_df = pd.DataFrame(data)
    return market_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]

def code_crawler(code):
    url = f"https://m.stock.naver.com/api/stock/{code}/price?pageSize=30&page=1"
    response = requests.get(url)
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("No data to decode")
        data = {}
    code_df = pd.DataFrame(data)
    return code_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]

# 그래프 생성 및 이미지 저장
def stock_graph(market, code, normalization):
    market_df = market_crawler(market)
    market_price = market_df['closePrice'].str.replace(',', '').astype(float)

    plt.figure(figsize=(8, 4))
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    # 시장 데이터 그래프
    x_market = market_df['localTradedAt'][::-1]
    y_market = market_price.to_list()
    y_market_normalization = preprocessing.minmax_scale(y_market)
    plt.plot(x_market, y_market_normalization if normalization == 'True' else y_market, label=market)

    # 종목 데이터 그래프 (선택 사항)
    if code:
        code_df = code_crawler(code)
        code_price = code_df['closePrice'].str.replace(',', '').astype(float)
        x_code = code_df['localTradedAt'][::-1]
        y_code = code_price.to_list()
        y_code_normalization = preprocessing.minmax_scale(y_code)
        plt.plot(x_code, y_code_normalization if normalization == 'True' else y_code, label=code)

    plt.legend(loc=0)

    # 그래프를 Base64로 인코딩
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    graph = base64.b64encode(image_png).decode('utf-8')
    return graph

# 상관계수 계산
def coefficient(market, code):
    market_df = market_crawler(market)
    market_price = market_df['closePrice'].str.replace(',', '').astype(float)
    y_market = preprocessing.minmax_scale(market_price.to_list())

    if code:
        code_df = code_crawler(code)
        code_price = code_df['closePrice'].str.replace(',', '').astype(float)
        y_code = preprocessing.minmax_scale(code_price.to_list())
        coef = np.corrcoef(y_market, y_code)[0, 1] * 100
        return f"{market}와 {code}의 상관계수는 {coef:.2f}% 입니다."
    else:
        return f"{code} 종목이 없어 {market}와의 상관계수를 계산할 수 없습니다."

# ARIMA 기반 가격 예측
def market_price_predict(market):
    market_df = market_crawler(market)
    market_price = market_df['closePrice'].str.replace(',', '').astype(float)
    train_data = market_price[:-5]
    model = ARIMA(train_data, order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)
    return forecast.tolist()

def code_price_predict(code):
    if code:
        code_df = code_crawler(code)
        code_price = code_df['closePrice'].str.replace(',', '').astype(float)
        train_data = code_price[:-5]
        model = ARIMA(train_data, order=(1, 1, 1))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=5)
        return forecast.tolist()
    return ['?', '?', '?', '?', '?']

# 예측 페이지 렌더링
def prediction(request):
    market = 'KOSPI'
    code = ''
    normalization = 'False'

    if request.GET:
        market = request.GET.get('market', market)
        code = request.GET.get('code', code)
        normalization = request.GET.get('normalization', normalization)

    graph = stock_graph(market, code, normalization)
    answer = coefficient(market, code)
    market_forecast = market_price_predict(market)
    code_forecast = code_price_predict(code)

    return render(request, 'prediction.html', {
        'graph': graph,
        'answer': answer,
        'market_forecast': market_forecast,
        'code_forecast': code_forecast,
        'market': market,
        'code': code,
    })