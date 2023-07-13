let CurrentIndex=0
let scenes=null
  
  function check(id){
    let taunt=document.querySelector('#'+id+' #checkbox-taunt')
    let ds = document.querySelector('#'+id+' #checkbox-ds')
    let reborn = document.querySelector('#'+id+' #checkbox-reborn')
    let surrounding=document.querySelector('#'+id+' .Minion');
    if (taunt.checked && ds.checked && reborn.checked){
      surrounding.classList="";
      surrounding.classList.add("Minion");
      surrounding.classList.add("taunt-ds-reborn");
    }
    else if (taunt.checked && ds.checked){
      surrounding.classList="";
      surrounding.classList.add("Minion");
      surrounding.classList.add("taunt-ds");
    }
    else if (taunt.checked && reborn.checked){
      surrounding.classList="";
      surrounding.classList.add("Minion");
      surrounding.classList.add("taunt-reborn");
    }
    else if (ds.checked && reborn.checked){
      surrounding.classList="";
      surrounding.classList.add("Minion");
      surrounding.classList.add("ds-reborn");
    }
    else if (taunt.checked){
      surrounding.classList="";
      surrounding.classList.add("Minion");
      surrounding.classList.add("taunt");
    }
    else if (ds.checked){
      surrounding.classList="";
      surrounding.classList.add("Minion");
      surrounding.classList.add("ds");
    }
    else if (reborn.checked){
      surrounding.classList="";
      surrounding.classList.add("Minion");
      surrounding.classList.add("reborn");
    }
    else {
      surrounding.classList="";
      surrounding.classList.add("Minion");
    }
  }

  function checkds(id){
    let checkbox=document.querySelector('#'+id+' #checkbox-ds')
    let surrounding=document.querySelector('#'+id+' .Minion');
    console.log(checkbox);
    if (checkbox.checked){
      surrounding.classList.add("ds");
    }
    else{
      surrounding.classList.remove("ds");
    }
  }


  function checkreborn(id){
    let checkbox=document.querySelector('#'+id+' #checkbox-reborn')
    let surrounding=document.querySelector('#'+id+' .Minion');
    console.log(checkbox);
    if (checkbox.checked){
      surrounding.classList.add("reborn");
    }
    else{
      surrounding.classList.remove("reborn");
    }
  }

  function handleKeyDown(event) {
    if (event.keyCode === 39) { // Left arrow key
      const currentTextbox = event.target;
      const allTextboxes = document.querySelectorAll('input[type="text"]');
      const currentIndex = Array.from(allTextboxes).indexOf(currentTextbox);
      if (currentIndex+1<allTextboxes.length) {
        const previousTextbox = allTextboxes[currentIndex + 1];
        previousTextbox.focus();
      }
    }
    if (event.keyCode === 37){
      const currentTextbox = event.target;
      const allTextboxes = document.querySelectorAll('input[type="text"]');
      const currentIndex = Array.from(allTextboxes).indexOf(currentTextbox);
      if (currentIndex>0) {
        const previousTextbox = allTextboxes[currentIndex - 1];
        previousTextbox.focus();
      }
    }
  }
  function SendData(){
    let result = document.getElementById("defile-result")
    console.log("yes");
    let minions=[];
    for (var i =1;i<15;i++){
      let taunt = null;
      let ds = null;
      let reborn = null;
      if (i>7){
        taunt = document.querySelector('#F'+(i-7)+ ' #checkbox-taunt').checked;
        console.log("definede");
        reborn= document.querySelector('#F'+(i-7)+ ' #checkbox-reborn').checked;
        ds= document.querySelector('#F'+(i-7)+ ' #checkbox-ds').checked;
      }
      else {
        taunt = document.querySelector('#E'+i+ ' #checkbox-taunt').checked;
        console.log("definede");
        reborn= document.querySelector('#E'+i+ ' #checkbox-reborn').checked;
        ds= document.querySelector('#E'+i+ ' #checkbox-ds').checked;
      }
      let Modify=2*i
      console.log("t"+(Modify-1))
      let attack = document.getElementById("t"+(Modify-1)).value;
      let health = document.getElementById("t"+Modify).value;
      minion={
        attack:attack, 
        health:health,
        taunt: taunt,
        ds: ds,
        reborn: reborn,
      }
      minions.push(minion);
    }
    var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://127.0.0.1:5000/process_data", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                
                const responseData = JSON.parse(xhr.responseText);
                const solution = responseData.solution;
                scenes = responseData.scenes;
                console.log(responseData.scenes);
                result.textContent=solution;
            }
        };
        xhr.send(JSON.stringify(minions));
  }

  function ForwardScene(){
    if (CurrentIndex<scenes.length-1){
      CurrentIndex++;
      updateBoardWithScene(scenes[CurrentIndex])
    }
  }

  function PreviousScene(){
    if (CurrentIndex>0){
      CurrentIndex--;
      updateBoardWithScene(scenes[CurrentIndex])
    }
  }


  function updateBoardWithScenes(scenes, delay,sceneIndex=0) {
    function displayScene() {
      if (sceneIndex < scenes.length) {
        const scene = scenes[sceneIndex];
        updateBoardWithScene(scene);
        sceneIndex++;
  
        // Call the next scene update after the delay
        setTimeout(displayScene, delay,sceneIndex);
      }
    }
    setTimeout(displayScene, delay);
  }

  function updateBoardWithScene(scene) {
    const elementE1 = document.querySelector('#E1 .Minion');
    const elementF1 = document.querySelector('#F1 .Minion');
    positionLineImage(elementE1, elementF1);

    // Iterate through the minions in the scene
    for (const minion of scene) {
      // Get the minion element by its ID
      const minionElement = document.getElementById(minion.name);

      // Update the attack and health input values
      const attackInput = minionElement.querySelector('.attack');
      const healthInput = minionElement.querySelector('.health');
      attackInput.value = minion.attack;
      healthInput.value = minion.health;

      // Update the taunt, ds, and reborn checkboxes
      const tauntCheckbox = minionElement.querySelector('#checkbox-taunt');
      const dsCheckbox = minionElement.querySelector('#checkbox-ds');
      const rebornCheckbox = minionElement.querySelector('#checkbox-reborn');
      tauntCheckbox.checked = minion.taunt;
      dsCheckbox.checked = minion.ds;
      rebornCheckbox.checked = minion.reborn;
    }
  }



  function positionLineImage(friendly, enemy) {
    const lineImage = document.getElementById('Arrow');
    const rect1 = friendly.getBoundingClientRect();
    const rect2 = enemy.getBoundingClientRect();
  
    const x1 = rect1.left + rect1.width / 2;
    const y1 = rect1.top + rect1.height / 2;
  
    const x2 = rect2.left + rect2.width / 2;
    const y2 = rect2.top + rect2.height / 2;
  
    const distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
  
    lineImage.style.width = distance + 'px';
    lineImage.style.transform = `rotate(${angle}deg)`;
    lineImage.style.top = y1 + 'px';
    lineImage.style.left = x1 + 'px';
    console.log(lineImage);
    lineImage.style.display="inline";
  }

