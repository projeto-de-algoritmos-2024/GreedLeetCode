class Solution:
    def earliestFullBloom(self, tempos_plantio, tempos_crescimento):
        sementes = sorted(zip(tempos_crescimento, tempos_plantio), reverse=True, key=lambda x: x[0])
        dia_atual = 0
        ultimo_dia = 0

        for crescimento, plantio in sementes:
            dia_atual += plantio
            ultimo_dia = max(ultimo_dia, dia_atual + crescimento)

        return ultimo_dia
