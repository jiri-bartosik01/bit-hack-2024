const indices = [0, 1, 3, 4, 5];
const allCards = document.querySelectorAll('div.company-big');
const cards = Array.from(allCards).filter((card, index) => indices.includes(index));


cards.forEach(card => {
    const newButton = document.createElement('a');
    const wrapper = document.createElement('div');
    const originalButton = card.querySelector('a.btn');
    wrapper.style.display = 'flex';
    wrapper.style.justifyContent = 'space-between';
    wrapper.style.alignItems = 'center';
    wrapper.style.width = '100%';
    wrapper.style.marginTop = "auto";
    newButton.classList.add('btn');
    newButton.classList.add('btn-outline-secondary');
    newButton.innerHTML = 'NÁVŠTĚVNOST';
    newButton.addEventListener('click', () => {

    });
    wrapper.appendChild(originalButton);
    wrapper.appendChild(newButton)
    card.appendChild(wrapper);
});


// add a modal iframe that will be shown when the button is clicked
const modal = document.createElement('div');
// modal.style.display = 'none';
modal.style.position = 'fixed';
modal.style.zIndex = '10000';
modal.style.left = '0';
modal.style.right = '0';
modal.style.top = '0';
modal.style.bottom = '0';
modal.style.backgroundColor = 'rgba(0,0,0,0.7)';

// iframe
const iframe = document.createElement('iframe')
iframe.src = 'http://localhost:5173';
iframe.style.position = 'absolute';
iframe.style.left = '50%';
iframe.style.top = '50%';
iframe.style.transform = 'translate(-50%, -50%)';
iframe.style.width = '80%';
iframe.style.height = '80%';
iframe.style.borderRadius = '10px';

modal.appendChild(iframe);
document.body.appendChild(modal);
