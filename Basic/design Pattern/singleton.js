// 클래스의 단일 인스턴스만을 원할 때 사용하는 패턴,
// 해당 클래스로 여러개의 인스턴스 생성 x => 단 하나의 인스턴스만을 위한 패턴


class DatabaseConnection {
    constructor() {
        this.databaseConnection = 'dummytext';
    }

    getNewDBConnection() {
        return this.databaseConnection;
    }
}

class Singleton {
  constructor() {
    throw new Error('Use the getInstance() method on the Singleton object!')
  }

  getInstance() {
    if (!Singleton.instance) {
      Singleton.instance = new DatabaseConnection()
    }

    return Singleton.instance
  }
}

module.exports = Singleton

// 싱글턴 패턴을 사용하는 이유
// 생성자가 여러번 호출되도, 실제로 생성되는 객체는 단 하나
// 이미 인스턴스가 있을 경우, 새로 생성 x

// 사용하는 이유
// 객체를 생성할 때마다 메모리 영역을 할당해야하는데, 최상단 전역등에서 단 한번만 생성 후 사용하는
// 경우등에서는 새롭게 생성할 필요 x

// 많이 사용하는 경우
// 데이터베이스 연결 상태등에 대한 정보를 싱글톤 패턴을 통해 만든 인스턴스가 가지고 있도록 구성
// 해당 인스턴스는 전역에서 모두 접근 가능하도록 설께

// 단점
// 싱글턴 패턴으로 생성된 인스턴스가 지나치게 많은 일을 할 경우에는 다른 클래스들과의 결합도가 높아짐
// 너무 많은 기능을 싱글턴 패턴안에 넣으면, 다른 클래스들이 싱글턴 인스턴스에 대한 의존성이 증가할 수 있음


// 참고
// https://yceffort.kr/2021/01/nodejs-4-design-pattern
// https://gyoogle.dev/blog/design-pattern/Singleton%20Pattern.html