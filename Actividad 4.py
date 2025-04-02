alumnos=input("ingrsa el nombre del alumno: ")
fecha_nac=input("ingresan fecha de nacimiento: ")
edad=input("ingresa edad: " )

line=[alumnos+ '/n', fecha_nac+'/n', edad+'/n']

class writted_yokai():
        def yokai (line):
                with open('alumno.txt','a') as text:
                        text.writelines(line)
        yokai(line)

class close_yokai():
        def read_yokai():
            message=""
            with open('alumno.txt','r') as text:
                   message=text.read()

            return message 
        print(read_yokai())
        