/* DioptraSpy
 * Copyright (C) 2025 Kanarath
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

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
