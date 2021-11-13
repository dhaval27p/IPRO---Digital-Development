 jQuery(document).ready(function() {
        $("#submit-button").click(function(e) {
            e.preventDefault();

            $.ajax({
                type: "POST",
                url: "/chat",
                data: {
                    question: $("#question").val()
                },

                success: function(result) {



                    response = result.response;

                    $("<div id='response'><p style='text-align: center';>Me: "+$("#question").val() +"</p></div>").appendTo("#textbox");
                    $("<div style='visibility: hidden'; id='kabir'>Me: "+$("#question").val() +"</p></div><br>").appendTo("#textbox");

                    var a = $("<div id='kabir'></div>").appendTo("#textbox");

                    let b = "<div class='animate' id='one'></div><div class='animate' id='two' ></div><div class='animate' id='three'></div>"
                    a.append(b);




                    setTimeout(function(){
                    a.append("<p>Kabir: "+response+"</p>");
                    $('.animate').remove();
                      }, ((Math.random()*4000)));

                    //$('#AI-response #animate').hide();
                    $("#question").val("")
                    $('#textbox').scrollTop($('#textbox')[0].scrollHeight);

                },
                error: function(result) {
                    alert('error');
                }
            });
        });
        $("#search").click(function(e) {
            e.preventDefault();

            $.ajax({
                type: "POST",
                url: "/deleteuser",
                data: {
                    user: $('#users').val()

                },

                success: function(result) {
                        firstname = result.firstname;
                        lastname = result.lastname;
                        time = result.time;
                        user = result.user;





                        if ($('#after-submit').length){


                            $('#after-submit').empty();
                            $('#deletebutton').remove();
                            if (user === "This username doesn't exist"){
                                    $("<div id = 'after-div'>"+user+"</div>").appendTo('#after-submit');}
                            else{
                                    $("<div id = 'after-div'>First name: <label class='admin-font'>"+firstname+"</label><br>Last name: <label class='admin-font'>"+lastname+"</label><br>Created: <label class='admin-font'>"+time+"</label></div>").appendTo('#after-submit');

                                    $("<button id ='deletebutton' type='submit' name='submit-buttons' value='delete'>DELETE</button>").appendTo("form");
                                    }
                        }
                        else{
                            if (user === "This username doesn't exist"){
                                $("<div id = 'after-div'>"+user+"</div>").appendTo('#after-submit');}
                            else{
                                $("<div id = 'after-div'>First name: <label class='admin-font'>"+firstname+"</label><br>Last name: <label class='admin-font'>"+lastname+"</label><br>Created: <label class='admin-font'>"+time+"</label></div>").appendTo('#after-submit');

                                $("<button id ='deletebutton' type='submit' name='submit-buttons' value='delete'>DELETE</button>").appendTo("form");
                             }
                        }


                },
                error: function(result) {
                    alert('error');
                }


            });
        });
        $('#deletebutton').click(function(e){
            e.preventDefault();

            $.ajax({
                type: "POST",
                url: "/deleteuser",
                data: {
                    users: $('#users').val()
                },
                success: function(result) {

                    //mit= result.users;
                    //$('#after-div').remove();
                    $('#delete-button').remove();
                    $("<div id = 'after-div'>Hello</div>").appendTo('#after-submit');

                },
                error: function(result) {
                    alert('error');
                }


            });





        });
    });




