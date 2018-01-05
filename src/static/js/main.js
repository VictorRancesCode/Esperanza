/**
 * Created by victor on 31-12-17.
 */
function facebookPublish(url) {
    window.open('https://www.facebook.com/dialog/share?app_id=145634995501895&display=wap&href=' + url, '_blank');
}


$(document).ready(function () {
    $('#lenguaje-es').click(function () {
        postLang("es");
        return false;
    });
    $('#lenguaje-en').click(function () {
        postLang("en");
        return false;
    });
});

function postLang(lenguaje) {
    console.log(lenguaje)
    document.getElementById("select_lenguaje").value = lenguaje;
    document.getElementById("form-lenguaje").submit();
}