/**
 * Создает новый лист на основе последнего листа в таблице, скрывая старый.
 * В имени листа используется дата создания.
 */
function createNewSheetFromLast() {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheets = ss.getSheets();
  
    // Проверка наличия листов
    if (sheets.length === 0) {
      Logger.log("В таблице нет ни одного листа.");
      return;
    }
  
    // Получаем последний лист
    let lastSheet = sheets[sheets.length - 1];
    let lastSheetName = lastSheet.getName();
  
    // Создаем новый лист на основе последнего
    let newSheet = lastSheet.copyTo(ss);
    let today = new Date();
    let newSheetName = Utilities.formatDate(today, ss.getSpreadsheetTimeZone(), "dd-MM-yyyy");
  
    // Проверяем, содержит ли последний лист дату, и, если да, добавляем 1 день
    const dateRegex = /(\d{4}-\d{2}-\d{2})/; // Регулярное выражение для поиска даты в формате yyyy-MM-dd
    const dateMatch = lastSheetName.match(dateRegex);
  
    if (dateMatch) {
      try {
        let lastDate = new Date(dateMatch[1]);
        lastDate.setDate(lastDate.getDate() + 1); // Добавляем один день
        newSheetName = Utilities.formatDate(lastDate, ss.getSpreadsheetTimeZone(), "dd-MM-yyyy");
      } catch (e) {
        Logger.log("Не удалось добавить день к дате в имени последнего листа. Используется текущая дата.");
      }
    }
  
    newSheet.setName(newSheetName);
  
    // Скрываем старый лист
    lastSheet.hideSheet();
  
    Logger.log(`Создан новый лист "${newSheetName}" на основе "${lastSheetName}". Старый лист "${lastSheetName}" скрыт.`);
  }
  
  /**
   * Создает пункт меню для запуска скрипта.
   */
  function onOpen() {
    const ui = SpreadsheetApp.getUi();
    ui.createMenu('Действия с Листами')
      .addItem('Создать новый лист из последнего', 'createNewSheetFromLast')
      .addToUi();
  }