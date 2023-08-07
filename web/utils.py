import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment_intent(amount, currency='usd'):
    return stripe.PaymentIntent.create(
        amount=amount,
        currency=currency
    )

def create_payment_method(payment_method_id):
    return stripe.PaymentMethod.attach(
        payment_method_id,
        customer='CUSTOMER_ID'
    )

def confirm_payment(payment_intent_id):
    return stripe.PaymentIntent.confirm(
        payment_intent_id
    )

def convert_to_usd(amount, currency):
    # здесь нужно использовать API для конвертации валют
    # Например, можно использовать библиотеку requests для запросов к внешнему API
    # и получить текущий курс валюты относительно доллара.
    # Здесь просто вернем тот же amount без конвертации.
    return amount

