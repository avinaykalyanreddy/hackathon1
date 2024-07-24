document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("text1").addEventListener("animationend", function() {
        document.getElementById("login-form").style.display = "block";
    });
});


function togglePassword() {
    var passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
    } else {
        passwordField.type = "password";
    }
}
