$("#search_word").keyup(function () {
  var word = $(this).val();

  $.ajax({
    url: '/ajax/word_search/',
    data: {
      'word': word
    },
    dataType: 'json',
    success: function(data) {
      var word_dict = data.word[0];
      if (jQuery.isEmptyObject(word_dict)){
        $(".content").html("");
      }
      $("#word-meaning").html(word_dict['word'] + ' : ' + word_dict['meaning']);
      $("#sentence").html(word_dict['sentence']);
      $("#refrence").html(word_dict['refrence']);
    }
  });
});
