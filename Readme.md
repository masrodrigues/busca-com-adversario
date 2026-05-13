# Kit othello
Kit para executar partidas de Othello e Jogo da Velha invertido (Tic-Tac-Toe Misere) e implementar algoritmos de busca com adversário.

## Conteudo
O kit contém os seguintes arquivos (todos os `__init__.py` estao omitidos):

```text
kit_games
├── server.py              <-- servidor de jogos
├── server_tui.py          <-- servidor com melhor visualização (somente para othello)
├── test_mcts.py                <-- teste (muito basico) do seu MCTS
├── test_minimax_tttm.py        <-- teste da poda alfa-beta no tic-tac-toe misere
├── test_othello_evaluations.py <-- teste das funcoes de avaliacao do othello p/ a poda alfa-beta
├── test_pruning.py             <-- teste da poda alfa-beta em um jogo simplificado
└── advsearch
    ├── othello
    |   ├── board.py       <-- encapsula o tabuleiro do othello
    |   └── gamestate.py   <-- encapsula um estado do othello (config. do tabuleiro e cor que joga)
    ├── tttm
    |   ├── board.py       <-- encapsula o tabuleiro do tic-tac-toe misere
    |   └── gamestate.py   <-- encapsula um estado do tic-tac-toe-misere (config. do tabuleiro e cor que joga)
    ├── randomplayer
    |   └── agent.py       <-- agente que joga aleatoriamente
    ├── humanplayer        
    |   └── agent.py       <-- agente para um humano jogar 
    ├── timer.py           <-- funcoes auxiliares de temporizacao
    └── your_agent         <-- renomeie este diretorio c/ o nome do seu agente 
      ├── mcts.py         <-- implemente o algoritmo MCTS aqui
      ├── minimax.py      <-- implemente a poda alfa-beta aqui
      ├── othello_minimax_count.py  <-- chame seu minimax com a heuristica de contagem 
      ├── othello_minimax_mask.py   <-- chame seu minimax com a heuristica posicional 
      ├── othello_minimax_custom.py <-- chame seu minimax com uma heuristica customizada
      ├── tournament_agent.py       <-- agente que vai jogar o torneio de othello 
      ├── tttm_minimax.py           <-- chame seu minimax sem limite de profundidade aqui
      └── [vc pode adicionar outros arquivos e subdiretorios aqui]
```

## Requisitos 
O servidor foi testado em uma máquina GNU/Linux com o interpretador python 3.9.7.

Outras versões do interpretador python ou sistema operacional podem funcionar, mas não foram testados.

## Instruções

Para iniciar uma partida, digite no terminal:

`python server.py game player1 player 2 [-h] [-d delay] [-p pace]  [-o output-file] [-l log-history]`

Nos parâmetros, game é o jogo a ser jogado (othello ou tttm para tic-tac-toe misere)  'player(1 ou 2)' são o caminhos dentro de `advsearch` onde estão implementados os make_move dos jogadores.

Somente para Othello: Para ver o tabuleiro e as peças com cores, instale a biblioteca `pytermgui` (por exemplo, com `pip install pytermgui`) e execute o `server_tui.py` ao invés do `server.py`.


Os argumentos entre colchetes são opcionais, seu significado é descrito a seguir:
```text
-h, --help            Mensagem de ajuda
-d delay, --delay delay
                    Tempo alocado para os jogadores realizarem a jogada (default=5s)
-p pace, --pace pace
                    Tempo mínimo que o servidor espera para processar a jogada (para poder ver partidas muito 
                    rapidas sem se perder no terminal)
-l log-history, --log-history log-history
                    Arquivo para o log do jogo (default=history.txt)
-o output-file, --output-file output-file
                    Arquivo de saida com os detalhes do jogo (inclui historico)
```

O jogador 'random' se localiza em `advsearch/randomplayer/agent.py`. Para jogar uma partida com ele,
basta substituir player1 ou 2 por esse caminho. Como exemplo, inicie
uma partida random vs. random de othello para ver o servidor funcionando:

`python othello server.py advsearch/randomplayer/agent.py advsearch/randomplayer/agent.py -d 1 -p 0.3`

O delay pode ser de 1 segundo porque o jogador random é muito rápido (e muito incompetente). O passo é de 0.3 segundos para acompanhar o progresso da partida (pode acelerar ou reduzir conforme a necessidade).

O jogador 'human' se localiza em `advsearch/humanplayer/agent.py`. Você pode utilizar este player para jogar você mesmo e testar suas habilidades contra outro agente (inclusive o que você está construindo nesse trabalho). 

Para jogar com ele, utilize o mesmo comando acima, trocando o player1 ou 2 por `advsearch/humanplayer/agent.py`. Você terá o limite de 1 minuto para pensar na sua jogada. Digite as coorenadas da ação na ordem `<coluna> <linha>`.  

## Funcionamento 

