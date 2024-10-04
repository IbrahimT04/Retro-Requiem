# color_sampler.py

import pygame


class SpriteColorSampler:
    def __init__(self, wall_sprite_path):
        """
        Initialize the SpriteColorSampler with the given sprite image.

        :param wall_sprite_path: Path to the sprite image.
        """

        # Load the sprite image only once
        try:
            self.wall_sprite_image = pygame.image.load(wall_sprite_path)
            print("Sprite image loaded successfully.")
        except pygame.error as e:
            print(f"Failed to load sprite image: {e}")

    def get_color(self, x, y):
        """
        Get the color at the specified coordinates (x, y).

        :param x: X-coordinate of the pixel.
        :param y: Y-coordinate of the pixel.
        :return: Color at the given coordinates as a (R, G, B, A) tuple.
        """
        try:
            # Get the color at the specified pixel location
            color = self.wall_sprite_image.get_at((x, y))
            return color
        except Exception as e:
            print(f"Error retrieving color at ({x}, {y}): {e}")
            return None

    @staticmethod
    def blend_colors(color1, color2):
        """
        Blend two colors and return the blended color.

        :param color1: First color as an (R, G, B, A) tuple.
        :param color2: Second color as an (R, G, B, A) tuple.
        :return: Blended color as an (R, G, B, A) tuple.
        """
        blended_color = (
            int(color1[0] + color2[0]) // 2,  # Red
            int(color1[1] + color2[1]) // 2,  # Green
            int(color1[2] + color2[2]) // 2,  # Blue
            # (color1[3] + color2[3]) // 2   # Alpha (transparency)
        )
        return blended_color
