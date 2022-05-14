# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:06:31 2021

@author:
        name: Matias Ott,
        mail:matota@gmail.com,       
"""


from tkinter.messagebox import askquestion,showwarning,showinfo
from tkinter import filedialog
from os.path import isdir,join,exists
from datetime import date
import modelo
import vista
from shutil import make_archive,rmtree
from smtplib import SMTP_SSL 
from ssl import create_default_context
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import remove,listdir,makedirs
from re import match
from zipfile import ZipFile
from userpaths import get_my_documents,get_desktop


class Controlador:
    def __init__(self):
        self.mi_modelo = modelo.Modelo(self)        
        self.mi_vista = vista.Vista(self)            
        self.arranque()                
        self.mi_vista.main_loop()
        self.archivoaGuardar=""
        
    def arranque(self):
        self.checkArchivo=exists('./Datos.xml')
        if self.checkArchivo==False:    
            self.mi_modelo.crecionArchivoDatos()
            self.mi_modelo.creacionIdiomaActivo()
            self.idiomaactualiza(self.mi_modelo.lecturaIdioma())           
            
            
        else:
            self.idiomaactualiza(self.mi_modelo.lecturaIdioma())
           
 
    
    def idiomaactualiza(self,tipo):
        self.mi_modelo.ingresoIdioma(tipo)
        if tipo=="esp":
            self.mi_vista.espanol()
        elif tipo =="por":
            self.mi_vista.portuguez()
        elif tipo =="uk":
            self.mi_vista.ingles()
        try:    
            self.mi_vista.eliminaTraductor()
        except:
            pass
        
        self.mi_vista.botonTraductor()
        
        if self.mi_modelo.lecturaDatos()=="123":                        
            self.mi_vista.BotonInicioIngreso()
            
        else:
            self.mi_vista.cluster()
            self.mi_vista.botonCreditos()
            self.mi_vista.botonEditarCorreoPagos()
        
     
    def traductoryRegistroIncial(self):
        if self.mi_modelo.lecturaDatos()=="123":
            self.mi_vista.eliminaBotonbotonTraductor()
            self.mi_vista.eliminaBotonInicioIngreso()
        else:
            self.mi_vista.eliminaBotonbotonTraductor()            
            self.mi_vista.eliminabotonCreditos()
            self.mi_vista.eliminabotonEditarCorreoPagos()
            self.mi_vista.eliminaCluster()

        
    def verificaCorrreo(self,op1,op2):
        self.correoVerdadero=self.esCorreo(op1)
        if self.correoVerdadero:
            if op1==op2:
                self.mi_modelo.ingresoDatosMail(op1)               
                self.mi_vista.eliminaregistroMail()
                self.mi_vista.cluster()
                self.mi_vista.botonTraductor()
                self.mi_vista.botonCreditos()
                self.mi_vista.botonEditarCorreoPagos()
                
                
            else:
                showwarning(self.variablesdeTraduccion('self.tcarteltituloverifica'),message=self.variablesdeTraduccion('self.tcartelparrafoverifica'))
                self.mi_vista.cargaErrorStrimbarRegistroMail()
        else:
            showwarning(self.variablesdeTraduccion('self.tcarteltituloverifica2'),message=self.variablesdeTraduccion('self.tcartelparrafoverifica2'))
            self.mi_vista.cargaErrorStrimbarRegistroMail()          
    
    def mail(self):
        self.dato=self.mi_modelo.lecturaDatos()
        return self.dato
    
    def esCorreo(self,correo):
        self.expresion_regular=r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return match(self.expresion_regular, correo) is not None
            
    def encuentraNumeroDirecctorio(self):
        self.ruta = get_my_documents()        
        self.ruta=self.ruta+"\\Klei\\DoNotStarveTogether"
        self.contenido=listdir(self.ruta)
        self.carpetasdeldirectorio=[nombre for nombre in self.contenido if isdir(join(self.ruta,nombre))] 
        self.p=len(self.carpetasdeldirectorio)
        self.e='e'
        i=0
        self.valorbuscado='Cluster_1'
        while i<self.p and self.e=='e':
            self.ruta2=self.ruta+'\\'+self.carpetasdeldirectorio[i]
            self.contenido2 = listdir(self.ruta2)
            if self.valorbuscado in self.contenido2:
                self.e=self.carpetasdeldirectorio[i]
            i+=1
        return self.e

    def fecha(self):
        self.fechadehoy = date.today()
        self.dia = str(self.fechadehoy.day)
        if len(self.dia)==1:
            dia=str(0)+self.dia
        else:
            self.dia==self.dia      
        self.mes = str(self.fechadehoy.month)
        if len(self.mes)==1:
            self.mes=str(0)+self.mes
        else:
            self.mes==self.mes
        self.año = str(self.fechadehoy.year)
        self.fechaconformato=self.dia+'-'+self.mes+'-'+self.año
        return self.fechaconformato
     
    def nombresCluster(self,cluster):
        self.numero=self.encuentraNumeroDirecctorio()
        try:            
            self.direMundo = get_my_documents()
            self.direMundo=self.direMundo+"\\Klei\\DoNotStarveTogether\\"+str(self.numero)+'\\Cluster_'+str(cluster)          
            self.dire=self.direMundo + '\\cluster.ini'            
            self.nc1=open(self.dire,'r')        
            self.onc1=self.nc1.readlines()
            self.nc1.close()
            self.nombredeclusterentero=str(self.onc1[12])
            self.nombredecluster=self.nombredeclusterentero[15:].strip()            
            if self.nombredecluster!="":
                return self.nombredecluster
            else:
                self.nombredecluster=self.variablesdeTraduccion('self.tnombrecluster')
                return self.nombredecluster
        except:
            self.nombredecluster=self.variablesdeTraduccion('self.tnombrecluster')
            return self.nombredecluster

    def zip(self,cluster,nombre):
        
        self.listaNoGenerado= ['No se ha generado','Não foi gerado','Has not been generated']
        if nombre not in self.listaNoGenerado:        
            self.mi_vista.avisozip()
            self.numero=self.encuentraNumeroDirecctorio()
            self.textofecha=self.fecha()
            self.direccionorigen= get_my_documents()
            self.direccionorigen=self.direccionorigen+"\\Klei\\DoNotStarveTogether\\"+str(self.numero)+'\\Cluster_'+ str(cluster)
            self.nombreArchivo= nombre +"-"+ str(self.textofecha)        
            self.archivo_zip = make_archive(self.nombreArchivo,'zip',self.direccionorigen)        
            self.enviomail(nombre,self.textofecha)
        else:
            showwarning(self.variablesdeTraduccion('self.tcarteltituloverifica2'),message=self.variablesdeTraduccion('self.tmensajenocluster')+" "+str(cluster))
        
          
        
    def enviomail(self,nombre,fecha):              
        self.username = "backup.dst.program@gmail.com"
        self.password= "rooxcilqkpxykwyc"
        self.destinatario= self.mi_modelo.lecturaDatos()
        self.asunto= self.variablesdeTraduccion('self.tenviomalasunto1') + " " +fecha +" "+ self.variablesdeTraduccion('self.tenviomalasunto2') +": "+ nombre
        
        self.mensaje= MIMEMultipart('alternative')
        self.mensaje['Subject']=self.asunto
        self.mensaje['From']=self.username
        self.mensaje['To']=self.destinatario    
  
        self.html='<p><strong>'+ self.variablesdeTraduccion('self.tenviomailcuerpo1') +':</strong></p><p>'+ self.variablesdeTraduccion('self.tenviomailcuerpo2') + '<strong> "' + str(nombre) + '" &nbsp;</strong>'+self.variablesdeTraduccion('self.tenviomailcuerpo3')+'<strong> "' + str(fecha) +'"</strong></p><p>&#128526;</p>'
        
        self.parte_html=MIMEText(self.html,'html')
        
        self.mensaje.attach(self.parte_html)
        
        self.archivoaenviar= nombre + "-"+self.textofecha + '.zip'
        
        self.mi_vista.deshabilitarAvisozip()
        self.mi_vista.avisoAdjuntando()
        
        
        with open(self.archivoaenviar,'rb')as self.adjunto:
            self.contenido_adjunto=MIMEBase('aplication', 'octet-strem',)
            self.contenido_adjunto.set_payload(self.adjunto.read())
        
        encoders.encode_base64(self.contenido_adjunto)

        paracodsiguiente='attachment;filename='+self.archivoaenviar
        self.contenido_adjunto.add_header('Content-Disposition',paracodsiguiente,)
        self.mensaje.attach(self.contenido_adjunto)  
        self.mensaje_final=self.mensaje.as_string()
        
        self.context= create_default_context()        
        
        self.mi_vista.deshabilitarAdjuntando()
        self.mi_vista.avisoEnviandoMail()
        
        with SMTP_SSL("smtp.gmail.com",465,context=self.context) as server:
            server.login(self.username,self.password)    
            server.sendmail(self.username,self.destinatario,self.mensaje_final)
        
        self.mi_vista.deshabilitarEnvidadoMail()
           
        showinfo(message=self.variablesdeTraduccion('self.tenvioCartel1')+ ": " + nombre, title=self.variablesdeTraduccion('self.tenvioCartel2')) 
        
        self.eliminaZip(self.archivoaenviar)   

    def eliminaZip(self,zip):
        try:
            remove(zip)            
        except:
            pass

    def seleccionaBandera(self):        
        self.banderaActiva=self.mi_modelo.lecturaIdioma()
        if self.banderaActiva=="esp":
            self.banderaPuesta='./banderas/esp.png'
        elif self.banderaActiva =="por":
            self.banderaPuesta='./banderas/por.jpg'
        elif self.banderaActiva =="uk":
            self.banderaPuesta='./banderas/uk.jpg'
        return self.banderaPuesta

    def variablesdeTraduccion(self,variable):
        self.variableencontrada=self.mi_vista.retornavariables(variable)
        return self.variableencontrada
    
    
    
    #____________________ Tiene que ver con la carga ____________________
    
    def buscarArchivoRestaura(self): 
        
        self.mi_vista.pasaAtrasCarga()     
        self.escritorio=get_desktop()
        self.archivoaGuardar=filedialog.askopenfilename(title=self.variablesdeTraduccion('self.tAbrir'),initialdir=self.escritorio,filetypes=(("zip files",".zip"), ("all files", "*.*")),)
        self.mi_vista.pasaAdelanteCarga()        
        self.mi_vista.seleccionDelArchivo(self.archivoaGuardar)
        self.mi_vista.eliminarBotonCargaBack()
        
        
    def remplazarMundo(self,valor):
        self.mi_vista.pasaAtrasCarga()

        self.numeroClusterElegido2=valor[8:9]
        
        self.acepta=askquestion(title=self.variablesdeTraduccion('self.tAlerta'),message=self.variablesdeTraduccion('self.tmensaje')+" " +str(valor) + "?")
        if self.acepta=="yes":
            self.direcciondeguardado=get_my_documents()        
            self.direcciondeguardado=self.direcciondeguardado+"\\Klei\\DoNotStarveTogether\\"+str(self.encuentraNumeroDirecctorio())+'\\Cluster_'+ str(self.numeroClusterElegido2)
            

            try:
                rmtree(self.direcciondeguardado)
            except:
                pass
            try:
                makedirs(self.direcciondeguardado)
            except FileExistsError:
                pass
    
            with ZipFile(self.archivoaGuardar, 'r') as zip_ref:
                zip_ref.extractall(self.direcciondeguardado)

            showinfo(message=self.variablesdeTraduccion('self.tmensajeConfirma'),title=self.variablesdeTraduccion('self.tenvioCartel2'))
            
            self.mi_vista.cancelar()
            self.mi_vista.eliminaCluster()
            self.mi_vista.cluster()
            self.mi_vista.destrozaCarga()

        else:
            self.mi_vista.cancelar()
            self.mi_vista.pasaAdelanteCarga()
            
        
    
        
    
        
    