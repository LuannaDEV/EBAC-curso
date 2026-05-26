import asyncio
import random
import itertools
import time


async def loading(texto, tempo=None):
    if tempo is None:
        tempo = random.uniform(1, 5)
    
    dots = itertools.cycle([".", "..", "..."])
    passos = int(tempo / 0.4)
    
    for _ in range(passos):
        print(f"\r{texto}{next(dots)}", end="", flush=True)
        await asyncio.sleep(0.4)
    
    print()




async def busca_pokemon_unova():
    inicio = time.perf_counter()
    

    
    await loading("BUSCANDO POKEMONS EM UNOVA", tempo = 2)
    await asyncio.sleep(random.uniform(1,5))
    mensagem = "POKEMONS ENCONTRADOS EM UNOVA: Ceruledge, Eeve"
    fim = time.perf_counter()
    return mensagem, fim - inicio
    
    
    
    
    
    
async def busca_pokemon_hoenn():
    inicio = time.perf_counter()
    await loading("BUSCANDO POKEMONS EM HOENN", tempo = 2)
    await asyncio.sleep(random.uniform(1,5))
    mensagem = "POKEMONS ENCONTRADOS EM HOENN: Charizard, Pikachu"
    fim = time.perf_counter()
    return mensagem, fim - inicio
    
    
    
async def busca_pokemon_johto():
    inicio = time.perf_counter()
    await loading("BUSCANDO POKEMONS EM JOHTO", tempo = 2)
    await asyncio.sleep(random.uniform(1,5))
    mensagem = "POKEMONS ENCONTRADOS EM JOHTO: Raichu, Blastoise "
    fim = time.perf_counter()
    return mensagem, fim - inicio
 
    

async def main():
    resultados = await asyncio.gather(busca_pokemon_hoenn(),busca_pokemon_unova(), busca_pokemon_johto())
    
    print("//RESULTADOS//")
    for mensagem, tempo in resultados:
        print(f"{mensagem} | tempo: {tempo:.2f}s")


asyncio.run(main())