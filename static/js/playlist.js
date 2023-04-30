var mySwiper = new Swiper('.swiper-container', {
    slidesPerView: 5,
    slidesPerGroup: 2,
    spaceBetween: 0,
    loop : true,
    autoplayDisableOnInteraction: false,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
});

//
//
// $(function(){$('.mainSlide').slick();})
//     $(function (){
//     $('.multipleSlide').slick({
//     infinite: true,
//     slidesToShow: 5,
//     slidesToScroll: 3
//     });
// })