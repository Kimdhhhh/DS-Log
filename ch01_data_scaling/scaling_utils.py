"""
[scaling_util 모듈]
다양한 스케일링 기법의 효과를 통계량과 시각화(Box plot)로 즉각 비교합니다.
"""
import pandas as pd
import plotly.express as px

def analyze_scaling(scaler, train_data, title='Scaling Result'):
    """
    Args:
        scaler : sklearn의 Scaler 또는 Pipeline 객체
        train_data : 변환할 원본 데이터프레임
        title : 결과 보고서 제목
    Returns:
        df_scaled : 변환이 완료된 데이터프레임
    """
    # 1. 스케일링 변환
    # 데이터프레임의 컬럼명을 보존하기 위해 fit_transform 결과를 다시 DF로 만듭니다.
    scaled_array = scaler.fit_transform(train_data)
    df_scaled = pd.DataFrame(scaled_array, columns=train_data.columns)
    
    # 2. 통계 확인
    print(f"\n" + "="*50)
    print(f" REPORT: {title}")
    print("="*50)
    print(df_scaled.describe())
    print("-"*50 + "\n")
    
    # 3. 시각화
    fig = px.box(df_scaled.melt(),
                 x='value',
                 y='variable',
                 color='variable',
                 orientation='h',
                 points='outliers',
                 title=f'전처리 결과 분석: {title}',
                 template='plotly_white')
    
    fig.update_layout(showlegend=False, height=400)
    fig.show()
    
    return df_scaled