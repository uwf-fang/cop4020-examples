document.addEventListener('DOMContentLoaded', () => {
    // --- Get References to DOM Elements ---
    const scoreDisplay = document.getElementById('score');
    const timeDisplay = document.getElementById('time');
    const startButton = document.getElementById('start-button');
    const gameArea = document.getElementById('game-area');
    const target = document.getElementById('target');
    const messageArea = document.getElementById('message-area');

    // --- Game State Variables ---
    let score = 0;
    let timeLeft = 15; // Initial time
    let gameInterval = null; // To hold the timer interval
    let isGameRunning = false;

    // --- Event Handlers ---

    /**
     * Handles the click event on the Start Button.
     * Initializes the game state and starts the timer.
     */
    function startGame() {
        if (isGameRunning) return; // Prevent starting multiple times

        // Reset game state
        score = 0;
        timeLeft = 15; // Reset timer duration
        scoreDisplay.textContent = score;
        timeDisplay.textContent = timeLeft;
        messageArea.textContent = ''; // Clear previous messages
        isGameRunning = true;
        startButton.disabled = true; // Disable button during game
        target.style.display = 'block'; // Make target visible

        moveTarget(); // Place the target initially

        // Start the game timer (an event triggered every second)
        gameInterval = setInterval(updateTimer, 1000);

        // Add the click listener to the target *only* when the game starts
        target.addEventListener('click', handleTargetClick);
    }

    /**
     * Handles the click event on the Target.
     * Increases score and moves the target.
     */
    function handleTargetClick() {
        if (!isGameRunning) return; // Only score if game is running

        score++;
        scoreDisplay.textContent = score;
        moveTarget(); // Move target immediately after click
    }

    /**
     * Updates the game timer every second.
     * Ends the game when time runs out.
     */
    function updateTimer() {
        timeLeft--;
        timeDisplay.textContent = timeLeft;

        if (timeLeft <= 0) {
            endGame();
        }
    }

    /**
     * Ends the game, clears the timer, and displays the final score.
     */
    function endGame() {
        isGameRunning = false;
        clearInterval(gameInterval); // Stop the timer event
        target.style.display = 'none'; // Hide the target
        startButton.disabled = false; // Re-enable start button
        messageArea.textContent = `Game Over! Final Score: ${score}`;

        // Important: Remove the target's click listener to prevent scoring after game ends
        target.removeEventListener('click', handleTargetClick);
    }

    /**
     * Moves the target to a random position within the game area.
     */
    function moveTarget() {
        const gameAreaWidth = gameArea.offsetWidth;
        const gameAreaHeight = gameArea.offsetHeight;
        const targetWidth = target.offsetWidth;
        const targetHeight = target.offsetHeight;

        // Calculate max possible top and left positions
        const maxTop = gameAreaHeight - targetHeight;
        const maxLeft = gameAreaWidth - targetWidth;

        // Generate random positions within bounds
        const randomTop = Math.max(0, Math.floor(Math.random() * maxTop));
        const randomLeft = Math.max(0, Math.floor(Math.random() * maxLeft));

        // Apply the new position using inline styles
        target.style.top = `${randomTop}px`;
        target.style.left = `${randomLeft}px`;
    }


    // --- Attach Initial Event Listener ---

    // The primary event listener that kicks everything off
    startButton.addEventListener('click', startGame);

});