#!/usr/bin/python
#-*- coding: utf-8 -*-

class Datos_GeneralesMedic:
    
    def __init__(self):
        self.Nombre = None
        self.Precio = None
        self.Marca = None

    def IngresaNombre(self, ):
        
        Nombre = input('Nombre del Medicamento: ')
        

    def IngresaPrecio(self, ):
        
        Precio = input("Precio del Medicamento: ")
        Marca = input('Marca del Medicamento: ')

    def MostrardatosGen(self, ):
        
        print("Medicamento:\n","Nombre:")
        print(super().Nombre)
        print("\nPrecio:",super().Precio,"\nMarca:",super().Marca,"\n")
        
        
    ejecucion=IngresaNombre()
    
        

