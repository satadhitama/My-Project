let board = [[null,null,null],
             [null,null,null],
             [null,null,null]]
let isGameRun = true;
let currentPlayer = "Player 2";
let playerScore = [0,0];

function cellClick(event) {
  if (isGameRun) {
    const position = event.target.dataset.cellPosition;
    const row = parseInt(position[0]);
    const col = parseInt(position[1]);
    const cellBoard = document.querySelector('.cell-'+position);
    if (currentPlayer === "Player 1") {
      if (board[row][col] === null) {
        board[row][col] = true;
        if (isWin(row, col) === false) {
          currentPlayer = "Player 2"; 
        }
        cellBoard.style.backgroundImage = "url(assets/circle.svg)";
      }
    } else {
      if (board[row][col] === null) {
        board[row][col] = false;
        if (isWin(row, col) === false) {
          currentPlayer = "Player 1"; 
        }
        cellBoard.style.backgroundImage = "url('assets/x.svg')";
      }
    }
    if (isWin(row, col) === true ) {
      isGameRun = false
      displayModal('win');
      if (currentPlayer === "Player 1") {
        playerScore[0]++;
      } else {
        playerScore[1]++
      }
      updateScore();
    } else if (isBoardNotIncludeNull() && isWin(row, col) === false) {
      isGameRun = false
      displayModal('draw');
    } else {
      updateCurrentPlayer(currentPlayer);
    }
  } 
}

function btnReset() {
  displayModal('reset');
}

function isWin(row, col) {
  let playerWin = false;
  const validAdjCell = checkAdjCell(row,col);
  for (let i = 0; i < validAdjCell.length; i++) {
    let validReversedCell = reversedCell(`${row}${col}`, validAdjCell[i]);
    let validNextCell = nextCell(`${row}${col}`, validAdjCell[i]);
    try {
      if (board[row][col] === board[validReversedCell[0]][validReversedCell[1]]
        && board[row][col] != null){
        playerWin = true;
        break;
      }
    } catch (e) {}
    try {
      if (board[row][col] === board[validNextCell[0]][validNextCell[1]]
        && board[row][col] != null){
        playerWin = true;
        break;
      }
    } catch (e) {}
  }
  return playerWin;
}

function checkAdjCell(row,col) { 
  let checkedCell = [];
  for (let i = row-1; i <= row+1; i++) {
    for (let j = col-1; j <= col+1; j++) {
      if (i != row || j != col) {
        try {
          if (board[i][j] === board[row][col]) {
            checkedCell.push(`${i}${j}`)
          }
        } catch (e) {continue;}
      }
    }
  }
  return checkedCell;
}

function nextCell(mainCell, adjCell) {
  let possibleCell = "";
  for (let i = 0; i < mainCell.length; i++) {
    if (parseInt(mainCell[i]) < parseInt(adjCell[i])) {
      possibleCell += `${parseInt(adjCell[i])+1}`;
    } else if(parseInt(mainCell[i]) > parseInt(adjCell[i])) {
      possibleCell += `${parseInt(adjCell[i])-1}`;
    } else {
      possibleCell += `${parseInt(adjCell[i])}`
    }
  }
  return possibleCell;
}

function reversedCell(mainCell, adjCell) {
  let possibleCell = "";
  for (let i = 0; i < mainCell.length; i++) {
    if (parseInt(mainCell[i]) < parseInt(adjCell[i])) {
      possibleCell += `${parseInt(mainCell[i])-1}`;
    } else if(parseInt(mainCell[i]) > parseInt(adjCell[i])) {
      possibleCell += `${parseInt(mainCell[i])+1}`;
    } else {
      possibleCell += `${parseInt(mainCell[i])}`
    }
  }
  return possibleCell;
}

function continueGame(event) {
  const modal = event.target.parentElement.parentElement.id;
  if (modal === "win") {
    clearModal("win");
  } else if (modal === 'draw') {
    clearModal("draw");
  } else {
    clearModal("reset");
  }
  boardSet();
  isGameRun = true;
}

function displayModal(modalID) {
  const modalContainer = document.querySelector('.modal-container');
  const modal = document.querySelector('#'+modalID);
  modalContainer.classList.add('modal-active');
  modal.classList.remove('not-displayed');
}

function boardSet() {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      board[i][j] = null;
      const cellBoard = document.querySelector(`.cell-${i}${j}`);
      cellBoard.style.backgroundImage = "";
    }
  }
}

function clearModal(modalID) {
  const modalContainer = document.querySelector('.modal-container');
  const modal = document.querySelector("#"+modalID);
  modalContainer.classList.remove('modal-active');
  modal.classList.add('not-displayed');
}

function isBoardNotIncludeNull() {
  isNotInclude = true;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === null) {
        isNotInclude = false;
        break;
      }
    }
  }
  return isNotInclude;
}

function updateCurrentPlayer(player) {
  const infoBarPlayer = document.querySelector('#current-player');
  const playerWinModal = document.querySelector('#player-win');
  infoBarPlayer.innerHTML = player;
  playerWinModal.innerHTML = player;
  if (player === "Player 1") {
    infoBarPlayer.style.color = "rgb(115, 115, 223)";
    playerWinModal.style.color = "rgb(115, 115, 223)";
  } else {
    infoBarPlayer.style.color = "rgb(223, 75, 75)";
    playerWinModal.style.color = "rgb(223, 75, 75)";
  }
}

function updateScore() {
  for (let i = 0; i < playerScore.length; i++) {
    const player = document.querySelector('#player-'+ (i + 1));
    player.innerHTML = playerScore[i];
  }
}

function resetGame() {
  boardSet();
  currentPlayer = "Player 1";
  playerScore = [0,0];
  updateCurrentPlayer(currentPlayer);
  updateScore();
  clearModal('reset');
}
