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
                    //<p>Kabir: "+response+"</p>
                    var a = $("<div id='kabir'></div>").appendTo("#textbox");
                    //var b = a.append("<div class='animate' id="first-bot"></div><div class='animate' id="second-bot"></div><div class='animate' id="third-bot"></div>");
                    //$('#AI-response #animate').hide();
                    let b = "<div class='animate' id='one'></div><div class='animate' id='two' ></div><div class='animate' id='three'></div>"
                    a.append(b);




                    setTimeout(function(){
                    a.append("<p>Kabir: "+response+"</p>");
                    $('.animate').remove();
                      }, ((Math.random()*3000)+1000));

                    //$('#AI-response #animate').hide();
                    $("#question").val("")
                    $('#textbox').scrollTop($('#textbox')[0].scrollHeight);

                },
                error: function(result) {
                    alert('error');
                }
            });
        });
    });




