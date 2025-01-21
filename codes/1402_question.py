class Solution:
    def maxSatisfaction(self, satisfaction):
        # Ordenamos os pratos em ordem decrescente de satisfação
        satisfaction.sort(reverse=True)

        max_score = 0
        current_sum = 0

        # Aplicação greedy para calcular o score máximo
        for sat in satisfaction:
            # Verificamos se adicionar o prato atual ainda aumenta o score
            if current_sum + sat > 0:
                current_sum += sat
                max_score += current_sum
            else:
                break  # Paramos porque os pratos restantes só diminuirão o score

        return max_score
