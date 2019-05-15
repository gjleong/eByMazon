var div = document.getElementById('taboo');

function replaceWords(event) {
    //Prevent form submission to server 
    event.preventDefault();
    var commentContent = document.getElementById('comments');
    console.log(commentContent.value);
    var badWords = ["crap", "ugly", "brat" ,"basterddouch"];
    console.log(commentContent.value);
    var censored = censore(commentContent.value, badWords);
    commentContent.value = censored;
}

function censore(string, filters) {
    // "i" is to ignore case and "g" for global
    var regex = new RegExp(filters.join("|"), "gi");
    console.log(regex);
    return string.replace(regex, function (match) {
        //replace each letter with a star
        var stars = '';
        for (var i = 0; i < match.length; i++) {
            stars += '*';
        }
        return stars;
    });

}
div.addEventListener('click',replaceWords);