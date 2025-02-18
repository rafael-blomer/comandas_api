#Rafael Ceccatto Blomer
from fastapi import APIRouter
from domain.entities.Produto import Produto

router = APIRouter()

@router.get("/produto/", tags=["Produto"])
def get_produto():
    return {"msg": "get todos executando"}, 200

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/produto/", tags=["Produto"])
def post_produto(corpo: Produto):
    return {"msg": "post executado", "nome": corpo.nome, "descricao": corpo.descricao, "foto" : corpo.foto, "valor_unitario": corpo.valor_unitario}, 200

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, corpo: Produto):
    return {"msg": "put executado", "id": id, "nome": corpo.nome, "descricao": corpo.descricao, "foto" : corpo.foto, "valor_unitario": corpo.valor_unitario}, 200

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 200