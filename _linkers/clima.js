function getClima() {
    var python = require("python-shell")
    var path = require("path")

    var cidade = document.getElementById("cidade").value
    document.getElementById("cidade").value = ""

    var opcoes = {
        scriptPath : path.join(__dirname, '/_engine/'),
        args : [cidade]
    }

    var clima = new python('clima.py', opcoes);

    clima.on('message', function(message) {
        swal(message);
    })
}