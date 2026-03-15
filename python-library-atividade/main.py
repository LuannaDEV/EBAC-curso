from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import os
from typing import Optional


app = FastAPI (
    title="API de livros.",
    description="API para gerenciar catalogo de livros.",
    version="1.0",
    contact={
        "name":"Luanna",
        "email": "dev.luanna.espindola@gmail.com"
    }
)

meus_livros = {
    1: {"nome_livro": "Crepusculo", "autor_livro": "Desconhecido", "ano_livro": 2009},
    2: {"nome_livro": "Harry Potter", "autor_livro": "J.K. Rowling", "ano_livro": 2008}
}


MEU_USUARIO= "admin"
MINHA_SENHA = "admin"

security = HTTPBasic()

def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)
    
    if not (is_username_correct and is_password_correct):
        raise HTTPException (status_code=401, detail= "Usuario ou senha incorretos",
                    
                             )

    return credentials.username
      

class Livro(BaseModel):
    
    nome_livro: str
    autor_livro: str
    ano_livro: int

@app.post("/adiciona/{id_livro}")
def post_livros(id_livro: int, livro: Livro):
    if id_livro in meus_livros:
        raise HTTPException(status_code=400, detail="Este livro ja existe")
    else:
        meus_livros[id_livro]= livro.dict()
            
        
        return {"O livro foi criado com sucesso"}


@app.get("/livros")
def get_livros(page:int = 1, limit: int= 10,order_by: str = "id", order_dir: str = "asc", credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail= "Page ou limit invalidos!")
    
    if not meus_livros:
        return{"mensagem": "Nao existe nenhum livro!"}
    
    
    
    lista_livros = [{"id": id, **dados} for id, dados in meus_livros.items()]

    reverse = order_dir == "desc"
    lista_livros.sort(key=lambda x: x[order_by], reverse=reverse)

    
    start = (page - 1) * limit                       
    livros_paginados = lista_livros[start: start + limit]
    
    
    return {
        "page": page,
        "limit": limit,
        "total": len(meus_livros),
        "livros": livros_paginados
    }
    
    
        

@app.put("/atualiza/{id_livro}")
def put_livros (id_livro: int, livro: Livro):
    meu_livro = meus_livros.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Este livro nao foi encontrado")
    else:
        meus_livros[id_livro] = livro.dict()
            
        
        return{"message": "As informacoes do seu livro foram atualizadsas com sucesso"}
    
    
@app.delete("/delete/{id_livro}")
def delete_livros(id_livro:int):
    if id_livro not in meus_livros:
        raise HTTPException(status_code=404, detail= "Este livro nao existe")
    else:
        del meus_livros[id_livro]
        return {"mensagem": "Tarefa deletada com sucesso!"}
    
