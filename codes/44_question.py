class Solution:
    def isMatch(self, texto, padrao):
        i, j = 0, 0 
        estrela = -1
        texto_voltar = 0

        while i < len(texto):
            if j < len(padrao) and (padrao[j] == texto[i] or padrao[j] == '?'):
                i += 1
                j += 1
            elif j < len(padrao) and padrao[j] == '*':
                estrela = j
                texto_voltar = i
                j += 1
            elif estrela != -1:
                j = estrela + 1
                texto_voltar += 1
                i = texto_voltar
            else:
                return False

        while j < len(padrao) and padrao[j] == '*':
            j += 1

        return j == len(padrao)
