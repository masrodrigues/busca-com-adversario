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

## Identificação

- Turma: A
- Integrantes:
  - Felipe Boff Molski - Cartão 00208153
  - Marco Antônio de Souza Rodrigues - Cartão 00308589

## Bibliotecas

A implementação usa apenas bibliotecas padrão do Python. Não há dependências adicionais obrigatórias.

## Minimax com poda alfa-beta

A função `minimax_move` foi implementada em `advsearch/othello_aurafarmer/minimax.py` de forma genérica, usando apenas a interface comum dos estados dos jogos:

- `legal_moves()`
- `next_state(move)`
- `is_terminal()`
- `winner()`

A avaliação sempre considera o jogador da raiz da busca (`root_player`), independente de quem joga no nó atual, conforme exigido pelo enunciado. A profundidade `-1` representa busca ilimitada (o decremento é ignorado nesse caso).

Tratamento de "passa a vez": no Othello, o `next_state` já devolve um estado em que o próximo jogador pode ser o mesmo jogador atual quando o adversário não tem jogadas legais. Como o ramo max/min em `_alphabeta` é decidido por `state.player == root_player`, o algoritmo trata corretamente turnos consecutivos do mesmo jogador, sem assumir alternância estrita. O caso em que nenhum dos dois tem jogadas legais (`player is None`) é absorvido por `is_terminal()`, que retorna a avaliação antes de tentar gerar sucessores.

Ordenação de jogadas: as jogadas são ordenadas (`sorted`) antes da expansão para tornar o resultado determinístico e dar uma ordem estável à poda.

## Tic-Tac-Toe Misere (avaliação — item a da seção 2.2)

O agente em `advsearch/othello_aurafarmer/tttm_minimax.py` usa minimax com profundidade ilimitada, pois a profundidade máxima do jogo é 9 e o fator de ramificação decresce a cada jogada. A poda alfa-beta com ordenação explora a árvore inteira em frações de segundo, bem dentro do limite de 1 minuto.

A função `utility` retorna:

- `1` para vitória do jogador avaliado (`state.winner() == player`);
- `-1` para derrota;
- `0` para empate.

Como o `utility` só é definido em estados terminais e o minimax é ilimitado, o algoritmo joga de forma ótima.

**(i) O minimax sempre ganha ou empata contra o `randomplayer`?** Sim. Em rodadas executadas com o servidor (`python server.py tttm ...`), o minimax venceu jogando como B contra o random e também como W. Como o agente joga de forma ótima, nunca chega a perder contra um oponente aleatório (sempre existe pelo menos uma sequência de jogadas que evita formar 3 em linha, e a busca completa a encontra), de modo que não foram observadas derrotas.

**(ii) O minimax sempre empata consigo mesmo?** Sim. Em minimax(B) × minimax(W) o resultado foi empate (placar 0/0). Como ambos os lados jogam otimamente em um jogo de soma zero com solução conhecida (empate sob jogo perfeito), o resultado se repete em qualquer execução — a ordenação determinística de jogadas garante reprodutibilidade.

**(iii) O minimax não perde para um humano jogando bem?** Nas partidas em que jogamos manualmente contra o agente (via `advsearch/humanplayer/agent.py`), não conseguimos vencer o minimax usando estratégias conhecidas para o misere (ocupar o centro, evitar pares de marcas em linha/coluna/diagonal). O melhor resultado obtido pelo humano foi o empate, o que é consistente com o jogo ótimo do agente.

Resumo dos resultados:

| Partida | Resultado |
| --- | --- |
| Minimax (B) × Random (W) | Minimax venceu (W eliminado por formar 3 em linha) |
| Random (B) × Minimax (W) | Minimax venceu (B eliminado por formar 3 em linha) |
| Minimax (B) × Minimax (W) | Empate |
| Humano (melhor estratégia) × Minimax | Empate (humano não venceu em nenhuma rodada) |

## Othello

Foram implementadas três avaliações para Othello:

- `evaluate_count`: diferença entre a quantidade de peças do jogador e do oponente.
- `evaluate_mask`: diferença de valores posicionais usando a máscara fixa `EVAL_TEMPLATE` fornecida no enunciado.
- `evaluate_custom`: combinação linear de cinco componentes (descrita abaixo).

### Heurística customizada

A `evaluate_custom` (em `othello_minimax_custom.py`) combina cinco componentes clássicos da literatura de Othello, ponderados de forma a privilegiar mobilidade e controle de cantos no começo/meio do jogo e maximizar peças no fim:

