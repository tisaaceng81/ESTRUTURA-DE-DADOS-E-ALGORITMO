import cNo
import cArvoreBinaria
import sys

if __name__ == '__main__':

  n = 7
  if (len(sys.argv) > 1):
      n = int(sys.argv[1])
      if n < 0:
          n = 7
  
  # --- CRIAÇÃO DAS ÁRVORES ---
  print(f" Criando Árvore 1 com {n} nós.")
  arvore1 = cArvoreBinaria.cArvoreBinaria(n)

  print(f" Criando Árvore 2 com {n} nós.")
  arvore2 = cArvoreBinaria.cArvoreBinaria(n)

  print(f" Criando Árvore 3 com {n + 1} nós.")
  arvore3 = cArvoreBinaria.cArvoreBinaria(n + 1)
  print("--------------------------\n")
  
  # --- EXIBIÇÃO DAS INFORMAÇÕES DAS ÁRVORES ---
  print(f"--- ANÁLISE DA ÁRVORE 1 ---")
  print(f" Altura da árvore: {arvore1.getAltura()}")
  folhas, completos, semi = arvore1.contaTiposDeNos()
  print(f" Nós do tipo folha: {folhas}")
  print(f" Nós do tipo completo (2 filhos): {completos}")
  print(f" Nós do tipo semi-cheio (1 filho): {semi}")
  print(f" Contagem de nós (recursivo): {arvore1.getNumNosTotal()}")
  print("--------------------------\n")

  # NOVO: Análise da Árvore 2
  print(f"--- ANÁLISE DA ÁRVORE 2 ---")
  print(f" Altura da árvore: {arvore2.getAltura()}")
  folhas, completos, semi = arvore2.contaTiposDeNos()
  print(f" Nós do tipo folha: {folhas}")
  print(f" Nós do tipo completo (2 filhos): {completos}")
  print(f" Nós do tipo semi-cheio (1 filho): {semi}")
  print(f" Contagem de nós (recursivo): {arvore2.getNumNosTotal()}")
  print("--------------------------\n")

  # NOVO: Análise da Árvore 3
  print(f"--- ANÁLISE DA ÁRVORE 3 ---")
  print(f" Altura da árvore: {arvore3.getAltura()}")
  folhas, completos, semi = arvore3.contaTiposDeNos()
  print(f" Nós do tipo folha: {folhas}")
  print(f" Nós do tipo completo (2 filhos): {completos}")
  print(f" Nós do tipo semi-cheio (1 filho): {semi}")
  print(f" Contagem de nós (recursivo): {arvore3.getNumNosTotal()}")
  print("--------------------------\n")

  # --- TESTE DAS COMPARAÇÕES ---
  print("--- COMPARAÇÕES ---")
  
  # Compara Árvore 1 e 2 (devem ser idênticas em tudo)
  print("--> Comparando Árvore 1 e 2 (Antes de modificar):")
  res_est = arvore1.saoEstruturalmenteIdenticas(arvore2)
  print(f"  - Estruturalmente idênticas? {'Sim ' if res_est else 'Não '}")
  res_tot = arvore1.saoIdenticas(arvore2)
  print(f"  - Totalmente idênticas? {'Sim ' if res_tot else 'Não '}")

  # Compara Árvore 1 e 3 (devem ser diferentes em tudo)
  print("\n--> Comparando Árvore 1 e 3:")
  res_est = arvore1.saoEstruturalmenteIdenticas(arvore3)
  print(f"  - Estruturalmente idênticas? {'Sim ' if res_est else 'Não '}")
  res_tot = arvore1.saoIdenticas(arvore3)
  print(f"  - Totalmente idênticas? {'Sim ' if res_tot else 'Não '}")

  # Modifica a Árvore 2 e compara novamente
  print("\n--> Comparando Árvore 1 e 2 (Após modificar o dado da raiz da Árvore 2):")
  arvore2.getRaiz().setDado(999) # Modificando o valor
  res_est = arvore1.saoEstruturalmenteIdenticas(arvore2)
  print(f"  - Estruturalmente idênticas? {'Sim ' if res_est else 'Não '}")
  res_tot = arvore1.saoIdenticas(arvore2)
  print(f"  - Totalmente idênticas? {'Sim ' if res_tot else 'Não '}")
  print("--------------------------\n")

  # --- IMPRESSÃO DOS PERCURSOS (da Árvore 1) ---
  print("--- PERCURSOS DA ÁRVORE 1 ---")
  print("Percurso em Pré-Ordem:")
  arvore1.percorreArvore(cArvoreBinaria.percursos.PRE_ORDEM)
  print("\n======================")
  print("\nPercurso em In-Ordem:")
  arvore1.percorreArvore(cArvoreBinaria.percursos.IN_ORDEM)
  print("\n======================")
  print("\nPercurso em Post-Ordem:")
  arvore1.percorreArvore(cArvoreBinaria.percursos.POST_ORDEM)
  print("\n======================")