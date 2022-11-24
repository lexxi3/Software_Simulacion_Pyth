import tkinter 
from tkinter import filedialog
import pyautogui
from tkinter import *
from tkinter import messagebox,filedialog
from PIL import Image,ImageTk
from re import A
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


 #Se define el ejercicio 1 opcion a --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opciona():
    filewin = Toplevel(root)
  
    formula=Label(filewin, 
	text="Fórmula de la relación de transmisión i = Z2/Z1 = N1/N2",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)

    label_ejerc_1= Label(filewin,font=("Century Gothic",11) ,text="""Ejercicio 1.1 opcion a): Calculo de Transmisión de fuerza
                         a partir del número de dientes del engrane i= Z2/Z1""", fg="black",bg="#85D5FE")
    label_ejerc_1.pack(padx=3, pady=20)

    label_num_dientesz1= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de dientes de la rueda motriz (Z1)",fg="black",bg="#D3D6FB")
    label_num_dientesz1.pack()
    campo_num_dientesz1=Entry(filewin)
    campo_num_dientesz1.pack()

    label_num_dientesz2= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de dientes de la rueda accionada (Z2)",fg="black",bg="#D3D6FB")
    label_num_dientesz2.pack()
    campo_num_dientesz2=Entry(filewin)
    campo_num_dientesz2.pack()


    #Definición de formulas

    def operacion(Z1, Z2):
        return (Z2/Z1)

    def ejecutar_operacion():
        valor_num_dientesz1 = int(campo_num_dientesz1.get())
        valor_num_dientesz2 = int(campo_num_dientesz2.get())

        resultado = operacion(valor_num_dientesz1, valor_num_dientesz2)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton1=Button(filewin, text="Ejecutar",command=ejecutar_operacion)
    boton1.pack()
    boton1.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="""La transmisión de fuerza cuando la rueda da 1 vuelta de la rueda motriz da:  """,fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Engranajes con palanca de ejercicio opcion a)")
        image = img.imread('engranajes_con_palanca_opcion_a).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



 #Se define el ejercicio 2 opcion a --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opciona():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula de la relación de transmisión i = Z2/Z1 = N1/N2",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)

    label_ejerc_12= Label(filewin,font=("Calibri",11) ,text="""Ejercicio 1.2 opcion a) : calcular la transmisión de fuerza a partir de las velocidades de la rueda motriz""",
                          fg="black",bg="#85D5FE")
    label_ejerc_12.pack()

    label_num_N1= Label(filewin,font=("Calibri",11) ,text="Ingresa la velocidad de giro de la rueda motriz (N1) en RPM",
                               fg="black",bg="#D3D6FB")
    label_num_N1.pack()
    campo_num_N1=Entry(filewin)
    campo_num_N1.pack()

    label_num_N2= Label(filewin,font=("Calibri",11) ,text="Ingresa la velocidad de giro de la rueda accionada (N2) en RPM",
                               fg="black",bg="#D3D6FB")
    label_num_N2.pack()
    campo_num_N2=Entry(filewin)
    campo_num_N2.pack()

    #Definición de formulas

    def operacion(N1,N2):
        return (N1/N2)

    def ejecutar_operacion():
        valor_num_N1 = int(campo_num_N1.get())
        valor_num_N2 = int(campo_num_N2.get())

        resultado = operacion(valor_num_N1, valor_num_N2)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton1=Button(filewin, text="Ejecutar",command=ejecutar_operacion)
    boton1.pack()
    boton1.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La  transmisión de fuerza a partir de las velocidades de la rueda motriz es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opciona():
        plt.title("Engranajes con palanca de ejercicio opcion a)")
        image = img.imread('engranajes_con_palanca_opcion_a).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciona)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()


#Se define el ejercicio 3 opcion a --------------------------------------------------------------------------------------------------------------------
def ejercicio_3_opciona():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula de la relación de transmisión i_multiple = Z1/ZN",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_13= Label(filewin,font=("Calibri",11) ,text="Ejercicio 1.3 opcion a) : Calcular la transmisión de fuerza múltiple i_múltiple =Z1/ZN ",
                        fg="black",bg="#85D5FE")
    label_ejerc_13.pack()

    label_num_dientesZ1= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de dientes de la rueda motriz (Z1)",fg="black",bg="#D3D6FB")
    label_num_dientesZ1.pack()
    campo_num_dientesZ1=Entry(filewin)
    campo_num_dientesZ1.pack()

    label_num_dientesZN= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de dientes de la rueda accionada (ZN)",fg="black",bg="#D3D6FB")
    label_num_dientesZN.pack()
    campo_num_dientesZN=Entry(filewin)
    campo_num_dientesZN.pack()


    #Definición de formulas

    def operacion(Z1, ZN):
        return Z1/ZN

    def ejecutar_operacion():
        valor_num_dientesZ1 = int(campo_num_dientesZ1.get())
        valor_num_dientesZN = int(campo_num_dientesZN.get())

        resultado = operacion(valor_num_dientesZ1, valor_num_dientesZN)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton51=Button(filewin, text="Ejecutar",command=ejecutar_operacion)
    boton51.pack()
    boton51.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La Transmisión de fuerza (i_múltiple) es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

