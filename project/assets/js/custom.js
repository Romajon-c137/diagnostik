(function ($) {

  "use strict";

  // PRE LOADER
  $(window).load(function () {
    $('.preloader').fadeOut(1000); // set duration in brackets    
  });


  //Navigation Section
  $('.navbar-collapse a').on('click', function () {
    $(".navbar-collapse").collapse('hide');
  });


  // Owl Carousel
  const width = window.screen.width;
  console.log('width', width);
  $('.owl-two').owlCarousel({
    animateOut: 'fadeOut',
    items: width <= 836 ? 1 : 2 && width <= 1258 ? 2 : 3,
    loop: true,
    autoplay: true,
    pagination: true
  })
  $('.owl-one').owlCarousel({
    animateOut: 'fadeOut',
    items: 1,
    loop: true,
    autoplay: true,

  })


  // PARALLAX EFFECT
  $.stellar();


  // SMOOTHSCROLL
  $(function () {
    $('.navbar-default a, #home a, footer a').on('click', function (event) {
      var $anchor = $(this);
      $('html, body').stop().animate({
        scrollTop: $($anchor.attr('href')).offset().top - 49
      }, 1000);
      event.preventDefault();
    });
  });


  // WOW ANIMATION
  new WOW({
    mobile: false
  }).init();

})(jQuery);



let btn = document.querySelector('#btn-load-more');
let hides = document.querySelectorAll('#hidden');
let closeBtn = document.querySelector('#btn-close')
btn.addEventListener('click', (e) => {
  for (let i = 0; i < hides.length; i++) 
  hides[i].style.display = 'block';

  btn.style.display = 'none';
  closeBtn.style.display = 'block';
})
closeBtn.addEventListener('click', (e) => {
  for (let i = 0; i < hides.length; i++) 
  hides[i].style.display = 'none';
 
  btn.style.display = 'block';
  closeBtn.style.display = 'none';
})


