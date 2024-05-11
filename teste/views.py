from django.shortcuts import render

# Create your views here.
def soma_numeros(request):
    if request.method == 'POST':
        n1 = request.POST['numero1']
        n2 = request.POST['numero2']

        soma = float(n1) + float(n2)
        mensagem = f'A soma de {n1} e {n2} é {soma}!'
    else:
        mensagem = 'Aperte o botão para somar'
    return render(request, 'soma.html', {'mensagem': mensagem })