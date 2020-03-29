# 03/24 (화) Component & Grid system

> - 학습해야 할 내용
>   - Bootstrap Component
>   - Bootstrap Grid System


```html
<div class = "{a}">
    <div class="{b}">
        <div class="col-{c}-{d}">...</div>
    </div>
</div>

```

## 1. Bootstrap Grid System 적용을 위해 {a}, {b}에 입력되어야 할 클래스

- a: `container`
- b: `row`

> Grid는 격자라는 의미로, 12개의 칸을 담을 수 있는 격자처럼 사용된다.  
> 먼저 담기 위한 그릇인 container와, 한 줄에 담길 요소를 row로 받아주어야  
> Grid system을 적용할 수 있다.

## 2. {c}, {d} 에 들어갈 수 있는 값과 그 의미.

### `{c}`: 화면 크기에 따른 break point를 적용할 수 있다.
- `none`- default: (extra small) view < 576px
- `sm`: (small) 576px <= view < 768px
- `md`: (medium) 768px <= view < 992px
- `lg`: (large) 992px <= view < 1200px
- `xl`: (extra large) 1200px <= view

### `{d}: row안에서 차지할 공간 - 1~12 사이의 값을 적용 가능하다.

## 3. Align-itmes-center를 사용하려면 d-flex 클래스와 함께 사용하여야 했었다. 그러나, Grid System에서는 d-flex 클래스를 생략하여도 올바르게 동작한다. 그 이유를 작성하라.

```html
<div class="container">
    <div class="row align-items-center">
        <div class="col">
            One of three columns
        </div>
        <div class="col">
            One of three columns
        </div>
        <div class="col">
            One of three columns
        </div>
    </div>
</div>
```
Grid 시스템은 크게 다음과 같은 항목들로 나눌 수 있다.  
`container` -> `layout` -> `flex` ( -> `card`)

### **1. Container**
- Grid의 가장 큰 범주
- layout & flex

#### props
`fluid`  
    - Removs viewport size breakpoints  
    - 화면에 따라 사이즈가 바뀌는게 아니라 항상 최대 넓이를 가짐  
    - 사이즈 조절하는 경우 사용.  

### **2. layout**
- 섹션을 구분하는데 사용한다
- flex 속성을 가진다.

이렇듯 flex속성을 갖고있기 때문에 justify / align 등의 사용이 가능하다.

## 4. Nav를 오른쪽 정렬하고자 할 때 {a} 에 들어가야 할 클래스 이름
- nav 역시 flex속성을 사용할 수 있다.

> 답) justify-flex-end