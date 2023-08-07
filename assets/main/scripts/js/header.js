const input = document.querySelector('.header-search-input');
const button = document.querySelector('.header-btn');

input.addEventListener('focus', () => {
    button.style.borderColor = '#5865F2';
    input.style.borderColor = '#5865F2';
});

input.addEventListener('blur', () => {
    button.style.borderColor = '#ccc';
    input.style.borderColor = '#ccc';
});