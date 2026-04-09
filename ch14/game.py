import pygame
import sys

def main():
    # ---------------------------------------------------------
    # SETUP PHASE
    # ---------------------------------------------------------
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Pygame with Exception Handling")
    except pygame.error as e:
        print(f"CRITICAL: Failed to initialize Pygame hardware: {e}")
        sys.exit(1)

    # 1. LOCALIZED EXCEPTION HANDLING (Asset Loading)
    # ---------------------------------------------------------
    # We try to load a file. If it fails, we catch the specific error
    # and recover by continuing the game without it.
    try:
        # Intentionally trying to load a file that doesn't exist
        player_image = pygame.image.load("missing_player_sprite.png")
    except FileNotFoundError as e:
        print(f"WARNING: Asset missing ({e}). Using a default colored square instead.")
        # Fallback logic goes here (e.g., drawing a simple rectangle)
    except pygame.error as e:
        print(f"WARNING: Image format not supported: {e}")

    clock = pygame.time.Clock()
    running = True
    print("Game started. Try pressing SPACE, ESCAPE, or clicking the mouse!")

    # 2. THE GLOBAL WRAPPER (Guaranteed Cleanup)
    # ---------------------------------------------------------
    # We wrap the entire game loop in a try-finally block.
    try:
        while running:

            # --- STEP 1: EVENT HANDLING ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("Event: Spacebar was pressed!")

                        # Let's simulate a random, unexpected crash happening in our game logic
                        # If you press SPACE, we divide by zero to trigger an exception!
                        print("Simulating a game crash now...")
                        crash_variable = 10 / 0

                    elif event.key == pygame.K_ESCAPE:
                        running = False

            # --- STEP 2: GAME LOGIC ---
            # (Game logic updates would go here)

            # --- STEP 3: DRAWING ---
            screen.fill((0, 0, 0))
            pygame.display.flip()
            clock.tick(60)

    # Catching any unexpected runtime errors during gameplay
    except Exception as e:
        print(f"\nFATAL GAME ERROR: The game crashed due to: {e}")
        # In a professional game, you might write this error to a crash_log.txt file here

    # The 'finally' block is our safety net.
    # It runs if the game ends normally OR if it crashes.
    finally:
        # ---------------------------------------------------------
        # CLEANUP PHASE
        # ---------------------------------------------------------
        print("\nExecuting guaranteed cleanup...")
        pygame.quit() # Safely destroys the window and frees hardware resources
        sys.exit()

# Python best practice: only run the main loop if this script is executed directly
if __name__ == "__main__":
    main()