$(document).ready(function(){
  $("input[type='button']".click(function(){
    var userVal = $("input[name='remember']:checked").val();
})

function submit_clicked(event){
  event.preventDefault();
  var content = $('{{ user_info }}').val();
  $.post(
    '/confirmation.*',
    content,
    handle_response
  );
}

function associate_events(){
  $('#submit').click(submit_clicked);
}

$(document).ready(associate_events); //only run when func is loaded
