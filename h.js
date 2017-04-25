$(function() {
    $('.cat').click(function() {
        console.log('click')
        $('.categ').remove()
            // $('.dropdown-menu').remove();-->
        $.ajax({
            url: '/categorylist',
            data: {

            },
            dataType: 'json',
            success: function(data) {
                $.each(data, function(key, value) {
                    var link = $("<li><a class='categ' href=/categorydetails/" + data[key].pk + '>' + data[key].fields['name'] + '</a> </li>')
                    $('.dropdown-menu').append(link)
                })
            }
        })
    })
})

$('#search').on('input', function(e) {
    console.log($('#search').val())
    if ($('#search').val()) {
        $.ajax({
            url: '/search/' + $('#search').val(),
            data: {

            },
            dataType: 'json',
            success: function(data) {
                jsonbook = $.parseJSON(data)
                console.log(jsonbook)

                if (!$.isEmptyObject(jsonbook)) {
                    $.each(jsonbook, function(key, value) {
                        console.log(jsonbook[key].fields['title'])

                        var link = $("<li><a class='categ' href=/categorydetails/" + data[key].pk + '>' + jsonbook[key].fields['title'] + '</a> </li>')
                        $('.dropdown-menu').append(link)
                    })
                }
            }
        })
    }
})