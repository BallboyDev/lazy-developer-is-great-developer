/**
 * 구동 환경
 * 1. macbookpro 14inch
 * 2. 웨일 브라우저
 * 3. https://www.doosanbears.com/ticket/reserve?date=202506
 */

const robot = require('robotjs')

robot.setMouseDelay(150)

// 화면 우측 붉은색 티켓 예메 버튼 위치
robot.moveMouse(1387, 286)
// 명령어 실행을 위한 터미널이 최 상단에 있으므로 버튼 클릭을 위한 더블 클릭
robot.mouseClick() // 브라우저 선택 
robot.mouseClick() // 버튼 클릭 -> 예매 창 오픈

// 예매 일자 선택 버튼 이동
robot.moveMouse(733, 518)
// robot.moveMouse(711, 416)

// 적당히 빠른 클릭 속도 설정
robot.setMouseDelay(100)
// 로딩을 기다리기 위한 반복 클릭
for (let i = 0; i < 10; i++) {
    robot.mouseClick()
}

// 예매 페이지 입장 후 최초 공지 창 닫기 버튼 이동 후 클릭
robot.moveMouse(660, 326)
robot.mouseClick()

// 2025-06-01 : 440번대 입장 성공

/**
 * 개선 점
 * 1. 서버 시간 확인 후 자동 입장 기능 구현
 * 2. 페이지 로딩으로 인한 클릭 대기 기능 구현
 */
