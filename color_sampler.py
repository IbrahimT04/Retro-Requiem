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
    def blend_colors(color1, color2, weightage):
        """
        Blend two colors and return the blended color.

        :param weightage:
        :param color1: First color as an (R, G, B) tuple.
        :param color2: Second color as an (R, G, B) tuple.
        :return: Blended color as an (R, G, B) tuple.
        """
        blended_color = (
            int(color1[0] * weightage + color2[0] * (1.0-weightage)) // 2,  # Red
            int(color1[1] * weightage + color2[1] * (1.0-weightage)) // 2,  # Green
            int(color1[2] * weightage + color2[2] * (1.0-weightage)) // 2,  # Blue
        )
        return blended_color

    @staticmethod
    def darken_colors(color, weightage):
        """
        shade the color to be darker

        :param weightage: Weightage of the darkening
        :param color: Color as an (R, G, B) tuple.
        :return: Darkened color as an (R, G, B) tuple.
        """
        darkened_color = (
            int(color[0] * weightage),  # Red
            int(color[1] * weightage),  # Green
            int(color[2] * weightage),  # Blue
        )
        return darkened_color
