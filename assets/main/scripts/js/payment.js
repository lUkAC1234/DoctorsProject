document.addEventListener('DOMContentLoaded', function() {
    const paymentForm = document.getElementById('payment-form');

    paymentForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(paymentForm);
        const productData = {
            name: formData.get('name'),
            price: parseFloat(formData.get('price'))
        };

        // Отправка данных на сервер через fetch
        fetch('/api/create_payment_intent/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Получаем CSRF-токен из куки
            },
            body: JSON.stringify(productData)
        })
        .then(response => response.json())
        .then(data => {
            // Получаем ответ от сервера и обрабатываем его
            const clientSecret = data.client_secret;

            // Подключаем Stripe.js и инициализируем платеж
            const stripe = Stripe('{{ STRIPE_PUBLIC_KEY }}');
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: elements.getElement('card') // Подключаем элемент для ввода карты
                }
            })
            .then(result => {
                if (result.error) {
                    // Обработка ошибок при оплате
                    console.error(result.error.message);
                } else {
                    // Успешная оплата
                    console.log('Payment succeeded:', result.paymentIntent);
                }
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

// Функция для получения CSRF-токена из куки
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
