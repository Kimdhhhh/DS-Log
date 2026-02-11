# CH01. Data Preprocessing & Scaling Pipeline Strategy

## 1. 개요 (Introduction)
본 프로젝트는 데이터의 특성(분포, 단위, 이상치)에 따른 최적의 스케일링 조합을 탐색하고, 이를 **Scikit-learn Pipeline**으로 공정화하여 분석의 재현성과 효율성을 극대화하는 것을 목적으로 합니다.

## 📂 프로젝트 구조 (Project Structure)
이 프로젝트는 분석 환경과 재사용 가능한 모듈로 구성되어 있습니다.

```text
.
├── 01_scailng.ipynb       # 스케일링 기법 기초 실험 및 분석
├── 02_pipeline.ipynb      # 최종 전처리 공정 구축 및 결과 보고
├── scaling_utils.py       # [핵심] 시각화 및 분석 헬퍼 모듈
├── README.md              # README.md
└── .gitignore             # 불필요한 파일(__pycache__) 제외 설정
```


## 2. 핵심 도구 (Key Tools)
###  scaling_utils.py (Custom Helper Module)
반복적인 데이터 진단 과정을 자동화하기 위해 직접 제작한 모듈입니다.
- **`analyze_scaling()`**: 어떤 스케일러나 파이프라인을 입력해도 **[변환 → 통계 요약 → 박스플롯 시각화]**를 한 번에 수행합니다.
- **문서화**: `help(scaling_utils)` 명령어를 통해 모듈 내 상세 사용법을 즉시 확인할 수 있습니다.

## 3. 데이터 전처리 전술 가이드 (Strategy Table)
데이터의 상태에 따라 다음과 같은 파이프라인 조합을 고려합니다.

| 데이터 증상 | 추천 파이프라인 조합 (Recipe) | 주요 목표 |
| :--- | :--- | :--- |
| **분포 쏠림 + 단위 불일치** | `PowerTransformer` → `StandardScaler` | 왜도 제거 및 정규화 |
| **이상치 과다 + 범위 제한** | `RobustScaler` → `MinMaxScaler` | 이상치 방어 및 범위 고정 |
| **기하학적 거리 중심** | `StandardScaler` → `Normalizer(L2)` | 방향성 및 벡터 길이 통일 |
| **정규분포 + 단위 불일치** | `StandardScaler` (단일 공정) | 평균 0, 표준편차 1 통일 |

## 4. 실전 적용 예시 (Use Case)
샘플 데이터(Feature 1: [0,1], Feature 2: [0,12], Feature 3: [100,101])에 대해 **StandardScaler** 파이프라인을 적용하여 모든 특성의 체급을 동일하게 정렬 완료했습니다.

<img width="100%" alt="Scaling Result" src="https://github.com/user-attachments/assets/686c96a0-d6b4-4b02-95a8-018809ccb3d1">

## 5. 시작하기 (Quick Start)
```python
import scaling_utils
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# 파이프라인 구축
pipe = Pipeline([('scaler', StandardScaler())])

# 헬퍼 함수를 통한 즉각적인 결과 보고
scaling_utils.analyze_scaling(pipe, X_train, "Final Report")