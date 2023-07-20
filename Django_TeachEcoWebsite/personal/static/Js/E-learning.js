

$(".slider-books").slick({
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay:true,
    arrows:false,
    speed: 1000,
    autoplaySpeed: 4000,
    responsive: [
        {
          breakpoint: 1008,
          settings: {
            arrows: false,
            slidesToShow: 3
          }
        },
        {
          breakpoint: 770,
          settings: {
            arrows: false,
            slidesToShow: 2
          }
        },
        {
            breakpoint: 475,
            settings: {
              arrows: false,
              slidesToShow: 2,
      

            }
          }
      ]
});


