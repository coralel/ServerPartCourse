/*------------------------------------------------------------------------------------------ function for sound/audio------------------------------------------------------------------------------------------------------------------------ */

window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("audio").style.top = "-200px";
  } else {
    document.getElementById("audio").style.top = "0";
  }
}   

/*------------------------------------------------------------------------------------------ function for menu------------------------------------------------------------------------------------------------------------------------ */
     
      /*--------------------function 1--------------------*/

function openNav() { /* open the menu when we click on the menu symbol*/
  document.getElementById("mySidenav").style.display = "block";
}
function closeNav() { /* close the menu when we click on X*/
  document.getElementById("mySidenav").style.display = "none";
}
     
      /*--------------------function 2--------------------*/

//pull the pathname from window location
const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav, compare each to pathname and mark the one that is active*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});






