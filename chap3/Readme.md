# 3장의 단어정리 및 코드모음 입니다.

MNIST에 필요한 데이터셋 및 pretrain 된 weight는 https://github.com/WegraLee/deep-learning-from-scratch 에서 다운받으실 수 있습니다.

### Perceptron

다수의 순호를 입력으로 받아 하나의 신호를 출력한다.

### Bias 

편향을 나타내는 매개변수로, 뉴런이 얼마나 쉽게 활성화되느냐를 제어한다.

### Weight

신호의 가중치를 나타내는 매개변수로, 각신호의 영향력을 제어한다.

### Activation function

활성화함수는 입력신호의 총합이 활성화를 일으키는지를 정하는 역할을 한다.

### Multi-layer perceptron 

여러 층으로 구성되고 시그모이드 함수 등의 매끈한 활성화 함수를 사용하는 네트워크(신경망)을 가리킨다.

### Step function 

임계값을 경계로 출력이 바뀌는 함수 (ex h(x) = 1 if x >= 0 , h(x) = 0 if x < 0)

### linear function 

선형함수, 입력에 상수배만큼 비례해 출력을 내는 함수 , ( f(x) = ax + b)

### Non linear function 

선형이 아닌 함수, 즉, 직선 1개로 그릴 수 없는 함수를 말한다.

### 신경망에서 비선형함수(non linear function)을 이용하는 이유는 ???? 

> 선형 함수를 이용하면 신경망의 층을 깊게 하는 의미가 없어지기 때문!
선형함수는 층을 아무리 깊게해도 ‘은닉층이 없는 네트워크’로도 똑같은 기능을 할 수 있다.
Ex) h(x) = cx 를 활성화 함수라고 하자. 이 활성화함수를 사용해 쌓은 3층 네트워크를 생각하면 
y(x) = h(h(h(x))) >>> y(x) = c*c*c*x. 곱셈을 세번 수행하지만 사실상 y = ax와 같은것 ( a = c^3) 
따라서 신경망의 층을 깊게사용하는 이점을 살리려면 비선형함수를 사용해야만 한다 ! 

### ReLU(rectified linear unit) 

0이하면 0 이고 0보다 크면 입력을 그대로 출력 . 즉, max(0,x) 

### Normalization 

데이터를 특정범위로 변환하는 처리

### Pre-processing 

신경망의 입력 데이터에 특정 변환을 가하는 것

