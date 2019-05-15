var primeiroNumero;
var segundoNumero;
const Soma = '+';
const Subtracao = '-';
const Multiplicacao = '*';
const Divisao = '/';
const msgError = 'Erro de operação';
const Vazio = '';
const Ponto = '.';
var quebrado;
const Botoes = document.querySelectorAll('button');
const Resultado = document.querySelector('#resultado');

Resultado.readOnly = true;

for (let i = 0; i < Botoes.length; i++) {
    Botoes[i].addEventListener('click', function () {

        if (this.classList.contains('clear')) {
            LimparResultado(Resultado);
        }

        if (Resultado.value == msgError) {
            return
        }

        if (this.classList.contains('numero')) {

            if (isNaN(getTextContent(this))) {

                if (Resultado.value.includes(Subtracao)) {
                    VerificaPonto(Resultado.value, Subtracao);
                }

                else if (Resultado.value.includes(Multiplicacao)) {
                    VerificaPonto(Resultado.value, Multiplicacao);
                }

                else if (Resultado.value.includes(Divisao)) {
                    VerificaPonto(Resultado.value, Divisao);
                }

                else {
                    VerificaPonto(Resultado.value, Soma);
                }

            }
            else {
                Resultado.value += getTextContent(this);
            }
        }

        if (this.classList.contains('somar') || this.classList.contains('subtrair') ||
            this.classList.contains('multiplicar') || this.classList.contains('dividir')) {

            Resultado.value == Vazio || Resultado.value.includes(Soma) || Resultado.value.includes(Subtracao) ||
                Resultado.value.includes(Multiplicacao) || Resultado.value.includes(Divisao)
                ? null : Resultado.value += getTextContent(this);
        }

        if (this.classList.contains('resultar')) {

            if (Resultado.value.includes(Soma)) {
                Resultado.value = Somar(Resultado, Soma);
            }

            else if (Resultado.value.includes(Subtracao)) {
                Resultado.value = Subtrair(Resultado, Subtracao);
            }

            else if (Resultado.value.includes(Multiplicacao)) {
                Resultado.value = Multiplicar(Resultado, Multiplicacao);
            }

            else if (Resultado.value.includes(Divisao)) {
                Resultado.value = Dividir(Resultado, Divisao);
            }
        }
    });
}

function getTextContent(obj) {
    return obj.textContent
}

function Somar(objResultado, soma) {

    quebrado = Quebra(objResultado, soma);
    primeiroNumero = quebrado[0];
    segundoNumero = quebrado[1];

    if (segundoNumero == Vazio)
        return msgError;
    else
        return parseFloat(primeiroNumero) + parseFloat(segundoNumero);
}

function Subtrair(objResultado, subtracao) {

    quebrado = Quebra(objResultado, subtracao);
    primeiroNumero = quebrado[0];
    segundoNumero = quebrado[1];

    if (segundoNumero == Vazio)
        return msgError;
    else
        return parseFloat(primeiroNumero) - parseFloat(segundoNumero);
}

function Multiplicar(objResultado, multiplicacao) {

    quebrado = Quebra(objResultado, multiplicacao);
    primeiroNumero = quebrado[0];
    segundoNumero = quebrado[1];

    if (segundoNumero == Vazio)
        return msgError;
    else
        return parseFloat(primeiroNumero) * parseFloat(segundoNumero);
}

function Dividir(objResultado, divisao) {

    quebrado = Quebra(objResultado, divisao);
    primeiroNumero = quebrado[0];
    segundoNumero = quebrado[1];

    if (segundoNumero == Vazio)
        return msgError;
    else
        return parseFloat(primeiroNumero) / parseFloat(segundoNumero);
}

function Quebra(objResultado, quebra) {
    return objResultado.value.split(quebra);
}

function LimparResultado(objResultado) {
    objResultado.value = Vazio
}

function VerificaPonto(objResultado, corte) {

    quebrado = objResultado.split(corte);

    if (quebrado.length > 1) {

        segundoNumero = quebrado[1]
        
        if (!segundoNumero.includes(Ponto)) {
            Resultado.value += Ponto
            //Se eu quiser substituir o . por 0  faço if abaixo.
            // if (!primeiroNumero.includes(Ponto)) {
            //if(Resultado.value == Vazio)
            //Resultado.value += 0;
            //Resultado.value += Ponto;

        }
    }
    else {

        primeiroNumero = quebrado[0];

        if (!primeiroNumero.includes(Ponto)) {
            Resultado.value += Ponto;
        }
    }
}