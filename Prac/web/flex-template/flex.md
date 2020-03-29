# web 01_Flex

HTML / CSS 배치 핵심: 왼쪽에 쌓인다
- 블록: 전체 너비
- 인라인: 컨텐츠 너비

> float : 정렬이 힘들다
> position : 특정한 영역 폭에서 수직정렬이 어려웠다.
> - absolute
> - fixed 브라우저

이러한 단점들을 보완하기 위해 **flex**ible box 를 사용한다.  

## 1. Flex 주요 개념
- `item`, `container` 
- `main axis` (가로축)  
- `corss axis` (세로축)
- `flex` 정의 시
    - main axis을 기준으로 배치가 시작된다. (default: `row`)
    - 모든 `item`은 행으로 배치된다. (`flex-direction`: `row` 기본 값)
    - 모든 `item`은 `cross axis`을 모두 채운다.
    - 모든 `item`은 본인의 너비 컨텐츠 영역만큼 너비를 가지게 된다.
        - 경우에 따라서, 본인이 지정받은 넓이보다 작을 수 있다. (`flex_wrap`:`nowrap`이 기본값이기 때문.)
            - 전체 아이템의 너비의 합이 컨테이너의 넓이보다 작을 때.  
                container {width: 1000px}  
                item {width:500px}  

            - 이런 경우, flex-wrap:wrap; 을 사용할 수 있다.

## 2. Flex 옵션들
- `flex-wrap`: 아이템의 길이가 더 클 때 사용 가능.  
    - `nowrap`: (기본값)한 줄에 하나씩만 담는다.  
    - `wrap`: 각각의 너비만큼 가지게 되고, 자리가 없으면 밑으로 내린다.

- `flex-grow`: 남은 너비를 일정 비율로 나눠감. (기본값 0)
- `justify-content`: main축 정렬 관련된 옵션 (기본값:flex-start) 
    - flex-start: 앞쪽 정렬
    - flex-end: 뒤쪽 정렬
    - center: 가운데 정렬
    - space-around
    - space-between: 각 아이템의 시작과 끝이 벽에 붙은 상태에서 균일한 space를 갖는다.
    - space-evenly: 시작과 끝에 공백을 둔 상태에서 균일한 space를 갖게끔 한다.

- `align-items`: 아이템의 배치 관련 옵션, cross축을 기준으로 정렬한다.
    - `stretch` : 기본값, 영역에 맞게 확장
    - `center`
    - `flex-start`
    - `flex-end`
    - `baseline`: 폰트 사이즈가 다를 때, 폰트 최하단의 높이를 맞춰준다.
- `order`: 아이템의 순서를 정의할 수 있다.
    - 기본값: 0
    - 음수값도 가질 수 있음.

- `align-self`: item에 직접 align을 지정할 수 있다.
    - 기본 `stretch`
    - `flex-start`
    - `flex-end`
    - `center`



즉 세로축의 개념이 있기 때문에 정렬을 좀 더 유연하게 가능하다.
```css
div {
    display:flex;
    flex-direction: {row, row-reverse, 
                     column, column-reverse 선택}
}
```

### flex를 지정했을 때 생기는 일
1) row를 기준으로 배치
2) main축의 처음부터 배치
3) 컨텐츠 크기 / 너비만큼의 영역(더 작을수도 있음)
4) 모든 영역은 cross axis 모두 채움
