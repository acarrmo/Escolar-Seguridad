from pyDatalog import pyDatalog, Logic

conocimiento = ""

class inferencias:
    def __init__(self):
        print('Base de conocimientos')

        self.conocimiento=Logic(True)
    
        pyDatalog.load("""
            + usar_computadora('experto','si')
            + usar_computadora('inexperto','no')

            es_experto(Y) <= usar_computadora(Y,Z) & resp_experto(Z)

            # Es médico
            + terminologia('medico','si')
            + pacientes('medico','si')
            + recetar('medico','si')

            # No es médico
            + terminologia('persona','no')
            + pacientes('persona','no')
            + recetar('persona','no')

            es_medico(X) <= terminologia(X,A) & pacientes(X,A) & recetar(X,A) & resp_medico(A)
            

            tipo_usuario(X,Y) <= es_medico(X) & es_experto(Y)
        """)

    def leer_perfil(self, datos):
        str_experto = datos[0]
        str_medico = ""
        
        if(datos[1] == "si" and datos[2]=="si" and datos[3] == "si"):
            str_medico = "si"
        elif(datos[1] == "si" and datos[2]=="no" and datos[3] == "si"):
            str_medico = "si"
        else:
            str_medico = "no"

        Logic(self.conocimiento)
        try:
            pyDatalog.assert_fact("resp_experto",str_experto)
            pyDatalog.assert_fact("resp_medico",str_medico)

            q = "tipo_usuario(X,Y)"

            rq_3 = pyDatalog.ask(q)

            arr_resp = [
                rq_3.answers[0][0],
                rq_3.answers[0][1]
            ]

            return arr_resp
        except:
            print("error")
