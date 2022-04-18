const width = window.screen.width;
const swiper1 = new Swiper(".swiper.swiper1", {
  slidesPerView: 1,
  spaceBetween: 10,
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination1",
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next1",
    prevEl: ".swiper-button-prev1",
  },
});
const swiper2 = new Swiper(".swiper.swiper2", {
  slidesPerView: width <= 995 ? 1 : 2 && width <= 1258 ? 2 : 3,
  spaceBetween: 30,
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination2",
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next2",
    prevEl: ".swiper-button-prev2",
  },
});

const swiper3 = new Swiper(".swiper.swiper3", {
  slidesPerView: width <= 995 ? 1 : 2 && width <= 1258 ? 2 : 3,
  spaceBetween: 30,
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination3",
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next3",
    prevEl: ".swiper-button-prev3",
  },
});

const swiper4 = new Swiper(".swiper.swiper4", {
  slidesPerView: width <= 995 ? 1 : 2 && width <= 1258 ? 2 : 3,
  spaceBetween: 30,
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination4",
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next4",
    prevEl: ".swiper-button-prev4",
  },
});

const swiper5 = new Swiper(".swiper.swiper5", {
  slidesPerView: width <= 995 ? 1 : 2 && width <= 1440 ? 2 : 3,
  spaceBetween: 30,
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination5",
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next5",
    prevEl: ".swiper-button-prev5",
  },
});

const swiper6 = new Swiper(".swiper.swiper6", {
  slidesPerView: width <= 995 ? 1 : 2 && width <= 1440 ? 2 : 3,
  spaceBetween: 30,
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination6",
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next6",
    prevEl: ".swiper-button-prev6",
  },
});

document.addEventListener("DOMContentLoaded", function () {
  // code
console.log('DOMContentLoaded');
  let btn = document.querySelector("#btn-load-more");
  let hides = document.querySelectorAll("#hidden");
  let closeBtn = document.querySelector("#btn-close");
  btn.addEventListener("click", (e) => {
    for (let i = 0; i < hides.length; i++) hides[i].style.display = "block";
    btn.style.display = "none";
    closeBtn.style.display = "block";
    if (width <= 1441) {
      let mediaCard = document.querySelectorAll(".media-card");
      for (let i = 0; i < mediaCard.length; i++) {
        mediaCard[i].style.display = "none";
      }
    }
  });
  closeBtn.addEventListener("click", (e) => {
    for (let i = 0; i < hides.length; i++) hides[i].style.display = "none";
    btn.style.display = "block";
    closeBtn.style.display = "none";
  });
  if (width <= 1441) {
    let mediaCard = document.querySelectorAll(".media-card");
    for (let i = 0; i < mediaCard.length; i++) {
      mediaCard[i].style.display = "none";
    }
  }

  let burger_menu = document.getElementById("burger-menu");

  burger_menu.addEventListener("click", (e) => {
    console.log("burger-menu");
  });

  let result_btn = document.getElementById("result-btn");
  let resultx_btn = document.getElementById("resultx-btn");
  let result__modal = document.getElementById("result__modal");
  let result__modal_content = document.querySelector(".result__modal-content");

  result__modal_content.addEventListener("click", (e) => {
    e.stopPropagation();
  });

  result_btn.addEventListener("click", (e) => {
    console.log("result-btn");
    result__modal.classList.toggle("active");
  });
  resultx_btn.addEventListener("click", (e) => {
    console.log("resultx-btn");
    result__modal.classList.toggle("active");
  });

  result__modal.addEventListener("click", (e) => {
    console.log("result__modal");
    result__modal.classList.toggle("active");
  });
});
