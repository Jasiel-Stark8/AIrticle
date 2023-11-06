// Save article data from <p> to PostgreSQL database
$(document).ready(function() {
    $('#save_article').on('click', function (event) {
        event.preventDefault(); // Prevent default form submission
        alert('Save button clicked'); // Debugging alert

        let topic = $('#article-data').text().split('.')[0];
        let articleContent = $('#article-data').text();
        let articleData = JSON.stringify({
            topic: topic,
            content: articleContent
        });

        $.ajax({
            url: '/save_article',
            type: 'POST',
            contentType: 'application/json',
            data: articleData,
            dataType: 'json'
        }).done(function (data) {
            let successMessage = $('<div class="alert alert-success" role="alert">')
                                    .text('Article Successfully Saved!');
            $('#flash_container').empty().append(successMessage);
        }).fail(function (err) {
            let errorMsg = (err.responseJSON && err.responseJSON.message) ? err.responseJSON.message : 'Failed to save article, kindly try again';
            let errorMessage = $('<div class="alert alert-danger" role="alert">')
                                    .text(errorMsg);
            $('#flash_container').empty().append(errorMessage);
            console.error(errorMsg);
        });
    });
});

// Edit content
$(document).ready(function() {
    $('#edit_article').on('click', function () {
        $('#article-data').attr('contentEditable', true);
        let successMessage = $('<div class="alert alert-success" role="alert">')
                                    .text('You can now edit this article!');
            $('#flash_container').empty().append(successMessage);
    });
});
