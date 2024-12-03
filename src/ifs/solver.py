# classe responsável pela seleção das variáveis e sua atribuição
# verificando se a solução é a melhor já encontrada e a condição de término
class solver:
    # Termination condition

    # Variable selection

    # Value selection

    # Solution comparator

    # While not Terminated

    Solution solve(Model model)
    {
        while(1)
            # Select variable
            
            # Select value

            # (un)assign the selected value to the selected variable
            if(value!=null)
                variable.assign(value)
            else
                variable.unassign()

        # Restore the best ever found solution
        # solution.restoreBest()

        return solution
    }

# Salva informações sobre as iterações
class Solution:
    def getIteration() # Iteração atual
    def getTime() # Tempo atual
    Model getModel() # Model

    # Store and Restore the best solution
    def saveBest():
        getModel().saveBest()
    def restoreBest():
        getModel.restoreBest()
    

