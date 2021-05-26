function navigation(event) {
  var reg = document.getElementById('registration');
  var login = document.getElementById('login');

  var reg_box = document.getElementsByClassName('box')[0];
  var login_box = document.getElementsByClassName('loginBox')[0];

  var x = event.target;

  if(x.id == 'registration' || x.id == 'regLink'){
    reg.classList.add('myactive');
    login.classList.remove('myactive');

    reg_box.style.display='block';
    login_box.style.display='none';
  }
  if(x.id == 'login' || x.id == 'loginLink'){
    reg.classList.remove('myactive');
    login.classList.add('myactive');

    reg_box.style.display='none';
    login_box.style.display='block';
  }
}
