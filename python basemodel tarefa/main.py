from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

tarefas = {
    1:{"nome": "estudar", "descricao": "estudar programacao", "concluido": False}
    
}

class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluido: bool
    
    
    
@app.get("/tarefas") 
def get_tarefas():
    if not tarefas:
        raise HTTPException(status_code=404, detail="Lista nao encontrada")
    return JSONResponse(content=list(tarefas.items()))
    

@app.post("/adiciona/{id_tarefa}")
def adiciona_tarefa(id_tarefa:int, tarefa: Tarefa):
    if id_tarefa in tarefas:
        raise HTTPException(status_code=400, detail= "Esta tarefa ja existe")
    tarefas[id_tarefa] = tarefa.dict()
    return {"mensagem": "tarefa adicionada com sucesso!"}

@app.put("/atualiza/{id_tarefa}")
def atualiza_tarefa(id_tarefa:int, tarefa:Tarefa):
    if not tarefas:
        raise HTTPException(status_code=404, detail="Tarefas nao encontradas")
    tarefas[id_tarefa] = tarefa.dict()
    
@app.put("/atualiza_status/{id_tarefa}")
def atualiza_status(id_tarefa:int):
    if not tarefas:
        raise HTTPException(status_code=404, detail="Tarefas nao encontradas")
    tarefas[id_tarefa] ["concluido"] = True
    return {"mensagem": "Status da tarefa alterado para concluido!"}

@app.delete("/delete/{id_tarefa}")
def deleta_tarefa(id_tarefa:int):
    if id_tarefa not in tarefas:
        raise HTTPException(status_code=404, detail= "Tarefa nao encontrada")
    del tarefas[id_tarefa]
    return {"mensagem": "Tarefa deletada com sucesso!"}
    
