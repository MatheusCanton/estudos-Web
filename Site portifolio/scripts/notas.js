const FATOR_MAC = 0.6
const FATOR_MP = 0.4
const provas = document.querySelector("td.prova input")
const acs =  document.querySelector("td.ac input")
const tdAc =  document.querySelector("td.mac")
const tdMp =  document.querySelector("td.mp")
const tdFinal = document.querySelector("td.final")

const adicionarAluno = document.querySelector("btn btn-sucesso adicionar-aluno")



const calculaMp =  function(){
    let nota = 0
    provas.forEach(function(prova){
        let valor = parseFloat(prova.value)
        if(valor > nota){
            nota = valor
        }
    })
    nota = nota * FATOR_MP
    
}

const calculaMac =  function(){
    let nota = 0, eZero =  false
    acs.forEach(function(ac){
        nota += parseFloat(ac.value)
        if(valor === 0 ){
            eZero =  true
        }
        nota += valor
    })

    if (!eZero){
        let media = (notaAC1 +notaAC2)/2,
        media = (notaAC1+notaAC2)/2,
        mac = (media *0.6).toFixed(2)
        tdAc.textContent = mac
        }       
}

const calculaMf = function(){
    let notaMac = parseFloat(tdMac.textContent),
        notaMp = parseFloat(tdMp.textContent),
        notaMf = notaMac +notaMp
    tdFinal.textContent = notaMf.toFixed(2)
        
}


acs.forEach(function(ac){
    ac.addEventListener('change',calculaMac)
    prova.addEventListener('change',calculaMp)
    prova.addEventListener('change',calculaMp)
})

provas.forEach(function(prova){
    ac.addEventListener('change',calculaMac)
    prova.addEventListener('change',calculaMp)
    prova.addEventListener('change',calculaMp)
})
adicionarAluno.addEventListener('click', function(){
    
    let tr = this.parentElement.parentElement,
    inputRa = tr.querySelector("input[name='ra']"),
    inputNome = tr.querySelector("input[name='nome']"),

    table = tr.parentElement.parentElement,
    tbody =  table.querySelector("tbody"),
    linhaTemplate = tbody.querySelector("tr"),
    clone =linhaTemplate.cloneNode(true)
    //fazer coisinhas
    
    clone.querySelector("td.ra").tdRa.textContent = inputRa
    clone.querySelector("td.nome").tdRa.textContent = inputNome
    clone.querySelectorAll('td.ac input').forEach(function(input){
        input.value = 0
        prova.addEventListener('change',calculaMp)
        prova.addEventListener('change',calculaMp)
    })

    clone.querySelectorAll('td.provas input').forEach(function(input){
        input.value = 0
    })
    
    clone.querySelectorAll("td.mac", "td.final").forEach(function(td){
        td.textContent ='0.0'
        if(td.className.indexOf("final") != -1){
            td.classList.remove("aprovado")
            td.classList.add("Reprovado")
        }

        
    })
    tbody.appendChild(clone) 
    
})