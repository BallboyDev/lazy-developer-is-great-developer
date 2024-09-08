// const { contextBridge } = require('electron')
// const rb = require('robotjs')

// contextBridge.exposeInMainWorld('versions', {
//     node: () => process.versions.node,
//     chrome: () => process.versions.chrome,
//     electron: () => process.versions.electron,
//     // we can also expose variables, not just functions
//     screenSize: () => {
//         const temp = rb.getScreenSize()
//         console.log('screen Size : ', temp)
//     }
// })


const { contextBridge } = require('electron')
const robot = require('robotjs')

contextBridge.exposeInMainWorld('versions', {
    node: () => process.versions.node,
    chrome: () => process.versions.chrome,
    electron: () => process.versions.electron,
    // we can also expose variables, not just functions
    screenSize: () => {
        const temp = robot.getScreenSize()
        console.log('screen Size : ', temp)
    }
})