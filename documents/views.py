from dnollkse.viewHelper import render

from documents.models import Document

# Create your views here.
def index(request):
    """
    Retrieves all documents and renders them on the index view.
    """
    documents = Document.objects.all()
    return render(request, "documents/index.dtl", {'items': documents})
