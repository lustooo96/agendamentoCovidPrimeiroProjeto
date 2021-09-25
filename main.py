from os import close
from PyQt5 import uic,QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

cpff = 0



#---------------------------------------------------------------------FUNÇÕES QUE ABREM TELA A PARTIR DE OUTRA E FECHAM ESSAS TELAS -----------------------------------------------
def chama_tela_login():
    tela_login.show()
    tela_login.Push_Registrar.clicked.connect(chama_tela_cadastro)
    tela_login.Push_Registrar.clicked.connect(tela_login.close)
    tela_login.Push_Registrar.clicked.connect(limpar_tela_login)
    tela_login.Push_Voltar.clicked.connect(chama_tela_inicial)
    tela_login.Push_Voltar.clicked.connect(tela_login.close)
    tela_login.Push_Voltar.clicked.connect(limpar_tela_login)
    tela_login.Push_Logar.clicked.connect(entra_db_tela_agendamento)
#---------------------------------------------------------------------
    
#ESSA FUNÇÃO CHAMA A TELA DE AGENDAR A VACINAÇÃO DO COVID   
def chama_tela_agendamento():
    tela_agendamento.show()
    tela_agendamento.pushButton.clicked.connect(chama_tela_menu_agendamento)
    tela_agendamento.pushButton.clicked.connect(tela_agendamento.close)
    tela_agendamento.pushButton_2.clicked.connect(salva_db_agendamento)
#---------------------------------------------------------------------  
    

#ESSA FUNÇÃO CHAMA A PRIMEIRA TELA.A TELA INIAL QUE VAI ESCOLHAR SE VAI PARA A TELA DE LOGIN OU CADASTRO
def chama_tela_inicial():
    tela_inicial.show()
#---------------------------------------------------------------------


#ESSA FUNÇÃO SERVE PARA CHAMAR A TELA DE SELECIONAR O AGENDAMENTO E TAMBEM É O MENU PRINCIPAL
def chama_tela_menu_agendamento():
    tela_menu_agendamento.show()
    tela_menu_agendamento.pushButton.clicked.connect(consulta_db_nome_usuario)
    tela_menu_agendamento.pushButton_logout.clicked.connect(chama_tela_login)
    tela_menu_agendamento.pushButton_logout.clicked.connect(tela_menu_agendamento.close)
    tela_menu_agendamento.pushButton_agendamento.clicked.connect(chama_tela_agendamento)
    tela_menu_agendamento.pushButton_agendamento.clicked.connect(tela_menu_agendamento.close)
   
#---------------------------------------------------------------------    


#ESSA FUNÇÃO SERVE PARA CHAMAR A TELA DE CADASTRO
def chama_tela_cadastro():
    tela_cadastro.show()
    tela_cadastro.pushButton_3.clicked.connect(salva_db_cadastro)

    tela_cadastro.pushButton_2.clicked.connect(tela_cadastro.close)
    tela_cadastro.pushButton_2.clicked.connect(chama_tela_inicial)
    tela_cadastro.pushButton_2.clicked.connect(limpar_tela_cadastro)
#---------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------------------------












#-----------------------------------------------------------------FUNÇÕES QUE FAZEM AS INTERAÇÕES COM O BANCO DE DADOS E ARMAZENA DADOS DOS USUARIO---------

