const carouselSlide = document.querySelector('.slide_list');
const carouselContents = document.querySelectorAll('.slide_item');

const prevBtn = document.querySelector('.prevBtn');
const nextBtn = document.querySelector('.nextBtn');
console.log(carouselContents);

let counter = 1;
const size = carouselContents[0].clientWidth; //100
console.log(size);
//transform:translate(-200px)
carouselSlide.style.transform="translateX("+-size*counter+"px)";


nextBtn.addEventListener('click',()=>{
    if(counter >= carouselContents.length-1) return;
    carouselSlide.style.transition="transform 0.3s ease-in-out";
    counter++;
    carouselSlide.style.transform="translateX("+ -size*counter+"px)";
});

prevBtn.addEventListener('click',()=>{
    if(counter<=0) return;
    carouselSlide.style.transition="transform 0.3s ease-in-out";
    counter--;
    carouselSlide.style.transform="translateX("+ -size*counter+"px)";
});


//Button Listeners


carouselSlide.addEventListener("transitionend", function () {
    if (carouselContents[counter].id === "lastClone") {
      carouselSlide.style.transition = "none";
      counter = carouselContents.length - 2;
      carouselSlide.style.transform = "translateX(" + -size * counter + "px)";
    }
    if (carouselContents[counter].id === "firstClone") {
      carouselSlide.style.transition = "none";
      counter = carouselContents.length - counter;
      carouselSlide.style.transform = "translateX(" + -size * counter + "px)";
    }
  });
  
