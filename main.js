const { app, BrowserWindow } = require("electron");
const path = require("path");

// --- Opcional: Para ejecutar scripts de Python desde Electron ---
// const { spawn } = require('child_process');

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    webPreferences: {
      // Estas dos líneas son importantes para que tu JS actual funcione dentro de Electron
      nodeIntegration: true,
      contextIsolation: false,
    },
    // Opcional: si creaste una carpeta 'assets' con un icono 'icon.png'
    // icon: path.join(__dirname, 'assets/icon.png')
  });

  // Carga tu archivo HTML principal en la ventana.
  mainWindow.loadFile(path.join(__dirname, 'dioptra_spy', 'dioptra-spy.html'));

  // Opcional: Descomenta la siguiente línea para abrir las herramientas de desarrollador
  // automáticamente. Muy útil para depurar.
  // mainWindow.webContents.openDevTools();
}

// Esta función se llama cuando Electron ha terminado de inicializarse.
app.whenReady().then(() => {
  createWindow();

  app.on("activate", function () {
    // En macOS, es común volver a crear una ventana si se hace clic en el icono del dock.
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

// Cierra la aplicación cuando todas las ventanas están cerradas (excepto en macOS).
app.on("window-all-closed", function () {
  if (process.platform !== "darwin") app.quit();
});
