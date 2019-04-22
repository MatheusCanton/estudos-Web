var aluno = "Joao da Silva",
    n1 = 7,
    n2 = 6.5

//var media = n1 *0.6 + n2 *04


function calculadoraDeMedia(vetor_notas){
    
    for(var contador =0 ;contador < notas.legth; contador++) {
        media += vetor_notas[contador]

    }   
    media = media /vetor_notas.legth
    return media 
}

var  merdia = 0,
       // contador = 0
//while (contador < notas.length)
  //  media += notas[contador]
    //contador += //ou ++

    for(var contador =0 ;contador < notas.legth; contador++) {

    }    
media = media/contador

console.log("Nota final de "+aluno+"é"+media)

if (media >= 6){
    console.log("Aluno"+aluno+"Passou!")

}else if (media <6 && media >=3 ){
    console.log("Aluno"+aluno+"Ficou de recuperação")

}else{
    console.log("Aluno"+aluno+"Nao passou")
}