#ESSA FUNÇÃO CRIA O CADASTRO DO USUARIO 
def salva_db_cadastro():
    nome = tela_cadastro.lineEdit_3.text()
    data = tela_cadastro.lineEdit_4.text()
    cpf = tela_cadastro.lineEdit.text()
    if tela_cadastro.radioButton_2.isChecked():
        sexo = tela_cadastro.radioButton_2.text()

    elif tela_cadastro.radioButton.isChecked():
        sexo = tela_cadastro.radioButton.text()

    elif tela_cadastro.radioButton_3.isChecked():
        sexo = tela_cadastro.radioButton_3.text()
    
    
    try :
        db = sqlite3.connect('Banco_cadastro.db')
        exe = db.cursor()
        if(nome != "" and data != "" and cpf != "" and len(cpf) > 10 and len(data) > 7 and sexo != ""):
            exe.execute("CREATE TABLE IF NOT EXISTS cadastro (usuario text , data date,cpf text ,sexo text)")
            exe.execute("INSERT INTO cadastro VALUES ('"+nome+"' , '"+data+"' , '"+cpf+"' , '"+sexo+"' ) ")
            print(sexo)
            QMessageBox.about(tela_cadastro,"Cadastro" ,"Cadastrado com sucesso")
        else :
            if (len(cpf) < 11 ):
                QMessageBox.about(tela_cadastro,"ERRO-CADASTRO" , "CPF INVALIDO")
            elif (len(data) < 8):
                QMessageBox.about(tela_cadastro,"ERRO-CADASTRO" , "DATA INVALIDA")
            else :
                QMessageBox.about(tela_cadastro,"ERRO-CADASTRO" , "DATA E CPF INVALIDO") 
            
        db.commit()
        db.close()
        tela_cadastro.lineEdit_3.setText("")
        tela_cadastro.lineEdit_4.setText("")
        tela_cadastro.lineEdit.setText("")    

        
    except sqlite3.Error as erro:
        print("erro ao inserir os dados",erro)
#----------------------------------------------------------------------------------------

#ESSA FUNÇÃO CONSULTA SE A PESSOA LOGADA TEM UM AGENDAMENTO E SE TIVER MOSTRA A ELA.
def consulta_db_nome_usuario():


    banco = sqlite3.connect('Banco_cadastro.db')
    exe = banco.cursor()
    try :
        exe.execute("select cpf_agendamento , estado , cidade , endereco , data_completa from cadastro_agendamento where cpf_agendamento = '"+cpff+"'  ")
        recebe = exe.fetchall()#ESSE COMANDO RECEBE OS VALORES SELECIONADOS PELO SELECT PARA CONSEGUIR ARMAZENAR E DEPOIS UTILIZA-LOS
        print(recebe)
        if (recebe != None ) :
            #A PATIR DO TRY , EU COMEÇO A USAR UMA LISTA PARA MOSTRAR NA TELA O AGENDAMENTO CADASTRADO PELA PESSOA.
            
            tela_menu_agendamento.tableWidget.setRowCount(len(recebe)) #SO POSSUI UMA ROW ,POIS CADA PESSOA SO PODE TER UM CADASTRO
            tela_menu_agendamento.tableWidget.setColumnCount(5) #QUANTIDADE DE DADOS DO AGENDAMENTO MOSTRADO NA TELA (ESTADO,CIDADE,ESDERECO E ETC)
            for a in range(0,len(recebe)): #OS DOIS FOR PARA PERCORRER A MATRIZ E ADICIONAR OS VALORES DENTRO DO TABLEWIDGET
                for b in range (0,5):
                    tela_menu_agendamento.tableWidget.setItem(a,b,QtWidgets.QTableWidgetItem(str(recebe[a][b])))#COLOCANDO AS INFORMAÇÕES NA TELA 
                    print(recebe[a][b])
            banco.close
        
    except sqlite3.Error as erro:
            print("erro ao inserir os dados",erro)
#---------------------------------------------------------------------------------


#ESSA FUNÇÃO É A PARTE DE VERIFICAÇÃO DO LOGIN------------------------------------
def entra_db_tela_agendamento():
    cpf = tela_login.Login_usuario.text()
    data = tela_login.Login_senha.text()
    

    
    try :
        db = sqlite3.connect('Banco_cadastro.db')
        exe = db.cursor()
        exe.execute("SELECT cpf , data FROM cadastro WHERE cpf LIKE '"+cpf+"' AND data LIKE '"+data+"' " )
        dado = exe.fetchone()
        
        if dado != None:
            global cpff 
            cpff = cpf
            QMessageBox.about(tela_login,"Login","Logado com sucesso")
            tela_login.close()
            chama_tela_menu_agendamento()
        
        else :
            QMessageBox.about(tela_login,"Login","CPF OU SENHA ERRADO") 
        
        tela_login.Login_usuario.setText("") 
        tela_login.Login_senha.setText("")

    except sqlite3.Error as erro:
         print("erro ao inserir os dados",erro)  
