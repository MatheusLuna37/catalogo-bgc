function dropDown(x) {
    x.classList.toggle("menu-button-selected");
    const menu = document.getElementById("menu");
    menu.classList.toggle("mobile-menu");
}

document.addEventListener('DOMContentLoaded', () => {
    let lastScrollY = window.scrollY;
    const header = document.querySelector('header');
    const mobile = document.getElementById('mobile-elements');
    let menu = mobile.nextElementSibling;
    const button = document.getElementById('menu-button');
  
    window.addEventListener('scroll', () => {
      if (window.scrollY > lastScrollY) {
        // Rolagem para baixo
        header.classList.add('hidden-header');
        if (menu.classList.contains('mobile-menu')) {
            dropDown(button);
        }
      } else {
        // Rolagem para cima
        header.classList.remove('hidden-header');
      }
      lastScrollY = window.scrollY;
    });
  });

document.getElementById("orderBtn").addEventListener("click", function () {
  const productName = document.getElementById("product-name").innerHTML;
  const size = document.getElementById("sizes").value;
  const message = `Gostaria de fazer o pedido de uma ${productName} no tamanho ${size}.`;
  const phone = '+558791690167';
  window.open(`https://wa.me/${phone}?text=${encodeURIComponent(message)}`, '_blank');
});
  