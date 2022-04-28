const toggler = document.querySelector(".navbar__toggler");
const navbar = document.querySelector(".navbar");
toggler.addEventListener("click", (e) => {
  navbar.classList.toggle("nav__expanded");
});
