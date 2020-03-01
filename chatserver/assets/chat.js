$(document).ready(function(){
  var socket = io.connect();

  socket.on('join', (msg) => {
    $('#user-list').empty();
    for (let k in msg){
      $('#user-list').append(`<li class="list-group-item">${msg[k]}</li>`)
    }
    // console.log(msg);
  });

  $('#submit').click((e) => {
    socket.emit('join', {name: $('#input').val()});
  });

});