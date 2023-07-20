$(".vertical").slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay:true,
    speed: 2000,
    arrows:false,
    responsive: [
        {
          breakpoint: 768,
          settings: {
            arrows: false,
            centerMode: false,
            slidesToShow: 2
          }
        },
        {
          breakpoint: 500,
          settings: {
            slidesToShow: 2
          }
        }
      ]
});
$(".horizontal").slick({
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplay:true,
    arrows:false,
    swipe: false,
    vertical: true,
    speed: 2000,
    responsive: [
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2
          }
        },
        {
          breakpoint: 500,
          settings: {
            arrows: false,
            slidesToShow: 1
          }
        }
      ]
})