function getSoma() {
    var {PythonShell} = require("python-shell")
    var path = require("path")

    var termo = document.getElementById("termo").value
    document.getElementById("termo").value = ""

    var opcoes = {
        scriptPath : path.join(__dirname, '../_engine/'),
        args : [termo]
    }

    var somaFib = new PythonShell('somaFib.py', opcoes);

    somaFib.on('message', function(message) {
        swal(message);
    })
}