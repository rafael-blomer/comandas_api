#Rafael Ceccatto Blomer
from fastapi import APIRouter
from domain.entities.Funcionario import Funcionario

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    return {"msg": "get todos executado"}, 200

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(corpo: Funcionario):
    return {"msg": "post executado", "nome": corpo.nome, "cpf": corpo.cpf, "telefone": corpo.telefone}, 200

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, corpo: Funcionario):
    return {"msg": "put executado", "id":id, "nome": corpo.nome, "cpf": corpo.cpf, "telefone": corpo.telefone}, 200

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 200