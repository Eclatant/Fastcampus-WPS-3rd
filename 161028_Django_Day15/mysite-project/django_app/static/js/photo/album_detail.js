function photoLike(photoPk, likeType) {
    var url = '/photo/ajax/photo/' + photoPk + '/' + likeType + '/';
    console.log(url);
    $.ajax({
        method: 'POST',
        url: url,
    })
        .done(function(response) {
            console.log(response);
        })
        .fail(function(response) {
            console.log(response);
        });
}