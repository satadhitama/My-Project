
const card = ["rock", 'paper', 'scissor']
let decisionArray = [[false, false, false],
                     [null, false, true], 
                     [true, null, false],
                     [false, true, null]];
let setRoundTime = 0;
let roundTime = setRoundTime;
let isGameSet = true;
let isPaused = true;

// Object player Human
function Human() {
  this.bestScore = 0;
  this.currentScore = 0;
  this.numberPick = 0;
  this.btnPick = function (event) {
    this.numberPick = parseInt(event.target.dataset.pick) ;
    this.cardImage(this.numberPick);
  }
  this.cardImage = function (cardNumber) {
    const playerCard = document.querySelector('.card-container.player');
    playerCard.style.backgroundImage = "url(assets/" + card[cardNumber-1] + ".png)";
  }
}

// Object player Enemy
function Enemy() {
  this.numberPick = function () { 
    return Math.ceil(Math.random() * 3);
  }
  this.cardImage = function (cardNumber) {
    const playerCard = document.querySelector('.card-container.enemy');
    playerCard.style.backgroundImage = "url(assets/" + card[cardNumber-1] + ".png)";
  }
}

function gameSet() {
  let play = setInterval(() => {
    if (isPaused) {
      clearInterval(play)
    } else {
      if (roundTime === 0) {
        let enemyPick = enemy.numberPick();
        let playerPick = [human.numberPick, enemyPick];
        let roundStatus = isWin(playerPick[0],playerPick[1]-1);
        displayStatus(roundStatus);
        updateCountdown(roundTime);
        enemy.cardImage(enemyPick);
        roundTime = setRoundTime;
        switch (roundStatus) {
          case true:
            if (human.currentScore === human.bestScore) {
              human.currentScore++;
              human.bestScore++;
            } else if (human.currentScore < human.bestScore) {
              human.currentScore++;
            }
            break;
          case false:
            human.currentScore = 0
            break;
        }
        updateBestScore(human.bestScore);
        updateCurrentScore(human.currentScore);
      } else {
        updateCountdown(roundTime);
        roundTime--; 
      }
    }
  }, 1000)
}

function startGame() {
  const time = document.querySelector('#round-time').value;
  const modal = document.querySelector('.modal-container');
  if (isNaN(time) || time === "") {
    const warning = document.querySelector('#input-warning');
    warning.classList.remove('hide');
  } else if (!isNaN(time) && parseInt(time) > 0) {
    modal.classList.add('hide');
    setRoundTime = parseInt(time);
    roundTime = setRoundTime;
    gameSet();
    isPaused = false;
  }
}

function btnPause(event) {
  pause = event.target.dataset.isPaused;
  const displayPause = document.querySelector('#pause');
  if (pause == "false") {
    displayPause.innerHTML = "&blacktriangleright;";
    displayPause.style.fontSize = "40px";
    displayPause.dataset.isPaused = "true";
    isPaused = true;
  } else {
    displayPause.innerHTML = "&#10074&#10074";
    displayPause.style.fontSize = "25px";
    displayPause.dataset.isPaused = "false";
    gameSet();
    isPaused = false;
  }
}

function btnReset() {
  const modal = document.querySelector('.modal-container');
  modal.classList.remove('hide');
  isPaused = true;
}

function closeModal() {
  const pauseCondition = document.querySelector('#pause').dataset.isPaused;
  const modal = document.querySelector('.modal-container');
  console.log(pauseCondition);
  if (setRoundTime > 0 && pauseCondition === "false") {
    gameSet();
    modal.classList.add('hide');
    isPaused = false;
  } else if (pauseCondition === "true") {
    modal.classList.add('hide');
  }
}

function updateCountdown(currentTime) {
  const countdown = document.querySelector('.countdown.bar');
  if (currentTime < 10) {
    countdown.innerHTML = "0" + currentTime;
  } else {
    countdown.innerHTML = currentTime;
  }
}

function updateBestScore(bestScore) {
  const displayBestScore = document.querySelector('#best-score');
  displayBestScore.innerHTML = bestScore;
}

function updateCurrentScore(currentScore) {
  const displayCurrentScore = document.querySelector('#current-score');
  displayCurrentScore.innerHTML = currentScore;
}

function isWin(humanPick, enemyPick) {
  return decisionArray[humanPick][enemyPick];
}

function displayStatus(condition) {
  const status = document.querySelector('.center-container');
  const playerStatus = document.querySelector('#player-status');
  let textStatus = "";
  switch (condition) {
    case true:
      textStatus = "WON"
      break;
    case false:
      textStatus = "LOST"
      break;
    case null:
      textStatus = "DRAW"
      break;
  }
  if (status.children.length === 0) {
    const paragraph = document.createElement("p");
    const text = document.createTextNode(textStatus);
    paragraph.id = "player-status"
    paragraph.appendChild(text);
    status.appendChild(paragraph)
  } else {
    status.classList.remove(status.classList[1])
    playerStatus.innerHTML = textStatus;
  }
  status.classList.add(textStatus.toLowerCase());
}

let human = new Human();
let enemy = new Enemy();

gameSet();
