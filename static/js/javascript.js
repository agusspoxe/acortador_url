document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();

    const URLoriginal = document.querySelector('#url').value;
    const URLcorta = "https://equipoA.com";

    document.querySelector('#equipoA').textContent = URLcorta;

    console.log("YUHUUUUU");
});