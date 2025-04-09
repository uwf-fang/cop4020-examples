document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contactForm');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const nameCount = document.getElementById('nameCount');
    const emailFeedback = document.getElementById('emailFeedback');
    const message = document.getElementById('responseMessage');
    const clearBtn = document.getElementById('clearBtn');
    const submitBtn = document.getElementById('submitBtn');

    // Helper function: validate email format
    function isValidEmail(email) {
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return pattern.test(email);
    }

    // Feature 1: Real-time character counter
    nameInput.addEventListener('input', () => {
        nameCount.textContent = `${nameInput.value.length} characters`;
    });

    // Feature 2: Live email validation feedback
    emailInput.addEventListener('input', () => {
        if (emailInput.value.trim() === '') {
            emailFeedback.textContent = '';
        } else if (!isValidEmail(emailInput.value)) {
            emailFeedback.textContent = 'Invalid email format';
            emailFeedback.className = 'error';
        } else {
            emailFeedback.textContent = 'Valid email!';
            emailFeedback.className = 'success';
        }
    });

    // Feature 3: Handle form submission
    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const name = nameInput.value.trim();
        const email = emailInput.value.trim();

        if (name === '' || email === '') {
            message.textContent = 'Please fill in all fields.';
            message.className = 'error';
            return;
        }

        if (!isValidEmail(email)) {
            message.textContent = 'Please enter a valid email.';
            message.className = 'error';
            return;
        }

        message.textContent = `Thanks, ${name}! We'll contact you at ${email}.`;
        message.className = 'success';

        // Add a quick animation effect
        message.style.opacity = 0;
        setTimeout(() => {
            message.style.opacity = 1;
        }, 100);

        // Reset form
        form.reset();
        nameCount.textContent = '0 characters';
        emailFeedback.textContent = '';
    });

    // Feature 4: Clear form with confirmation
    clearBtn.addEventListener('click', () => {
        const confirmClear = confirm('Are you sure you want to clear the form?');
        if (confirmClear) {
            form.reset();
            nameCount.textContent = '0 characters';
            emailFeedback.textContent = '';
            message.textContent = '';
        }
    });

    // Feature 5: Hover effect is handled via CSS in <style>
});
