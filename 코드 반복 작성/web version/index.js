window.onload = () => {
    console.log('text modify repeat work ( ver 2.1 )');
    console.log('made by Ballboy Seung Woo Yang');
    console.log('Copyleft ○ 2020 All Wrongs reserved');
    console.log('===== menual =====');
    console.log('<#0> => value');
    console.log('<#i> => index');
    // console.log('-- comment => comment');

    // 실행버튼, change 버튼 클릭시 실행
    this.document.getElementById('change').onclick = () => {
        let data = this.document.getElementById('data').value.split('\n');  // 입력된 데이터를 라인별로 분할하여 리스트로 저장
        let form = this.document.getElementById('form').value;
        let trans_list = [...new Set(form.match(/<#[0-9]>/gi))];    // form 에서 사용된 변환문자(<#n>) 중복없이 리스트로 저장
        let result = '';

        data.map((v, i) => {
            result = result + this.formet(v, i, form, trans_list) + '\n';   // 라인별 데이터를 최종 형태로 변형
        })

        this.document.getElementById('result').value = result;  // 최종 결과물 result에 출력
    }

    formet = (data_list, i, form, trans_list) => {
        let sub_result = form
        let data_value = data_list.split(/ |\t/gi).filter((v) => { return v !== '' })   // 입력된 라인을 blank 값에 따라 한번더 list로 분할

        sub_result = sub_result.replace(/<#i>/gi, i); // form형식에 작성된 index 변환문자(<#i>)를 index 값으로 변경

        trans_list.map((trans_value, i) => {
            sub_result = sub_result.split(trans_value).join(data_value[i])  // 데이터 리스트와 변환 문자 리스트를 비교하여 같은 index의 값끼리 변환
        })

        return sub_result;
    }

    // menual 버튼 클릭시 실행
    // 예시 data와 form을 입력, 사용방법을 출력
    this.document.getElementById('menual').onclick = () => {
        this.document.getElementById('data').value = '1-1\t1-2\t1-3\t1-4\n2-1\t2-2\t2-3\t2-4\n3-1 3-2 3-3 3-4\n4-1 4-2 4-3 4-4\n5-1 5-2 5-3 5-4\n6-1 6-2 6-3 6-4';
        this.document.getElementById('form').value = '-- <#i> 번째 반복 -- \nline1 = <#0>\nline2 = <#1>\nline3 = <#2>\nline4 = <#0>';
        this.document.getElementById('result').value = '데이터 입력칸(좌상단)에 순차적으로 입력될 데이터를 한 줄 단위로 입력한다.\nex) a\n    b\n    c\n    d\n    e\n\n반복 형식 입력칸(좌하단)에 반복될 형식을 입력한다.\nex)\n입력문자 : <#0>\n\n데이터화 형식이 입력이 되었으면 change 버튼을 클릭한다.\nresult)\n입력문자 : a\n입력문자 : b\n입력문자 : c\n입력문자 : d\n입력문자 : e\n\n결과창에 나타난 데이터를 확인한다.';
    }
    // empty 버튼 클릭시 실행
    // 모든 textarea 내용 삭제
    this.document.getElementById('empty').onclick = () => {
        this.document.getElementById('data').value = '';
        this.document.getElementById('form').value = '';
        this.document.getElementById('result').value = '';
    }

}