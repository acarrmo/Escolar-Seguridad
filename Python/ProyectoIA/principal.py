from modulos.interaccionvoz import interaccionvoz as iv
from modulos.gramatica import gramatica as gr
from modulos.nucleofuncional import nucleo as nf 
from modulos.inferencia import inferencias as inf

iv = iv()
gr = gr()
nf = nf()
inf = inf()

arr_estereotipo = []


#   Llenar formulario mediante voz
for pr in iv.arr_preguntas_base:
    iv.reproducir_voz(pr)
    str_escuchar_voz = iv.escuchar_voz()
    if(str_escuchar_voz!='---'):
        evaluacion = gr.evaluacion_semantica(str_escuchar_voz)
        while(True):
            if(evaluacion != "error"):
                arr_estereotipo.append(evaluacion[1])
                break
            else:
                iv.reproducir_voz("Por favor menciona la respuesta adecuada")
                str_escuchar_voz = iv.escuchar_voz()
                evaluacion = gr.evaluacion_semantica(str_escuchar_voz)
    

# Tipo de usuario
perfil = inf.leer_perfil(arr_estereotipo)

tipo_usuario=""

if(perfil[0]=="medico" and perfil[1]=="experto"):
    tipo_usuario=1
elif(perfil[0]=="medico" and perfil[1]=="inexperto"):
    tipo_usuario=2
if(perfil[0]=="persona" and perfil[1]=="experto"):
    tipo_usuario=3
elif(perfil[0]=="persona" and perfil[1]=="inexperto"):
    tipo_usuario=4


# Decir que el test se llena de forma manual
iv.reproducir_voz("Iniciar test, se responde de forma manual")
nf.iniciar_test(tipo_usuario)

