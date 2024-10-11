document.getElementById('caixa-upload').addEventListener('click', function() {
    document.getElementById('input-arquivo').click();
});

document.getElementById('input-arquivo').addEventListener('change', function(evento) {
    const arquivo = evento.target.files[0];
    if (arquivo && arquivo.name.endsWith('.csv')) {
        alert('Arquivo CSV selecionado: ' + arquivo.name);
    } else {
        alert('Por favor, selecione um arquivo CSV.');
    }
});

document.getElementById('caixa-upload').addEventListener('dragover', function(evento) {
    evento.preventDefault();
    this.style.backgroundColor = '#ececff';
});

document.getElementById('caixa-upload').addEventListener('dragleave', function(evento) {
    this.style.backgroundColor = 'transparent';
});

document.getElementById('caixa-upload').addEventListener('drop', function(evento) {
    evento.preventDefault();
    this.style.backgroundColor = 'transparent';

    const arquivo = evento.dataTransfer.files[0];
    if (arquivo && arquivo.name.endsWith('.csv')) {
        alert('Arquivo CSV carregado: ' + arquivo.name);
    } else {
        alert('Por favor, solte um arquivo CSV.');
    }
});