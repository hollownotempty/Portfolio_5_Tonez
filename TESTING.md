# Testing

## Manual Testing

## User Story Testing



## Bugs

![cart_render_type_error](#)
<details>
 <summary>1. TypeError found when trying to render cart items in the cart</summary>
 This was fixed by introducing the quantity variable to the for loop. 

```
    for item_id, quantity in cart.items():
            pack = get_object_or_404(Packs, pk=item_id)
            total += pack.price
            product_count += 1
            stripe_price_id = pack.stripe_price_id
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'pack': pack,
                'stripe_price_id': stripe_price_id,
            })
```
</details>


<details>
 <summary>2. Shopping cart only able to display one item at a time, needed to account for and display all items in the cart.</summary>
 This was tricky to fix as I was using Stripe Checkout, which uses stripe_price_id's to determine the product being sold. This is relayed using this code from the Stripe documentation.

 ```
    def create_checkout_session():
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': '{{PRICE_ID}}',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success.html',
                cancel_url=YOUR_DOMAIN + '/cancel.html',
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)
 ```

Products are added on the Stripe dashboard and you use the given price_id to reference items in your code, normally giving each item a checkout page of their own. I resolved this using the following code, grabbing every item from the shopping cart, their individual stripe_price_id (which I defined for each product in the Packs model) and appending the information to the array that Stripe's documentation uses. 

```
def create_checkout_session(request):
    """ Create checkout session Stripe """

    YOUR_DOMAIN = 'https://8000-hollownotempty-portfolio-kuwz79nvo6k.ws-eu34.gitpod.io/'

    cart = request.session.get('cart', {})

    line_items = []

    for item_id, quantity in cart.items():
        pack = get_object_or_404(Packs, pk=item_id)
        stripe_price_id = pack.stripe_price_id
        pd = {
            'price': stripe_price_id,
            'quantity': quantity,
        }
        
        line_items.append(pd)

    checkout_session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=YOUR_DOMAIN + 'checkout/success/',
        cancel_url=YOUR_DOMAIN + 'cart/',
    )

    return redirect(checkout_session.url, code=303)
```

With this code, the Stripe checkout page displays the checkout for all the items in the cart. 
</details>