- **Posicional (peso 3)**: usa o mesmo `EVAL_TEMPLATE` da `evaluate_mask`, somando o valor das casas ocupadas pelo jogador e subtraindo o das ocupadas pelo oponente.
- **Mobilidade (peso 10)**: diferença entre o número de jogadas legais do jogador e do oponente. Restringir o leque de respostas do oponente é considerado um dos sinais mais importantes em Othello.
- **Cantos (peso 35)**: diferença de cantos ocupados (cantos são casas estáveis — nunca podem ser capturados).
- **Casas "X" e "C" perigosas (peso 15)**: para cada canto ainda vazio, penaliza ocupar as 3 casas adjacentes a ele (linhas/colunas e a diagonal X), pois entregam o canto ao oponente.
- **Diferença de peças (peso variável)**: peso baixo (`0.5`) até ~52 peças no tabuleiro e peso alto (`2`) no fim do jogo, quando o número de peças vira o critério de vitória.

Estados terminais são avaliados como `+100000` / `-100000` / `0` para sobrepor qualquer outro componente.

**Fontes:** os componentes (mobilidade, estabilidade de cantos, casas X/C perigosas) e a própria máscara `EVAL_TEMPLATE` foram retirados de descrições clássicas de heurísticas de Othello, em particular a página <https://web.fe.up.pt/~eol/IA/MIA0203/trabalhos/Damas_Othelo/Docs/Eval.html> (referenciada também em `othello_minimax_mask.py`) e do artigo "An Analysis of Heuristics in Othello" de Sannidhanam & Annamalai. A combinação linear (pesos e a mudança de peso da contagem de peças no fim) foi calibrada empiricamente pelo grupo a partir das partidas do mini-torneio local.

### Critério de parada

Profundidade máxima fixa igual a 3 nos três agentes (`evaluate_count`, `evaluate_mask`, `evaluate_custom`). Essa escolha mantém todas as jogadas dentro do limite de 5 segundos exigido pelo enunciado, mesmo nas posições de meio de jogo (em que o fator de ramificação chega a ~10–15) e na máquina de referência mais lenta citada no enunciado (Xeon E5-2650). Aprofundamento iterativo não foi adotado nos agentes básicos para manter a comparação entre as três heurísticas justa (mesma profundidade).

## Mini-torneio de Othello (item b da seção 2.2)

Resultados coletados com o servidor do kit (`python server.py othello <p1> <p2> -d 10 -p 0`):

| Partida | Placar final | Vencedor |
| --- | --- | --- |
| Contagem (B) × Valor posicional (W) | B=30, W=34 | Valor posicional |
| Valor posicional (B) × Contagem (W) | B=52, W=12 | Valor posicional |
| Contagem (B) × Customizada (W) | B=28, W=36 | Customizada |
| Customizada (B) × Contagem (W) | B=41, W=23 | Customizada |
| Valor posicional (B) × Customizada (W) | B=16, W=48 | Customizada |
| Customizada (B) × Valor posicional (W) | B=42, W=22 | Customizada |

Resumo agregado:

| Heurística | Vitórias | Derrotas | Peças capturadas (total) |
| --- | --- | --- | --- |
| Customizada | 4 | 0 | 167 |
| Valor posicional | 2 | 2 | 124 |
| Contagem | 0 | 4 | 93 |

**Implementação mais bem-sucedida:** a heurística customizada (`evaluate_custom`), com 4 vitórias em 4 partidas e o maior total de peças capturadas. Em segundo, a `evaluate_mask` (2 vitórias, ambas contra a contagem).

## Agente de torneio

O arquivo `advsearch/othello_aurafarmer/tournament_agent.py` usa minimax com poda alfa-beta, profundidade 3 e a heurística `evaluate_custom`. Essa escolha foi feita porque:

- a heurística customizada teve o melhor desempenho no mini-torneio local (4/4 vitórias);
- atende à exigência do enunciado de não usar puramente nenhuma das duas heurísticas básicas;
- não gera processos/threads em background, não lê arquivos externos nem usa dados pré-calculados (sem risco de desclassificação por "doping");
- mantém o tempo por jogada bem abaixo dos 5 segundos exigidos.

O agente entregue para a competição do dia 03/junho poderá receber refinamentos adicionais (ajuste fino de pesos, aprofundamento iterativo limitado por tempo, ordenação de jogadas guiada pela heurística) sem alterar a estrutura aqui descrita.

## Extra: MCTS

Foi implementada uma versão opcional de MCTS em `advsearch/othello_aurafarmer/mcts.py`, com:

- seleção por UCT;
- expansão de jogadas não visitadas;
- simulação aleatória até estado terminal;
- retropropagação de vitória, empate ou derrota;
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
