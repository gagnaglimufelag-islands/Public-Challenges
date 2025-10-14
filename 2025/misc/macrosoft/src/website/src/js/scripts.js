document.addEventListener('DOMContentLoaded', function() {
    console.log("Pizza Palace website loaded!");

    const currentPage = window.location.pathname.split("/").pop() || "index.html";
    const navLinks = document.querySelectorAll('.navbar .nav-button');

    navLinks.forEach(link => {
        let linkPage = link.getAttribute('href').split("/").pop();
        if (linkPage === "" && currentPage === "index.html") {
             link.classList.add('active');
        } else if (linkPage === currentPage) {
            link.classList.add('active');
        }

        if (currentPage === "index.html" && window.location.hash) {
            if (window.location.hash.length > 1 && link.getAttribute('href') === 'menu.html') {
            }
        }
    });


    if (document.getElementById('pizza-menu-container')) {
        fetchPizzas();
    }

    if (currentPage === "menu.html" && window.location.hash) {
        const targetId = window.location.hash.substring(1);
        setTimeout(() => {
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
                // Optional: highlight the card
                targetElement.style.border = '2px solid var(--accent-color)';
                targetElement.style.boxShadow = '0 0 15px var(--accent-color)';
                setTimeout(() => {
                    targetElement.style.border = '1px solid var(--border-color)';
                    targetElement.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
                }, 3000);
            }
        }, 500);
    }

});

async function fetchPizzas() {
    const menuContainer = document.getElementById('pizza-menu-container');
    if (!menuContainer) return;

    const loadingMessage = menuContainer.querySelector('.loading-message');

    try {
        const response = await fetch('data/pizzas.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const pizzas = await response.json();

        if (loadingMessage) {
            loadingMessage.remove();
        }
        renderPizzas(pizzas);
    } catch (error) {
        console.error('Error fetching or parsing pizzas:', error);
        if (loadingMessage) {
            loadingMessage.textContent = 'Sorry, we couldn\'t load the menu at this time. Please try again later.';
            loadingMessage.classList.remove('loading-message');
            loadingMessage.classList.add('error-message');
        } else {
            menuContainer.innerHTML = '<p class="error-message">Sorry, we couldn\'t load the menu at this time. Please try again later.</p>';
        }
    }
}

function renderPizzas(pizzas) {
    const menuContainer = document.getElementById('pizza-menu-container');
    if (!pizzas || pizzas.length === 0) {
        menuContainer.innerHTML = '<p class="info-message">No pizzas available on the menu right now. Check back soon!</p>';
        return;
    }

    pizzas.forEach(pizza => {
        const pizzaCard = document.createElement('div');
        pizzaCard.classList.add('pizza-card');
        if (pizza.id) {
            pizzaCard.id = pizza.id;
        }

        let toppingsList = '';
        if (Array.isArray(pizza.toppings)) {
            toppingsList = pizza.toppings.join(', ');
        } else {
            toppingsList = pizza.toppings;
        }

        let cardHTML = `
            <h3>${pizza.name}</h3>
            <p class="toppings"><strong>Toppings:</strong> ${toppingsList}</p>
        `;

        if (pizza.price) {
            cardHTML += `<p class="price">${pizza.price}kr</p>`;
        }

        pizzaCard.innerHTML = cardHTML;
        menuContainer.appendChild(pizzaCard);
    });
}
