# sistema-gerenciamento-de-estudantes
repository for the cesar school first python challenge, a students manager system

No README.md adicione as seguintes informações:

 a. Forneça detalhes da solução do desafio. Como você realizou? 

 b. Forneça detalhes sobre os comandos utilizados, como git init, git remote add origin, git add, git commit e git push, git checkout.

 c. Explique como você verificou seu código do desafio foi adicionado ao repositório no Github.

 d. Se você encontrou algum desafio ou dificuldade durante o processo e descreva como você resolveu esses problemas.

 ## Sobre o desafio:

 Desafio proposto após o módulo de python da formação Fast Transição - Turma 2.
 O desafio proposto consistia em codar um Sistema para gerenciamento de registro de estudantes, podendo adicionar, exibir, procurar e calcular a média dos estudantes. Além disso foi proposto que o sistema houvesse a função de escrever em arquivo e recuperar esses dados.

 ## Sobre a resolução do problema:

 Durante a abstração do desafio, decidi por usar uma lista de dicionários para armazenar esses estudantes, inicialmente pensei em utilizar um dicionário de dicionários, mas não encontrei uma forma consistente de realizar dessa forma.

 Comecei adicionando o texto principal no console que apresenta as opções do sistema, de 1 à 7, utilizei a estrutura "match case", devido a sua simplicidade e facilidade de compreensão. Já implementando a opção de sair utilizando a função exit() da biblioteca sys.

 Subi esse esbouço inicial num repositório criado no github à partir dos comandos git init, git remote add origin <URL-do-repositório>. Seguindo pelos comandos para subir os arquivos iniciais, git add *, git commit -m "", e git push origin main.

 Após isso decidi que dividiria cada operação em funções, para facilitar a manutenção do código e para dividir as responsabilidades. Criei uma função para cada opção do sistema de gerenciamento.

 ### Feature 1 - Adicionar registro

    Iniciei criando uma nova branch para trabalhar na primeira função adicionada ao sistema, realizando um git checkout -b "<nome-da-branch>.

 Externamente ao loop while que criei para repetir o código enquanto não for dado o comando de sair, criei uma lista de estudantes para onde os registros seriam adicionados. Na função adicionarAluno() capturei os dados necessários, "nome", "id" e "notas" essa última sendo adicionadas todas de uma vez com espaçamento. Tratei a entrada das notas com a função split para tornar as notas em uma lista, e apliquei a função eval() para converter todos os dados para int. Ao final é apresentada a confirmação da entrada seguida pelo retorno da função sendo a adição desses dados formatados adicionados a lista como um dicionário.

    Realizei a adição das alterações ao stage e commitei, as alterações na nova branch. No navegador realizei a checagem para ver se as alterações tinham subido e abri um novo pull request. Confirmando o pull, as alterações foram aplicadas a branch main.

 ### Feature 2 - Exibir registro de alunos

    Iniciei a segunda implementação criando uma nova branch git checkout -b "<nome-da-branch>.

 Para essa segunda função, foi adicionada uma nova entrada ao match case da nova função exibirAlunos().
 Essa função se limita a percorrer a lista e imprimir os dicionários inseridos através de um laço for na lista de estudantes.

    Após finalizado o processo de subir as alterações e abrir pull request. Aprovando em seguida.

 ### Feature 3 - Procurar estudante pelo ID

    Nova branch criada.

 O case '3' foi adicionado para a nova função procurarAlunoPeloId(id).
 Essa função recebe como parâmetro um id, em que ele percorrer a lista checando os id's inseridos, ao encontrar ele retorna a mensagem de encontrado e retorna o dicionário do estudante, o return para a execução do loop. Caso não seja encontrado a mensagem de aluno não encontrado é exibida.

    As alterações foram adicionadas ao repositório remoto e solicitado o pull request, seguido pela aprovação.

 ### Feature 4 - Calcular média das Notas

    Nova branch criada e case '4' adicionado ao código.

 Essa função possui duas variáveis, uma para o somatório das notas e outra para a quantidade de notas, então a lista é percorrida realizando a função sum() nas notas e capturando o tamanho da lista com o len(), ao final do loop a média é calculada levando em consideração esses dois valores e retornando ao console.

    As alterações foram adicionadas ao repositório remoto e solicitado o pull request, seguido pela aprovação.

  ### Feature 5 - Salvar os Resgistros em Arquivo

    Nova branch criada e case '5' adicionado ao código.

  A função salvarRegistrosEmTxt(), utiliza a declaração with open("arquivo", "w") para gerar um novo arquivo onde é passado dentro dela um loop na lista de estudantes e formatação utilizanda, passando vírgula para separar as entradas e quebra de linha entre alunos, para que fique um aluno por linha.

    As alterações foram adicionadas ao repositório remoto e solicitado o pull request, seguido pela aprovação.

 ### Feature 6 - Carregar os Resgistros do Arquivo

     Nova branch criada e case '6' adicionado ao código.

A última função adicionada carregarRegistroTxt() tem a função de abrir um arquivo, capturar os registros e armazenar na lista para ser reutilizado pelas outras funções do sistema.

Essa última funcionalidade percorre as linhas do arquivo, capturando os registros, formatando utilizando as funções strip() e replace(), para então adicionálas a uma lista de retorno. Após finalizar esse processo, essa lista então é percorrida e transformada num formato de dicionário, e então readicionada a lista de alunos do sistema utilizando a função append(). Após finalizar todo o processo uma mensagem é exibida, demonstrando que o carregamento foi realizado com sucesso.

    As alterações então foram adicionadas ao repositório remoto e solicitado o pull request, seguido pela aprovação.

## Considerações finais.

O desafio proposto foi ótimo para reforçar os conceitos de manipulação de arquivos e trabalho com versionamento de códigos. A todo momento tomando o devido cuidado de trabalhar cada feature nova em uma nova branch para só então ser adicionada a branch principal através de um pull request.

As maiores dificuldades que tive durante a execução do desafio foi escolher qual a estrutura de dados mais adequada para armazenar os alunos e o tratamento das strings capturadas no arquivo de texto, que vem ser devidamente tratadas e tipadas para poder retornar ao sistema principal.

Agradeço a equipe da Cesar School e aos companheiros de turma pela ajuda e pelas discussões sobre o desafio.