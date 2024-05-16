## Modelagem Conceitual
### Definição das variáveis, seus domínios e restrições

#### Variáveis:
	professor P, disciplina D, sala de Aula S, horário H, Dia DIA

#### Domínio:
	P = {pofessores}
	D = {disciplinas}
	S = {salas}
	H = {horários}
	DIA = {dias}

#### Restrições:

**Hard Constrains:**

- Um professor não pode tá em mais de uma sala ao mesmo tempo.
- Uma sala de aula só pode ser ocupada por um professor e disciplina em determinado horário e dia.
- Pelo menos uma turma de cada disciplina em um mesmo fluxo precisa de estar em horários diferentes
- Disciplinas com carga horária de 60 horas deve ocupar o mesmo horário em dois dias diferentes(seg-qua, ter-qui, qua-sex, seg-sex, ter-sex, seg-qui)
- Disciplinas com carga horária de 60 horas deve ocupar o mesmo horário em três dias diferentes (seg-qua-sex)
- Um professor não pode assumir menos que a carga horária mínima
- Um professor não pode assumir mais que a carga horária máxima
- Disciplinas que precisam de laboratório ser alocados para salas que são laboratórios

**Soft Constrains:**
- Uma mesma turma de uma disciplina não ter aula no mesmo dia
- Os horários de '12:00-13:50' e '18:00-19:50' não serem escolhidos
- Disciplinas que não precisam de laboratório ser alocados para salas que não são laboratórios
- Não ter aula no sábado
- Pelo menos 20% das salas estarem livres
- Cada professor deve ministrar as discipinas de sua área de atuação
- Atender aos horários preferências dos professores
	