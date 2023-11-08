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
        let $articleContent = $('#article-data p');

        // Toggle the contentEditable state and button text
        if ($articleContent.attr('contentEditable') === 'true') {
            $articleContent.attr('contentEditable', 'false');
            $(this).text('Edit'); // Change button text to 'Edit'
            alert('Editing is now disabled.'); // Alert the user
        } else {
            $articleContent.attr('contentEditable', 'true');
            $(this).text('Done Editing'); // Change button text to 'Done Editing'
            alert('You can now edit this article!'); // Alert the user
        }
    });
});

// Copy content
$(document).ready(function() {
    $('#copy_article').on('click', function () {
        // Select the content of the paragraph containing the article
        var $articleContent = $('#article-data p');

        // Check if there's any content to copy
        if($articleContent.text().trim().length === 0){
            alert('There is no content to copy.');
            return;
        }

        // Create a range and selection to select the text
        var range = document.createRange();
        var selection = window.getSelection();
        
        // Clear any current selections
        selection.removeAllRanges();

        // Select the paragraph content
        range.selectNodeContents($articleContent.get(0));
        selection.addRange(range);

        // Try to execute the copy command
        try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'successful' : 'unsuccessful';
            console.log('Copy command was ' + msg);
            alert('Copying text command was ' + msg);
        } catch (err) {
            console.log('Oops, unable to copy', err);
            alert('Oops, unable to copy. ' + err);
        }

        // Clear the selection
        selection.removeAllRanges();
    });
});


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

    // Event handler for export buttons
    $('.format_dropdown button').on('click', function () {
        let exportFormat = $(this).attr('id');
        let topic = $('#article-data').next().text().split('\n')[0].trim();
        let content = $('#article-data').siblings('p').text().trim();
    
        // Create a form and submit it to trigger the download
        $('<form>', {
            'action': '/export',
            'method': 'post'
        })
        .append($('<input>', {
            'name': 'topic',
            'value': topic,
            'type': 'hidden'
        }))
        .append($('<input>', {
            'name': 'content',
            'value': content,
            'type': 'hidden'
        }))
        .append($('<input>', {
            'name': 'exportFormat',
            'value': exportFormat,
            'type': 'hidden'
        }))
        .appendTo(document.body)
        .submit();
    });
});
