Calculadora de Média de Aluno

Programa em Python que calcula a média das notas de um aluno a partir de notas digitadas pelo usuário no terminal, informando ao final se o aluno foi aprovado ou reprovado.

 Descrição

O programa solicita o nome do aluno e, em seguida, permite que o usuário digite quantas notas quiser, uma por vez. A cada nota digitada, ela é armazenada em uma lista. Quando o usuário digitar a letra S, a entrada de notas é encerrada e o programa calcula automaticamente a média e exibe a situação final do aluno (aprovado ou reprovado).

Funcionalidades

Cadastro do nome do aluno via input().
Entrada de múltiplas notas em um laço while, até o usuário digitar S para sair.
Cálculo automático da média das notas inseridas.
Verificação da situação do aluno:
Aprovado, se a média for maior ou igual a 7.
Reprovado, caso contrário.
Tratamento para o caso em que nenhuma nota foi inserida (lista vazia), exibindo uma mensagem de aviso ao invés de tentar calcular a média.
Relatório final formatado, exibido no terminal com o nome do aluno, a média calculada e a situação.

 Como executar
 
Certifique-se de ter o Python 3 instalado. Você pode verificar com:
bash
   python3 --version
Clone este repositório:
bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
Execute o script:
bash
   python3 media_aluno.py
   
 Exemplo de uso
 
Digite o nome do aluno: Maria
Digite a nota do aluno (ou 'S' para sair): 8.5
Digite a nota do aluno (ou 'S' para sair): 7.0
Digite a nota do aluno (ou 'S' para sair): S
Operação encerrada
_______________________________________________________
Nome do aluno: Maria
Média = 7.75
Situação do aluno: Aluno Aprovado

 Tecnologias utilizadas
 
Python 3

 Estrutura do código
 
Trecho	Conteúdo
Entrada de dados	Cadastro do nome do aluno e laço while para receber as notas até S
Cálculo da média	Verificação se a lista de notas está vazia e cálculo com sum()/len()
Situação do aluno	Estrutura if/else que define aprovação (média ≥ 7) ou reprovação
Relatório final	Exibição formatada do nome, média e situação do aluno no terminal

 Limitações conhecidas
 
O programa não trata a entrada de valores inválidos (que não sejam número nem a letra S), o que pode gerar um erro de conversão (ValueError).
Se o usuário digitar S maiúsculo ou minúsculo, o programa reconhece normalmente (entrada.lower() == 's'), mas qualquer outra letra é tratada como tentativa de nota numérica.
Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar.
