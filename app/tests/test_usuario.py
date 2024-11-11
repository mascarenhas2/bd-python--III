import pytest
from app.models.usuario_model import Usuario

def test_usuario_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("", "catio@bubu.com", "123456")

def test_usuario_nome_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario(000, "catio@bubu.com", "123456") 

def test_usuario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("Caio", "", "123456")

def test_usuario_email_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Caio", 000, "123456")  

def test_usuario_senha_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("Caio", "catio@bubu.com", "")

def test_usuario_senha_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Caio", "catio@bubu.com", 12345)  