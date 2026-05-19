import asyncio
import random
import itertools


async def loading(texto, tempo=None):
    if tempo is None:
        tempo = random.uniform(1, 5)
    
    dots = itertools.cycle([".", "..", "..."])
    passos = int(tempo / 0.4)
    
    for _ in range(passos):
        print(f"\r{texto}{next(dots)}", end="", flush=True)
        await asyncio.sleep(0.4)




async def busca_pokemon_unova():
    
    

    
    await loading("BUSCANDO POKEMONS EM UNOVA", tempo = 3)
    await asyncio.sleep(random.uniform(1,5))
    print("\nPOKEMON ENCONTRADO EM UNOVA -> blastoise")
    await asyncio.sleep(random.uniform(1,5))
    print("\nPOKEMON ENCONTRADO EM UNOVA -> ceruledge")
    await asyncio.sleep(random.uniform(1,5))
    await loading("BUSCANDO POKEMONS EM UNOVA", tempo = 3)
    print("NAO EXISTEM OUTROS POKEMONS EM UNOVA.")
    
    
    
    
    
    
async def busca_pokemon_hoenn():
    await loading("BUSCANDO POKEMONS EM HOENN", tempo = 4)
    await asyncio.sleep(random.uniform(1,5))
    print("\nPOKEMON ENCONTRADO EM HOENN-> charizard")
    await asyncio.sleep(random.uniform(1,5))
    print("\nPOKEMON ENCONTRADO EM HOENN --> pikachu")
    await loading("BUSCANDO POKEMONS EM UNOVA", tempo = 3)
    print("NAO EXISTEM OUTROS POKEMONS EM HOENN.")
    
    
    
async def busca_pokemon_johto():
    await loading("BUSCANDO POKEMON EM JOHTO", tempo = 5)
    await asyncio.sleep(random.uniform(1,5))
    print("\n POKEMON ENCONTRADO EM JOHTO -> tyranitar")
    await asyncio.sleep(random.uniform(1,5))
    print("\n POKEMON ENCONTRADO EM JOHTO -> raichu")
    await loading("BUSCANDO POKEMON EM JOHTO", tempo = 4)
    print("NAO EXISTEM OUTROS POKEMONS EM JOHTO.")
    
 
    

async def main():
    await asyncio.gather(busca_pokemon_hoenn(),busca_pokemon_unova(), busca_pokemon_johto())
    


asyncio.run(main())
