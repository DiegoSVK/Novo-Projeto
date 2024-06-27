import time
from time import strftime
import smtplib
from email.message import EmailMessage

# Função com a lógica de enviar email
def enviar_email():
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login('exemplo.mail', 'senha-teste')

        msg = EmailMessage()
        msg['Subject'] = 'Deu certo'
        msg['From'] = 'exemplo.com'
        msg['To'] = 'seuemail.com'

        conteudo = 'Teste Exemplo'
        msg.set_content(conteudo)
        servidor.send_message(msg)
       
    except Exception as err:
        print(f'Falha \n {err}')
    finally:
        servidor.quit()
    print('Email enviado com sucesso')

# Quando esta função for chamada, atualiza a hora atual a cada 1 segundo até que a condição seja satisfeita
def relogio():
    try:
        usuario = input('Digite a hora para enviar (formato HH:MM:SS): ')
        inicio = True
        while inicio:
            hora_atual = strftime("%H:%M:%S")
            time.sleep(1)
            print(hora_atual)
            if hora_atual == usuario:
                enviar_email()
                inicio = False
    except Exception as erro:
        print(f'{erro}')

# Menu de opções
def menu():
    op = 1
    print('Selecione uma opção:')
    while op:
        print('\n 1- Enviar email automático \n 2- Agendar email automático')
        op = int(input())
        if op == 1:
            print('Mail-teste (ainda não definido)')
        elif op == 2:
            # Chamando função relogio com hora agendada para enviar email
            relogio()
        elif op == 0:
            print('Saindo do Sistema...')
        else:
            print('Opção inválida')

# Chamando a função menu
menu()
