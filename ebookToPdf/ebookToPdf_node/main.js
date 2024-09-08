const { app, BrowserWindow, clipboard } = require('electron')
const path = require('path')

const createWindow = () => {
    const win = new BrowserWindow({
        width: 400,
        height: 400,
        resizable: false,
        webPreferences: {
            // Dom 로딩 후 실행
            preload: path.join(__dirname, 'preload.js')
        }
    })

    win.loadFile('index.html')
}

// app : event lifecycle 관리
app.whenReady().then(() => {
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

/** Package and distribute application */
/**
 * npm install --save-dev @electron-forge/cli
 * npx electron-forge import
 * 
 * npm run make
 */
