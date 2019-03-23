function getPesoAltura(){
    var {PythonShell} = require('python-shell')
    var path = require('path')

    var peso = document.getElementById("peso").value
    var altura = document.getElementById("altura").value

    document.getElementById("peso").value = ""
    document.getElementById("altura").value = ""

    var opcoes = {
        scriptPath: path.join(__dirname, '../_engine/'),
        args: [peso, altura]
    }

    var imc = new PythonShell('imc.py', opcoes)

    imc.on("message", function(message){
        swal(message)
    })
}