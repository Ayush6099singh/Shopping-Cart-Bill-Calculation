#### Shopping Cart Bill Calculation ####
def shoping_card(customer_name,card_amount):

    def calculate_card():
        return card_amount

    def apply_discount(card_amount):
        if card_amount >= 5000:
            discount = card_amount * 0.2
            return discount
        elif card_amount >= 3000:
            discount = card_amount * 0.1
            return discount
        else:
            return 0

    def calculate_delivery_charge(card_amount):
        if card_amount >= 1000:
            return 0
        else:
            return 50

    def generate_bill(card_amount, discount, delivery_charge):
        total_amount = card_amount - discount + delivery_charge
        print("--- Shopping Cart Bill ---")
        print("Customer Name:", customer_name)
        print("Cart Amount:", card_amount)
        print("Discount:", discount)
        print("Delivery Charge:", delivery_charge)
        print("Total Amount to Pay:", total_amount)

    card_amount = calculate_card()
    discount = apply_discount(card_amount)
    delivery_charge = calculate_delivery_charge(card_amount)
    generate_bill(card_amount, discount, delivery_charge)


shoping_card("Ayush", 4500)