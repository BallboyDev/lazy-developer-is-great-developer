let data = { LANGKIND: '', CO_CD: '', DIV_CD: '', TR_CD: '', INDEX: '' }
// let data = { langkind: '', coCd: '', divCd: '', trCd: '', index: '' }

let snakeToCamel = (before) => {
    let size = before.length;
    let mid = before.toLowerCase();
    let result = ''; let seq = false;
    for (let i = 0; i < size; i++) {
        let chkRe = /[A-Za-z]/g;
        if (chkRe.test(mid[i])) {
            if (seq) {
                result += mid[i].toUpperCase()
                seq = false
            } else {
                result += mid[i]
            }
        } else {
            seq = true
        }
    }

    return result
}

// console.log(snakeToCamel('DIV_CDS_TR_CD_CO_CD'))

let jsonToJson = (json) => {
    let changeJson = {}
    let jsonKeys = Object.keys(json)
    jsonKeys.map((key) => {
        changeJson[snakeToCamel(key)] = json[key]
    })
    return changeJson
}

console.log(data)
console.log(jsonToJson(data))