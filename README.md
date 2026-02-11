## DS & MLE 역량 강화 기록 (DS-Log)

---

안녕하세요! 이 레포지토리는 다양한 머신러닝 자산을 **로컬(Windows) 환경**에서 직접 분석하고 역량을 내재화 하는 과정을 기록합니다.


## 핵심 목표

1. **Implemetation Detail :** 함수 내부의 데이터 변환 과정, 사용된 파라미터, 파이프라인의 기술적 흐름을 서술합니다.
2. **Engineering Rationale:** 왜 이 알고리즘이 해당 데이터셋에 최적인지, 선택한 이유(논리)를 서술합니다.
3. **Key Insight:** 모델 성능(Accuracy 등)의 수치적 변화나 분석을 통해 얻은 비즈니스적 통찰을 서술합니다.

##  주요 프로젝트 (Top 5 Focused)

### 1. 데이터 스케일링 최적화 (`01_data-Scaling`)
- **Focus:** 이상치가 포함된 데이터셋에서 모델 강건성 확보
- **Insight:** `StandardScaler` 대비 `RobustScaler`의 이상치 대응 능력 실험 및 검증
- **Result:** 로컬 환경에서 시각화를 통해 스케일러별 데이터 분포 변화 확인



*(나머지 2, 3, 4, 5번도 같은 형식으로 추가)*

---

##  환경 및 도구

로컬 환경에서의 재현성과 라이브러리 간 충돌 방지를 위해 독립된 가상환경에서 진행
- **IDE:** Visual Studio Code
- **Language:** Python 3.12.10
- **Version Control:** Git / GitHub
- **Dependency Tracking:** `requirements.txt`를 통한 버전 고정 및 형상 관리
---

## 성장 기록
- **Problem Solving:** AWS SageMaker 전용 코드를 로컬 환경에서 작동하도록 `boto3` 의존성을 제거하고 순수 `scikit-learn` 로직으로 변환하는 과정에서 파이프라인의 구조를 깊게 이해하게 됨.
- **Philosophy:** "모든 기술은 오픈북이다. 중요한 건 라이브러리 사용법이 아니라 그 안의 흐름을 통제하는 논리다."



---



