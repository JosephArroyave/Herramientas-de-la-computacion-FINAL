#Funcion que da valor de los descuentos segun el Rol.
#Rol 1 para estudiante, Rol 2 para profesor
def informacion(Rol):
    if Rol == 1:
        return 0.5
    else:
        return 0.2

#Varibles del menu    
Hamburguesa = 3000
pizza = 2500
HotDog = 2300
producto = 0
cantidad = 0
#Bienvenida al programa
print ("BIENVENIDO A LA CAFETERIA")
print ("Ingrese sus datos porfavor: ")
#Datos del cliente
Cedula = int(input("Ingrese su numero de identificación: "))
Rol = int(input("Si es estudiante ingrese 1, si es profesor ingrese 2: "))
#Lista del menu
print ("Menu: \n1. Hamburguesa = 3000 / Codigo: 101. \n2. Pizza = 2500 / Codigo: 102.\n3. Hot dog: 2300 / Codigo: 103\n")
comida = int(input("Ingrese el codigo del producto que desea: "))
if comida == 101: #Pedido Hamburgesa
    cantidad = int(input("Ingrese el numero de unidades del producto seleccionado: "))
    producto = Hamburguesa * cantidad - (informacion(Rol)*cantidad*Hamburguesa)
    if Rol == 1: #Estudiante
        print ("El estudiante","con cedula",Cedula,",debe pagar",producto ,"por el producto" ,comida)
    else: #Profesor
        print ("El estudiante","con cedula",Cedula,",debe pagar",producto ,"por el producto" ,comida)
elif comida == 102: #Pedido Pizza
    cantidad = int(input("Ingrese el numero de unidades del producto seleccionado: "))
    producto = pizza * cantidad - (informacion(Rol)*cantidad*pizza) 
    if Rol == 1: #Estudiante
        print ("El estudiante","con cedula",Cedula,",debe pagar",producto ,"por el producto" ,comida)
    else: #Profesor
        print ("El estudiante","con cedula",Cedula,",debe pagar",producto ,"por el producto" ,comida)
elif comida == 103: #Pedido Hotdog
    cantidad = int(input("Ingrese el numero de unidades del producto seleccionado: "))
    producto = HotDog * cantidad - (informacion(Rol)*cantidad*HotDog)
    if Rol == 1: #Estudiante
        print ("El estudiante","con cedula",Cedula,",debe pagar",producto ,"por el producto" ,comida)
    else: #Profesor
        print ("El estudiante","con cedula",Cedula,",debe pagar",producto ,"por el producto" ,comida)








