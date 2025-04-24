const robot = require('robotjs')

robot.setMouseDelay(500)

for (let i = 0; i < 100; i++) {
    console.log('click', i)
    robot.mouseClick()
}
