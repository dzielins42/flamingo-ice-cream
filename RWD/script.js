$(function() {
   
    /* var button =  $('.btn');
    console.log(button);
    var card = $('.card');
    console.log(card);
    
    
    card.on('click', function(){
        event.preventDefault(); // jeżeli funkcja zakłada przeładowanie strony
        var newDiv= $("<div>");
        card.after(newDiv);
        console.log("nanana")
    });

     $.ajax({
        url: 'https://swapi.co/api/films/',
        dataType: 'json'
        }).done(function(response){
          console.log(response);
        }).fail(function(error){
            console.log(error)
        }); 
*/

     $.ajax({
        url: 'https://swapi.co/api/films/',
        dataType: 'json'
        }).done(function(response){
          console.log(response);
        }).fail(function(error){
            console.log(error)
        }); 


    var card = $('.card');
    var movieUrl = 'https://swapi.co/api/films/';
    
    var cardTitle = $( '.card-title' );

    function insertContent( movies ) {
        console.log(movies);
        //tutaj zrób pętlę po filmach
        movies.forEach(function(el){
            console.log(el.title);
            //wygeneruj kolejne LI i wstaw do listy movieList
            cardTitle.append($('<div class="card-body"></div>').text(el.title));
        });


    }

    function loadMovies() {
        /*tutaj wykonaj połączenie Ajaxem
        $.ajax(movieUrl)
            .done(function(response){
                console.log(response.results[0].planets[0]); //element z r o indx 2 - po kluczach z objektu z debuggera
                insertContent(response.results); //pod zmienna movies daje response res.
                //moge wtedy szukać w tym co mi zwróci kopiuje ajax i odwoluje sie do response.results[0].planets[0] no i szukam
            })
            .fail(function(error){
                console.log(error);
            }); */
    }

    loadMovies();
    


});


