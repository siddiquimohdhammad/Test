// for toggle button in mobile view
let toggle = ()=>{
    let menu = document.getElementById('mob-menu');
    if(menu.style.display === 'flex'){
        menu.style.display = 'none';
    }else{
        menu.style.display = 'flex';
        menu.style.flexDirection = 'column';
    }
}

// for carousel-card
let slideIndex = 0;

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("carousel-card");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "flex";
  setTimeout(showSlides, 4000); // Change image every 2 seconds
}

showSlides();