#-----------------------------------------------------------    



def salva_db_agendamento():
    estado = tela_agendamento.lineEdit_1.text()
    cidade = tela_agendamento.lineEdit_2.text()
    endereco = tela_agendamento.lineEdit_3.text()
    data = tela_agendamento.calendarWidget.selectedDate()
    data_completa = str(data.toPyDate())

    try:
        db = sqlite3.connect('Banco_cadastro.db')
        exe = db.cursor()
        
        exe.execute("CREATE TABLE IF NOT EXISTS cadastro_agendamento ( estado text , cidade text,endereco text , cpf_agendamento text , data_completa text)")
        
        if (estado != "" and cidade != "" and endereco != "" and endereco != cidade ) :
            
            exe.execute("SELECT estado , cidade ,endereco , data_completa FROM cadastro_agendamento WHERE estado LIKE '"+estado+"' AND cidade LIKE '"+cidade+"' AND endereco LIKE '"+endereco+"' and data_completa LIKE '"+data_completa+"' ")
            dado_agendamento = exe.fetchmany()
        
          

            if (dado_agendamento != None  ) :
                exe.execute("INSERT INTO cadastro_agendamento VALUES ('"+estado+"' , '"+cidade+"' , '"+endereco+"' , '"+cpff+"' , '"+data_completa+"') ")
                QMessageBox.about(tela_agendamento,"Agendamento","AGENDADO COM SUCESSO")       
                
               

        else :
            QMessageBox.about(tela_agendamento,"Agendamento","ALGUM AGENDAMENTO ERRADO")   
                


        db.commit()
        db.close()
        tela_agendamento.lineEdit_1.setText("")
        tela_agendamento.lineEdit_2.setText("")
        tela_agendamento.lineEdit_3.setText("")
        

       
    except sqlite3.Error as erro:
         print("erro ao inserir os dados",erro)


#-----------------------------------------------------------------TERMINA A PARTE DE INTERAÇÃO COM O BANCO DE DADOS---------------------------------











#----------------------------------------------------------------PARTE DE LIMPAR A TELA ----------------------------------------

#ESSA FUNÇÃO LIMPA A TELA DE LOGIN
def limpar_tela_login():
    tela_login.Login_usuario.setText("") 
    tela_login.Login_senha.setText("")    
#---------------------------------------------------------------------

#ESSA FUNÇÃO LIMPA A TELA DE CADASTRO 
def limpar_tela_cadastro():
    tela_cadastro.lineEdit_3.setText("")
    tela_cadastro.lineEdit_4.setText("")
    tela_cadastro.lineEdit.setText("")    
#------------------------------------------------------------------------------------------------------------------------------------------








app = QtWidgets.QApplication([])
tela_inicial =uic.loadUi("Tela_Inicial.ui")
tela_login = uic.loadUi("Login.ui")
tela_cadastro = uic.loadUi("CADASTRO.ui")
tela_agendamento = uic.loadUi("Tela_vacinação.ui")
tela_menu_agendamento = uic.loadUi("menu_agendamento.ui")



tela_inicial.show()
tela_inicial.pushButton.clicked.connect(chama_tela_login)
tela_inicial.pushButton.clicked.connect(tela_inicial.close)

tela_inicial.pushButton_2.clicked.connect(chama_tela_cadastro)
tela_inicial.pushButton_2.clicked.connect(tela_inicial.close)


app.exec()