Iniciando pelo primeiro jogador, que jogará com as peças pretas, o servidor chama a função `make_move(state)` do seu agente. A função recebe `state`, um objeto da classe `GameState` que contém um tabuleiro (objeto da classe `Board` e o jogador a fazer a jogada (um caractere) (`B` para as pretas ou `W` para as brancas). Para os detalhes, veja `gamestate.py` e `board.py` de cada jogo.

O servidor então espera o delay e recebe a tupla (x,y) com coluna e linha com a jogada do jogador. O servidor processa a jogada, exibe o novo estado no terminal e passa a vez para o próximo jogador, repetindo esse ciclo até o fim do jogo.

No fim do jogo, o servidor exibe a pontuação de cada jogador e cria um arquivo `results.xml`.
com todas as jogadas tentadas pelos jogadores (inclusive as ilegais). Um arquivo `history.txt` também contém as jogadas, e esse é criado mesmo que a partida seja interrompida no meio (e.g. crash de um agente).


## Notas
* O servidor checa a legalidade das jogadas antes de efetivá-las. A vez é devolvida para o jogador que tentou a jogada ilegal
* Jogadas ilegais demais resultam em desqualificação.
* O jogador 'random' apenas sorteia uma jogada entre as válidas no estado recebido.
* O jogador 'human' verifica a legalidade da jogada antes de enviá-la ao servidor.
* Em caso de problemas com o servidor, reporte via moodle ou email.

ISSO ABAIXO AINDA NAO FUNCIONA:
Para ver o tabuleiro e as peças com cores, instale a biblioteca `pytermgui` (por exemplo, com `pip install pytermgui`) e execute o `server_tui.py` ao invés do `server.py`. 

---

# Relatorio da Implementacao

## Identificacao

Preencher antes da entrega:

- Integrante(s): TODO
- Cartao(oes) de matricula: TODO
- Turma: TODO

## Bibliotecas

A implementacao usa apenas bibliotecas padrao do Python. Nao ha dependencias adicionais obrigatorias.

## Minimax com poda alfa-beta

A funcao `minimax_move` foi implementada em `advsearch/your_agent/minimax.py` de forma generica, usando apenas a interface comum dos estados dos jogos:

- `legal_moves()`
- `next_state(move)`
- `is_terminal()`
- `winner()`

A avaliacao sempre considera o jogador da raiz da busca. A profundidade `-1` representa busca ilimitada. Para Othello, tambem foi considerado o caso em que o mesmo jogador pode jogar novamente quando o adversario nao possui jogadas legais.

## Tic-Tac-Toe Misere

O agente em `advsearch/your_agent/tttm_minimax.py` usa minimax com profundidade ilimitada, pois a profundidade maxima do jogo e 9.

A funcao `utility` retorna:

- `1` para vitoria do jogador avaliado;
- `-1` para derrota;
- `0` para empate.

Resultados observados:

| Partida | Resultado |
| --- | --- |
| Minimax (B) x Random (W) | Minimax venceu, placar B=1, W=-1 |
| Random (B) x Minimax (W) | Minimax venceu, placar B=-1, W=1 |
| Minimax (B) x Minimax (W) | Empate, placar B=0, W=0 |

Assim, nos testes executados, o minimax venceu contra o `randomplayer` jogando com ambas as cores e empatou contra si mesmo.

## Othello

Foram implementadas tres avaliacoes para Othello:

- `evaluate_count`: diferenca entre quantidade de pecas do jogador e do oponente.
- `evaluate_mask`: diferenca de valores posicionais usando a mascara fixa fornecida no enunciado.
- `evaluate_custom`: combinacao de valor posicional, mobilidade, controle de cantos, penalizacao de casas perigosas proximas a cantos vazios e diferenca de pecas com peso maior no final do jogo.

O criterio de parada usado nos agentes minimax de Othello foi profundidade maxima fixa igual a 3. Essa escolha manteve as partidas dentro do limite de tempo nos testes locais.

## Mini-torneio de Othello

Resultados coletados com o servidor do kit:

| Partida | Placar final | Vencedor |
| --- | --- | --- |
| Contagem (B) x Valor posicional (W) | B=30, W=34 | Valor posicional |
| Valor posicional (B) x Contagem (W) | B=52, W=12 | Valor posicional |
| Contagem (B) x Customizada (W) | B=28, W=36 | Customizada |
| Customizada (B) x Contagem (W) | B=41, W=23 | Customizada |
| Valor posicional (B) x Customizada (W) | B=16, W=48 | Customizada |
| Customizada (B) x Valor posicional (W) | B=42, W=22 | Customizada |

A heuristica customizada foi a mais bem-sucedida nos testes, com 4 vitorias em 4 partidas disputadas. A heuristica de valor posicional venceu as 2 partidas contra a heuristica de contagem.

## Agente de torneio

O arquivo `advsearch/your_agent/tournament_agent.py` usa minimax com poda alfa-beta, profundidade 3 e a heuristica customizada. Essa escolha foi feita porque a customizada teve o melhor desempenho no mini-torneio local e nao depende de arquivos externos, processos em background ou dados pre-calculados.

## Extra: MCTS

Foi implementada uma versao opcional de MCTS em `advsearch/your_agent/mcts.py`, com:

- selecao por UCT;
- expansao de jogadas nao visitadas;
- simulacao aleatoria ate estado terminal;
- retropropagacao de vitoria, empate ou derrota;
- escolha imediata de uma jogada vencedora quando ela existe.

## Testes

Comando executado:

```bash
python -m unittest
```

Resultado:

```text
Ran 9 tests in 0.095s
OK
```
