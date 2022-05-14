# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:06:31 2021

@author:
        name: Matias Ott,
        mail:matota@gmail.com,       
"""


from xml.etree.ElementTree import SubElement,parse,Element,ElementTree


class Modelo:
    def __init__(self, controlador):
        self.controlador = controlador

    def crecionArchivoDatos(self):
        self.root=Element('root')    
        self.documento=SubElement(self.root,'Usuario')
        SubElement(self.documento,'Mail').text="123"        
        self.archivo=ElementTree(self.root)
        self.archivo.write('./Datos.xml')
        
    def ingresoDatosMail(self,op1):
        self.tree=parse('./Datos.xml')
        self.root=self.tree.getroot()
        self.root[0][0].text=op1
        self.tree.write('./Datos.xml')

    def lecturaDatos(self):
        self.tree=parse('./Datos.xml')
        self.root=self.tree.getroot()
        self.valor=self.root[0][0].text        
        return self.valor    
    
    def creacionIdiomaActivo(self):
        self.root=Element('root')    
        self.documento=SubElement(self.root,'Usuario')
        SubElement(self.documento,'Idioma').text="uk"        
        self.archivo=ElementTree(self.root)
        self.archivo.write('./Idioma.xml')
    
    def ingresoIdioma(self,ideo):
        self.tree=parse('./Idioma.xml')
        self.root=self.tree.getroot()
        self.root[0][0].text=ideo
        self.tree.write('./Idioma.xml')
        
    def lecturaIdioma(self):
        self.tree=parse('./Idioma.xml')
        self.root=self.tree.getroot()
        self.valor=self.root[0][0].text
        return self.valor 