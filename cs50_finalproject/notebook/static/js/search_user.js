$("#search_user").keyup(function () {
  var username = $(this).val();

  $.ajax({
    url: '/ajax/search_user/',
    data: {
      'username': username
    },
    dataType: 'json',
    success: function(data) {
      var user_dict = data.user[0];
      if (jQuery.isEmptyObject(user_dict)){
        $(".content").html("");
        $("#image").attr("src", "");
        $("a#url").attr("href", "#");
      }
      $("#username").html(user_dict['username']);
      $("#image").attr("src", data.image);
      $("a#url").attr("href", "http://localhost:8000/userwordslist/?username="+user_dict['username']);
    }
  });
});
