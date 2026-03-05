from fastapi import FastAPI, HTTPException 


app = FastAPI()


tarefas = {
    
    1: {"nome": "estudar", "descricao": "estudar programacao", "concluida": False}
    
}

@app.get("/tarefas")
def get_tarefas():
    if not tarefas:
        raise HTTPException(status_code=404, detail= "tarefas nao encontradas")
    else:
        return tarefas.items()
    
    
@app.post("/adicionar/{id_tarefa}")
def adicionar_tarefa(id_tarefa: int, nome: str, descricao: str, concluida: bool):
    if id_tarefa in tarefas:
        raise HTTPException(status_code=400, detail= "Uma tarefa com este id ja existe!")
    
    tarefas[id_tarefa] = {
            "id_tarefa": id_tarefa, "nome": nome, "descricao": descricao, "concluida": concluida
        }
    return {"tarefa adicionada!"}

@app.put("/atualizar/{id_tarefa}")
def atualizar_tarefa(id_tarefa: int):
    if id_tarefa not in tarefas:
        raise HTTPException(status_code=404, detail = "Tarefa nao encontrada!")
    else:
        tarefas[id_tarefa] ["concluida"] = True
        return {"mensagem": "O Status da tarefa foi alterado para concluido"}
    

@app.delete("/deletar/{id_tarefa}")
def deletar_tarefa(id_tarefa: int):
    if id_tarefa not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    else:
        del tarefas[id_tarefa]
        return {"mensagem": "Tarefa deletada com sucesso"}