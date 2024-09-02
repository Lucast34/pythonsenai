# desenvolve um jogo da velha desenvolvido em python que funcione no terminal
from pickletools import int4
import velha_funcoes as jv

jogador = 'X'
vencedor = False
while vencedor == False:
    jv.desenhar_tabuleiro()

    jogada = int(input('onde deseja joga? '))

    jv.jogar(jogada, jogador)

    jv.desenhar_tabuleiro()

    jogador = jv.troca(jogador)
    vencedor = jv.vitoria()


jogador = jv.troca(jogador)
print(f'Ojogador "{jogador}" venceu')
