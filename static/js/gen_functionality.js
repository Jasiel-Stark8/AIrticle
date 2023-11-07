// Save article data from <p> to PostgreSQL database
$(document).ready(function() {
    $('#save_article').on('click', function (event) {
        event.preventDefault(); // Prevent default form submission

        let topic = $('#article-data').next().text().split('\n')[0].trim();
        console.log(topic);
        let content = $('#article-data').siblings('p').text().trim(); // the p tag is a sibling not a child
        console.log(content);
        let articleData = JSON.stringify({
            topic: topic,
            content: content
        });

        $.ajax({
            url: '/save_article',
            type: 'POST', // Using POST as the method
            contentType: 'application/json',
            data: articleData,
            dataType: 'json',
            success: function (data) {
                let successMessage = $('<div class="alert alert-success" role="alert">')
                                        .text('Article Successfully Saved!');
                $('#flash_container').empty().append(successMessage);
            },
            error: function (xhr, status, error) {
                let errorMsg = xhr.responseJSON && xhr.responseJSON.message ? xhr.responseJSON.message : 'Failed to save article, please try again';
                let errorMessage = $('<div class="alert alert-danger" role="alert">')
                                        .text(errorMsg);
                $('#flash_container').empty().append(errorMessage);
                console.error(errorMsg);
            }
        });
    });
});

// Edit content
$(document).ready(function() {
    $('#edit_article').on('click', function () {
        $('#article-data p').attr('contentEditable', true);
        let successMessage = $('<div class="alert alert-success" role="alert">')
                                    .text('You can now edit this article!');
            $('#flash_container').empty().append(successMessage);
    });
});

// Copy content


// Export content
$(document).ready(function () {
    $('#export_article').on('click', function (event) {
        event.stopPropagation(); // Prevent click event from propagating to document
        $('.format_dropdown').toggle('fast'); // Use toggle to show/hide the dropdown
    });

    // Close the dropdown menu if clicked outside
    $(document).on('click', function () {
        $('.format_dropdown').hide('fast');
    });

    // Prevent clicks within the dropdown from closing it
    $('.format_dropdown').on('click', function (event) {
        event.stopPropagation(); // Prevent click event from propagating to document
    });

    // Main functionality bla bla bla
    let content = $('#article-data').siblings('p').text().trim();
    let exportFormat = '';
});



// THEME
function toggleTheme() {
    if (document.documentElement.getAttribute("data-theme") === "dark") {
      document.documentElement.setAttribute("data-theme", "light");
    } else {
      document.documentElement.setAttribute("data-theme", "dark");
    }
  }