

var transacoes = []; // Array para armazenar transações

document.addEventListener('DOMContentLoaded', function () {
  // Carregar transações salvos ao iniciar a página
  abrirTransacoes();
});

function inserirTransacao() {
  var dataTransacao = document.getElementById('dataTransacao').value;
  var descricao = document.getElementById('descricao').value;
  var valor = document.getElementById('valor').value;
  var saldo = document.getElementById('saldo').value;
  var numeroConta = document.getElementById('numeroConta').value;

  var transacao = {
    data: dataTransacao,
    descricao: descricao,
    valor: valor,
    saldo: saldo,
    numeroConta: numeroConta
  };

  transacoes.push(transacao);

  // Limpar campos de entrada
  limparCampos();

  // Atualizar tabela de transações
  listarTransacoes();

  // Salvar transações no localStorage
  salvarTransacoes();
}

function listarTransacoes() {
  var tabelaTransacoes = document.getElementById('tabelaTransacoes');
  tabelaTransacoes.innerHTML = ''; // Limpar tabela

  // Cabeçalho da tabela
  var cabecalho = tabelaTransacoes.insertRow();
  cabecalho.insertCell(0).textContent = 'Data da Transação';
  cabecalho.insertCell(1).textContent = 'Descrição';
  cabecalho.insertCell(2).textContent = 'Valor';
  cabecalho.insertCell(3).textContent = 'Saldo';
  cabecalho.insertCell(4).textContent = 'Número da Conta';
  cabecalho.insertCell(5).textContent = 'Ação'; // Nova coluna para o botão de exclusão


  // Adicionar transações à tabela
  for (var i = 0; i < transacoes.length; i++) {
    var linha = tabelaTransacoes.insertRow();
    linha.insertCell(0).textContent = transacoes[i].data;
    linha.insertCell(1).textContent = transacoes[i].descricao;
    linha.insertCell(2).textContent = transacoes[i].valor;
    linha.insertCell(3).textContent = transacoes[i].saldo;
    linha.insertCell(4).textContent = transacoes[i].numeroConta;

    //Adicionar botão de exclusão
    var cellAcao = linha.insertCell(5);
    var btnExcluir = document.createElement('button');
    btnExcluir.textContent = 'Excluir';
    btnExcluir.addEventListener('click', criarFuncaoExcluir(i));
    cellAcao.appendChild(btnExcluir);
  }
}
function criarFuncaoExcluir(indice) {
  return function () {
  excluirTransacao(indice);
  };
}
      
function excluirTransacao(indice) {
  transacoes.splice(indice, 1);
  listarTransacoes();
}

function limparCampos() {
  document.getElementById('dataTransacao').value = '';
  document.getElementById('descricao').value = '';
  document.getElementById('valor').value = '';
  document.getElementById('saldo').value = '';
  document.getElementById('numeroConta').value = '';
}

function salvarTransacoes() {
  // Salvar transações no localStorage
  localStorage.setItem('transacoes', JSON.stringify(transacoes));
}

function abrirTransacoes() {
  // Recuperar transações do localStorage ao iniciar a página
  var transacoesSalvas = localStorage.getItem('transacoes');
  if (transacoesSalvas) {
    transacoes = JSON.parse(transacoesSalvas);
    listarTransacoes();
  }
}








