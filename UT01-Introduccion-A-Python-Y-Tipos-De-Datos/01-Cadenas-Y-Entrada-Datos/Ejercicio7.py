email = input("Escriba su email:")
nombre = email[:email.find("@")]
dominio = email[email.find("@")+1:]
longitud = len(email)
print("Nombre de ususario:",nombre)
print("Dominio del correo:",dominio)
print("Longitud del correo:",longitud)
if nombre.count("0")+nombre.count("1")+nombre.count("2")+nombre.count("3")+nombre.count("4")+nombre.count("5")+nombre.count("6")+nombre.count("7")+nombre.count("8")+nombre.count("9")>0:
    print("SÍ contiene números el correo electrónico.")
else:
    print("NO contiene números el correo electrónico.")