#Generar grafica de opcion a)
    def GenerarGrafica_opcionf():
        plt.title("Engranajes con palanca de ejercicio opcion a)")
        image = img.imread('engranajes_con_palanca_opcion_a).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



#Se define el ejercicio 1 opcion b --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opcionb():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula  de la velocidad periférica de la rueda motriz = D1 *  π * N` ",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_21= Label(filewin,font=("Calibri",11) ,text="Ejercicio 2.1 opcion b) : Calcular la velocidad periférica de la rueda motriz ",
                        fg="black",bg="#85D5FE")
    label_ejerc_21.pack()

    label_num_diametroD1= Label(filewin,font=("Calibri",11) ,text="Ingrese el diametro de la rueda motriz (D1)",fg="black",bg="#D3D6FB")
    label_num_diametroD1.pack()
    campo_num_diametroD1=Entry(filewin)
    campo_num_diametroD1.pack()

    label_num_revoN1= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de revoluciones de la rueda motriz(N1)",fg="black",bg="#D3D6FB")
    label_num_revoN1.pack()
    campo_num_revoN1=Entry(filewin)
    campo_num_revoN1.pack()


    #Definición de formulas

    def operacion(D1, N1):
        return (D1*math.pi*N1)

    def ejecutar_operacion():
        valor_num_diametroD1 = int(campo_num_diametroD1.get())
        valor_num_revoN1 = int(campo_num_revoN1.get())

        resultado = operacion(valor_num_diametroD1, valor_num_revoN1)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton21=Button(filewin, text="Ejecutar",command=ejecutar_operacion)
    boton21.pack()
    boton21.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La Transmisión de fuerza (i_múltiple) es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Velocidad periférica de rueda motriz de ejercicio opcion b)")
        image = img.imread('velocidad_periférica_opcion_b).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



#Se define el ejercicio 2 opcion b --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opcionb():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula de la velocidad periférica de la rueda accionada = D2 *  π * N2 ",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_22= Label(filewin,font=("Calibri",11) ,text="Ejercicio 2.2 opcion b) : Calcular la velocidad periférica de la rueda accionada",
                        fg="black",bg="#85D5FE")
    label_ejerc_22.pack()

    label_num_diametroD2= Label(filewin,font=("Calibri",11) ,text="Ingrese el diametro de la rueda accionada (D2)",fg="black",bg="#D3D6FB")
    label_num_diametroD2.pack()
    campo_num_diametroD2=Entry(filewin)
    campo_num_diametroD2.pack()

    label_num_revoN2= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de revoluciones de la rueda accionada(N2)",fg="black",bg="#D3D6FB")
    label_num_revoN2.pack()
    campo_num_revoN2=Entry(filewin)
    campo_num_revoN2.pack()


    #Definición de formulas

    def operacion(D2, N2):
        return (D2*math.pi*N2)

    def ejecutar_operacion():
        valor_num_diametroD2 = int(campo_num_diametroD2.get())
        valor_num_revoN2 = int(campo_num_revoN2.get())

        resultado = operacion(valor_num_diametroD2, valor_num_revoN2)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton21=Button(filewin, text="Ejecutar",command=ejecutar_operacion)
    boton21.pack()
    boton21.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La Transmisión de fuerza (i_múltiple) es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Velocidad periférica de rueda accionada de ejercicio opcion b)")
        image = img.imread('velocidad_periférica_opcion_b).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



#Se define el ejercicio 1 opcion c --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opcionc():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula  de la Transmisión parcial -> i1=(n1/n2) =(d2/d1)  ",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_21= Label(filewin,font=("Calibri",11) ,text="Ejercicio 3.1 opcion c) : Calcular la Transmisión parcial 1 y 2 ",
                        fg="black",bg="#85D5FE")
    label_ejerc_21.pack()

    label_num_revoN1= Label(filewin,font=("Calibri",11) ,text="Ingrese  el número de revoluciones motriz (N1)",fg="black",bg="#D3D6FB")
    label_num_revoN1.pack()
    campo_num_revoN1=Entry(filewin)
    campo_num_revoN1.pack()

    label_num_revoN2= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de revoluciones accionada(N2)",fg="black",bg="#D3D6FB")
    label_num_revoN2.pack()
    campo_num_revoN2=Entry(filewin)
    campo_num_revoN2.pack()


    label_num_revoN3= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de revoluciones accionada(N3)",fg="black",bg="#D3D6FB")
    label_num_revoN3.pack()
    campo_num_revoN3=Entry(filewin)
    campo_num_revoN3.pack()

    label_num_revoN4= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de revoluciones accionada(N4)",fg="black",bg="#D3D6FB")
    label_num_revoN4.pack()
    campo_num_revoN4=Entry(filewin)
    campo_num_revoN4.pack()


    #Definición de formulas

    def operacion3(N1, N2):
        return (N1/N2)

    def ejecutar_operacion3():
        valor_num_revoN1 = int(campo_num_revoN1.get())
        valor_num_revoN2 = int(campo_num_revoN2.get())

        resultado = operacion3(valor_num_revoN1, valor_num_revoN2)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton3=Button(filewin, text="Ejecutar",command=ejecutar_operacion3)
    boton3.pack()
    boton3.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La Transmisión parcial 1 es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

    def operacion31(N3, N4):
        return (N3/N4)

    def ejecutar_operacion31():
        valor_num_revoN3 = int(campo_num_revoN3.get())
        valor_num_revoN4 = int(campo_num_revoN4.get())

        resultado3 = operacion31(valor_num_revoN3, valor_num_revoN4)
        label_valor_result3.config(text = resultado3)

    #BOTON DE EJECUCION

    boton31=Button(filewin, text="Ejecutar",command=ejecutar_operacion31)
    boton31.pack()
    boton31.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result3= Label(filewin,font=("Calibri",11) ,text="La Transmisión parcial 2 es:  ",fg="white",bg="black")
    label_result3.pack()

    label_valor_result3= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result3.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Transmision parcial de opcion c)")
        image = img.imread('transmision_parcial_opcion_c).jpg')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()


