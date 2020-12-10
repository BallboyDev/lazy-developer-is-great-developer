let data = [
    { langkind: '', coCd: '', divCd: '', trCd: '', index: '', },
    { langkind: '', coCd: '', divCd: '', trCd: '', index: '', },
    { langkind: '', coCd: '', divCd: '', trCd: '', index: '', },
    { langkind: '', coCd: '', divCd: '', trCd: '', index: '', },
    { langkind: '', coCd: '', divCd: '', trCd: '', index: '', },
]

let camelToSnake = (before) => {
    let size = before.length
    let result = ''
    for (let i = 0; i < size; i++) {
        let upper = before[i].toUpperCase(); let lower = before[i].toLowerCase(); let chkRe = /[A-Za-z]/g;
        // (숫자, 특수문자)
        if (!chkRe.test(before[i])) { result += before[i] }
        // upper
        else if (before[i] === upper) { result = result + '_' + upper }
        // lower
        else if (before[i] === lower) { result += upper }
    }

    return result
}

let arrToArr = (arr) => {
    let changeArr = []
    arr.map((json) => {
        let changeJson = {}
        // console.log(v)
        let jsonKeys = Object.keys(json)
        jsonKeys.map((key) => {
            // console.log(key)
            changeJson[camelToSnake(key)] = json[key]
        })
        // console.log(changeJson)
        changeArr.push(changeJson)
    })
    return changeArr
}

console.log(arrToArr(data))
