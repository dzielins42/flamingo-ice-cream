$(function() {

var mainDiv = $('#main');
console.log(mainDiv);
var categoriesUrl = 'http://192.168.0.115:8000'

    $.ajax({
        method: "GET",
        url: categoriesUrl +"/categories/",    /*/1,2,3,4,5 - wyświetli konkretny id*/
        dataType: "json"
    }).done(function(response) {
        console.log(response);
    });


    function insertContent(categories) {
        console.log(categories);
       
      var cardA = $('<div class="card" style="width: 18rem"></div>')
        .append($('<img class="card-img-top" src="https://place-hold.it/300" alt="Card image cap"></img>'))
        .append($('<div class="card-body"></div>')
            .append($('<h5 class="card-title">Card title</h5>').text(categories.title))
            .append($('<p class="card-text">Some quick example text to build on the card title and make up the bulk of the cards content.</p>').text(categories.description))
        )
        mainDiv.append(cardA);
       
        cardA.on('click', function(){
            console.log("nanana")
            mainDiv.children().remove();
             
            $.ajax(categoriesUrl + "/categories?parent=" + categories.id)
            .done(function(response){
                response.forEach(element => {
                    insertContent(element)
                });
            })
            .fail(function(error){
                console.log(error);
            });
        });

        
    }

   


    function loadCategories(id) {
        //tutaj wykonaj połączenie Ajaxem
        $.ajax(categoriesUrl + "/categories?parent__isnull=true")
            .done(function(response){
                response.forEach(element => {
                    insertContent(element)
                });
            })
            .fail(function(error){
                console.log(error);
            });
    }

loadCategories();
});    
