window.onload = () => {
    console.log('ballboy\'s development tool ( ver 3.0 )');
    console.log('made by Ballboy Seung Woo Yang');
    console.log('Copyleft ○ 2021 All Wrongs reserved');

    // radio 버튼 상태 확인
    radioStatus = () => {
        for (let i = 0; i < this.document.getElementsByClassName('radio').length; i++) {
            if (this.document.getElementsByClassName('radio')[i].checked === true) {
                return this.document.getElementsByClassName('radio')[i].value
            }
        }

        return 'error'
    }

    // 실행버튼, change 버튼 클릭시 실행
    this.document.getElementById('change').onclick = () => {
        let data = ''; let form = ''; let trans_list = ''; let result = '';
        switch (this.radioStatus()) {
            case 'query':
                let index = 0
                form = this.document.getElementById('form').value
                data = this.document.getElementById('data').value.split('\n').map((v, i) => {
                    if (v.indexOf('=>') > -1) {
                        return {
                            colName: v.split('=>')[0].trim(),
                            value: v.split('=>')[1].trim()
                        }
                    } else if (v.trim().length !== 0) {
                        return {
                            colName: `colName${i}`,
                            value: v.trim()
                        }
                    }
                }).filter((v) => { return (v || '') !== '' })

                form = form.split('').map((v) => {
                    if (v === '?') {
                        return index < data.length ? `#{${data[index++].colName}}` : v
                    } else {
                        return v
                    }
                }).join('')

                data.map((v) => {
                    let reg1 = new RegExp(`#{(${v.colName})}`, 'gi')
                    form = form.replace(reg1, `'${v.value}'`)
                })

                this.document.getElementById('result').value = form
                break;
            case 'repeat':
                form = this.document.getElementById('form').value;
                data = this.document.getElementById('data').value.split('\n').map((v1, i1) => {
                    return {
                        index: i1,
                        values: v1.split(/ |\t/gi).filter((v) => { return v !== '' }).map((v2, i2) => {
                            return {
                                [`value${i2}`]: v2
                            }
                        })
                    }
                })

                data.map((v1, i1) => {
                    let temp = form.replace(/#{i}/gi, i1)
                    v1.values.map((v2, i2) => {
                        let reg2 = new RegExp(`#{(${i2})}`, 'gi')
                        temp = temp.replace(reg2, v2[`value${i2}`])
                    })
                    trans_list = `${trans_list}${temp}\n`
                })

                this.document.getElementById('result').value = trans_list
                break;

            case 'error':
                console.error('에러 발생...???!!!! 왜지?!?!!!???!!')
                console.error('이거 출력되면... 승우한테 문의 하.... 지 말아주세요')
                console.error('저도 이게 어떻게 돌아가는지 지금은 잘.... 기억이 안날꺼 같아요.......')
                console.error('이게 발생 할 수가... 있나?!!?!??!?!??!?!')
                break;
        }
    }

    // menual 버튼 클릭시 실행
    // 예시 data와 form을 입력, 사용방법을 출력
    this.document.getElementById('menual').onclick = () => {
        switch (this.radioStatus()) {
            case 'query':
                this.document.getElementById('form').value = '----------예시1---------- \nSELECT * \n  FROM TEMP_TABLE T \n WHERE CO_CD = ? \n   AND DIV_CD = ? \n   AND EMP_CD = ?\n\n----------예시2---------- \nSELECT * \n  FROM TEMP_TABLE T \n WHERE CO_CD = #{coCd} \n   AND EMP_CD = #{empCd} \n   AND DIV_CD = #{divCd}'
                this.document.getElementById('data').value = 'coCd => 1000\ndivCd => 2000\nempCd => 3000'
                this.document.getElementById('result').value = '< query 변환 사용법 >\n1. form 입력칸(좌상단)에 쿼리를 입력한다.\n2. data 입력칸(좌하단)에 데이터를 입력한다.\n3. change 버튼을 클릭한다.\n\nform칸에 입력된 쿼리에서 \'?\' 문자는 쿼리 변환시 data칸에 입력된 데이터를 입력 라인 순서대로 변환됩니다.\n\nform칸에 Mybatis와 같이 #{colName} 형식으로 입력시에는 data칸에 입력된 데이터의 colName에 맞춰 변환이 이루어 집니다.\n\n----------예시1---------- \nSELECT * \n  FROM TEMP_TABLE T \n WHERE CO_CD = \'1000\' \n   AND DIV_CD = \'2000\' \n   AND EMP_CD = \'3000\'\n\n----------예시2---------- \nSELECT * \n  FROM TEMP_TABLE T \n WHERE CO_CD = \'1000\' \n   AND DIV_CD = \'2000\' \n   AND EMP_CD = \'3000\''
                break;
            case 'repeat':
                this.document.getElementById('data').value = '1-1\t1-2\t1-3\t1-4\n2-1\t2-2\t2-3\t2-4\n3-1 3-2 3-3 3-4\n4-1 4-2 4-3 4-4\n5-1 5-2 5-3 5-4\n6-1 6-2 6-3 6-4';
                this.document.getElementById('form').value = '-- #{i} 번째 반복 -- \nline1 = #{0}\nline2 = #{1}\nline3 = #{2}\nline4 = #{0}';
                this.document.getElementById('result').value = '데이터 입력칸(좌상단)에 순차적으로 입력될 데이터를 한 줄 단위로 입력한다.\nex) a\n    b\n    c\n    d\n    e\n\n반복 형식 입력칸(좌하단)에 반복될 형식을 입력한다.\nex)\n입력문자 : <#0>\n\n데이터화 형식이 입력이 되었으면 change 버튼을 클릭한다.\nresult)\n입력문자 : a\n입력문자 : b\n입력문자 : c\n입력문자 : d\n입력문자 : e\n\n결과창에 나타난 데이터를 확인한다.';
                break;
        }

    }
    // empty 버튼 클릭시 실행
    // 모든 textarea 내용 삭제
    this.document.getElementById('empty').onclick = () => {
        this.document.getElementById('data').value = '';
        this.document.getElementById('form').value = '';
        this.document.getElementById('result').value = '';
    }

}