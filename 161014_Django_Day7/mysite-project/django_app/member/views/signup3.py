from django.shortcuts import render
from member.forms import SignupModelForm


def signup3(request):
    context = {}
    if request.method == 'POST':
        pass
    else:
        form = SignupModelForm()
        context['form'] = form
        return render(request, 'member/signup2.html', context)
