import random
import string

print("--- 🤖 BEM-VINDO AO PYBOT VERSÂO 2 🤖 ---")

# Criamos uma variavel que começa como true (verdadeiro)
programa_rodando = True

# O loop 'while' vai repetir tudo o que estiver embaixo dele sem parar
while programa_rodando:
    print("/n--- MENU DE OPÇÔES ---")
    print("1 - Gerar uma senha segura rápido")
    print("2 - Contar uma piada de programador")
    print("3 - Sair do programa")

    opçao = input("Escolha uma Opção (1, 2 ou 3):")

    if opçao == "1":
        # Codigo simples do gerador que fizemos hoje
        letras_numeros = string.ascii_letters + string.digits
        senha = "".join(random.choices(letras_numeros, k=10))
        print(f" 🔒 Senha gerada com sucesso: {senha}")

    elif opçao == "2":
        print("🤖 Piada: Por que o desenvolvedor faliu?")
        print("🤖 Resposta: Porque ele gastou todo o seu 'cache'! 💻😂")

    elif opçao == "3":
         print("🤖 Encerrando o sistema... Obrigado por usar o pybot! Até mais.")
         programa_rodando = False # Isso muda a condição para Falso e para o loop!

    else:
        print("❌ Opção invalida! Digite 1, 2 ou 3.")

        print("---------------------------------")
        print("O programa foi fechado de verdade agora.")

              