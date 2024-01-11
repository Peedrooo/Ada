# Graph Neural Network

- **Introdução**: Arquitetura de rede neural baseada em grafos para resolver problemas de otimização combinatória expressos como problemas de satisfação de restrições (CSPs).

- **Problemas de Satisfação de Restrições**: Definição formal de CSPs, como podem ser transformados em CSPs binários e como podem ser vistos como problemas de maximização de restrições (Max-CSPs).

- **Método**: Rede neural recorrente não supervisionada (RUN-CSP) que usa passagem de mensagens entre as variáveis de um CSP para encontrar uma atribuição aproximada que satisfaça o máximo de restrições possível.

- **Experimentos**: Avaliação de desempenho do RUN-CSP em quatro problemas NP-difíceis: Max-2-SAT, Max-Cut, 3-COL e Max-IS. O artigo compara o RUN-CSP com outros métodos baseados em heurísticas, programação semi-definida e redes neurais. O artigo mostra que o RUN-CSP é competitivo, escalável, genérico e rápido.

- **Max-Cut: Resultados de corte em instâncias Gset para RUN-CSP, DSDP e BLS**: Método para resolver o problema do corte máximo ponderado usando RUN-CSP, uma rede neural recorrente não supervisionada para problemas de satisfação de restrições. O método é comparado com dois algoritmos baseados em programação semi-definida positiva (DSDP e BLS) em um conjunto de instâncias de benchmark chamado Gset.

- **Coloração: Foco no caso de três cores**: Avaliação de desempenho de RUN-CSP no problema de decisão 3-COL, que pergunta se um dado grafo é 3-colorível sem conflitos. O método é comparado com uma heurística gulosa, uma heurística híbrida de última geração (HybridEA) e uma rede neural gráfica (GNN-GCP) em instâncias aleatórias "difíceis" e em quatro classes diferentes de grafos.

- **Conjunto Independente: Extensão da função de perda**: A página experimenta o problema do conjunto independente máximo Max-IS, que requer uma extensão da função de perda de RUN-CSP para recompensar atribuições com muitas variáveis definidas como 1. O método é comparado com um solucionador de última geração (ReduMIS) e uma heurística gulosa em instâncias aleatórias e em um conjunto de instâncias de benchmark geradas pelo modelo RB.


### Tópicos Relevantes
Supervisionado: O treinamento não é supervisionado e requer apenas um conjunto de instâncias do problema.

Escalonável: Redes treinadas em instâncias pequenas alcançam bons resultados em entradas muito maiores.

Genérico: A arquitetura é genérica e pode aprender a encontrar soluções aproximadas para qualquer binário Max-CSP.


### Notebook
https://github.com/toenshoff/RUN-CSP

