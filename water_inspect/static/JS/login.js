

  $(document).ready(function(){
      $("#left_body_2").hide();
      $("#right_body_2").hide();
      
    $("#sign_up").click(function(){
        $("#left").toggleClass("col-md-8");
        $("#left").toggleClass("col-md-4");
        $("#right").toggleClass("col-md-4 ");
        $("#right").toggleClass("col-md-8");

        $("#left").toggleClass("bg2");
        $("#left").toggleClass("bg1");
        $("#right").toggleClass("bg1");
        $("#right").toggleClass("bg2");

        $("#left_body_2").toggle(2000);
        $("#right_body_2").toggle(2000);
        $("#whole_left").toggle(2000);
        $("#whole_right").toggle(2000);
      });

      $("#sign_in").click(function(){
        $("#left").toggleClass("col-md-8");
        $("#left").toggleClass("col-md-4");
        $("#right").toggleClass("col-md-4 ");
        $("#right").toggleClass("col-md-8");

        $("#left").toggleClass("bg2");
        $("#left").toggleClass("bg1");
        $("#right").toggleClass("bg1");
        $("#right").toggleClass("bg2");

        $("#left_body_2").toggle(2000);
        $("#right_body_2").toggle(2000);
        $("#whole_left").toggle(2000);
        $("#whole_right").toggle(2000);
      });
  });