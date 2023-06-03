### TypeScript 1 

#### - 타입스크립트를 사용하는 이유 -



##### 자바스크립트는 Dynamic Typing이 가능

- 5 - '3'이 가능함
- 서비스가 커질 수록 유연성이 커지는건 좋지 않음



##### TypeScript의 에러메세지는 JavaScript의 에러메세지보다 정확함



##### TypeScript는 하나의 에디터 기능이라고 생각하면 편리함





##### 기본문법 1

-  변수에 타입 지정

  - `let name:string = 'choi'` : name이라는 변수에는 (string) 타입의 값만 들어갈 수 있음
  - `let nameList : string[] = ['kim', 'park']` : array안에는 (string)만 가능
  - `let nameObj : {name:string} = {} = {name:'kim}` obj의 name에는 (string)만 가능,  {name? : string} => 옵셔널 느낌
  - `let name :string | number = 123 | '123'` 
  - `let name :string[] | number =`
  - type 타입 = string | number
  - let 타입 :Name = '123' => 상단에서 선언한 타입 재사용

  - ```txt
    funstion 함수(x:number) :number {
    	return x * 2
    }
    
    무조건 number가 들어와야 되고, number가 return 되야함
    ```

  - ```txt
    type Member = [number, boolean];
    
    let cws:Member = [123, true];
    ```

  - ```txt
    type Member = {
    	name : string
    }
    ```

  - 

