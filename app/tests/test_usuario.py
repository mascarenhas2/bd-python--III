import pytest
from app.models.usuario_model import Usuario

def test_usuario_nome_sem_informacao_preencher_novamente():
    with pytest.raises(ValueError, match="É necessário preencher o NOME para prosseguir."):
        Usuario("", "catio@bubu.com", "123456")

def test_usuario_nome_invalido_erro_caracteres_invalido():
    with pytest.raises(TypeError, match="ERRO! Nome invalido."):
        Usuario(000, "catio@bubu.com", "123456") 

def test_usuario_email_sem_informacao_preencher_novamente():
    with pytest.raises(ValueError, match="É necessário preencher o E-MAIL para prosseguir."):
        Usuario("Caio", "", "123456")

def test_usuario_email_invalido_caracteres_invalido():
    with pytest.raises(TypeError, match="ERRO! E-mail invalido."):
        Usuario("Caio", 000, "123456")  

def test_usuario_senha_sem_informacao_preencher_novamente():
    with pytest.raises(ValueError, match="É necessário preencher a senha para prosseguir."):
        Usuario("Caio", "catio@bubu.com", "")

def test_usuario_senha_invalida_caracteres_invalidos():
    with pytest.raises(TypeError, match="ERRO! Senha invalida."):
        Usuario("Caio", "catio@bubu.com", 12345)  