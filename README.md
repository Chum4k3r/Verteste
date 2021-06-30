# Verteste

Esse aplicativo é resultado de um processo avaliativo para a Vertesis.

Desenvolvido por: João Vitor Gutkoski Paes

Confira o codigo fonte no [Github](https://github.com/Chum4k3r/Verteste)


## Instalando

Faça o download do código fonte, ou clone o repositório

```
git clone https://github.com/Chum4k3r/Verteste verteste
```

Após concluído o download, instale o pacote usando pip:

```
pip install -e verteste
```


## Primeiros passos

Para abrir o programa, pode-se utilizar o seguinte comando:

```
python -m verteste
```

Assim, o programa será carregado a partir do módulo instalado e abrirá instantaneamente.

### Exemplos

Uma série de projetos de teste estão disponíveis no diretório `verteste/examples` e podem ser carregados no programa
para avaliar rapidamente algumas funcionalidades.


## Elementos do programa

O software trabalha com uma série de elementos, estes são Projetos, Listas e Linhas.

Os projetos são tratados no menu `Arquivo` pois à cada projeto pode ser criado um arquivo JSON para gurdar suas informações.

As listas e linhas são tratadas no menu `Editar` pois cada inclusão, remoção, ou edição, dizem respeito à uma edição do projeto.

O programa funciona com base no projeto e lista ativos, ou seja, o projeto e lista selecionados em suas respectivas caixas de seleção.


### Projetos

O programa funciona baseado em projetos. Cada projeto pode ser salvo em um arquivo JSON,
dessa forma, todas as funcionalidades do programa estarão disponíveis a partir de pelo menos um projeto aberto.

Um novo projeto pode ser criado a partir do menu `Arquivo > Novo projeto`, ou utilizando o atalho `Ctrl + Shift + N`.

Uma janela para inserir o Nome e a Descrição do projeto surgirá e, em caso de confirmação,
o projeto será adicionado a caixa de seleção e suas informações estarão disponíveis na região apropriada da interface gráfica.

Cada projeto pode conter diversas listas.


### Listas

Cada lista contém dados de causa e efeito, na forma de linhas de conteúdo.
Para criar uma nova lista em seu projeto, utilize o menu `Editar > Nova lista`, ou o atalho `Ctrl + N`.

Aparecerá uma janela para inserir o Nome da lista e, em caso de confirmação, a lista estará disponível na caixa de seleção
e suas informações estarão disponíveis nos campos apropriados.

Ainda assim, não existem linhas em nossa lista, então vamos incluí-las.


### Linhas

Para inserir novas linhas em sua lista utilize o menu `Editar > Inserir linha` ou o atalho `Ctrl + I`.
Surge, entao, uma janela para inserir as informações da linha.

Após inserir os dados, em caso de confirmação, a linha aparecerá na tabela abaixo das informações da lista.

Da mesma forma que a linha aparece abaixo da lista, as listas pertencentes ao projeto estão visíveis
no quadro abaixo das informações do projeto ativo.


### Editando informações

Todas as informações inseridas para criar Projetos, Listas ou Linhas são editáveis por meio dos menus ou atalhos.

Para editar o projeto, utiliza-se o menu `Arquivo > Alterar projeto` ou o atalho `Ctrl + Shift + E`. A mesma janela de criação
surgirá, agora com os dados do projeto já presentes para edição.

Para editar uma linha, utiliza-se o menu `Editar > Alterar linha`, ou o atalho `Ctrl + E`. A mesma janela de criação de linhas aparece,
agora com a caixa de seleção entitulada ID ativa, permitindo a escolha da linha que será editada e atualizando os campos
com as informações pré-existentes na linha.

Ao clicar duas vezes em uma linha, na tabela, a janela de edição de linha também aparece, porém, a única linha editável é a mesma clicada,
ou seja, a caixa de seleção de linhas estará desativada.

Uma lista só pode ter seu nome alterado, para isso, vá ao menu `Editar > Alterar lista` ou use o atalho `Ctrl + A`.
É possível editar o nome de uma lista que não está selecionada, ao clicar duas vezes em seu nome no quadro de listas, à esquerda na janela.
Esse procedimento tornará a lista ativa.


### Salvando e carregando informações

Após um certo tempo trabalhando no projeto, pode ser interessante salvá-lo para retomar seus dados em uma sessão futura, para isso,
basta utilizar o menu `Arquivo > Salvar projeto`, ou o atalho `Ctrl + S`.

Uma janela para escolher um nome de arquivo e local de armazenamento se apresentará. Após confirmar, todas as listas do projeto,
e as linhas presentes nas listas, serão salvas juntamente com o projeto em um arquivo JSON.

Para carregar um projeto salvo, vá ao menu `Arquivo > Abrir projeto`, ou o atalho `Ctrl + O`, uma janela similar a de salvamento
permite escolher o arquivo JSON de projeto que será aberto.


### Remover linhas, listas e fechar projetos

Um projeto que não será mais trabalhado pode ser removido da caixa de seleção. Para isso, selecione o projeto na caixa e vá ao menu
`Arquivo > Fechar projeto`, ou utilize o atalho `Ctrl + Shift + C`.

#### **Atenção! Qualquer alteração deve ser salva antes de fechar o mesmo.**

Caso uma lista, não seja mais necessária no projeto, o menu `Editar > Remover lista`. Uma janela com um quadro exibindo todas as listas
do projeto se abrira. Esse quadro permite múltipla seleção e, ao confirmar, as listas selecionadas serão removidas do projeto.

Para remover uma linha, o menu `Editar > Remover linha`, ou atalho `Ctrl + R` realizam o mesmo procedimento das listas, agora com o quadro
exibindo as linhas disponíveis.


### Demais menus

É possível consultar esse README a partir do programa no menu `Ajuda > Manual` ou o atalho `Ctrl + H`.

As informações sobre desenvolvimento e versao do software estao presentes no menu `Ajuda > Sobre`, ou `Ctrl + Shift + B`.




###### Santa Maria, 29 de junho de 2021
