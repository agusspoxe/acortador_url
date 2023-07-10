function isValidUrl(url_larga) {
    console.log("checking: " + url_larga);
    try {
        new URL(url_larga);
        return true;
    } catch (err) {
        return false;
    }
}

function acorta_url(url_larga) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'escuchar_url_larga');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ "url_larga": url_larga }));

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
            const url_corta = response["respuesta"];
            // console.log(url_corta);
            // document.querySelector('#url_acortada_generada').textContent = url_corta;

            document.getElementById('url_acortada_error').classList.add("hidden");
            document.getElementById('url_acortada_title').classList.remove("hidden");
            var a = document.getElementById('url_acortada_generada'); //or grab it by tagname etc
            a.textContent = url_corta;
            a.href = 'http://' + url_corta;
        }

        document.getElementById('btn_submit').disabled = false;
        document.getElementById('btn_submit').classList.remove("disabled");

    }
}

document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();
    const url_larga = document.querySelector('#url').value;
    if (isValidUrl(url_larga)) {
        document.getElementById('btn_submit').classList.add("disabled");
        document.getElementById('btn_submit').disabled = true;
        acorta_url(url_larga);
    } else {
        console.error("URL invalida");
        document.getElementById('url_acortada_error').classList.remove("hidden");
    }
});
