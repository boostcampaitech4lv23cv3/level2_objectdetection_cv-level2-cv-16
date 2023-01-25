# **💡 CV16조 비전길잡이 - boostcamp 4기💡**
## **🚮 Trash Object Detection**
![image](https://user-images.githubusercontent.com/103131249/214495508-2f73b8a1-6eae-4c55-b4a9-4abccafb9701.png)

## **🚮 Contributors**
|민기|박민지|유영준|장지훈|최동혁|
|:----:|:----:|:----:|:---:|:---:|
|[<img alt="revanZX" src="https://avatars.githubusercontent.com/u/25689849?v=4&s=100" width="100">](https://github.com/revanZX)|[<img alt="arislid" src="https://avatars.githubusercontent.com/u/46767966?v=4&s=100" width="100">](https://github.com/arislid)|[<img alt="youngjun04" src="https://avatars.githubusercontent.com/u/113173095?v=4&s=100" width="100">](https://github.com/youngjun04)|[<img alt="FIN443" src="https://avatars.githubusercontent.com/u/70796031?v=4&s=100" width="100">](https://github.com/FIN443)|[<img alt="choipp" src="https://avatars.githubusercontent.com/u/103131249?v=4&s=117" width="100">](https://github.com/choipp)|
|ConvNext</br>Optimization</br>Ensemble test| Yolov7</br>EDA</br>Ensemble test | Swin_Base</br>Loss Function</br>Ensemble test | Dynamic Head</br>DetectoRS</br>Augmentation | PM</br>TTA</br>Pre-trained test|

## **🚮 Links**
<div style='display: flex; align-items: center; '>
    <span>비전 길잡이 노션 - &nbsp</span><a href='https://www.notion.so/vision-pathfinder/Object-Detection-98d7238151d24cfcbd3f365cb68b57af'><img src='https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white'></img></a>
</div>

[비전 길잡이 발표자료 & WrapUpReport](./appendix/)

## **🚮 Result**
![result](https://user-images.githubusercontent.com/25689849/214493814-4ee7cef2-a8fd-4264-a795-ea59a71b50d0.png)

---

## **🚮 Data**
![Dataset_Example](https://user-images.githubusercontent.com/70796031/214493481-2d7a678b-f4a5-4620-9efd-9eb2bb505209.png)
- 전체 이미지 개수 : 9,754 장 (train 4,883 장, test 4,871 장)
- 10개 클래스 : General trash, Paper, Paper pack, Metal, Glass, Plastic, Styrofoam, Plastic bag, Battery, Clothing
- 이미지 크기 : (1024, 1024)


## **🚮 Stratified-Kfold 적용**
![Class_DisTribution_Graph](https://user-images.githubusercontent.com/25689849/214494486-ba4ef612-af00-4574-b6e2-253cdc08c390.png)
 - 클래스 별 annotation 수를 나타낸 분포 - 클래스 별 불균형 심함 
 - Train 데이터와 validation 데이터에 동일한 분포를 적용
 - Stratified group k-fold (k=5)를 사용 · 5쌍의 train, validation set을 구성

## **🚮 Augmentation**
![Augmentation](https://user-images.githubusercontent.com/103131249/214497415-911bfdc0-b86a-4fc7-889e-4db4513674f4.png)
 - One of (Flip, RandomRotate90) - 360도 회전 구현
 - One of (CLAHE, Random Brightness Contrast) - 선명도, 밝기 조절
 - One of (Blur, Gaussian Blur, Median Blur, Motion Blur) + Gaussian Noise - 노이즈 추가
 - Multi scaling - 11개의 이미지 크기로 resizing
 - Mosaic - one stage model에만 적용


## **🚮 Ensemble**
![Ensemble](https://user-images.githubusercontent.com/103131249/214497553-a8b6c95f-ae49-4151-9cf9-74cb85016704.png)
- Confusion matrix 확인결과 모델별로 class별 성능 특화되는 것 확인
- 점수가 가장 높은 convNeXt xlarge의 부족한 부분을 다른 모델에서 보완할 수 있게 앙상블 진행
  - ConvNeXt  : 높은 classification 성능 -> 적은 수의 bbox를 탐지하여 비교적 낮은 mAP50 score
  - YoloV7    : 타 모델 대비 매우 낮은 classification 성능 -> bbox를 더 많이 탐지하는 강점
  - Dyhead    : convNext와 YoloV7의 중간에 해당하는 결과 -> 상호 보완 역할
 

## **🚮 최종 Model**
![Final Model](https://user-images.githubusercontent.com/103131249/214495149-60c3b0b7-cae0-4e6c-b65d-a7a1ce801ffa.png)
- Public mAP 0.7395 / Private mAP 0.7280
- Convnext xlarge split + Dyhead swin large + Swin base + YOLOv7을 앙상블 했을 때 가장 높은 점수를 보임

## **🚮 LB Timeline⌛**
![LB_Timeline_Graph](https://user-images.githubusercontent.com/25689849/214494581-2e84ac05-cd7f-4c7a-83d2-a918e5f8f295.png)
- **💡전체 프로젝트 기간동안 뚜렷한 우상향 그래프로 모델 성능을 개선💡**

## **🚮 Directory Structure**
```
|-- appendix : 이 프로젝트에 대한 발표자료와 WrapUp Report
|-- README.md
|-- configs
|   |-- _trashDet_ : 모든 모델 설정은 _trashDet_을 사용
|   |   |-- _base_
|   |   |   |-- datasets
|   |   |   |-- default_runtime.py
|   |   |   |-- models
|   |   |   `-- schedules
|   |   |-- cbnet
|   |   |-- convnext
|   |   |-- dcn
|   |   |-- detectors
|   |   |-- detr
|   |   |-- dyhead
|   |   |-- efficientnet
|   |   |-- focalnet
|   |   |-- htc
|   |   |-- retinanet
|   |   |-- swin
|   |   |-- swinv2
|   |   |-- timm
|   |   |-- universenet
|   |   `-- yolox
|-- custom_tool  : confusion metrix나 kfold등 자체 제작 툴
|-- dataset      : Kfold 적용
|-- mmcv_custom  : apex 모듈을 사용한 모델 의존 파일
|-- mmdet        : ConvNeXt 등 외부 모델 구현
|-- wandb        : wandb 파일 저장
|-- work_dirs    : 학습 결과물
|-- requirements.txt
|-- train.py     : 동일한 학습을 하기 위한 팀 공용 학습 파일
`-- inference.py : 동일한 추론을 하기 위한 팀 공용 추론 파일
```