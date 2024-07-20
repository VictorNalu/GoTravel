 // Login pop-up form handler
 document.getElementById('loginButton').addEventListener('click', function () {
    document.getElementById('overlay').style.display = 'flex';
    document.getElementById('popupForm').classList.remove('hidden');
});

// Login pop-up close form handler
document.getElementById('closeButton').addEventListener('click', function () {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('popupForm').classList.add('hidden');
});

// Sign Up pop-up form handler
document.getElementById('signUpButton').addEventListener('click', function () {
    document.getElementById('signUp_overlay').style.display = 'flex';
    document.getElementById('signUp_popupForm').classList.remove('hidden');
});

// Sign Up pop-up close form handler
document.getElementById('closeSignUpButton').addEventListener('click', function () {
    document.getElementById('signUp_overlay').style.display = 'none';
    document.getElementById('signUp_popupForm').classList.add('hidden');
});

