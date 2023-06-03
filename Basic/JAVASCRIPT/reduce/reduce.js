const afterStudy = [
    {name: '최우석', team:'APM-FE', englishName: 'Ralph'},
    {name: '오민석', team:'AI-FE', englishName: 'Bernard'},
    {name: '이은지', team:'AI-FE', englishName: 'Sophie'},
    {name: '??', team:'',}
];

// 위의 배열을 아래와 같은 형식의 데이터로 변경하려 합니다.

// {
//     'Ralph': {name: '최우석', team: 'APM-FE'},
//     'Bernard': {name: '오민석', team: 'AI-FE'},
//     'Sophie': {name: '이은지', team: 'AI-FE'}
// }

// 처음 든 생각
// 1. afterStudy 배열을 전체 순회, 2. 각 로우별로 name이랑 다른 값 찾아서 넣기

// const testCase1 = {}

// for (let ix = 0, ixLen = afterStudy.length; ix < ixLen; ix++) {
//     const memberInfo = afterStudy[ix];
//     const {name, team, englishName} = memberInfo;

//     if (englishName) {
//         testCase1[englishName] = {'name':name, 'team':team}
//     }
// }

// console.log(testCase1);

// 이후에 든 생악
// english Name이 없거나 하는, 예외 케이스 로직 추가외에 뭔가 큰 다른거는 생각이 안났음


// reduce를 사용해보자

const testCase2 = afterStudy.reduce((prev, memberInfo) => {
    if (!memberInfo.englishName) {
        return prev;
    }

    prev[memberInfo.englishName] = {name: memberInfo.name, team: memberInfo.team};
    return prev;
}, {})