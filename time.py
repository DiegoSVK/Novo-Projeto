import time
from time import strftime
import smtplib
from email.message import EmailMessage

#função  com a logica email
def email ():
   
    try:
        servidor = smtplib.SMTP('smtp.gmail.com',587)
        servidor.starttls()
        servidor.login('exemplo.mail','senha-teste')

        
        msg = EmailMessage()
        msg['Subject'] = 'Deu certo'
        msg['From'] = 'exemplo.com '
        msg['To'] = 'seuemail.com'

        conteudo ='Teste Exemplo'
        msg.set_content(conteudo)
        servidor.send_message(msg)
       

        
    except  Exception as err:
        print(f'Falha \n {err}')
    finally:
        servidor.quit()
    print('Realizado com sucesso')
        
# quando esta função for chamada atualiza a hora atual a cada 1 segudo até que a condição seja satisfeita
def relogio():
    try:
        usuario = input('Digite a hora a enviar:')
        inicio = True
        while inicio:
            hora_atual = strftime("%H:%M:%S")
            time.sleep(1)
            print(hora_atual)
            if(hora_atual == usuario):
                email()
                inicio = False
    except Exception as erro:
        print(f'{erro}')
    
# menu de opções
def menu ():
    op =1
    print('Selecione uma opção')
    while op:
        print('\n 1-Enviar email automatico \n 2-Agendar Email automatico')
        op = int(input())
        if(op == 1):
            print('Mail-teste(ainda nao definido)')
        elif(op == 2):
            # chamando função relegio com hora agendada para enviar email
            relogio()
        elif(op == 0):
            print('Saindo do Sistema...')
        else:
            print('Opção invalida')

# chamando a função menu
menu()