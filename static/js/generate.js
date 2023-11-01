// Display username
$(document).ready(function(){
    $.ajax({
        url: '/auth/get_username',
        type: 'GET',
        success: function(response) {
            let username = response.username;
            $('#usernameButton').append(`Hi ${username} 👋`);
        },
        error: function(error) {
            console.log("Error fetching username:", error);
        }
    });
});

// FORMAT RESPONSE
function formatContent(content) {
    let paragraphs = content.split('\n\n');
    let formattedContent = $('<div></div>');  // Create a container div

    paragraphs.forEach((paragraph) => {
        let newElement;
        if (paragraph.startsWith('Introduction:')) {
            newElement = $('<h1></h1>').text(paragraph).css({
                "color": "#333",
                "font-size": "24px",
                "margin-bottom": "10px"
            });
        } else if (paragraph.startsWith('Main Body:')) {
            newElement = $('<h2></h2>').text(paragraph).css({
                "color": "#444",
                "font-size": "22px",
                "margin-bottom": "10px"
            });
        } else if (paragraph.startsWith('Conclusion:')) {
            newElement = $('<h3></h3>').text(paragraph).css({
                "color": "#555",
                "font-size": "20px",
                "margin-bottom": "10px"
            });
        } else {
            newElement = $('<p></p>').text(paragraph).css({
                "color": "#666",
                "font-size": "18px",
                "margin-bottom": "10px"
            });
        }
        formattedContent.append(newElement);
    });

    return formattedContent;
}


// SUBMIT, RETRIEVE AND DISPLAY RESPONSE
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
            let content = formatContent(response.generated_article); // Use the new function here
            let i = 0;
            $(".article-display p").html(""); // Clear existing text
            let interval = setInterval(function(){
                $(".article-display p").append(content[i]);
                i++;
                if(i >= content.length){
                    clearInterval(interval);
                }
            }, 15); // Change this number to speed up or slow down the effect
        },
        error: function(error){
          console.log("Error: ", error);
          $(".article-display p").text("Failed to generate an article.");
          $("#load").hide(); // Hide new loading animation
        }
      });
    });
  });


//   Page animations
const element = document.querySelector('.aritcle-length');
const choices = new Choices(element, {
    animationDuration: 200, // length of the animation in ms
    shouldSort: false,
    classNames: {
        containerOuter: 'choices',
        containerInner: 'choices__inner my-choices-container-inner',
        item: 'choices__item my-choices-item',
        choice: 'choices__choice my-choices-choice',
    }
});


// Save article data from <p> to PostgreSQL database
$('.fa-bookmark').on('click', function () {
    let articleContent = $('#article-data').text();
    let articleData = JSON.stringify({
        content: articleContent
    });

    $.ajax({
        url: '/save_article',
        type: 'POST',
        contentType: 'application/json',
        data: articleData,
    }).done(function (data) {
        alert('Succesfuly Saved Article');
    }).fail(function (err) {
        console.error(err);
        $('#error_messages').text('Failed to save article, kindly try again');
    });
});


// Edit content
$(document).ready(function(){
    $('.fa-pen-to-square').on('click', function () {
        $('.article-display').attr('contenteditable', 'true').focus();
        alert('Ready to edit');
    });
});
