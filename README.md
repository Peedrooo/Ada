# Ada
Algoritmo gerador de grade horária para a Universidade de Brasilia


## Problema
Na universidade de brasilia, realizar a montagem da grade horária é um processo manual e demorado, que envolve muitas pessoas e muitas horas de trabalho. Sendo necessário montar com base no fluxo de disciplinas, disponibilidade de professores, e demanda por disciplinas, sendo muito suscetível a erros e atrasos.

## Objetivos

### Objetivo Geral
Desenvolver um algoritmo para automatizar a criação da grade horária do curso de Engenharia de Software da Universidade de Brasília, considerando o fluxo de disciplinas, disponibilidade de professores e demanda por disciplinas. Posteriormente, expandir essa automatização para os demais cursos da instituição. O algoritmo deverá ser servido por uma API em fastapi, que receberá os dados de entrada e retornará a grade horária gerada.

### Objetivos Específicos
O algoritmo deve ser capaz de:
- Ler os dados de entrada, que são:
    - Fluxo de disciplinas
    - Disponibilidade de professores e suas respectivas disciplinas
    - Demanda por disciplinas
    - Salas disponíveis e suas respectivas infraestruturas (laboratório, capacidade)
    - Horários disponíveis das salas
    - Carga mínima e máxima dos professores

- Gerar uma grade horária onde:
    - Todas as disciplinas do fluxo são ofertadas
    - Todos os professores estão alocados
    - A demanda por disciplinas busca ser atendida
    - Os horários disponíveis são respeitados

- Gerar uma grade horária que não possua:
    - Conflitos de horários:
        - Um professor não pode estar em duas salas ou mais ao mesmo tempo
    - Conflitos de salas:
        - Uma sala não pode estar sendo usada por dois professores ou mais ao mesmo tempo
        - Uma sala não pode estar sendo usada por duas disciplinas ou mais ao mesmo tempo
    - Sobrecarga de professores:
        - Um professor não pode assumir menos de da sua carga mínima
        - Um professor não pode assumir mais de sua carga máxima

- Preferencial:
    - Pelo menos 20% das salas devem estar livres
    - Horários preferenciais dos professores
    - Horários preferenciais das salas
    - Cada professor deve ministrar as disciplinas de sua área de atuação/ preferência

A API deve ser capaz de:
- Receber os dados de entrada
- Retornar a grade horária gerada


## Monografia

## Reuniões de orientação

### Playlist
[![Acompanhamento - Ada](https://i.ytimg.com/vi/LXb3TcfPPYM/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDar4isIXedFtg2SUVVW0RL6_5pkw)](https://www.youtube.com/playlist?list=PLYDa724AZH7Yi8K3G2jPexBRYz8NtaB1l)