#Se define el ejercicio 2 opcion c --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opcionc():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula  de la Transmisión parcial -> i= i1 * i2  ",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_21= Label(filewin,font=("Calibri",11) ,text="Ejercicio 3.2 opcion c) : Calcular la Transmisión total ",
                        fg="black",bg="#85D5FE")
    label_ejerc_21.pack()

    label_num_revoN1= Label(filewin,font=("Calibri",11) ,text="Ingrese  el número de revoluciones motriz (N1)",fg="black",bg="#D3D6FB")
    label_num_revoN1.pack()
    campo_num_revoN1=Entry(filewin)
    campo_num_revoN1.pack()

    label_num_revoN2= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de revoluciones accionada(N2)",fg="black",bg="#D3D6FB")
    label_num_revoN2.pack()
    campo_num_revoN2=Entry(filewin)
    campo_num_revoN2.pack()


    label_num_revoN3= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de revoluciones accionada(N3)",fg="black",bg="#D3D6FB")
    label_num_revoN3.pack()
    campo_num_revoN3=Entry(filewin)
    campo_num_revoN3.pack()

    label_num_revoN4= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de revoluciones accionada(N4)",fg="black",bg="#D3D6FB")
    label_num_revoN4.pack()
    campo_num_revoN4=Entry(filewin)
    campo_num_revoN4.pack()


    #Definición de formulas

    def operacion32(N1, N2, N3, N4):
        return ((N1/N2)*(N3/N4))

    def ejecutar_operacion32():
        valor_num_revoN1 = int(campo_num_revoN1.get())
        valor_num_revoN2 = int(campo_num_revoN2.get())
        valor_num_revoN3 = int(campo_num_revoN3.get())
        valor_num_revoN4 = int(campo_num_revoN4.get())

        resultado = operacion32(valor_num_revoN1, valor_num_revoN2,   valor_num_revoN3,   valor_num_revoN4)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton32=Button(filewin, text="Ejecutar",command=ejecutar_operacion32)
    boton32.pack()
    boton32.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La Transmisión parcial 1 es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Transmision total opcion c)")
        image = img.imread('transmision_total_opcion_c).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()




#Se define el ejercicio 1 opcion d --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opciond():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula del diametro activo -> dw=da - 2*c  ",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_41= Label(filewin,font=("Calibri",11) ,text="Ejercicio 4.1 opcion d) : Calcular el diametro activo ",
                        fg="black",bg="#85D5FE")
    label_ejerc_41.pack()

    label_num_da= Label(filewin,font=("Calibri",11) ,text="Ingrese  el diametro exterior(da)",fg="black",bg="#D3D6FB")
    label_num_da.pack()
    campo_num_da=Entry(filewin)
    campo_num_da.pack()

    label_num_c= Label(filewin,font=("Calibri",11) ,text="Ingrese el valor de corrección (c)",fg="black",bg="#D3D6FB")
    label_num_c.pack()
    campo_num_c=Entry(filewin)
    campo_num_c.pack()

    #Definición de formulas

    def operacion41(da, c):
        return (da - 2*c)

    def ejecutar_operacion41():
        valor_num_da = int(campo_num_da.get())
        valor_num_c = int( campo_num_c.get())

        resultado41 = operacion41(valor_num_da, valor_num_c)
        label_valor_result41.config(text = resultado41)

    #BOTON DE EJECUCION

    boton41=Button(filewin, text="Ejecutar",command=ejecutar_operacion41)
    boton41.pack()
    boton41.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result41= Label(filewin,font=("Calibri",11) ,text="El diametro activo (dw) es:  ",fg="white",bg="black")
    label_result41.pack()

    label_valor_result41= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result41.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Diametro activo de Correa trapezoidal de ejercicio opcion d)")
        image = img.imread('diámetro_activo_opcion_d).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



#Se define el ejercicio 2 opcion d --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opciond():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula de número de revoluciones transmisión -> i= N1/N2  ",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_42= Label(filewin,font=("Calibri",11) ,text="Ejercicio 4.2 opcion d) : Calcular el número de revoluciones transmisión ",
                        fg="black",bg="#85D5FE")
    label_ejerc_42.pack()

    label_num_revoN1= Label(filewin,font=("Calibri",11) ,text="Ingresa el Número de revoluciones de propulsión (N1) en RPM",fg="black",bg="#D3D6FB")
    label_num_revoN1.pack()
    campo_num_revoN1=Entry(filewin)
    campo_num_revoN1.pack()

    label_num_revoN2= Label(filewin,font=("Calibri",11) ,text="Ingresa el Número de revoluciones de salida (N2) en RPM",fg="black",bg="#D3D6FB")
    label_num_revoN2.pack()
    campo_num_revoN2=Entry(filewin)
    campo_num_revoN2.pack()

    #Definición de formulas

    def operacion42(N1, N2):
        return ((N1)/(N2))

    def ejecutar_operacion42():
        valor_num_revoN1 = int(campo_num_revoN1.get())
        valor_num_revoN2 = int( campo_num_revoN2.get())

        resultado42 = operacion42(valor_num_revoN1, valor_num_revoN2)
        label_valor_result42.config(text = resultado42)

    #BOTON DE EJECUCION

    boton42=Button(filewin, text="Ejecutar",command=ejecutar_operacion42)
    boton42.pack()
    boton42.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result42= Label(filewin,font=("Calibri",11) ,text="El número de revoluciones Transmisión es:  ",fg="white",bg="black")
    label_result42.pack()

    label_valor_result42= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result42.pack()

