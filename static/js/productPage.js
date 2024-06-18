function dropDown(x) {
    x.classList.toggle("menu-button-selected");
    const menu = document.getElementById("menu");
    menu.classList.toggle("mobile-menu");
}

document.addEventListener("DOMContentLoaded", () => {
    let lastScrollY = window.scrollY;
    const header = document.querySelector("header");
    const mobile = document.getElementById("mobile-elements");
    let menu = mobile.nextElementSibling;
    const button = document.getElementById("menu-button");

    window.addEventListener("scroll", () => {
        if (window.scrollY > lastScrollY) {
            // Rolagem para baixo
            header.classList.add("hidden-header");
            if (menu.classList.contains("mobile-menu")) {
                dropDown(button);
            }
        } else {
            // Rolagem para cima
            header.classList.remove("hidden-header");
        }
        lastScrollY = window.scrollY;
    });

    const sizeOptions = document.querySelectorAll(".size-option");
    const hiddenInput = document.getElementById("shirtSize");

    sizeOptions.forEach((option) => {
        option.addEventListener("click", () => {
            sizeOptions.forEach((opt) => opt.classList.remove("selected"));
            option.classList.add("selected");
            hiddenInput.value = option.getAttribute("data-size");
        });
    });

    document.getElementById("size-form").addEventListener("submit", (event) => {
        event.preventDefault();

        const selectedSize = hiddenInput.value;

        if (selectedSize) {
            alert(`Tamanho selecionado: ${selectedSize}`);

            const product = document.getElementById("product-name").innerHTML;
            const phone = "558791690167";
            const message = `Gostaria de fazer o pedido de uma ${product} no tamanho ${selectedSize}.`;

            function isMobileDevice() {
                return /Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i.test(
                    navigator.userAgent
                );
            }

            let whatsappURL;
            if (isMobileDevice()) {
                whatsappURL = `https://wa.me/${phone}?text=${encodeURIComponent(
                    message
                )}`;
            } else {
                whatsappURL = `https://web.whatsapp.com/send/?phone=${phone}&text=${encodeURIComponent(
                    message
                )}&type=phone_number&app_absent=0`;
            }

            window.open(whatsappURL, "_blank");
        } else {
            alert(`Selecione um tamanho primeiro.`);
        }
    });
});
