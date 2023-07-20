$(".blog-pictures").slick({
  infinite: true,
  speed: 500,
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay:true,
  arrows:false,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 2,
        centerMode:true,
      
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,

      }
    }
  
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
  });
 
$("#aa").click(function(){
  $(".dro-cat").stop().slideToggle(1000)
  $(".dro-pos").slideUp(800)
})
$(".bb").click(function(){
  $(".dro-pos").stop().slideToggle(1200)
  $(".dro-cat").slideUp(700)
})


var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("wrapper").style.top = "0";
  } else {
    document.getElementById("wrapper").style.top = "-100px";
  }
  prevScrollpos = currentScrollPos;
}
$(".hello-msg").click(function(){
  $(".login-drop").stop().slideToggle(1000);
})