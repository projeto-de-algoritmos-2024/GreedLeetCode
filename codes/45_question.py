class Solution:
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0  # Já estamos no final

        # Variáveis para rastrear o alcance máximo e os saltos necessários
        jumps = 0
        current_end = 0  # Fim do alcance atual
        farthest = 0  # Alcance mais distante que podemos alcançar

        for i in range(n - 1):  # Não precisamos considerar o último índice
            # Atualiza o alcance mais distante que podemos alcançar
            farthest = max(farthest, i + nums[i])

            # Se chegarmos ao final do alcance atual, incrementamos o número de saltos
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Se o alcance atual já cobre o último índice, podemos parar
                if current_end >= n - 1:
                    break

        return jumps