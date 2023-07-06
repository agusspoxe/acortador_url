document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();
    document.getElementById('btn_submit').disabled = true;

    const url_larga = document.querySelector('#url').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'escuchar_url_larga');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({"url_larga": url_larga}));

    xhr.onreadystatechange = function()
    {
        if(xhr.readyState == 4 && xhr.status == 200)
        {
            document.getElementById('btn_submit').disabled = false;
            var response = JSON.parse(xhr.responseText);
            const url_corta = response["respuesta"];
            console.log(url_corta);
            document.querySelector('#url_acortada_generada').textContent = url_corta;
        }
    }
});
