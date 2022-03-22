from .forms import NewsletterForm


def newsletter_form(request):
    """ Context processor to access Newsletter form on the base template """

    context = {
        'NewsletterForm': NewsletterForm,
    }
    return context
