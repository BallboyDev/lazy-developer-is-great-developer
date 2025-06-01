const robot = require('robotjs')

robot.setMouseDelay(200)

const count = process?.argv[2] || 5

console.log("count >>", count)

for (let i = 0; i < count; i++) {
    console.log('click', i)
    robot.mouseClick()
}
