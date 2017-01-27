# finding-combo 
Implementation of the techniques described in the papers: 
 - "Attempting to find infinite combos in fighting games using hidden markov models"
 
    [Slides] http://homepages.dcc.ufmg.br/~gzuin/arquivos/pres_attempting-discover-infinite.pdf
    [Paper]  http://homepages.dcc.ufmg.br/~gzuin/arquivos/artigos/attempting-discover-infinite-cor3.pdf

- "Discovering combos in fighting games trough evolutionary methods"

    [Slides] http://homepages.dcc.ufmg.br/~gzuin/arquivos/pres_discovering-combos-fighting.pdf
    [Paper]  http://dl.acm.org/citation.cfm?id=2908908 

	
	
The first one basically uses hidden markov models to train a machine to find large combos inside fighting games. The consultations are made using the viterbi algorithm.
The second paper addresses the usage of an evolutionary method to evolve a population of small combos (generated randomly and with our previous knowledge) into a large one through multiple the generations.
