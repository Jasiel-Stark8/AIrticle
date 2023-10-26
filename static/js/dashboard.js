// $(document).ready(function () {
//     // Header profile dropdown functionality
//     let ('.dropdown').css('dropdown-content', 'hidden');
//     $('.dropdown').on('click', function (e) {
//         (this).css('dropdown-content', 'block');
//     });
// });


$(document).ready(function(){
    $("#generate-article-form").submit(function(event){
      event.preventDefault();
      $("#load").show(); // Show new loading animation
      let formData = {
        topic: $("input[name='topic']").val(),
        keywords: $("input[name='keywords']").val(),
        article_length: $("select[name='article_length']").val()
      };
  
      $.ajax({
        type: "POST",
        url: "/generate",
        data: formData,
        success: function(response){
          $("#load").hide(); // Hide new loading animation
          let content = response.generated_article;
          let i = 0;
          $(".article-display p").text("");
          let interval = setInterval(function(){
            $(".article-display p").append(content[i]);
            i++;
            if(i >= content.length){
              clearInterval(interval);
            }
          }, 15); // Higher the slower the animation
        },
        error: function(error){
          console.log("Error: ", error);
          $(".article-display p").text("Failed to generate an article.");
          $("#load").hide(); // Hide new loading animation
        }
      });
    });
  });
  
  
