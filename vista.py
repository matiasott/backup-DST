# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:06:31 2021

@author:
        name: Matias Ott,
        mail:matota@gmail.com,       
"""

from tkinter import PhotoImage, Tk, Label, Entry, Button, StringVar, Frame,Toplevel
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from webbrowser import open_new_tab
from PIL import Image,ImageTk


class Vista():
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = Tk()
        self.ventana.geometry('604x380')
        self.ventana.resizable(0,0)
        self.tVentanaPrincipal='BackUp - D.S.T.'
        self.ventana.title(self.tVentanaPrincipal)
        self.ventana.iconbitmap("./ico/icono.ico")
        self.imagenFondo=PhotoImage(file="./imagenes/fondo.png")              
        self.Fondo=Label(self.ventana,image=self.imagenFondo).place(x=0,y=0)
        self.imagenBaner=PhotoImage(file="./imagenes/Bannerprogrma.png")
        self.Baner=Label(self.ventana,image=self.imagenBaner).place(x=0,y=0)    
            
    def BotonInicioIngreso(self):
        self.frameBotonInicio=Frame(self.ventana,width=300,height='200')
        self.frameBotonInicio.place(x=182, y=180)
        self.frameBotonInicio.config(bg='black')
        
        self.botonIncio=Button(self.frameBotonInicio,text=self.tingreseBotonInicio,width=30,cursor="dot", command=self.registroMail)
        self.botonIncio.grid(row=0,column=0,padx=5,pady=2)
        self.botonIncio.config(background="black",fg="#799CAA",justify="center")        
    
    def eliminaBotonInicioIngreso(self):
        self.frameBotonInicio.destroy()
        self.ventana.update()
        
    def botonTraductor(self):
        self.frameBotonTRaductor =Frame(self.ventana,width=10,height='30')
        self.frameBotonTRaductor .place(x=30, y=340)
        self.frameBotonTRaductor .config(bg='black')
        
        self.imgBandera = Image.open(self.controlador.seleccionaBandera())
        self.imgBandera = self.imgBandera.resize((30,15), Image.ANTIALIAS) 
        self.imgBandera = ImageTk.PhotoImage(self.imgBandera)
        self.botonTraductoractivo =Button(self.frameBotonTRaductor, image=self.imgBandera, text="", compound="top",cursor="dot", command=self.Traductor)
        self.botonTraductoractivo.grid(row=0,column=1,padx=5,pady=2)   

    def eliminaBotonbotonTraductor(self):
        self.frameBotonTRaductor.destroy()
        self.ventana.update()

    def Traductor(self):
        
        self.controlador.traductoryRegistroIncial()
        
        self.ventana.update()
              
            
        self.frameTraductor=Frame(self.ventana,width=300,height='200')
        self.frameTraductor.place(x=210, y=180)
        self.frameTraductor.config(bg='black')
        
        self.labelSeleccioneIdioma=Label(self.frameTraductor,text=self.tseleccioneIdioma)
        self.labelSeleccioneIdioma.grid(row=0,column=0,padx=5,pady=2,columnspan=2)
        self.labelSeleccioneIdioma.config(background="black",fg="#799CAA",justify="center")
        
        self.esp = Image.open('./banderas/esp.png')
        self.esp = self.esp.resize((30,15), Image.ANTIALIAS) 
        self.esp = ImageTk.PhotoImage(self.esp)
        self.botonesp =Button(self.frameTraductor,image=self.esp, text="Español", compound="top",cursor="dot",background="black",fg="#799CAA", command=lambda:  self.controlador.idiomaactualiza("esp"))
        self.botonesp.grid(row=3,column=0,padx=2,pady=2)        
        
        self.por = Image.open('./banderas/por.jpg')
        self.por = self.por.resize((30,15), Image.ANTIALIAS) 
        self.por = ImageTk.PhotoImage(self.por)
        self.botonpor =Button(self.frameTraductor,image=self.por, text="Português", compound="top",cursor="dot",background="black",fg="#799CAA", command=lambda:  self.controlador.idiomaactualiza("por"))
        self.botonpor.grid(row=3,column=1,padx=2,pady=2)
        
        self.uk = Image.open('./banderas/uk.jpg')
        self.uk = self.uk.resize((30,15), Image.ANTIALIAS) 
        self.uk = ImageTk.PhotoImage(self.uk)
        self.botonuk =Button(self.frameTraductor,image=self.uk, text="English", compound="top",cursor="dot",background="black",fg="#799CAA", command=lambda:  self.controlador.idiomaactualiza("uk"))
        self.botonuk.grid(row=3,column=2,padx=2,pady=2)
    
    def eliminaTraductor(self):
        self.frameTraductor.destroy()
        self.ventana.update()
    
    def registroMail(self):
        
        
        self.controlador.traductoryRegistroIncial()
        
        self.ventana.update()
        
        self.ventanaCarga=Frame(self.ventana,width=300,height='200')
        self.ventanaCarga.place(x=80, y=100)
        self.ventanaCarga.config(bg='black')
        
        self.tituloMail=Label(self.ventanaCarga, text=self.tingreseMail)
        self.tituloMail.grid(row=0, column=0)
        self.tituloMail.config(background="black",fg="#799CAA",justify="center")
        
        self.correo_ingresado=StringVar()
        self.correo_confirmacion_ingresado=StringVar()        
        
        self.mail=Entry(self.ventanaCarga,textvariable=self.correo_ingresado,width=60,insertbackground="#799CAA")
        self.mail.grid(row=3,column=0,padx=5,pady=2)
        self.mail.config(background="black",fg="#799CAA",justify="right")        
        
        self.confirmacion_mail=Entry(self.ventanaCarga,textvariable=self.correo_confirmacion_ingresado,width=60,insertbackground="#799CAA")
        self.confirmacion_mail.grid(row=4,column=0,padx=5,pady=2)
        self.confirmacion_mail.config(background="black",fg="#799CAA",justify="right")
        
        self.confirma_mail=Button(self.ventanaCarga,text=self.tingreseBoton,width=60,cursor="dot", command=self.enpaquetaCorrreo)
        self.confirma_mail.grid(row=5,column=0,padx=5,pady=2)
        self.confirma_mail.config(background="black",fg="#799CAA",justify="right")
                
        try:
            self.cargadatosmail(self.mail)
            self.cargadatosmail(self.confirmacion_mail)
        except:
            pass
    
    def eliminaregistroMail(self):
        self.ventanaCarga.destroy()
        self.ventana.update()
    
    def enpaquetaCorrreo(self):
        self.op1=self.correo_ingresado.get()
        self.op2=self.correo_confirmacion_ingresado.get()
        self.controlador.verificaCorrreo(self.op1,self.op2)
        
    def cargaErrorStrimbarRegistroMail(self):
        self.valor=self.controlador.mail()
        if self.valor!="123":
            self.mail.delete(0,"end")
            self.confirmacion_mail.delete(0,"end")            
            self.mail.insert(0,self.valor)            
            self.confirmacion_mail.insert(0,self.valor) 
        
        
    def cargadatosmail(self,dato):
        self.valor=self.controlador.mail()
        if self.valor!="123":
            self.entrada=dato.insert(0,self.valor)    
        
    def botonEditarCorreoPagos(self):
        self.ventanaEdita=Frame(self.ventana,width=50,height='30')
        self.ventanaEdita.place(x=280, y=340)
        self.ventanaEdita.config(bg='black')
        
        self.cargaBackUp=Button(self.ventanaEdita,text=self.tbotonCargaMundo,width=13,cursor="dot", command=self.cargarBackUp) 
        self.cargaBackUp.grid(row=0,column=0,padx=5,pady=2)       
        self.cargaBackUp.config(background="black",fg="#799CAA",justify="right")
        
        self.editar=Button(self.ventanaEdita,text=self.teditarCorreo,width=13,cursor="dot", command=self.registroMail) 
        self.editar.grid(row=0,column=1,padx=5,pady=2)       
        self.editar.config(background="black",fg="#799CAA",justify="right")
        
        self.imgp = Image.open('./imagenespago/paypal.png')
        self.imgp = self.imgp.resize((15,15), Image.ANTIALIAS) 
        self.imgp = ImageTk.PhotoImage(self.imgp)
        self.botonNuevop =Button(self.ventanaEdita, image=self.imgp, text="", compound="top",cursor="dot", command=self.paypal)
        self.botonNuevop.grid(row=0,column=2,padx=5,pady=2)
        
        self.imgm = Image.open('./imagenespago/logomercadopago.png')
        self.imgm = self.imgm.resize((15,15), Image.ANTIALIAS) 
        self.imgm = ImageTk.PhotoImage(self.imgm)
        self.botonNuevomer =Button(self.ventanaEdita, image=self.imgm, text="", compound="top",cursor="dot", command=self.mercadoPago)
        self.botonNuevomer.grid(row=0,column=3,padx=5,pady=2)
        
        self.linkcafecito="https://cafecito.app/matota"
        self.imgcafe = Image.open('./imagenespago/cafecito.png')
        self.imgcafe = self.imgcafe.resize((15,15), Image.ANTIALIAS) 
        self.imgcafe = ImageTk.PhotoImage(self.imgcafe)
        self.botoncafe =Button(self.ventanaEdita, image=self.imgcafe, text="",fg="#799CAA", compound="top",cursor="dot", command=lambda:  self.OpenUrl(self.linkcafecito))
        self.botoncafe.grid(row=0,column=4,padx=5,pady=2)
        
    def eliminabotonEditarCorreoPagos(self):
        self.ventanaEdita.destroy()
        self.ventana.update()
    
    def botonCreditos(self): 
           
        self.ventanaFcredito=Frame(self.ventana,width=10,height='30')
        self.ventanaFcredito.place(x=530, y=10)
        self.ventanaFcredito.config(bg='black')
        
        self.botoncredito=Button(self.ventanaFcredito,text=self.tCreditos,width=7,cursor="dot", command=self.credito) 
        self.botoncredito.grid(row=0,column=1,padx=5,pady=2)       
        self.botoncredito.config(background="black",fg="#799CAA",justify="right")
        
    def eliminabotonCreditos(self):
        self.ventanaFcredito.destroy()       
        self.ventana.update()
    
    def cluster(self):
        self.ventana.update()
        
        self.ventanaCluster=Frame(self.ventana,width=300,height='200')
        self.ventanaCluster.place(x=180, y=100)
        self.ventanaCluster.config(bg='black',relief="groove")       
        
        self.nombre1=self.controlador.nombresCluster(1)
        self.cluster1=Label(self.ventanaCluster,text="Cluster 1\n"+self.ticluidoenCluster + ": "+ self.nombre1)
        self.cluster1.grid(row=0,column=0,padx=5,pady=2,sticky="W")
        self.cluster1.config(background="black",fg="#799CAA",justify="left")

        self.Back1=Button(self.ventanaCluster,text='BackUp',width=10,cursor="dot",command=lambda: self.controlador.zip(1,self.nombre1))
        self.Back1.grid(row=0,column=1,padx=5,pady=2)
        self.Back1.config(background="black",fg="#799CAA",justify="left")       
        
        self.nombre2=self.controlador.nombresCluster(2)
        self.cluster2=Label(self.ventanaCluster,text="Cluster 2\n"+self.ticluidoenCluster + ": "+ self.nombre2)
        self.cluster2.grid(row=1,column=0,padx=5,pady=2,sticky="W")
        self.cluster2.config(background="black",fg="#799CAA",justify="left")

        self.Back2=Button(self.ventanaCluster,text='BackUp',width=10,cursor="dot",command=lambda: self.controlador.zip(2,self.nombre2))
        self.Back2.grid(row=1,column=1,padx=5,pady=2,sticky="W")
        self.Back2.config(background="black",fg="#799CAA",justify="left")
        
        self.nombre3=self.controlador.nombresCluster(3)
        self.cluster3=Label(self.ventanaCluster,text="Cluster 3\n"+self.ticluidoenCluster + ": " + self.nombre3)
        self.cluster3.grid(row=2,column=0,padx=5,pady=2,sticky="W")
        self.cluster3.config(background="black",fg="#799CAA",justify="left")

        self.Back3=Button(self.ventanaCluster,text='BackUp',width=10,cursor="dot",command=lambda: self.controlador.zip(3,self.nombre3))
        self.Back3.grid(row=2,column=1,padx=5,pady=2,sticky="W")
        self.Back3.config(background="black",fg="#799CAA",justify="left")
        
        self.nombre4=self.controlador.nombresCluster(4)
        self.cluster4=Label(self.ventanaCluster,text="Cluster 4\n"+self.ticluidoenCluster + ": "+ self.nombre4)
        self.cluster4.grid(row=3,column=0,padx=5,pady=2,sticky="W")
        self.cluster4.config(background="black",fg="#799CAA",justify="left")

        self.Back4=Button(self.ventanaCluster,text='BackUp',width=10,cursor="dot",command=lambda: self.controlador.zip(4,self.nombre4))
        self.Back4.grid(row=3,column=1,padx=5,pady=2)
        self.Back4.config(background="black",fg="#799CAA",justify="left")
        
        self.nombre5=self.controlador.nombresCluster(5)
        self.cluster5=Label(self.ventanaCluster,text="Cluster 5\n"+self.ticluidoenCluster + ": "+ self.nombre5)
        self.cluster5.grid(row=4,column=0,padx=5,pady=2,sticky="W")
        self.cluster5.config(background="black",fg="#799CAA",justify="left")

        self.Back5=Button(self.ventanaCluster,text='BackUp',width=10,cursor="dot",command=lambda: self.controlador.zip(5,self.nombre5))
        self.Back5.grid(row=4,column=1,padx=5,pady=2)
        self.Back5.config(background="black",fg="#799CAA",justify="left")
    
    
    def eliminaCluster(self):   
        self.ventanaCluster.destroy()       
        self.ventana.update()
        
    def avisozip(self):        
        self.ventanaAviso=Frame(self.ventana,width=50,height='30')
        self.ventanaAviso.place(x=80, y=342)
        self.ventanaAviso.config(bg='black')
        
        self.zip=Label(self.ventanaAviso, text=self.tavisoZip)
        self.zip.grid(row=0, column=0)
        self.zip.config(background="black",fg="#799CAA",justify="left")        
        
        self.ventana.update()    
    
    def deshabilitarAvisozip(self):     
        self.ventanaAviso.destroy()
        self.ventana.update() 
        
    def avisoAdjuntando(self):
        self.enviandoAdjunto=Frame(self.ventana,width=50,height='30')
        self.enviandoAdjunto.place(x=80, y=342)
        self.enviandoAdjunto.config(bg='black')
        
        self.adjunto=Label(self.enviandoAdjunto, text=self.tavisoAdjunto)
        self.adjunto.grid(row=0, column=0)
        self.adjunto.config(background="black",fg="#799CAA",justify="left")
        
        self.ventana.update()        
    
    def deshabilitarAdjuntando(self):        
        self.enviandoAdjunto.destroy()
        self.ventana.update()
        
    def avisoEnviandoMail(self):
        self.enviandoMail=Frame(self.ventana,width=50,height='30')
        self.enviandoMail.place(x=80, y=342)
        self.enviandoMail.config(bg='black')
        
        self.enviado=Label(self.enviandoMail, text=self.tavisoEnviadoMail)
        self.enviado.grid(row=0, column=0)
        self.enviado.config(background="black",fg="#799CAA",justify="left") 
        
        self.ventana.update()      
    
    def deshabilitarEnvidadoMail(self):        
        self.enviandoMail.destroy()
        self.ventana.update()    
       
        
        
    def espanol(self):        
        self.tVentanaPrincipal='Backup de Tus Mundos'
        self.teditarCorreo='Editar su Email'
        self.tCreditos='Créditos'
        self.tingreseMail='Ingrese su Email y Verifique:'
        self.tingreseBoton='Ingrese'
        self.tingreseBotonInicio='Ingrese su Email'
        self.tseleccioneIdioma='Seleccione el Idioma'
        self.ticluidoenCluster='Nombre'
        self.tavisoZip='Comprimiendo el archivo'
        self.tavisoAdjunto='Adjuntando archivo'
        self.tavisoEnviadoMail='Enviando Email'
        self.tpaypal='Gracias por su colaboración'
        self.tpaypalIralLink='Ir al Link'
        self.tpaypalQR='Escanee el código'
        self.tCreditos='Créditos'
        self.tcreditosParrafo1='Autor'
        self.tcreditosParrafo2='Colaborador'
        self.tcarteltituloverifica='ERROR'
        self.tcartelparrafoverifica='Re Ingrese su email, ambos deben ser iguales'
        self.tcarteltituloverifica2='ERROR'
        self.tcartelparrafoverifica2='Ingrese un email valido'
        self.tnombrecluster='No se ha generado'
        self.tenviomalasunto1='Backup al día'
        self.tenviomalasunto2='del mundo'
        self.tenviomailcuerpo1='Hola Gamer'
        self.tenviomailcuerpo2='Esta es la última actualización del mundo'
        self.tenviomailcuerpo3='realizada el dia'
        self.tenvioCartel1='Se ha enviado el archivo a tu email'
        self.tenvioCartel2='Genial'
        
        
        self.ttraductor1='Traducción al portugués'
        self.ttraductor2='Traducción al inglés'
        
        self.tmensajenocluster='No existe un mundo creado para este Cluster'

        #todo lo que tiene que ver con carga de archivos
        self.tbotonCargaMundo='Restaurar Mundo'
        self.tSubirArchivo='Seleccione el Archivo .zip'
        self.tCancelar='Cancelar'
        self.tSeleccionMundo='Seleccione Mundo a Remplazar'
        self.tSeleccionArchivoMensaje='Archivo Seleccionado'
        self.tMundoRemplazar='Mundo a remplazar'
        self.tGuardar='Guardar'

        self.tAbrir='Abrir'
        self.tAlerta='Alerta'
        self.tmensaje='¿Esta seguro que quiere remplazar el'
        self.tmensajeConfirma='Se han remplazado los archivos'
        self.tdebeseleccionarunmundo='Debe seleccionar un mundo'
        
        

        self.ventana.update()
        
    def portuguez(self):
        self.tVentanaPrincipal='Backup de Teus Mundos'
        self.teditarCorreo='Edite seu Email'
        self.tCreditos='Créditos'
        self.tingreseMail='Digite seu Email e Verifique:'
        self.tingreseBoton='Ingresse'
        self.tingreseBotonInicio='Digite seu Email'
        self.tseleccioneIdioma='Selecione o Idioma'
        self.ticluidoenCluster='Nome'
        self.tavisoZip='Comprimindo o arquivo'
        self.tavisoAdjunto='Anexando arquivo'
        self.tavisoEnviadoMail='Enviando Email'
        self.tpaypal='Obrigado pela sua cooperação'
        self.tpaypalIralLink='Ir para o Link'
        self.tpaypalQR='Digitalize o código'
        self.tCreditos='Créditos'
        self.tcreditosParrafo1='Autor'
        self.tcreditosParrafo2='Colaborador'
        self.tcarteltituloverifica='ERRO'
        self.tcartelparrafoverifica='Digite novamente seu email, ambos têm que ser iguais'
        self.tcarteltituloverifica2='ERRO'
        self.tcartelparrafoverifica2='Ingresse com um email válido'
        self.tnombrecluster='Não foi gerado'
        self.tenviomalasunto1='Backup do dia'
        self.tenviomalasunto2='do mundo'
        self.tenviomailcuerpo1='Olá Gamer.'
        self.tenviomailcuerpo2='Esta é a última atualização do mundo'
        self.tenviomailcuerpo3='realizada o dia'
        self.tenvioCartel1='O arquivo foi enviado para o seu email'
        self.tenvioCartel2='Legal'
        
        self.ttraductor1='Tradução ao português'
        self.ttraductor2='Tradução ao inglês'
        
        self.tmensajenocluster='Não existe mundo criado para esse cluster'
        
        
        #todo lo que tiene que ver con carga de archivos
        self.tbotonCargaMundo='Restaurar Mundo'
        self.tSubirArchivo='Selecione o arquivo .zip'
        self.tCancelar='Cancelar'
        self.tSeleccionMundo='Selecione o Mundo a Substituir'
        self.tSeleccionArchivoMensaje='Arquivo Selecionado'
        self.tMundoRemplazar='Mundo para substituir'
        self.tGuardar='Guardar'

        self.tAbrir='Abrir'
        self.tAlerta='Alerta'
        self.tmensaje='Tem certeza que quer substituir o'
        self.tmensajeConfirma='Os arquivos foram substituídos'
        self.tdebeseleccionarunmundo='Você deve selecionar um mundo'
        
        
        
        self.ventana.update()
    
    def ingles(self):
        self.tVentanaPrincipal='Backup of Your Worlds'
        self.teditarCorreo='Edit your Email'
        self.tCreditos='Credits'
        self.tingreseMail='Enter your Email and Verify:'
        self.tingreseBoton='Enter'
        self.tingreseBotonInicio='Enter your Email'
        self.tseleccioneIdioma='Select the language'
        self.ticluidoenCluster='Name'
        self.tavisoZip='Compressing file'
        self.tavisoAdjunto='Attaching file'
        self.tavisoEnviadoMail='Sending email'
        self.tpaypal='Thank you for your cooperation'
        self.tpaypalIralLink='Go to the Link'
        self.tpaypalQR='Scan the code'
        self.tCreditos='Credits'
        self.tcreditosParrafo1='Author'
        self.tcreditosParrafo2='Collaborator'
        self.tcarteltituloverifica='ERROR'
        self.tcartelparrafoverifica='Re enter your email, both  must be the same'
        self.tcarteltituloverifica2='ERROR'
        self.tcartelparrafoverifica2='Enter a valid email'
        self.tnombrecluster='Has not been generated'
        self.tenviomalasunto1='Backup of the day'
        self.tenviomalasunto2='of the world'
        self.tenviomailcuerpo1='Hello, Gamer'
        self.tenviomailcuerpo2='This is the last update of the world'
        self.tenviomailcuerpo3='made the day'
        self.tenvioCartel1='The file has been sent to your email'
        self.tenvioCartel2='Cool'
        
        self.ttraductor1='Translation to portuguese'
        self.ttraductor2='Translation to english'
        
        self.tmensajenocluster='There is no created world for the cluster'
        
        
        #todo lo que tiene que ver con carga de archivos
        self.tbotonCargaMundo='Restore World'
        self.tSubirArchivo='Select the .zip file'
        self.tCancelar='Cancel'
        self.tSeleccionMundo='Select World to Replace'
        self.tSeleccionArchivoMensaje='Selected File'
        self.tMundoRemplazar='World to replace'
        self.tGuardar='Save'

        self.tAbrir='Open'
        self.tAlerta='Alert'
        self.tmensaje='Are you sure you want to replace the'
        self.tmensajeConfirma='The files have been replaced'
        self.tdebeseleccionarunmundo='You must select a world'
        
        
        
        
        self.ventana.update()

    def retornavariables(self,variable):
        self.diccionarioVariables={
            'self.tcarteltituloverifica':self.tcarteltituloverifica,
            'self.tcartelparrafoverifica':self.tcartelparrafoverifica,
            'self.tcarteltituloverifica2':self.tcarteltituloverifica2,
            'self.tcartelparrafoverifica2':self.tcartelparrafoverifica2,
            'self.tnombrecluster':self.tnombrecluster,
            'self.tenviomalasunto1':self.tenviomalasunto1,
            'self.tenviomalasunto2':self.tenviomalasunto2,
            'self.tenviomailcuerpo1':self.tenviomailcuerpo1,
            'self.tenviomailcuerpo2':self.tenviomailcuerpo2,
            'self.tenviomailcuerpo3':self.tenviomailcuerpo3,
            'self.tenvioCartel1':self.tenvioCartel1,
            'self.tenvioCartel2':self.tenvioCartel2,
            'self.tmensajenocluster':self.tmensajenocluster,
            'self.tAbrir':self.tAbrir,
            'self.tAlerta':self.tAlerta,
            'self.tmensaje':self.tmensaje,
            'self.tmensajeConfirma':self.tmensajeConfirma   
        }
        
        self.valorS=self.diccionarioVariables[variable]
        
        return self.valorS
    
    
    def credito(self):
        self.ventanacredito=Toplevel()
        self.ventanacredito.config(bg="black")
        self.ventanacredito.geometry('604x342')
        self.ventanacredito.resizable(0,0)
        self.ventanacredito.title(self.tCreditos)
        self.ventanacredito.iconbitmap("./ico/icono.ico")        
        self.imagenFondocredito=PhotoImage(file="./imagenes/imagenCredito.png")
        self.Fondocredito=Label(self.ventanacredito,image=self.imagenFondocredito).place(x=0,y=0)
        self.ventanacredito.attributes('-topmost', True)
        
        
        self.ventanacreditoslabel=Frame(self.ventanacredito,width=26,height='30')
        self.ventanacreditoslabel.place(x=10, y=50)
        self.ventanacreditoslabel.config(bg="black",background=('#33594C'))
             
        
        self.titulocedritoLabel=Label(self.ventanacreditoslabel, text=self.tCreditos)
        self.titulocedritoLabel.grid(row=0, column=0,padx=5,pady=2)
        self.titulocedritoLabel.config(background="#33594C",fg="black",justify="left",)
        
        self.cedritoLabel=Label(self.ventanacreditoslabel, text=self.tcreditosParrafo1+": \nMatias Ott\nEmail: matota@gmail.com\nArgentina\n\n"+self.tcreditosParrafo2+": \nAdrian Orellano\nCorreo: adrorellano@gmail.com\n\n"+self.ttraductor1+":\nAgustin Cortelezzi\n\n"+self.ttraductor2+":\nAgustin Cortelezzi\nEmail: agustin.cortelezzi@gmail.com",width=26)
        self.cedritoLabel.grid(row=2, column=0,padx=5,pady=2,sticky="W",ipadx=12)
        self.cedritoLabel.config(background="black",fg="#799CAA",justify="left")
        
        self.ventanacredito.mainloop()  
    
    def paypal(self):            
        self.ventanaInfo =Toplevel()
        self.ventanaInfo.geometry('604x380')
        self.ventanaInfo.resizable(0,0)
        self.ventanaInfo.title("PayPal")
        self.ventanaInfo.iconbitmap("./ico/icono.ico")
        self.imagenFondoInfo=PhotoImage(file="./imagenes/fondoInfo.png")              
        self.FondoInfo=Label(self.ventanaInfo,image=self.imagenFondoInfo).place(x=0,y=0)
        self.ventanaInfo.attributes('-topmost', True)
        
        self.ventanaTextoInfo=Frame(self.ventanaInfo,width=300,height='30')
        self.ventanaTextoInfo.place(x=200, y=120)
        self.ventanaTextoInfo.config(bg='black')
        
        self.tituloInfo=Label(self.ventanaTextoInfo, text=self.tpaypal)
        self.tituloInfo.grid(row=0, column=0,columnspan=2,padx=4,pady=3)
        self.tituloInfo.config(font=14,background="black",fg="#799CAA",justify="center")
        
        self.linkpaypal="https://www.paypal.com/donate/?hosted_button_id=ZJPMUFCGLXUHL"
        self.img = Image.open('./imagenespago/paypal.png')
        self.img = self.img.resize((50,40), Image.ANTIALIAS) 
        self.img = ImageTk.PhotoImage(self.img)
        self.botonNuevo1 =Button(self.ventanaTextoInfo, image=self.img, text=self.tpaypalIralLink,fg="black", compound="top",cursor="dot",background="white",justify="center", command=lambda:  self.OpenUrl(self.linkpaypal))
        self.botonNuevo1.grid(row=3,column=0,padx=4,pady=3)
        
        self.qrpaypal = Image.open("./imagenespago/CódigoQRpaypal.png")
        self.qrpaypal = self.qrpaypal.resize((100,100), Image.ANTIALIAS)
        self.qrpaypal = ImageTk.PhotoImage(self.qrpaypal) 
        self.qrlabelpaypal=Label(self.ventanaTextoInfo,image=self.qrpaypal,text=self.tpaypalQR,fg="black", compound="top",background="white",justify="center")
        self.qrlabelpaypal.grid(row=3,column=1,padx=4,pady=5)    
        
        self.ventanaInfo.mainloop()
    
    def mercadoPago(self):            
        self.ventanamercado =Toplevel()
        self.ventanamercado.geometry('604x380')
        self.ventanamercado.resizable(0,0)
        self.ventanamercado.title("PayPal")
        self.ventanamercado.iconbitmap("./ico/icono.ico")
        self.imagenFondoInfo=PhotoImage(file="./imagenes/fondoInfo.png")              
        self.FondoInfo=Label(self.ventanamercado,image=self.imagenFondoInfo).place(x=0,y=0)
        self.ventanamercado.attributes('-topmost', True)
        
        self.ventanaTextoMercado=Frame(self.ventanamercado,width=300,height='30')
        self.ventanaTextoMercado.place(x=180, y=120)
        self.ventanaTextoMercado.config(bg='black')
        
        self.tituloInfo=Label(self.ventanaTextoMercado, text=self.tpaypal)
        self.tituloInfo.grid(row=0, column=0,columnspan=3,padx=4,pady=3)
        self.tituloInfo.config(font=12,background="black",fg="#799CAA",justify="center")
        
        self.link300M="https://mpago.la/1unpfL6"
        
        self.link500M="https://mpago.la/1WAKtf8"
        
        self.link1000M="https://mpago.la/2ohaLYR"       
        
        
        self.img300 = Image.open('./imagenespago/logomercadopago.png')
        self.img300 = self.img300.resize((50,40), Image.ANTIALIAS) 
        self.img300 = ImageTk.PhotoImage(self.img300)
        self.botonNuevo300 =Button(self.ventanaTextoMercado, image=self.img300, text="",fg="#799CAA", compound="top",cursor="dot",background="white",justify="center", command=lambda:  self.OpenUrl(self.link300M))
        self.botonNuevo300.grid(row=3,column=0,padx=4,pady=1)
        
        self.tituloInfo300=Label(self.ventanaTextoMercado, text="$AR300")
        self.tituloInfo300.grid(row=4,column=0,padx=4,pady=1)
        self.tituloInfo300.config(font=14,background="black",fg="#799CAA",justify="center")
        
        
        self.img500 = Image.open('./imagenespago/logomercadopago.png')
        self.img500 = self.img500.resize((50,40), Image.ANTIALIAS) 
        self.img500 = ImageTk.PhotoImage(self.img500)
        self.botonNuevo500 =Button(self.ventanaTextoMercado, image=self.img500, text="",fg="#799CAA", compound="top",cursor="dot",background="white",justify="center", command=lambda:  self.OpenUrl(self.link500M))
        self.botonNuevo500.grid(row=3,column=1,padx=4,pady=1)
        
        self.tituloInfo500=Label(self.ventanaTextoMercado, text="$AR500")
        self.tituloInfo500.grid(row=4,column=1,padx=4,pady=1)
        self.tituloInfo500.config(font=14,background="black",fg="#799CAA",justify="center")
        
        
        self.img1000 = Image.open('./imagenespago/logomercadopago.png')
        self.img1000 = self.img1000.resize((50,40), Image.ANTIALIAS) 
        self.img1000 = ImageTk.PhotoImage(self.img1000)
        self.botonNuevo1000 =Button(self.ventanaTextoMercado, image=self.img1000, text="",fg="#799CAA", compound="top",cursor="dot",background="white",justify="center", command=lambda:  self.OpenUrl(self.link1000M))
        self.botonNuevo1000.grid(row=3,column=2,padx=4,pady=1)
        
        self.tituloInfo1000=Label(self.ventanaTextoMercado, text="$AR1000")
        self.tituloInfo1000.grid(row=4,column=2,padx=4,pady=1)
        self.tituloInfo1000.config(font=14,background="black",fg="#799CAA",justify="center")
        
        
        
        self.ventanamercado.mainloop() 
        
    def OpenUrl(self,url):        
        open_new_tab(url)     
        
    def main_loop(self):        
        self.ventana.mainloop()
        
        
    
    
    
    #____________________ Tiene que ver con la carga ____________________
    
    
    
    def cargarBackUp(self):
        self.ventanacargaArcchivo =Toplevel()
        self.ventanacargaArcchivo.geometry('604x380')
        self.ventanacargaArcchivo.resizable(0,0)
        self.ventanacargaArcchivo.title("PayPal")
        self.ventanacargaArcchivo.iconbitmap("./ico/icono.ico")
        self.imagenFondoInfo3=PhotoImage(file="./imagenes/imagencarga.png")              
        self.FondoInfo=Label(self.ventanacargaArcchivo,image=self.imagenFondoInfo3).place(x=0,y=0)
        self.pasaAdelanteCarga()
        
        self.botonsubirBack()
        self.botonCancelar()
    
    def destrozaCarga(self):
        self.ventanacargaArcchivo.destroy()    

        self.ventanacargaArcchivo.mainloop()
    def pasaAtrasCarga(self):
        self.ventanacargaArcchivo.attributes('-topmost', False)
        
    def pasaAdelanteCarga(self):
        self.ventanacargaArcchivo.attributes('-topmost', True)   
        
    def botonsubirBack(self):
        self.frameBack=Frame(self.ventanacargaArcchivo,width=300,height='30')
        self.frameBack.place(x=200, y=30)
        self.frameBack.config(bg='black')
 
        self.botonIncio=Button(self.frameBack,text=self.tSubirArchivo,width=30,cursor="dot", command=self.controlador.buscarArchivoRestaura)
        self.botonIncio.grid(row=0,column=0,padx=5,pady=2)
        self.botonIncio.config(background="black",fg="#799CAA",justify="center")   
    
    def eliminarBotonCargaBack(self):
        self.frameBack.destroy()
        self.ventanacargaArcchivo.update()
    
    def seleccionDelArchivo(self,valor):
        if valor=="":
            self.botonsubirBack()
            self.botonCancelar()
        else:
            self.cajaMundosSelecciona()
            self.frameSeleccionArchi=Frame(self.ventanacargaArcchivo,width=10,height='10')
            self.frameSeleccionArchi.place(x=3, y=320)
            self.frameSeleccionArchi.config(bg='black')
            
            

            self.tituloInfo=Label(self.frameSeleccionArchi, text=self.tSeleccionArchivoMensaje+":\n" + valor,font=4)
            self.tituloInfo.grid(row=0, column=0,columnspan=2,padx=4,pady=3)
            self.tituloInfo.config(background="black",fg="#799CAA",justify="left")
    
    def eliminaseleccionDelArchivo(self):
        self.frameSeleccionArchi.destroy()
        self.ventanacargaArcchivo.update()
    
    def cajaMundosSelecciona(self):
        
        self.frameBack2=Frame(self.ventanacargaArcchivo,width=300,height='10')
        self.frameBack2.place(x=200, y=25)
        self.frameBack2.config(bg='black')
    
        self.valuesCluster=["Cluster 1 - "+ self.controlador.nombresCluster(1),"Cluster 2 - "+ self.controlador.nombresCluster(2),"Cluster 3 - "+ self.controlador.nombresCluster(3),"Cluster 4 - "+ self.controlador.nombresCluster(4),"Cluster 5 - "+ self.controlador.nombresCluster(5)]
        
        self.eleccionDeCluster=Combobox(self.frameBack2,values=self.valuesCluster,background="black",font="black")
        self.eleccionDeCluster.grid(row=3,column=0,padx=5,pady=2)
        
        self.botonIncio=Button(self.frameBack2,text=self.tSeleccionMundo,width=30,cursor="dot", command=lambda: self.seleccionaMundoBack(self.eleccionDeCluster))
        self.botonIncio.grid(row=4,column=0,padx=5,pady=2)
        self.botonIncio.config(background="black",fg="#799CAA",justify="center")
    
    def eliminacajaMundosSelecciona(self):
        self.frameBack2.destroy()
        self.ventanacargaArcchivo.update()
    
    
    def seleccionaMundoBack(self,valor):
        
        self.mundo=valor.get()
        
        if self.mundo!="":         
      
            self.eliminacajaMundosSelecciona()
            self.botonGuardar(self.mundo)        
            
            
            self.frameSeleccionArchi2=Frame(self.ventanacargaArcchivo,width=10,height='10')
            self.frameSeleccionArchi2.place(x=3, y=280)
            self.frameSeleccionArchi2.config(bg='black')  

            self.tituloInfo=Label(self.frameSeleccionArchi2, text=self.tMundoRemplazar+":\n" + self.mundo,font=4)
            self.tituloInfo.grid(row=0, column=0,columnspan=2,padx=4,pady=3)
            self.tituloInfo.config(background="black",fg="#799CAA",justify="left")
            
        else:
            showinfo(self.tcarteltituloverifica2,message=self.tdebeseleccionarunmundo)
            
            
    
    def eliminaseleccionaMundoBack(self):
        self.frameSeleccionArchi2.destroy()
        self.ventanacargaArcchivo.update()
    
    def botonGuardar(self,mundo):
        
        self.frameGuardar=Frame(self.ventanacargaArcchivo,width=10,height='10')
        self.frameGuardar.place(x=200, y=30)
        self.frameGuardar.config(bg='black') 
        
        self.botonIncio=Button(self.frameGuardar,text=self.tGuardar,width=30,cursor="dot", command=lambda: self.controlador.remplazarMundo(mundo))
        self.botonIncio.grid(row=4,column=0,padx=5,pady=2)
        self.botonIncio.config(background="black",fg="#799CAA",justify="center")
        
    def eliminarbotonGuardar(self):
        self.frameGuardar.destroy()
        self.ventanacargaArcchivo.update()
            
       
    def botonCancelar(self):
                
        self.frameCancelar=Frame(self.ventanacargaArcchivo,width=10,height='10')
        self.frameCancelar.place(x=500, y=340)
        self.frameCancelar.config(bg='black') 
        
        self.botonIncio=Button(self.frameCancelar,text=self.tCancelar,width=10,cursor="dot", command=self.cancelar)
        self.botonIncio.grid(row=0,column=0,padx=5,pady=2)
        self.botonIncio.config(background="black",fg="#799CAA",justify="center")
        
    def cancelar(self):
        try:
            self.eliminarBotonCargaBack()            
        except:
            pass
        try:
            self.eliminaseleccionDelArchivo()            
        except:
            pass
        try:
            self.eliminacajaMundosSelecciona()           
        except:
            pass
        try:
            self.eliminaseleccionaMundoBack()           
        except:
            pass
        try:
             self.eliminarbotonGuardar()          
        except:
            pass
        
        self.botonsubirBack()
      
        
        
        
        
    