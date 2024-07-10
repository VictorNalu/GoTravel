$(document).ready(function() {
    // Function to handle login
    function handleLogin(event) {
        event.preventDefault();
        const email = $('#login-email').val();
        const password = $('#login-password').val();

        $.ajax({
            url: '/login',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ email, password }),
            success: function(data) {
                if (data.success) {
                    alert('Login successful!');
                    window.location.href = '/dashboard';
                } else {
                    alert('Login failed: ' + data.message);
                }
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    }

    // Function to handle signup
    function handleSignup(event) {
        event.preventDefault();
        const email = $('#signup-email').val();
        const password = $('#signup-password').val();
        const confirmPassword = $('#signup-confirm-password').val();

        if (password !== confirmPassword) {
            alert('Passwords do not match');
            return;
        }

        $.ajax({
            url: '/signup',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ email, password }),
            success: function(data) {
                if (data.success) {
                    alert('Signup successful! Please log in.');
                    window.location.href = '/login.html';
                } else {
                    alert('Signup failed: ' + data.message);
                }
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    }

    // Function to load recommendations
    function loadRecommendations() {
        $.getJSON('/recommendations', function(data) {
            const recommendationsContainer = $('#recommendations');
            data.forEach(function(recommendation) {
                recommendationsContainer.append(`
                    <div>
                        <h3>${recommendation.title}</h3>
                        <img src="${recommendation.image}" alt="${recommendation.title}">
                        <p>${recommendation.description}</p>
                    </div>
                `);
            });
        }).fail(function(error) {
            console.error('Error:', error);
        });
    }

    // Function to load most visited places
    function loadMostVisitedPlaces() {
        $.getJSON('/most-visited-places', function(data) {
            const placesContainer = $('.most-visited-places');
            placesContainer.empty();
            data.forEach(function(place) {
                placesContainer.append(`<div><img src="${place.image}" alt="${place.name}"></div>`);
            });
        }).fail(function(error) {
            console.error('Error:', error);
        });
    }

    // Function to load festivals
    function loadFestivals() {
        $.getJSON('/festivals', function(data) {
            const festivalsContainer = $('.festivals-images');
            festivalsContainer.empty();
            data.forEach(function(festival) {
                festivalsContainer.append(`<div><img src="${festival.image}" alt="${festival.name}"></div>`);
            });
        }).fail(function(error) {
            console.error('Error:', error);
        });
    }

    // Add event listeners
    $('#login-form').on('submit', handleLogin);
    $('#signup-form').on('submit', handleSignup);

    // Load dynamic content
    loadRecommendations();
    loadMostVisitedPlaces();
    loadFestivals();
});
