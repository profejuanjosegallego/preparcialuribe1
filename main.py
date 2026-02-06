#Centralizar el llamado a las funciones y ejecutar solo este codigo
from funcionUno import crear_lista_ingenieros
from funcionDos import autenticar_usuario
from funcionesUtiles import calcular_promedio,clasificar_promedio

#Como incluir en el main la funcion1?
correoBD="correo@gmail.com"
contraseñaBD="admin123"

todoSalioBien=autenticar_usuario(correoBD,contraseñaBD,3)
if todoSalioBien:
    mediciones=[120,250,340,500,301,310,300,40,87,500] #Como vuelvo esta linea una funcion
    promedio=calcular_promedio(mediciones)
    estadoOperacion=clasificar_promedio(promedio)
    print(estadoOperacion)
else:
    print("🥹 No se continua porque el Login fallo")