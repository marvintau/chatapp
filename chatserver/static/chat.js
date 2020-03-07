const err_msg = {
  EXPIRED: '服务器没有您的记录，您重新登录吧',
  EXISTING_NAME: '服务器这边重名了，您改个名字吧'
};

const isLogged = () => {
  let nickname = localStorage.nickname;
  return nickname !== undefined && nickname !== null;
}

const localLogin = (nickname) => {
  localStorage.setItem('nickname', nickname);
  $('#submit').text('说')
}

const localLogout = () => {
  localStorage.removeItem('nickname');
  $('#submit').text('加入')
}

$(document).ready(function(){
  var socket = io(`${window.location.host}`)
  .on('connect', () => {
    console.log(socket.id, 'connected');
  })
  .on('connect_error', () => {
    console.error('连接错误，没有连到服务器');
  })
  .on('welcome', ({users}) => {
    console.log('other people logged in')
    $('#user-list').empty();
    for (let k of users){
      $('#user-list').append(`<li class="list-group-item">${k}</li>`)
    }
  })
  .on('logged', ({error, users, name:nickname}) => {
    console.log('logged in')
    if (error !== undefined){

      // 发生任何登陆问题时，先在本地登出
      localLogout();
      alert(err_msg[error]);
    } else {

      $('#user-list').empty();
      for (let k of users){
        $('#user-list').append(`<li class="list-group-item">${k}</li>`)
      }  

      // 收到欢迎信息后才在本地登入。当然如果是relogin的话
      // 意味着localStorage会再写一次nickname，但是没有关系。
      localLogin(nickname);
    }
  })
  .on('heard', ({name, message}) => {
    console.log('message received')
    $('#content').append(`<div class="message"><span class="name">${name}: </span><span class="content">${message}</span></div>`)
  })
  // .on('');

  const login = (nickname) => {

    if (nickname.length === 0){
      alert('抱歉，您的昵称不能为空啊')
    } else {
      socket.emit('join', {name: nickname});
    }
  }

  const say = (word) => {
    if (word.length === 0){
      alert('抱歉，发言也不能为空啊')
    } else {
      socket.emit('say', {name: localStorage.nickname, message: word});
    }
  }

  const submit = (e) => {
    if (isLogged()){
      say($('#input').val());
    } else {
      login($('#input').val());
    }
    $('#input').val('');
  }

  $('#submit').click(submit);

  // console.log(localStorage.nickname)
  if (isLogged()){
    console.log('islogged')
    socket.emit('rejoin', {name: localStorage.nickname})
  }
  
  console.log('loaded')
});