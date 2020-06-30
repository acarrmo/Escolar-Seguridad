class nucleo:
    arr_medico_exp = [
        "¿El paciente tiene fiebre?|s:2|n:0",
        "¿El paciente tiene rash?|s:2|n:1",
        "¿Tiene síntomas respiratorios?|s:0|n:1",
        "¿Tiene leucopenia?|s:2|n:1",
        "¿Tiene artromialgias?|s:1|n:0",
        "¿Es positiva la prueba de Rumpel-Leede?|s:2|n:1",
        "¿Fiebre mayor a 5 días?|s:0|n:1"
    ]

    arr_medico_inexp = [
        "¿El paciente tiene fiebre?|s:2|n:0",
        "¿Tiene síntomas respiratorios?|s:0|n:1",
        "¿Tiene leucopenia?|s:2|n:1",
        "¿Tiene artromialgias?|s:1|n:0"
    ]

    arr_persona_exp = [
        "¿Tienes fiebre?|s:2|n:0",
        "¿Tienes sarpullido?|s:2|n:1",
        "¿Tienes tos o dificultad para respirar?|s:0|n:1",
        "¿Sientes debilidad y cansancio?|s:2|n:1",
        "¿Tienes dolor muscular o de articulaciones?|s:1|n:0",
        "¿Al presionar una parte del antebrazo por aproximadamente 5 minutos se te quedan marcados puntos rojos?|s:2|n:1",
        "¿Has tenido fiebre por más de 3 días?|s:0|n:1"
    ]

    arr_persona_inexp = [
        "¿Sientes fiebre?|s:2|n:0",
        "¿Tienes tos o dificultad para respirar?|s:0|n:1",
        "¿Sientes debilidad y cansancio?|s:2|n:1",
        "¿Tienes dolor muscular o de articulaciones?|s:1|n:0"
    ]

    arr_tipo_usuario = {
        "1" : "medico experto",
        "2" : "medico inexperto",
        "3" : "persona experto",
        "4" : "persona inexperto"
    }

    arr_tipo_resp=["s","S","n","N","y","Y"]

    def __init__(self):
        print("Nucleo funcional")
        

    def iniciar_test(self, tipo):
        print("Test para detección de dengue\r\n")
        arr_opciones = ["1","2","3","4"]
        
        str_tipo = str(tipo)
    
        if(str_tipo in arr_opciones):
            if(str_tipo == "1"):
                self.applicar_test(str_tipo,self.arr_medico_exp)
            elif(str_tipo == "2"):
                self.applicar_test(str_tipo,self.arr_medico_inexp)
            elif(str_tipo == "3"):
                self.applicar_test(str_tipo,self.arr_persona_exp)
            elif(str_tipo == "4"):
                self.applicar_test(str_tipo,self.arr_persona_inexp)
        else:
            print("Elige una de las opciones indicadas anteriormente: ")
    
    def applicar_test(self, tipo,preguntas):
        puntaje = 0

        tipo=self.arr_tipo_usuario[tipo]
        indicaciones = "\r\nSu tipo de usuario es: "+tipo+"\r\n\n"
        indicaciones += "- Las preguntas del test se responden con S para sí, y N para No\r\n"
        indicaciones += "- Si el resultado del puntaje del test es mayor o igual a 6 indica que sí tiene dengue\r\n"
        indicaciones += "\r\n"    
        print(indicaciones)

        for p in preguntas:
            pregunta=p.split('|')[0]
            int_si = int(p.split('|')[1].split(':')[1])
            int_no = int(p.split('|')[2].split(':')[1])

            resp = input(pregunta+" ")

            while(True):
                if(resp in self.arr_tipo_resp):
                    if(resp == "s" or resp == "S" or resp == "y" or resp =="Y"):
                        puntaje+=int_si
                    elif(resp == "n" or resp == "N"):
                        puntaje+=int_no
                    break
                else:
                    resp = input("Ingrese la respuesta en formato s/n por favor: ")

        print("\r\nEl puntaje obtenido fue de: "+str(puntaje)+"\r\n")
        if(puntaje>=6):
            print("Persona portadora de dengue")
        else:
            print("Persona no portadora de dengue")
