from re import sub
import psycopg2
conexion1 = psycopg2.connect("dbname=Fase1 user=postgres password=ajkimtepaz")
cursor1=conexion1.cursor()
flag = 1
while flag:
    print('Ingrese una opción\n(I) Ingresar.\n(S) Salir.\n')
    option = input()
    option = str(option)
    if option == 'I' or option == 'i':
        superuser = False
        super_pass = False
        user_aut = False
        user_pass = False
        print('Ingrese su usuario')
        user = input()
        user = str(user)
        sql = "SELECT (usuario) FROM usuarios"
        cursor1.execute(sql)
        for fila in cursor1:
            if 'Ajkim' == user: superuser = True
            if fila[0] == user: 
                user_aut = True
                continue
        if superuser:
            print('Superusuario ingrese su contraseña')
            contra = input()
            contra = str(contra)
            if contra == '12345': 
                super_pass = True
            if super_pass: 
                print('Ha ingresado como superusuario.')
                flag_ingresar_usuario = 1
                while flag_ingresar_usuario:
                    print('\n Elija una opción. \n (A) Agregar Usuario \n (S) Salir')
                    option = input()
                    option = str(option)
                    if option == 'A' or option == 'a':
                        flag_nombre = 1
                        while flag_nombre:
                            print('\nIngrese el NOMBRE del nuevo Usuario\nSin Espacios Ni Caracteres Numéricos\nSolo letras\nMenor a 20 Caracteres\n-----------')
                            nombre = input()
                            nombre = str(nombre)
                            if nombre.isalpha():
                                if len(nombre)>20:
                                    print('El nombre es demasiado largo')
                                else:
                                    flag_contra = 1
                                    while flag_contra:
                                        print('-----------\nIngrese la contraseña del nuevo Usuario\nSin espacios \nMayor a 4 caracteres\nMenor a 20 caracteres\n-----------')
                                        contrasenia = input()
                                        contrasenia = str(contrasenia)
                                        if len(contrasenia)<4:
                                            print('La contraseña es demasiado corta\n\n')
                                        elif len(contrasenia)>20:
                                            print('La contraseña es demasiado larga\n\n')
                                        else:
                                            sql = "insert into usuarios(usuario,contra) values (%s,%s)" 
                                            datos = (nombre,contrasenia)
                                            cursor1.execute(sql, datos)
                                            conexion1.commit()
                                            print('Usuario INGRESADO a la base de datos\n\n')
                                            flag_contra = 0
                                            flag_nombre = 0
                            else:
                                print('El nombre contiene caracteres inválidos')
                    elif option == 'S' or option == 's':
                        print('Ha salido de la sesión de superusuerio %s'%user)
                        flag_ingresar_usuario = 0
                    else:
                        print('Opción Inválida')
            else:
                print('Contraseña Inválida')
        elif user_aut:
            print('Usuario normal ingrese su contraseña')
            sql = "SELECT (contra) FROM usuarios where usuario = '%s'"%user
            cursor1.execute(sql)
            contra = input()
            contra = str(contra)
            for fila in cursor1:
                if fila[0] == contra:
                    user_pass = True
                    continue
            if user_pass:
                print('Ha ingresado como %s'%user)
                flag_orden_vuelo = 1
                while flag_orden_vuelo:
                    print('\n Ingrese la opcion \n (O) Ordenar \n (B) Bitácora\n (S) Salir de la sesión \n')
                    option = input()
                    option = str(option)
                    if option == 'O' or option == 'o':
                        print('Ordenar')
                        subtotal = 0
                        descuento = 0
                        serv_com = 0
                        serv_beb = 0
                        serv_pel = 0
                        servicios = serv_com + serv_pel + serv_beb

                        flag_clase = 1
                        while flag_clase:
                            print('Elija la clase del vuelo.')
                            print('1.Primera\n2.Segunda\n3.Tercera')
                            clase = input()
                            clase = str(clase)
                            if clase == '1' or clase == 'Primera' or clase == 'primera': 
                                clase = 'Primera'
                                flag_clase = 0
                            elif clase == '2' or clase == 'Segunda' or clase == 'segunda': 
                                clase = 'Segunda'
                                flag_clase = 0
                            elif clase == '3' or clase == 'Tercera' or clase == 'tercera':
                                clase = 'Tercera'
                                flag_clase = 0
                            else:
                                print('Clase inválida')
                        flag_serv = 1
                        while flag_serv:
                            print('Desea incluir servicio de comida\n(y/N)')
                            serv = input()
                            serv = str(serv)
                            if serv == 'y' or serv == 'Y':
                                flag_clas_serv = 1
                                while flag_clas_serv:
                                    print('Elija en número de clase.')
                                    print('1.Primera Q50.00\n2.Segunda Q40.00\n3.Tercera Q25.00')
                                    clase_com = input()
                                    clase_com = str(clase_com)
                                    if clase_com == '1' or clase_com == 'Primera' or clase_com == 'primera': 
                                        clase_serv = 50
                                        flag_clas_serv = 0
                                    elif clase_com == '2' or clase_com == 'Segunda' or clase_com ==  'segunda': 
                                        clase_serv = 40
                                        flag_clas_serv = 0
                                    elif clase_com == '3' or clase_com == 'Tercera' or clase_com ==  'tercera':
                                        clase_serv = 25
                                        flag_clas_serv = 0
                                    else:
                                        print('Clase inválida')
                                flag_cant_serv = 1
                                while flag_cant_serv:
                                    print('Ingrese la cantidad de servicios de comida')
                                    serv_com = input()
                                    try:
                                        serv_com = int(serv_com)
                                        servicios = servicios + serv_com
                                        subtotal = subtotal + (serv_com * int(clase_com))
                                        flag_cant_serv = 0
                                        flag_serv = 0
                                    except:
                                        print('Debe ingresar un número entero')
                            elif serv == 'n' or serv == 'N':
                                flag_serv = 0
                            else:
                                print('Ingrese una opción')
                        flag_serv = 1
                        while flag_serv:
                            print('Desea incluir servicio de bebida\n(y/N)')
                            serv = input()
                            serv = str(serv)
                            if serv == 'y' or serv == 'Y':
                                flag_clas_serv = 1
                                while flag_clas_serv:
                                    print('Elija en número de clase.')
                                    print('1.Primera Q35.00\n2.Segunda Q25.00\n3.Tercera Q.10')
                                    clase_com = input()
                                    clase_com = str(clase_com)
                                    if clase_com == '1' or clase_com == 'Primera' or clase_com == 'primera': 
                                        clase_serv = 35
                                        flag_clas_serv = 0
                                    elif clase_com == '2' or clase_com == 'Segunda' or clase_com ==  'segunda': 
                                        clase_serv = 25
                                        flag_clas_serv = 0
                                    elif clase_com == '3' or clase_com == 'Tercera' or clase_com ==  'tercera':
                                        clase_serv = 10
                                        flag_clas_serv = 0
                                    else:
                                        print('Clase inválida')
                                flag_cant_serv = 1
                                while flag_cant_serv:
                                    print('Ingrese la cantidad de servicios de bebida')
                                    serv_beb = input()
                                    try:
                                        serv_beb = int(serv_beb)
                                        servicios = servicios + serv_beb
                                        subtotal = subtotal + (serv_beb * int(clase_serv))
                                        flag_cant_serv = 0
                                        flag_serv = 0
                                    except:
                                        print('Debe ingresar un número entero')
                            elif serv == 'n' or serv == 'N':
                                flag_serv = 0
                            else:
                                print('Ingrese una opción')
                        flag_serv = 1
                        while flag_serv:
                            print('Desea incluir servicio de peliculas\n(y/N)')
                            serv = input()
                            serv = str(serv)
                            if serv == 'y' or serv == 'Y':
                                flag_clas_serv = 1
                                while flag_clas_serv:
                                    print('Elija en número de clase.')
                                    print('1.Primera Q70.00\n2.Segunda Q55.00\n3.Tercera Q25.00')
                                    clase_com = input()
                                    clase_com = str(clase_com)
                                    if clase_com == '1' or clase_com == 'Primera' or clase_com == 'primera': 
                                        clase_serv = 70
                                        flag_clas_serv = 0
                                    elif clase_com == '2' or clase_com == 'Segunda' or clase_com ==  'segunda': 
                                        clase_serv = 55
                                        flag_clas_serv = 0
                                    elif clase_com == '3' or clase_com == 'Tercera' or clase_com ==  'tercera':
                                        clase_serv = 25
                                        flag_clas_serv = 0
                                    else:
                                        print('Clase inválida')
                                flag_cant_serv = 1
                                while flag_cant_serv:
                                    print('Ingrese la cantidad de servicios de peliculas')
                                    serv_pel = input()
                                    try:
                                        serv_pel = int(serv_pel)
                                        servicios = servicios + serv_pel
                                        subtotal = subtotal + (serv_pel * int(clase_serv))
                                        flag_cant_serv = 0
                                        flag_serv = 0
                                    except:
                                        print('Debe ingresar un número entero')
                            elif serv == 'n' or serv == 'N':
                                flag_serv = 0
                            else:
                                print('Ingrese una opción')
                        float(subtotal)
                        if servicios > 10:
                            descuento = descuento  + subtotal*0.10
                        if clase == 'Primera' and serv_beb > 0 and serv_com > 0 and serv_pel > 0:
                            descuento = descuento + subtotal*0.05
                        total = subtotal - descuento

                        sql = ("insert into facturas(cajero,vuelo,servicios,subtotal,descuento,total) values ('{0}','{1}',{2},{3},{4},{5})".format(user,clase,servicios,subtotal,descuento,total))
                        cursor1.execute(sql)
                        conexion1.commit()
                        print('__________________________________________________')
                        print('El vuelo es de %s clase' %clase)
                        print('La cantidad de servicios de comida es %i'%serv_com)
                        print('La cantidad de servicios de bebida es %i'%serv_beb)
                        print('La cantidad de servicios de peliculas es % i'%serv_pel)
                        print('El subtotal es %.2f'%subtotal)
                        print('El descuento es %.2f'%descuento)
                        print('El total es %.2f'%total)
                        print('_________________________________________________')
                    elif option == 'B' or option == 'b':
                        print('Bitácora')
                        cursor1.execute("select * from facturas")
                        for fila in cursor1:
                            print(fila)
                        print('Deseea realizar una acción? \n (E)Eliminar entradas \n(M)Modificar Entradas \n (Cualquier Tecla) Salir')
                        accion = input()
                        accion = str(accion)
                        if accion == 'E' or accion == 'e':
                            print('Ingrese el id de los valores que desee eliminar')
                            id_mod = input()
                            id_mod = int(id_mod)
                            if id_mod > len(fila):
                                print('Debe ingresar un ID válido')
                            else:
                                sql = ("delete from facturas where id_factura = '{0}'".format(id_mod))
                                cursor1.execute(sql)
                                conexion1.commit()
                                flag_mod = 0
                                
                        elif accion == 'M' or accion == 'm':
                            print('Ingrese el id de los valores que desee modificar')
                            id_mod = input()
                            #flag_mod = 1
                            #while flag_mod:

                            id_mod = int(id_mod)
                            if id_mod > len(fila):
                                print('Debe ingresar un ID válido')
                            else:
                                print('Solo puede modificar el nómbre del Cajero que realizó la transaccion')
                                print('Ingrese el nuevo nombre')
                                user_val = False
                                nombre = input()
                                str
                                sql = "SELECT (usuario) FROM usuarios"
                                cursor1.execute(sql)
                                for fila in cursor1:
                                    if fila[0] == nombre: 
                                        user_val = True
                                        continue
                                if user_val:
                                    sql = ("update facturas set cajero = '{0}' where id_factura={1}".format(nombre,id_mod))
                                    cursor1.execute(sql)
                                    conexion1.commit()
                                    flag_mod = 0
                                else:
                                    print('El cajero no está registrado')
                            
                                
                    elif option == 'S' or option == 's':
                        print('Ha salido de la sesión de %s'%user)
                        flag_orden_vuelo = 0
            else:
                print('Contraseña Inválida \n \n')
        else:
            print('Usuario Inválido\n\n')
    elif option == 'S' or option == 's':
        flag = 0
    else: 
        print('Opcion Inválida. Ingrese (I) o (S)')
conexion1.close()      
print('Gracias por usar el programa')

#sql="insert into Poblacion(prom_peso_General, prom_altura_General, prom_peso_Femenino, prom_altura_Femenino) values (%s,%s,%s,%s)"
#datos=(str(promedio_pesoF),str(promedio_alturaF),str(promedio_pesoF),str(promedio_alturaF))
#cursor1.execute(sql, datos)
#conexion1.commit()