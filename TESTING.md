# Testing

## Manual Testing

## User Story Testing

1. As {User} I want {Be able to search for packs} so that {So i can filter specifically what I'm looking for }.

    <details>
    <summary>Steps</summary>

        1. From home page click on Pack

        2. Click on the search bar at the top of the page

        3. Type in what you are searching for

        4. The list of packs will be narrowed down to those containing your search query
    </details>

2. As {ADMIN} I want {TO BE ABLE TO ADD, REMOVE OR UPDATE ANY PRODUCT} so that {CONTROL THE PRODUCTS ON THE SITE}.

    <details>
    <summary>Steps</summary>

        1. Sign in to your superuser account from the login menu

        2. This will display an admin link in the nav bar that you will click

        3. From here click on the task that you want to achieve (add, remove, update etc.)

        4. Follow the details on screen to fulfil your task
    </details>

3. As {User} I want {See a list of all the packs available} so that {I can browse for sounds I want or may not know I want}.

    <details>
    <summary>Steps</summary>

        1. From the home menu, click on packs

        2. Here there will be a list of all packs available on the site

    </details>

4. As {User} I want {Be able to filter by category} so that {I can see the broad range of packs in the category I'm looking for }.

    <details>
    <summary>Steps</summary>

        1. From the packs menu, find a pack with a category you are interested in

        2. From here you can click on the category displayed on the product card

        3. Alternatively if you are on a pack details page you can click on the category from there

        4. This will display the packs page narrowed down to those with that category
        
    </details>

5. As {User} I want {be able to login and sign up easily} so that {i can access my profile}.

    <details>
    <summary>Steps</summary>

        1. From the home menu click login

        2. Here there will be a link to login to your account or click sign up

        3. If you are signing up, fill in your infomartion

        4. Check your email for a confirmation email

        5. Following this email your account will be created and you can sign in with the details you signed up with
        
    </details>

6. As {User} I want {Be able to hear a demo of any pack} so that {I can decide if I want to purchase this pack or not}.

    <details>
    <summary>Steps</summary>

        1. From the packs menu, click on a pack you are interested in buying

        2. At the bottom of the pack detail page there will be an embeded soundcloud player you can hear a demo through
        
    </details>

7. As {User} I want {Register a profile} so that {I can have a profile on the site}.

    <details>
    <summary>Steps</summary>

        1. A user profile is created automatically when you sign up for the website
        
    </details>

8. As {User} I want {Be able to download my purchased packs} so that {I can have them on any system or redownloaded them if I lose them}.

    <details>
    <summary>Steps</summary>

        1. After completing a purchase you will be redirected to a success page

        2. On this page is a summary of your order including your order number and the products you ordered

        3. Click the name of a purchased product to download it
        
    </details>

9. As {User} I want {See popular packs on the home page} so that {I can discover new sounds based on what's new or popular}.

    <details>
    <summary>Steps</summary>

        1. From the home menu these can be seen in the carousel on the right hand side of the screen
        
    </details>

10. As {User} I want {Have a list of my purchased packs} so that {So that I can see what packs I have available}.

    <details>
    <summary>Steps</summary>

        1. After purchasing a pack you it will be on your profile page

        2. This can be accessed by clicking the profile link on the navbar

        3. On this page is a list of previous purchases

        4. Find the purchase you are looking for 

        5. On the right hand side of the table will be the names of the packs purchased

        6. Clicking a name will initiate the download for that pack
        
    </details>

11. As {USER} I want {TO BE ABLE TO CONTACT THE SITE} so that {I CAN ENQUIRE ABOUT ANY ISSUES I MAY HAVE}.

    <details>
    <summary>Steps</summary>

        1. From any page on the site, click the contact link 

        2. Fill out the form on this page with your subject and any relevant information about your enquiry

        3. From here the admins can reply to these messages from the admin panel, sending an email to the person who filled out the form
        
    </details>

## Stripe CLI

 The Stripe CLI was used to test the webhook handling. The exact methods of testing were found in the [Stripe Documentation](https://stripe.com/docs/payments/handling-payment-events#use-cli) and were followed precisely to ensure that the handler worked as intended. 


## Bugs

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

<details>
 <summary>3. Stripe: HTTP 500 (Internal Server Error) when locally testing webhooks.</summary>
    The solution for this was quite easy as it was simply a matter of adding a trailing '/' to the webhook url 
</details>

<details>
 <summary>4. Programming Error with database when trying to view orders in admin panel.</summary>
    From digging around on the internet, I believe this was an issue with my database that I couldn't quite pin point, so to solve the problem I flushed my database out and migrated it again. This fixed the issue but unfortunately deleted my superusers and product info so I had to re-make them. 
</details>

<details>
 <summary>5. Deployed app returning to incorrect site on payment success.</summary>
    I realised after deployment that the YOUR_DOMAIN variable was still returning to the local host. Once this was changed to the heroku domain, the site worked perfectly. 
</details>


<details>
 <summary>6. Add product form not validating properly.</summary>
    The view for adding a product was using `form.save` and not `form.save()`, causing it not to validate properly.
</details>

<details>
 <summary>7. Add product form not posting and leaving 'Field required' warnings next to image and file field.</summary>
    This was fixed by adding the enctype to the form element. 

```
<form action="{% url 'add_product' %}" class="form" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form|crispy }}
            <button type="submit" class="btn btn-dark mt-3">Add Product</button>
        </form>
```
</details>