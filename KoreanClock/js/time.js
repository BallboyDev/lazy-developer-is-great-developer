var kors = [
	'이', '삼', '십', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '일',
	'오', '전', '후', '굿', '열', '한', '두', '세', '네', '다', '볼', '여', '섯', '일', '곱', '덟', '아', '홉', '시',
	'이', '삼', '사', '오', '십', '일', '이', '보', '삼', '사', '오', '육', '칠', '팔', '구', '분',
	'이', '삼', '사', '오', '십', '일', '이', '이', '삼', '사', '오', '육', '칠', '팔', '구', '초'
]

var dlf = function(d){
	var kor = "";
	if(d.ten != 0){
		switch(d.ten){
		case(2):
			kor = "이";
			break;
		case(3):
			kor = "삼";
			break;
		}
		kor += "십";
	}
	
	switch(d.one){
	case(1):
		kor += "일";
		break;
	case(2):
		kor += "이";
		break;
	case(3):
		kor += "삼";
		break;
	case(4):
		kor += "사";
		break;
	case(5):
		kor += "오";
		break;
	case(6):
		kor += "육";
		break;
	case(7):
		kor += "칠";
		break;
	case(8):
		kor += "팔";
		break;
	case(9):
		kor += "구";
		break;
	}
	kor += "일";
	return kor;
}

var tl = function(h){
	var kor = "오";
	if(h.o >= 12)
		kor += "후";
	else
		kor += "전";
	
	if(h.ten != 0)
		kor += "열";
	switch(h.one){
	case(1):
		kor += "한";
		break;
	case(2):
		kor += "두";
		break;
	case(3):
		kor += "세";
		break;
	case(4):
		kor += "네";
		break;
	case(5):
	case(6):
		if(h.one == 5)
			kor += "다섯";
		else
			kor += "여섯";
		break;
	case(7):
		kor += "일곱";
		break;
	case(8):
		kor += "여덟";
		break;
	case(9):
		kor += "아홉";
		break;
	}
	kor += "시";
	return kor;
}

var qns_ch = function(qc){
	var kor = "";
	
	if(qc.ten != 0){
		switch(qc.ten){
		case(2):
			kor += "이"; break;
		case(3):
			kor += "삼"; break;
		case(4):
			kor += "사"; break;
		case(5):
			kor += "오"; break;
		}
		kor += "십";
	}
	
	switch(qc.one){
	case(1):
		kor += "일"; break;
	case(2):
		kor += "이"; break;
	case(3):
		kor += "삼"; break;
	case(4):
		kor += "사"; break;
	case(5):
		kor += "오"; break;
	case(6):
		kor += "육"; break;
	case(7):
		kor += "칠"; break;
	case(8):
		kor += "팔"; break;
	case(9):
		kor += "구"; break;
	}
	
	if(qc.name == "m")
		kor += "분";
	else
		kor += "초";
	return kor;
}

var time = function(){
	var timeKor="";
	var t = new Date();
	var d = {};
	d.o = t.getDate();
	d.ten = Math.floor(d.o / 10);
	d.one = d.o % 10;
	var h = {}
	h.o = t.getHours();
	h.ten = Math.floor((h.o-12) / 10);
	h.one = (h.o-12) % 10;
	var m = {};
	m.o = t.getMinutes();
	m.name = "m";
	m.ten = Math.floor(m.o / 10);
	m.one = m.o % 10;
	var s = {};
	s.o = t.getSeconds();
	s.name = "s";
	s.ten = Math.floor(s.o / 10);
	s.one = s.o % 10;
	
	timeKor = timeKor + dlf(d) + tl(h) + qns_ch(m) + qns_ch(s);
	
	var timeBox = document.getElementById("time-box");
	var k = 0;
	var kor = "";
	
	for(var i = 0; i < 8; i++){
		for(var j = 0; j < 8; j++){
			if(timeKor[k] == kors[(i*8)+j]){
				kor = kor + "<span>" + kors[(i*8)+j] + "</span>";
				k++;
			} else {
				kor = kor + kors[(i*8)+j];
			}
		}
		if(i != 8){
			kor = kor + "<br>";
		}
	}
	timeBox.innerHTML = kor;
	kor = "";
}

window.onload = function(){
	//time();
	setInterval("time()", 1000);
};