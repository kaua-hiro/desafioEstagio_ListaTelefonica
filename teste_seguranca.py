from utils.security import gerar_hash_senha, verificar_senha, criar_token_acesso

print("--- Testando Hashing e Verificação de Senha ---")
senha_original = "minhasenha123"
senha_hasheada = gerar_hash_senha(senha_original)

print(f"Senha Original: {senha_original}")
print(f"Senha Hasheada: {senha_hasheada}")
print("-" * 20)

senha_correta = "minhasenha123"
if verificar_senha(senha_correta, senha_hasheada):
    print(f"'{senha_correta}' -> VERIFICAÇÃO CORRETA (OK)")
else:
    print(f"'{senha_correta}' -> VERIFICAÇÃO INCORRETA (ERRO)")

senha_errada = "senha_errada"
if verificar_senha(senha_errada, senha_hasheada):
    print(f"'{senha_errada}' -> VERIFICAÇÃO CORRETA (ERRO)")
else:
    print(f"'{senha_errada}' -> VERIFICAÇÃO INCORRETA (OK)")

print("\n" + "=" * 50 + "\n")

print("--- Testando Geração de Token JWT ---")
dados_do_usuario = {"sub": "usuario@exemplo.com"}
token = criar_token_acesso(data=dados_do_usuario)

print(f"Dados do usuário para o token: {dados_do_usuario}")
print(f"Token JWT Gerado: {token}")