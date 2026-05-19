from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import os
from typing import Optional

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Column, Integer, String
import aiosqlite


DATABASE_URL = "sqlite:///./livros.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal  = sessionmaker(autocommit= False, autoflush=False, bind=engine)
Base = declarative_base()

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
      

class LivroDB(Base):
    __tablename__ = "Livros"
    id = Column(Integer, primary_key=True, index=True)
    nome_livro = Column(String, index=True)
    autor_livro = Column(String, index=True)
    ano_livro = Column(Integer, index=True)

Base.metadata.create_all(bind=engine)

def sessao_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


class Livro(BaseModel):
    
    nome_livro: str
    autor_livro:str
    ano_livro:int


@app.post("/adiciona/{id_livro}")
def post_livros(livro: Livro,db: Session = Depends(sessao_db),credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    db_livro = db.query(LivroDB).filter(LivroDB.nome_livro == livro.nome_livro, LivroDB.autor_livro == livro.autor_livro).first()
    if db_livro:
        raise HTTPException(status_code=400, detail = "Este livro ja existe!")
    
    novo_livro = LivroDB(nome_livro=livro.nome_livro, autor_livro= livro.autor_livro, ano_livro = livro.ano_livro)
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    
    return{"mensagem": "o livro foi criado com sucesso!"}




@app.put("/atualiza/{id_livro}")
def put_livros (id_livro: int,livro: Livro,db: Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    db_livro = db.query(LivroDB).filter(LivroDB.nome_livro == livro.nome_livro, LivroDB.autor_livro == livro.autor_livro).first()
    if not db_livro:
        raise HTTPException(status_code=404, detail= "Livro nao encontrado")
    
    db_livro.nome_livro = livro.nome_livro
    db_livro.autor_livro = livro.autor_livro
    db_livro.ano_livro = livro.ano_livro
    db.commit()
    db.refresh(db_livro)
    
    return {"mensagem": "O livro foi atualizado com sucesso"}



@app.delete("/delete/{id_livro}")
def delete_livros(id_livro:int,livro: Livro, db: Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    db_livro = db.query(LivroDB).filter(LivroDB.id == id_livro).first()
    if not db_livro:
        raise HTTPException(status_code=404, detail = "Livro nao encontrado")
    db.delete(db_livro)
    db.commit() 
    return{"mensagem": "livro deletado com sucesso"}







@app.get("/livros")
def get_livros(order_by: str = "id", order_dir: str = "asc", page:int = 1, limit: int= 10,db: Session = Depends (sessao_db), credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail= "Page ou limit invalidos!")
    
    livros= db.query(LivroDB).offset((page - 1) * limit).limit(limit).all()
    
    if not livros:
        return{"mensagem": "Nao existe nenhum livro!"}
    
    
    total_livros = db.query(LivroDB).count()
    
    return {
        "page":page,
        "limit":limit,
        "total":total_livros,
        "livros":[{"id": livro.id, "nome_livro": livro.nome_livro, "autor_livro": livro.autor_livro, "ano_livro": livro.ano_livro} for livro in livros]
    }
    


    


#order_by: ordena pelo nome do campo

    campos_validos = {"id", "nome_livro", "autor_livro", "ano_livro"} 
    if order_by not in campos_validos:
        raise HTTPException(status_code=400, detail="Campo de ordenação inválido!")
    
#order_dir: define se vai paginar de forma descrente ou crescente, asc: crescente, desc: crescente
    if order_dir not in ("asc", "desc"):
        raise HTTPException(status_code=400, detail="order_dir inválido! Use 'asc' ou 'desc'.")
    
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
    
    
        


    
    