#Se genera grafica del ejercicio opcion d)
    def GenerarGrafica_opciong():
        plt.title("Número de revoluciones transmisión Correa trapezoidal de ejercicio opcion d)", fontsize =11)
        image = img.imread('num_revo_transmisión_opcion_d).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



#Se define el ejercicio 1 opcion e --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opcione():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="Fórmula  de la Transmisión parcial -> Dp=m*Z ",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_21= Label(filewin,font=("Calibri",11) ,text="Ejercicio 5.1 opcion e) : Calcular el  Diámetro primitivo (Dp)",
                        fg="black",bg="#85D5FE")
    label_ejerc_21.pack()

    label_num_m= Label(filewin,font=("Calibri",11) ,text="Ingrese el módulo (m) en mm",fg="black",bg="#D3D6FB")
    label_num_m.pack()
    campo_num_m=Entry(filewin)
    campo_num_m.pack()

    label_num_dientesz= Label(filewin,font=("Calibri",11) ,text="Ingrese el número de dientes de la rueda (Z)",fg="black",bg="#D3D6FB")
    label_num_dientesz.pack()
    campo_num_dientesz=Entry(filewin)
    campo_num_dientesz.pack()

    #Definición de formulas
    def operacion51(m, Z):
        return ((m*Z))

    def ejecutar_operacion51():
        valor_num_m = int(campo_num_m.get())
        valor_num_dientesz = int(campo_num_dientesz.get())

        resultado = operacion51(valor_num_m, valor_num_dientesz)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION
    boton51=Button(filewin, text="Ejecutar",command=ejecutar_operacion51)
    boton51.pack()
    boton51.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La Transmisión parcial 1 es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opcione():
        plt.title("Rueda dentada  con sus elementos de opcion e)")
        image = img.imread('Rueda_dentada_opcion_e).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcione)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



#Se define el ejercicio 2 opcion e --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opcione():
    filewin = Toplevel(root)
    formula=Label(filewin, 
	text="""Fórmula  para calcular las dimensiones:
                         Altura del diente (h): h=2.25*m
                         Altura de la cabeza del diente (hc): hc=m
                         Altura del pie del diente (hp): hp=1.25*m
                         Espesor del diente (e): e=0.5*P
                         Anchura del diente (B): B=m*10""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_52= Label(filewin,font=("Calibri",11) ,text="Ejercicio 5.2 opcion e) : Calcular el  Diámetro primitivo (Dp)",
                        fg="black",bg="#85D5FE")
    label_ejerc_52.pack()

    label_modulo= Label(filewin,font=("Calibri",11) ,text="Ingrese el módulo (m) en mm",fg="black",bg="#D3D6FB")
    label_modulo.pack()
    campo_modulo=Entry(filewin)
    campo_modulo.pack()

    label_paso_circular= Label(filewin,font=("Calibri",11) ,text="Ingrese el Paso circular (P) en mm",bg="#D3D6FB")
    label_paso_circular.pack()
    campo_paso_circular=Entry(filewin)
    campo_paso_circular.pack()



#Definición de formulas

#calcular altura del diente------------------------------------------------------------------------------------------
    def operacion51_1(m):
        return ((2.25*m))

    def ejecutar_operacion51_1():
        valor_modulo = int(campo_modulo.get())

        resultado51_1 = operacion51_1( valor_modulo)
        label_valor_result51_1.config(text =resultado51_1)
        
    #BOTON DE EJECUCION
    boton51_1=Button(filewin, text="Ejecutar",command=ejecutar_operacion51_1)
    boton51_1.pack()
    boton51_1.config(bg="Blue",fg="white",cursor="cross")
    
    # Resultados
    label_result51_1= Label(filewin,font=("Calibri",11) ,text="La altura del diente(h) en  mm es:  ",fg="white",bg="black")
    label_result51_1.pack()

    label_valor_result51_1= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result51_1.pack()

#Calcular la altura de la cabeza del diente
    def operacion51_2(m):
        return ((m))

    def ejecutar_operacion51_2():
        valor_modulo = int(campo_modulo.get())

        resultado51_2= operacion51_2( valor_modulo)
        label_valor_result51_2.config(text =resultado51_2)

    #BOTON DE EJECUCION
    boton51_2=Button(filewin, text="Ejecutar",command= ejecutar_operacion51_2)
    boton51_2.pack()
    boton51_2.config(bg="Blue",fg="white",cursor="cross")   

    # Resultados
    label_result51_2= Label(filewin,font=("Calibri",11) ,text="La altura de la cabeza del diente(hc) en  mm es:  ",fg="white",bg="black")
    label_result51_2.pack()

    label_valor_result51_2= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result51_2.pack()

#Calcular la altura del pie del diente
    def operacion51_3(m):
        return ((1.25*m))

    def ejecutar_operacion51_3():
        valor_modulo = int(campo_modulo.get())

        resultado51_3= operacion51_3( valor_modulo)
        label_valor_result51_3.config(text =resultado51_3)

    #BOTON DE EJECUCION
    boton51_3=Button(filewin, text="Ejecutar",command= ejecutar_operacion51_3)
    boton51_3.pack()
    boton51_3.config(bg="Blue",fg="white",cursor="cross")   

    # Resultados
    label_result51_3= Label(filewin,font=("Calibri",11) ,text="La altura del pie del diente(hp) en  mm es:  ",fg="white",bg="black")
    label_result51_3.pack()

    label_valor_result51_3= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result51_3.pack()

#Calcular el espesor del diente
    def operacion51_4(P):
        return ((0.5*P))

    def ejecutar_operacion51_4():
        valor_paso_circular= int(campo_paso_circular.get())

        resultado51_4= operacion51_4( valor_paso_circular)
        label_valor_result51_4.config(text =resultado51_4)

    #BOTON DE EJECUCION
    boton51_4=Button(filewin, text="Ejecutar",command= ejecutar_operacion51_4)
    boton51_4.pack()
    boton51_4.config(bg="Blue",fg="white",cursor="cross")   

    # Resultados
    label_result51_4= Label(filewin,font=("Calibri",11) ,text="El espesor del diente(e) en  mm es:  ",fg="white",bg="black")
    label_result51_4.pack()

    label_valor_result51_4= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result51_4.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Rueda dentada  con sus elementos de opcion e)")
        image = img.imread('Rueda_dentada_opcion_e).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()
    


 #Se define el ejercicio 1--------------------------------------------------------------------------------------------------------------------
def ejercicio_61_opcionf():
    filewin = Toplevel(root)
    label_ejerc_61= Label(filewin,font=("Calibri",11) ,text="Ejercicio 6.1: Calculo de numero de revoluciones por Accionamiento simple de Rueda Dentada",
                        fg="black",bg="#85D5FE")
    label_ejerc_61.pack()

    label_num_dientesz1= Label(filewin,font=("Calibri",11) ,text="Numero de dientes 1",fg="black",bg="#D3D6FB")
    label_num_dientesz1.pack()
    campo_num_dientesz1=Entry(filewin)
    campo_num_dientesz1.pack()

    label_num_dientesz2= Label(filewin,font=("Calibri",11) ,text="Numero de dientes 2",fg="black",bg="#D3D6FB")
    label_num_dientesz2.pack()
    campo_num_dientesz2=Entry(filewin)
    campo_num_dientesz2.pack()

    label_revol_ini= Label(filewin,font=("Calibri",11) ,text="Revolucion Inicial",fg="black",bg="#D3D6FB")
    label_revol_ini.pack()
    campo_revol_ini=Entry(filewin)
    campo_revol_ini.pack()



    #Definición de formulas

    def operacion(z1,z2,n1):
        return (z1*n1)/z2

    def ejecutar_operacion():
        valor_num_dientesz1 = int(campo_num_dientesz1.get())
        valor_num_dientesz2 = int(campo_num_dientesz2.get())
        valor_revol_ini = int(campo_revol_ini.get())

        resultado = operacion(valor_num_dientesz1, valor_num_dientesz2, valor_revol_ini)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton61=Button(filewin, text="Ejecutar",command=ejecutar_operacion)
    boton61.pack()
    boton61.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="El numero de revoluciones final de la rueda es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()




#Se define el ejercicio2--------------------------------------------------------------------------------------------------------------------
def ejercicio_71_opciong():
    filewin = Toplevel(root)

    label_ejerc_71= Label(filewin,font=("Courier New",11) ,text="Ejercicio 7.1 opcion g): Calculo de transmision total de Accionamiento múltiple por Rueda dentada ",
                         fg="black",bg="#85D5FE")
    label_ejerc_71.pack()

    label_num_dientesz1= Label(filewin,font=("Calibri",11) ,text="Numero de dientes 1",fg="black",bg="#D3D6FB")
    label_num_dientesz1.pack()
    campo_num_dientesz1=Entry(filewin)
    campo_num_dientesz1.pack()

    label_num_dientesz2= Label(filewin,font=("Calibri",11) ,text="Numero de dientes 2",fg="black",bg="#D3D6FB")
    label_num_dientesz2.pack()
    campo_num_dientesz2=Entry(filewin)
    campo_num_dientesz2.pack()

    label_num_dientesz3= Label(filewin,font=("Calibri",11) ,text="Numero de dientes 3",fg="black",bg="#D3D6FB")
    label_num_dientesz3.pack()
    campo_num_dientesz3=Entry(filewin)
    campo_num_dientesz3.pack()

    label_num_dientesz4= Label(filewin,font=("Calibri",11) ,text="Numero de dientes 4",fg="black",bg="#D3D6FB")
    label_num_dientesz4.pack()
    campo_num_dientesz4=Entry(filewin)
    campo_num_dientesz4.pack()
  

    #Definición de formulas

    def operacion(z1,z2,z3,z4):
        return ((z2*z4)/(z1*z3))

    def ejecutar_operacion():
        valor_num_dientesz2 = int(campo_num_dientesz2.get())
        valor_num_dientesz4 = int(campo_num_dientesz4.get())
        valor_num_dientesz1 = int(campo_num_dientesz1.get())
        valor_num_dientesz3 = int(campo_num_dientesz3.get())

        resultado = operacion(valor_num_dientesz1, valor_num_dientesz2, valor_num_dientesz3, valor_num_dientesz4)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton71=Button(filewin, text="Ejecutar",command=ejecutar_operacion)
    boton71.pack()
    boton71.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La transmision total es: ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result.pack()

    
#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Engranaje y rueda de ejercicio opcion g)")
        image = img.imread('engranaje_opcion_g).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()

    

#EJERCICIO 3--------------------------------------------------------------------------------------------------------------
def ejercicio_81_opcionh():
    filewin = Toplevel(root)

    label_ejerc_81= Label(filewin,font=("Calibri",11) ,text="Ejercicio 8.1 opcion h): Calculo de Accionamiento de cremallera sin fin",fg="black",bg="#85D5FE")
    label_ejerc_81.pack()

    label_dientes_cremallera= Label(filewin,font=("Calibri",11) ,text="Dientes de la cremallera",fg="black",bg="#D3D6FB")
    label_dientes_cremallera.pack()
    campo_dientes_cremallera=Entry(filewin)
    campo_dientes_cremallera.pack()
    
    label_modulo_cremallera= Label(filewin,font=("Calibri",11) ,text="Modulo",fg="black",bg="#D3D6FB")
    label_modulo_cremallera.pack()
    campo_modulo_cremallera=Entry(filewin)
    campo_modulo_cremallera.pack()


    #Definición de formulas
    def operacion_81(z,m):
        return (z*m*math.pi)

    def ejecutar_operacion_81():
    
        #valor dientes z
        valor_dientes_cremallera_z = int(campo_dientes_cremallera.get())
        #valor modulo m
        valor_modulo_cremallera_m = int(campo_modulo_cremallera.get())
       

        resultado_81 = operacion_81(valor_dientes_cremallera_z,valor_modulo_cremallera_m)
        label_valor_result_81.config(text = resultado_81)


    #BOTON DE EJECUCION
    boton81=Button(filewin, text="Ejecutar",command=ejecutar_operacion_81)
    boton81.pack()
    boton81.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result_81= Label(filewin,font=("Calibri",11) ,text="El accionamiento de la cremallera es: ",fg="white",bg="black")
    label_result_81.pack()

    label_valor_result_81= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result_81.pack()

#Se genera grafica del ejercicio opcion h)
    def GenerarGrafica_opciong():
        plt.title("Cremallera de ejercicio opcion h)")
        image = img.imread('cremallera_opcion_h).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()

#Ejercicio 9.1 opcion i) ---------------------------------------------------
def ejercicio_91_opcioni():

    filewin = Toplevel(root)
    label_ejerc_91= Label(filewin,font=("Calibri",11) ,text="Ejercicio 9.1 opcion i): Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas",
                         fg="black",bg="#85D5FE")
    label_ejerc_91.pack()

    label_dato1_ej91= Label(filewin,font=("Calibri",11) ,text="Introduzca el numero de dientes del engranaje 1 de entrada:",fg="black",bg="#D3D6FB")
    label_dato1_ej91.pack()
    campo_dato1_ej91=Entry(filewin)
    campo_dato1_ej91.pack()

    label_dato2_ej91= Label(filewin,font=("Calibri",11) ,text="Introduzca el numero de dientes del engranaje 2 de entrada:",fg="black",bg="#D3D6FB")
    label_dato2_ej91.pack()
    campo_dato2_ej91=Entry(filewin)
    campo_dato2_ej91.pack()

    label_dato3_ej91= Label(filewin,font=("Calibri",11) ,text="Introduzca el numero de dientes del engranaje 1 de salida:",fg="black",bg="#D3D6FB")
    label_dato3_ej91.pack()
    campo_dato3_ej91=Entry(filewin)
    campo_dato3_ej91.pack()

    label_dato4_ej91= Label(filewin,font=("Calibri",11) ,text="Introduzca el numero de dientes del engranaje 2 de salida:",fg="black",bg="#D3D6FB")
    label_dato4_ej91.pack()
    campo_dato4_ej91=Entry(filewin)
    campo_dato4_ej91.pack()

    #Definición de formulas

    def operacion_91(z1,z2,z3,z4):
        return ((z1*z3)/(z2*z4))


    def ejecutar_operacion_91():

        #Cuantos dientes tiene el engranaje 1 de entrada
        valor_dientes_engranajez1 = int(campo_dato1_ej91.get())

        #Cuantos dientes tiene el engranaje 2 de entrada
        valor_dientes_engranajez3 = int(campo_dato2_ej91.get())

        #Cuantos dientes tiene el engranaje 1 de salida
        valor_dientes_engranajez2 = int(campo_dato3_ej91.get())
    
        #Cuantos dientes tiene el engranaje 2 de salida
        valor_dientes_engranajez4 = int(campo_dato4_ej91.get())

        resultado_91 = operacion_91(valor_dientes_engranajez1,valor_dientes_engranajez3,valor_dientes_engranajez2, valor_dientes_engranajez4)
        label_valor_result_91.config(text = resultado_91)


        #BOTON DE EJECUCION

    boton91=Button(filewin, text="Ejecutar",command=ejecutar_operacion_91)
    boton91.pack()
    boton91.config(bg="Blue",fg="white",cursor="cross")


    label_result_91= Label(filewin,font=("Calibri",11) ,text="La relación de transmisión de las ruedas es : ",fg="white",bg="black")
    label_result_91.pack()


    label_valor_result_91= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result_91.pack()

#Se genera grafica del ejercicio opcion i)
    def GenerarGrafica_opcioni():
        plt.title("Juego de ruedas de ejercicio opcion i)")
        image = img.imread("juego_ruedas_opcioni).png")
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcioni)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()
        
    


#Ejercicio 10.1 ---------------------------------------------------
def ejercicio_10_1_opcionj():
    
    filewin = Toplevel(root)
    label_ejerc_10_1= Label(filewin,font=("Calibri",17) ,text="Ejercicio 10.1 opcion j): Calculo momento de giro de engranaje conversion par",
                         fg="black",bg="#85D5FE")
    label_ejerc_10_1.pack()

    label_dato1_ej10_1= Label(filewin,font=("Calibri",11) ,text="Introduzca el numero de diente z1:",fg="black",bg="#D3D6FB")
    label_dato1_ej10_1.pack()
    campo_dato1_ej10_1=Entry(filewin)
    campo_dato1_ej10_1.pack()

    label_dato2_ej10_1= Label(filewin,font=("Calibri",11) ,text="Introduzca el numero de dientes z2:",fg="black",bg="#D3D6FB")
    label_dato2_ej10_1.pack()
    campo_dato2_ej10_1=Entry(filewin)
    campo_dato2_ej10_1.pack()

    label_dato3_ej10_1= Label(filewin,font=("Calibri",11) ,text="Introduzca el numero par de salida:",fg="black",bg="#D3D6FB")
    label_dato3_ej10_1.pack()
    campo_dato3_ej10_1=Entry(filewin)
    campo_dato3_ej10_1.pack()


    #Definición de formulas

    def operacion_10_1(z1,z2,M2):
        return ((M2*z1)/z2)

    def ejecutar_operacion_10_1():
    
        #valor z1
        valor_dientes_engrane_z1 = int(campo_dato1_ej10_1.get())
        #valor z2
        valor_dientes_engrane_z2 = int(campo_dato2_ej10_1.get())
        #valor M2
        valor_revol_engrane_M2 = int(campo_dato3_ej10_1.get())

        resultado_10_1 = operacion_5(valor_dientes_engrane_z1,valor_dientes_engrane_z2,valor_revol_engrane_M2)
        label_valor_result_10_1.config(text = resultado_10_1)


    #BOTON DE EJECUCION
    boton10_1=Button(filewin, text="Ejecutar",command=ejecutar_operacion_10_1)
    boton10_1.pack()
    boton10_1.config(bg="Blue",fg="white",cursor="cross")

    # Resultados
    label_result_10_1= Label(filewin,font=("Calibri",11) ,text="El momento de momento de giro de impulsión es: ",fg="white",bg="black")
    label_result_10_1.pack()

    label_valor_result_10_1= Label(filewin,font=("Calibri",11) ,text="",fg="black",bg="white")
    label_valor_result_10_1.pack()

#Se genera grafica del ejercicio opcion j)
    def GenerarGrafica_opcionj():
        plt.title("Engranaje como convertidor par de ejercicio opcion j)")
        image = img.imread("engranaje_opcionj).png")
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionj)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()
    
    

#abrir imagen de formulas de Accionamiento simple por Rueda dentada interdependencia y transmisión 
def abroimagenf11():
    messagebox.showinfo("Formula para calcular interdependencia de la rueda dentada",
                        message="Esta es la formula para calcular interdependencia de la rueda dentada")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("400x310+100+100")
    ventanaAbrir.title("Formula 1 de Accionamiento simple por Rueda dentada interdependencia")
    imagenf11=PhotoImage(file="formula_1_ejer_1_AS_ruedadent_interdepen.png", master=ventanaAbrir)
    lblImagen11=Label(ventanaAbrir,image=imagenf11)

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("400x310+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula1_opcionf).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)

        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenf11, command=descarga, height=240, width=330).place(x=30, y=30)
 #cambio de codigo en comando, original command=abroimagenf11
    ventanaAbrir.mainloop()
  


def abroimagenf12():
    messagebox.showinfo("Formula 2 para calcular transmision de la rueda dentada",
                        message="Esta es la formula para calcular transmision de la rueda dentada")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("400x220+100+100")
    ventanaAbrir.title("Formula 2 de Accionamiento simple por Rueda dentada transmisión")
    imagenf12=PhotoImage(file="formula_1_ejer_1_AS_ruedadent_transmision.png", master=ventanaAbrir)
    lblImagen12=Label(ventanaAbrir,image=imagenf12)
    

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("400x310+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula2_opcionf).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)

        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenf12, command=descarga, height=168, width=260).place(x=65, y=30)
 #cambio de codigo en comando, original command=abroimagenf12
    ventanaAbrir.mainloop()


def abroimagenf13():
    messagebox.showinfo("Formula 3 para calcular la distancia entre ejes",
                        message="Esta es la formula para la distancia entre ejes")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("400x220+100+100")
    ventanaAbrir.title("Formula 3 de Accionamiento simple por Rueda dentada transmisión")
    imagenf13=PhotoImage(file="formula_1_ejer_2_AS_ruedadent_distancia.png", master=ventanaAbrir)
    lblImagen13=Label(ventanaAbrir,image=imagenf13)
    
#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula3_opcionf).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)

        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenf13, command=descarga, height=168, width=260).place(x=65, y=25)
 #cambio de codigo en comando, original command=abroimagenf13
    ventanaAbrir.mainloop()



#abrir imagen de formulas de Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total
def abroimageng21():
    messagebox.showinfo("Formula 1 para calcular la transmision parcial",
                        message="Esta es la formula para calcular la transmision parcial")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("430x440+100+100")
    ventanaAbrir.title("Formula 1 de Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total")
    imageng21=PhotoImage(file="formula_2_ejer_1_reuda_dent_TP.png", master=ventanaAbrir)
    lblImagen21=Label(ventanaAbrir,image=imageng21)
    

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula1_opciong).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imageng21, command=descarga, height=405, width=400).place(x=10, y=20)
 #cambio de codigo en comando, original command=abroimageng21
    ventanaAbrir.mainloop()

def abroimageng22():
    messagebox.showinfo("Formula 2 para calcular la transmision total",
                        message="Esta es la formula para calcular la transmision total")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("445x320+100+100")
    ventanaAbrir.title("Formula 2 de Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total")
    imageng22=PhotoImage(file="formula_2_ejer_2_reuda_dent_TT.png", master=ventanaAbrir)
    lblImagen22=Label(ventanaAbrir,image=imageng22)
    

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula2_opciong).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imageng22, command=descarga, height=267, width=405).place(x=10, y=30)
 #cambio de codigo en comando, original command=abroimageng22
    ventanaAbrir.mainloop()


#abrir imagen de formulas de Accionamiento por cremallera y por tornillo sin fin,
#carrera de cremallera accionamiento por tornillo sin fin, interdependencias
def abroimagenh31():
    messagebox.showinfo("Formula1 para calcular tornillo sin fin",
                        message="Esta es la formula para calcular tornillo sin fin")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("550x400+100+100")
    ventanaAbrir.title("Formula 1 de Accionamiento por cremallera y por tornillo sin fin")
    imagenh31=PhotoImage(file="formula_3_ejer_1_tornillo.png", master=ventanaAbrir)
    lblImagen31=Label(ventanaAbrir,image=imagenh31)
    #Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula1_opcionh).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenh31, command=descarga, height=338, width=500).place(x=20, y=45)
 #cambio de codigo en comando, original command=abroimagenh31
    ventanaAbrir.mainloop()


def abroimagenh32():
    messagebox.showinfo("Formula 2 para calcular cremallera sin fin",
                        message="Esta es la formula para calcular cremallera sin fin")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("450x250+100+100")
    ventanaAbrir.title("Formula 2 de Accionamiento por cremallera y por tornillo sin fin")
    imagenh32=PhotoImage(file="formula_3_ejer_2_cremallera.png", master=ventanaAbrir)
    lblImagen32=Label(ventanaAbrir,image=imagenh32)

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula2_opcionh).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenh32, command=descarga, height=99, width=300).place(x=60, y=50)
 #cambio de codigo en comando, original command=abroimagenh32
    ventanaAbrir.mainloop()




#4 abrir imagen de formulas de Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas
def abroimageni4():
    messagebox.showinfo("Formula para calcular ruedas de cambio interdependencia",
                        message="Esta es la formula para calcular  ruedas de cambio interdependencia")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("700x460+100+100")
    ventanaAbrir.title("Formula de Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas")
    imageni4=PhotoImage(file="formula_4_ejer_1_ruedas.png", master=ventanaAbrir)
    lblImagen4=Label(ventanaAbrir,image=imageni4)
    #Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula_opcioni).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imageni4, command=descarga, height=314, width=666).place(x=60, y=90)
 #cambio de codigo en comando, original command=abroimageni4
    ventanaAbrir.mainloop() 



#5 abrir imagen de formulas de Engranajes como convertidores de par, transmisión de engranajes y conversión de par
def abroimagenj51():
    messagebox.showinfo("Formula 1 para calcular Transmisión de engranajes",
                        message="Esta es la formula para calcular Transmisión de engranajes")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("435x500+100+100")
    ventanaAbrir.title("Formula 1 de Engranajes como convertidores de par, transmisión de engranajes y conversión de par")
    imagenj51=PhotoImage(file="formula_5_ejer_1_engranajes_transmision.png", master=ventanaAbrir)
    lblImagen51=Label(ventanaAbrir,image=imagenj51)

    #Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x110+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula1_opcionj).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenj51, command=descarga, height=314, width=400).place(x=10, y=100)
 #cambio de codigo en comando, original command=abroimagenj51
    ventanaAbrir.mainloop() 


def abroimagenj52():
    messagebox.showinfo("Formula para calcular Conversión de par",
                        message="Esta es la formula para calcular Conversión de par")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("435x400+100+100")
    ventanaAbrir.title("Formula 2 de Engranajes como convertidores de par, transmisión de engranajes y conversión de par")
    imagenj52=PhotoImage(file="formula_5_ejer_2_engranajes_conversion_par.png", master=ventanaAbrir)
    lblImagen52=Label(ventanaAbrir,image=imagenj52)
         #Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenj52, command=descarga, height=235, width=400).place(x=10, y=30)
 #cambio de codigo en comando, original command=abroimagenj52
    ventanaAbrir.mainloop() 


root=Tk()
root.geometry("600x400+0+0")
root.title("Simulacion de mecanismos")
root.configure(background ='LightBlue2', width=1000, height=500)

        
frame1=Frame(root,width=610, height=400)
frame1.pack()
frame1.config(bg="LightBlue2",bd=20)
label_saludos= Label(frame1, font=("Century Gothic", 24),text="Bienvenido querido/a  estudiante", fg="white",bg="black")
label_saludos.place(x="5",y="0")
label_explicacion1= Label(frame1, font=("Century Gothic", 11), text="Lo invitamos a resolver problemas de mecanismos",
                          fg="black")
label_explicacion2= Label(frame1, font=("Century Gothic", 11), text="para simular que se aplican en robotica",
                          fg="black")
label_explicacion3= Label(frame1, font=("Century Gothic", 11), text="Buena suerte!",
                          fg="black")
label_explicacion1.place(x=30,y=108, width=450, height=20)
label_explicacion2.place(x=30,y=128, width=450, height=20)
label_explicacion3.place(x=30,y=268, width=450, height=20)
menubar1 = Menu(root)
root.config(menu=menubar1)
        
        
opciones1 = Menu(menubar1)
submenu6= Menu(menubar1, tearoff=0)
#Submenu de Accionamiento simple por Rueda dentada interdependencia y transmisión con sus formulas
submenu6.add_command(label="Formula 1 para calcular la interdependencia", command=abroimagenf11)
submenu6.add_command(label="Formula 2 para calcular la transmision", command=abroimagenf12)
submenu6.add_command(label="Formula 3 para calcular distancia entre ejes", command=abroimagenf13)
opciones1.add_cascade(label="f) Accionamiento simple por Rueda dentada interdependencia y transmisión", menu= submenu6)


#Submenu de Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total
submenu7= Menu(menubar1, tearoff=0)
submenu7.add_command(label="Formula 1 para calcular la transmision parcial", command=abroimageng21)
submenu7.add_command(label="Formula 2 para calcular la transmision total", command=abroimageng22)
opciones1.add_cascade(label="g) Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total", menu= submenu7)


#Submenu de Accionamiento por cremallera y por tornillo sin fin, carrera de cremallera accionamiento por tornillo sin fin, interdependencias
submenu8=Menu(menubar1, tearoff=0)
submenu8.add_command(label="Formula 1 para calcular el tornillo sin fin", command=abroimagenh31)
submenu8.add_command(label="Formula 2 para calcular la creamellera sin fin", command=abroimagenh32)
opciones1.add_cascade(label="h) Accionamiento por cremallera y por tornillo sin fin,carrera de cremallera accionamiento por tornillo sin fin, interdependencias", menu= submenu8)

#Submenu de Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas
submenu9=Menu(menubar1, tearoff=0)
submenu9.add_command(label="Formula para calcular ruedas de interdependencia", command=abroimageni4)
opciones1.add_cascade(label="i) Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas", menu= submenu9)

#Submenu de Engranajes como convertidores de par, transmisión de engranajes y conversión de par
submenu10=Menu(menubar1, tearoff=0)
submenu10.add_command(label="Formula 1 para calcular Transmisión de engranajes", command=abroimagenj51)
submenu10.add_command(label="Formula 2 para calcular Conversión de par",command=abroimagenj52)
opciones1.add_cascade(label="j) Engranajes como convertidores de par, transmisión de engranajes y conversión de par", menu= submenu10)
      
opciones1.add_separator()
opciones1.add_command(label="Salir", command=root.destroy)


menubar1.add_cascade(label="Formulas", menu=opciones1) 


#Se crea el menu Ejercicios con sus submenus           
opciones2 = Menu(menubar1, tearoff=0)


#Submenu de Ejercicio opcion a) Engranajes con palanca
submenu1=Menu(menubar1, tearoff=0)
submenu1.add_command(label="Ejercicio 1.1 para calcular Transmisión de fuerza ", command=ejercicio_1_opciona)
submenu1.add_command(label="Ejercicio 1.2 para calcular  Transmisión simple ",command=ejercicio_2_opciona)
submenu1.add_command(label="Ejercicio 1.3 para calcular  Transmisión de fuerza  múltiple",command=ejercicio_3_opciona)
opciones2.add_cascade(label="Ejercicio opcion a) Engranajes con palanca", menu= submenu1)

#Submenu de Ejercicio opcion b) Accionamiento simple por correa
submenu2=Menu(menubar1, tearoff=0)
submenu2.add_command(label="Ejercicio 2.1 para calcular la velocidad periférica de la rueda motriz", command=ejercicio_1_opcionb)
submenu2.add_command(label="Ejercicio 2.2 para calcular la velocidad periférica de la rueda accionada",command=ejercicio_2_opcionb)
opciones2.add_cascade(label="Ejercicio opcion b) Accionamiento simple por correa", menu= submenu2)


#Submenu de Ejercicio opcion c)Accionamiento múltiple por correa
submenu3=Menu(menubar1, tearoff=0)
submenu3.add_command(label="Ejercicio 3.1 para calcular la transmisión parcial", command=ejercicio_1_opcionc)
submenu3.add_command(label="Ejercicio 3.2 para calcular la transmisión total",command=ejercicio_2_opcionc)
opciones2.add_cascade(label="Ejercicio opcion c) Accionamiento  múltiple por correa", menu= submenu3)

#Submenu de Ejercicio opcion d) Accionamiento por correa trapezoidal
submenu4=Menu(menubar1, tearoff=0)
submenu4.add_command(label="Ejercicio 4.1 para calcular el diametro activo", command=ejercicio_1_opciond)
submenu4.add_command(label="Ejercicio 4.2 para calcular el número de revoluciones transmisión", command=ejercicio_2_opciond)
opciones2.add_cascade(label="Ejercicio opcion d) Accionamiento por correa trapezoidal", menu= submenu4)

#Submenu de Ejercicio opcion e) La rueda dentada y sus dimensiones
submenu5=Menu(menubar1, tearoff=0)
submenu5.add_command(label="Ejercicio 5.1 para calcular Diámetro primitivo Dp", command=ejercicio_1_opcione)
submenu5.add_command(label="Ejercicio 5.2 para calcular llas dimensiones de la rueda",command=ejercicio_2_opcione)
opciones2.add_cascade(label="Ejercicio opcion e) La rueda dentada y sus dimensiones", menu= submenu5)


opciones2.add_command(label="Ejercicio opcion f)", command=ejercicio_61_opcionf)
opciones2.add_command(label="Ejercicio opcion g)", command=ejercicio_71_opciong)
opciones2.add_command(label="Ejercicio opcion h)", command=ejercicio_81_opcionh)
opciones2.add_command(label="Ejercicio opcion i)", command=ejercicio_91_opcioni)
opciones2.add_command(label="Ejercicio opcion j)", command=ejercicio_10_1_opcionj)
menubar1.add_cascade(label="Ejercicios", menu=opciones2) 

#Se crea el submenu Ajustes
def help():
    filewin = Toplevel(root)
    label_help= Label(filewin,font=("Calibri",11) ,text="""Gracias por usar el software de mecanismos simulados.
                      Si tiene alguna duda, comunicarse con los alumnos Abril Mejia y Raúl Iván Ramirez Aguilar """,
                      fg="white",bg="sea green")
    label_help.pack()

def about():
    filewin = Toplevel(root)
    label_about= Label(filewin,font=("Calibri",11) ,text="Software dedicado a la practica de datos de mecanismos por software",fg="white",bg="sea green")
    label_about.pack()


submenu1= Menu(menubar1, tearoff=0)
submenu1.add_command(label="Agradecimientos", command=help)
submenu1.add_command(label="Agradecimientos", command=help)
submenu1.add_command(label="Que es nuestro software", command=about)
opciones2.add_cascade(label="Ajustes", menu= submenu1)        


root.config(menu=menubar1)
#ventanaDescargar=Tk()
#ventanaDescargar.mainloop()
root.mainloop()
