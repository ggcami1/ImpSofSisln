alumno=input("ingresa el nombre del alumno: ")
fecha_nac_alumo=input("Ingresa la fecha de nacimiento del alumno: ")
edad_alumno=input("Ingresa la edad dl alumno: ")

lineas=[alumno+'\n',fecha_nac_alumo+'\n',edad_alumno+'\n']

class writed_doctxt():
    def documento (lineas):
        with open('actividad 5.txt','a') as txt:
            txt.writelines(lineas)
    documento(lineas)

class close_doctxt():
    def leer_documento():
        msj=""
        with open('actividad 5.txt','r') as txt:
            msj=txt.read()
    
        return msj
    print(leer_documento())