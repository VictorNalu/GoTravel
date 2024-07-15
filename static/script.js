 // Button clicks and form visibility handler
 document.getElementById('loginButton').addEventListener('click', function () {
    document.getElementById('overlay').style.display = 'flex';
    document.getElementById('popupForm').classList.remove('hidden');
});
document.getElementById('signUpButton').addEventListener('click', function () {
    document.getElementById('overlay').style.display = 'flex';
    document.getElementById('popupForm').classList.remove('hidden');
});
document.getElementById('closeButton').addEventListener('click', function () {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('popupForm').classList.add('hidden');
});
