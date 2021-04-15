function submitForm () {
    var nameInput = document.getElementById('nameInput').value;
    var passInput = document.getElementById('passInput').value;
    var alertMessage = document.getElementById('alertMsg');
    
    if (nameInput.length >= 3 && passInput.length >= 8) {
      alertMessage.style.visibility = 'visible';
      alertMessage.style.backgroundColor = '#27ae60';
      alertMessage.innerHTML = 'Hello, ' + nameInput;
    } else if (nameInput == '' && passInput == '') {
      alertMessage.style.visibility = 'visible';
      alertMessage.style.backgroundColor = '#e74c3c';
      alertMessage.innerHTML = 'Username and Password are required.';
    } else if (nameInput.length < 3 && passInput.length < 8) {
      alertMessage.style.visibility = 'visible';
      alertMessage.style.backgroundColor = '#e74c3c';
      alertMessage.innerHTML = 'Username and Password are too short.';
    } else if (nameInput == '') {
      alertMessage.style.visibility = 'visible';
      alertMessage.style.backgroundColor = '#e74c3c';
      alertMessage.innerHTML = 'Username is required.';         
    } else if (passInput == '') {
      alertMessage.style.visibility = 'visible';
      alertMessage.style.backgroundColor = '#e74c3c';
      alertMessage.innerHTML = 'Password is required.';         
    } else if (nameInput.length < 3) {
      alertMessage.style.visibility = 'visible';
      alertMessage.style.backgroundColor = '#e74c3c';
      alertMessage.innerHTML = 'Username is too short, 3 characters minimum.';
    } else if (passInput.length < 8) {
      alertMessage.style.visibility = 'visible';
      alertMessage.style.backgroundColor = '#e74c3c';
      alertMessage.innerHTML = 'Password is too short, 8 characters minimum.';
    } 
  }