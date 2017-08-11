from dnollkse.viewHelper import render
from faq.models import Faq


def faq(request):
    faq = Faq.objects.all()
    return render(request, "faq/index.dtl", {'faq': faq})
