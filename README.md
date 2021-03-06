# K-NN_Recomendation
  한국외국어대학교 컴퓨터.전자시스템공학부 졸업과제로 서버 백엔드로 개발했던 K-NN기반 상품추천알고리즘을 소개하고자 합니다. 
  
## 소개
  이 프로젝트는 '한국외국어대학교'에서 졸업프로젝트 목적으로 연결해준 '수동예림' 회사와 협업하여 제작했습니다. 이 회사는 도장을 판매하고 있습니다. 사람들에게 'vonvon'이나 '잼라이브'와 같은 놀이 어플리케이션을 통해 도장을 홍보하고 추천하는 웹페이지를 만들어 볼 것을 제안했습니다. 저를 포함한 4명의 팀원은 유저들의 취향에 관한 간단한 설문조사를 진행하고 그에 맞는 도장 사진과 이름을 제공하여 유저들에게 흥미를 이끌어 내고자 했습니다. 
  
## 구상
  이 설문에 참여해서 유저에게 도장을 추천해 주는 과정은 다음과 같습니다.
  
  1. 각 도장에 예상되는 선호 특징을 개발자 주관으로 정의하여 Feature로 사용한다.
  2. 설문 받을 내용을 1의 Feature와 연관이 있도록 선지를 제작한다. 
  3. 설문을 완료한 유저의 Feature와 가장 유사한 5개의 도장을 추려내어 랜덤으로 하나를 반환하거나, 제일 비슷한 한개의 도장을 반환한다.

* Feature 

  ![stamps](https://user-images.githubusercontent.com/44831709/137267422-517ade9a-0c18-4675-bfd3-28c135cced0c.png)
  
  위와 같은 도장들을 개발자 주관으로 지도학습(Supervised Learning)을 시킵니다. Feature로 정의될 항목은 다음과 같습니다.
  
  나이, 종교, 띠, 도장의 밝기, 별자리, 디자인, 가격, 글자 새김, 재료, 동양/서양풍, 성별

* 설문의 선지 

  ![survey](https://user-images.githubusercontent.com/44831709/137267744-1fd05abc-72e5-4213-be43-01d7fee2319e.png)
  ![survey2](https://user-images.githubusercontent.com/44831709/137281576-230b9a04-5b50-48af-883b-d2ac9ac2d060.png)

  위와 같은 형식으로 설문에 참가하는 유저들에게 정보를 가져옵니다. 

* K-NN과 유사도 검사 

  ![vector](https://user-images.githubusercontent.com/44831709/137268037-3302ec68-6dce-45ba-ae8c-0fe071a4d87a.png)
  
  설문에 참여한 유저는 위에서 정의한 Feature들을 바탕으로 하나의 벡터로 간주합니다. K-NN 기반으로 이러한 Feature들을 바탕으로 유저와 가장 유사한 5개의 도장을 선택합니다. 
  
  여기서 유사도 검사는 Euclidean distance와 Cosine-Similarity 를 사용했습니다. 
