
// Calculator display
let dataCalculate = ['0'];
let opResult = '';
let tempOperation = '';

function button(event) {
  let btnVal = event.target.dataset.buttonValue;

  if (parseInt(dataCalculate[dataCalculate.length - 1]) === 0 && !isNaN(btnVal) && dataCalculate[dataCalculate.length - 1].indexOf('.') === -1) {
    if (dataCalculate[dataCalculate.length - 1] === '0') {
      dataCalculate[dataCalculate.length - 1] = btnVal;
    }
    else {
      dataCalculate[dataCalculate.length - 1] = '-' + btnVal;
    }
    dispayResult();
  }
  else {
    if (isNaN(btnVal)) {
      if (btnVal === "clear") {
        dataCalculate = ['0'];
        dispayResult();
      }
      else if (btnVal === "del") {
        if (!isNaN(dataCalculate[dataCalculate.length - 1])) {
          if (dataCalculate.length === 1 && dataCalculate[0].length === 1) {
            dataCalculate = ['0'];
          }
          else {
            let tempDigit = dataCalculate[dataCalculate.length - 1]
            dataCalculate[dataCalculate.length - 1] = "";
            for (let i = 0; i < tempDigit.length-1; i++) {
              dataCalculate[dataCalculate.length - 1] += tempDigit[i];
            }
          }
        }
        else {
          dataCalculate.pop();
        }
        dispayResult();
      }
      else if (btnVal === "plus-min") {
        if (!isNaN(dataCalculate[dataCalculate.length - 1])) {
          if (dataCalculate[dataCalculate.length - 1][0] === "-") {
            dataCalculate[dataCalculate.length - 1] = dataCalculate[dataCalculate.length - 1].substring(1,dataCalculate[dataCalculate.length - 1].length);
          }
          else {
            dataCalculate[dataCalculate.length - 1] = '-' + dataCalculate[dataCalculate.length - 1].substring(0,dataCalculate[dataCalculate.length - 1].length);
          }
        }
        else {
          dataCalculate.push('-0');
        }
        dispayResult();
      }
      else if (btnVal === '.') {
        if (!isNaN(dataCalculate[dataCalculate.length - 1]) && dataCalculate[dataCalculate.length - 1].indexOf('.') === -1) {
          dataCalculate[dataCalculate.length - 1] += btnVal;
        }
      }
      else if (btnVal === '=') {
        if ((tempOperation === '' && opResult === '') && getOperation(dataCalculate) !== '0') {
          updateTempData();
          displayHistory()
        }
        if (checkHistory() === true && getOperation(dataCalculate) !== '0') {
          displayHistory();
        }
        updateTempData();
      }
      else {
        if (dataCalculate[dataCalculate.length - 1].length > 1 || !isNaN(dataCalculate[dataCalculate.length - 1])) {
          dataCalculate.push(btnVal);
        }
        else {
          dataCalculate[dataCalculate.length - 1] = btnVal;
        }
      }
    }
    else {
      if (!isNaN(dataCalculate[dataCalculate.length - 1]) || dataCalculate[dataCalculate.length - 1].indexOf('.') !== -1) {
        dataCalculate[dataCalculate.length - 1] += btnVal;
      }
      else {
        dataCalculate.push(btnVal)
      }
      dispayResult();
    }
  }
  if (dataCalculate[dataCalculate.length - 1] === "") {
    dataCalculate.pop();
  }
  displayOperation();
  // console.log(dataCalculate)
}

function calculate() {
  let tempResult = [];
  if (isNaN(dataCalculate[dataCalculate.length - 1]) && dataCalculate[dataCalculate.length - 1].length === 1) {
    dataCalculate.pop();
  }
  dataCalculate.forEach(data => {
    if (data.endsWith('.')) {
      data = data.substring(0, data.length-1);
    }
    tempResult.push(data)
  });
  while (tempResult.length > 1) {
    let operationResult = 0;
    for (let i = 1; i < tempResult.length; i+=2) {
      let firstVal = 0;
      let secondVal = 0;
      // Check type of num
      if (tempResult[i - 1].indexOf('.') !== -1) {
        firstVal = parseFloat(tempResult[i - 1]);
      } else {firstVal = parseInt(tempResult[i - 1])}
      if (tempResult[i + 1].indexOf('.') !== -1) {
        secondVal = parseFloat(tempResult[i + 1]);
      } else {secondVal = parseInt(tempResult[i + 1])}
      // Check Operator
      if (tempResult[i] === '*' || tempResult[i] === '/') {
        if (tempResult[i] === '*') {
          operationResult = firstVal * secondVal;
        }
        else {
          operationResult = firstVal / secondVal;
        }
        tempResult.splice(i - 1, 2);
        tempResult[i - 1] = operationResult.toString();
  
        break;
      }
      else if (tempResult[i] === '+' || tempResult[i] === '-') {
        if ((tempResult.indexOf('*') !== -1 || tempResult.indexOf('/') !== -1) &&
            (tempResult[i] !== '*' || tempResult[i] !== '/')) {
            continue;
        }
        if(tempResult[i] === '+') {
          operationResult = firstVal + secondVal;
        }
        else {
          operationResult = firstVal - secondVal;
        }
        tempResult.splice(i - 1, 2);
        tempResult[i - 1] = operationResult.toString();
        break;
      }
    }
  }
  return tempResult['0']
}

function dispayResult() {
  let resultDisplay = document.querySelector('.display-num.result');
  let result = calculate();
  resultDisplay.innerHTML = result;
}

function getOperation(arrOperation) {
  let operation = '';
  for (let i = 0; i < arrOperation.length; i++) {
    for (let j = 0; j < arrOperation[i].length; j++) {
      if (arrOperation[i][j] === '*') {
        operation += '&times;';
      }
      else if (arrOperation[i][j] === '/') {
        operation += '&div;';
      }
      else {
        operation += arrOperation[i][j];
      }
    }
  }
  return operation
}

function displayOperation() {
  let operationDisplay = document.querySelector('.display-num.operation');
  operationDisplay.innerHTML = getOperation(dataCalculate);
}


function checkHistory() {
  let validOperation = true;
  if (getOperation(tempOperation) === getOperation(dataCalculate) && calculate() === opResult) {
    validOperation = false;
  }
  return validOperation;
}

function displayHistory() {
  let arrOperation = dataCalculate;
  if (isNaN(arrOperation[arrOperation.length - 1]) && arrOperation[arrOperation.length - 1].length === 1) {
    arrOperation.pop();
  }
  let historyDisplay = document.querySelector('.history');
  let paragraph = document.createElement('p');
  paragraph.innerHTML = getOperation(arrOperation) + ' = ' + calculate();
  paragraph.classList.add('operation-history');
  historyDisplay.appendChild(paragraph);
}

function updateTempData() {
  opResult = calculate();
  let arrOperation = dataCalculate;
  if (isNaN(arrOperation[arrOperation.length - 1]) && arrOperation[arrOperation.length - 1].length === 1) {
    arrOperation.pop();
  }
  tempOperation = getOperation(arrOperation);
}

function clearHistory() {
  let btnClearHistory = document.querySelector('.btn.clear-history');
  let historyDisplayed = document.querySelector('.history');
  btnClearHistory.addEventListener('click', () => {
    console.log(historyDisplayed.children)
    // historyDisplayed.removeChild(historyDisplayed.getRootNode);
  });
}