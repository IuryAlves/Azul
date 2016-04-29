# coding: utf-8
import os
import base64
from django.shortcuts import redirect, render
from django.views.generic import View


class FormView(View):

    def get(self, request, id_empresa=None, id_torre=None):
        return render(request, 'index.html')

    def post(self, request):
        id_empresa = request.POST.get("id_empresa")
        id_torre = request.POST.get("id_torre")

        return redirect('form_view',
                        id_empresa=id_empresa,
                        id_torre=id_torre)




    # def get(self, request):
    #     imagem_path1 = os.path.join(settings.BASE_DIR, 'core', 'imagem.jpg')
    #     imagem_path2 = os.path.join(settings.BASE_DIR, 'core', 'imagem2.jpg')
    #     with open(imagem_path1, 'rb') as imagem1, open(imagem_path2, 'rb') as imagem2:
    #         imagens = [base64.b64encode(imagem1.read()),
    #                    base64.b64encode(imagem2.read())
    #                    ]
    #
    #     context = {'imagens': imagens}
    #     return render_to_response('plot.html', context=context)

