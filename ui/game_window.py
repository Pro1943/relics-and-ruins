"""
RPG Game Window using Pygame - Grid-based movement with performance optimization
"""
import sys
import random
from pathlib import Path
from typing import Dict, Tuple, Set, Optional

import pygame  # [web:4]

# Game constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TILE_SIZE = 40
GRID_WIDTH = WINDOW_WIDTH // TILE_SIZE  # 32 tiles
GRID_HEIGHT = WINDOW_HEIGHT // TILE_SIZE  # 18 tiles
LOADING_RADIUS = 4  # 4x4 tiles loaded with properties
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
FOREST_GREEN = (34, 139, 34)
TREE_BROWN = (101, 67, 33)
RED = (255, 0, 0)

# Asset paths
BASE_PATH = Path(__file__).parent.parent
TEXTURES_PATH = BASE_PATH / "textures"
PLAYER_TEXTURE = TEXTURES_PATH / "charecters" / "boy.png"
GRASS_TEXTURE = TEXTURES_PATH / "blocks" / "grass.png"
TREES_FOLDER = TEXTURES_PATH / "blocks" / "trees"


class Tile:
    """Represents a single tile in the grid"""

    def __init__(self, x: int, y: int, tile_type: str = "grass"):
        self.x = x
        self.y = y
        self.tile_type = tile_type
        self.has_tree = False
        self.properties_loaded = False

    def load_properties(self):
        """Load full properties for tiles in loading radius"""
        self.properties_loaded = True

    def unload_properties(self):
        """Unload properties for tiles outside loading radius"""
        self.properties_loaded = False


class TileMap:
    """Manages the tile grid and rendering"""

    def __init__(self, width: int, height: int, screen: pygame.Surface):
        self.width = width
        self.height = height
        self.screen = screen
        self.tiles: Dict[Tuple[int, int], Tile] = {}
        self.loaded_chunks: Set[Tuple[int, int]] = set()
        self.tree_positions: Set[Tuple[int, int]] = set()

        # Textures
        self.grass_surface = self.load_grass_texture()
        self.tree_surface = self.load_tree_texture()

        self.initialize_map()
        self.spawn_trees()

    def load_grass_texture(self) -> pygame.Surface:
        """Load grass tile texture"""
        if GRASS_TEXTURE.exists():
            try:
                img = pygame.image.load(str(GRASS_TEXTURE)).convert_alpha()  # [web:19]
                img = pygame.transform.smoothscale(img, (TILE_SIZE, TILE_SIZE))  # [web:13]
                return img
            except Exception as e:
                print(f"Failed to load grass texture: {e}")

        # Create placeholder grass texture
        surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        surface.fill(FOREST_GREEN)
        return surface

    def load_tree_texture(self) -> pygame.Surface:
        """Load tree texture"""
        tree_file = TREES_FOLDER / "tree1.png"
        if tree_file.exists():
            try:
                img = pygame.image.load(str(tree_file)).convert_alpha()  # [web:19]
                width = int(TILE_SIZE * 1.5)
                height = int(TILE_SIZE * 1.5)
                img = pygame.transform.smoothscale(img, (width, height))  # [web:13]
                return img
            except Exception as e:
                print(f"Failed to load tree texture: {e}")

        # Create placeholder tree texture
        width = int(TILE_SIZE * 1.5)
        height = int(TILE_SIZE * 1.5)
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill(TREE_BROWN)
        return surface

    def initialize_map(self):
        """Create all tiles"""
        for y in range(self.height):
            for x in range(self.width):
                tile = Tile(x, y, "grass")
                self.tiles[(x, y)] = tile

    def spawn_trees(self):
        """Spawn trees randomly, only once"""
        tree_spawn_chance = 0.05
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < tree_spawn_chance:
                    self.tiles[(x, y)].has_tree = True
                    self.tree_positions.add((x, y))

    def update_loaded_chunks(self, player_x: int, player_y: int):
        """Update which chunks are loaded with full properties"""
        # Clear old loaded chunks
        for pos in self.loaded_chunks:
            x, y = pos
            if (x, y) in self.tiles:
                self.tiles[(x, y)].unload_properties()

        self.loaded_chunks.clear()

        # Load new chunks in radius
        for dy in range(-LOADING_RADIUS, LOADING_RADIUS + 1):
            for dx in range(-LOADING_RADIUS, LOADING_RADIUS + 1):
                nx = player_x + dx
                ny = player_y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    self.tiles[(nx, ny)].load_properties()
                    self.loaded_chunks.add((nx, ny))

    def get_tile(self, x: int, y: int) -> Optional[Tile]:
        """Get tile at position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles.get((x, y))
        return None

    def draw(self, camera_offset: Tuple[int, int]):
        """Draw all tiles and trees"""
        offset_x, offset_y = camera_offset

        # Draw grass
        for y in range(self.height):
            for x in range(self.width):
                screen_x = x * TILE_SIZE + offset_x
                screen_y = y * TILE_SIZE + offset_y

                # Cull tiles outside screen
                if (
                    screen_x + TILE_SIZE < 0
                    or screen_x > WINDOW_WIDTH
                    or screen_y + TILE_SIZE < 0
                    or screen_y > WINDOW_HEIGHT
                ):
                    continue

                self.screen.blit(self.grass_surface, (screen_x, screen_y))

        # Draw trees (on top)
        for (x, y) in self.tree_positions:
            screen_x = x * TILE_SIZE + TILE_SIZE // 2 + offset_x
            screen_y = y * TILE_SIZE + TILE_SIZE // 2 + offset_y

            tree_rect = self.tree_surface.get_rect(center=(screen_x, screen_y))
            self.screen.blit(self.tree_surface, tree_rect.topleft)


class Player:
    """Represents the player entity"""

    def __init__(self, x: int, y: int, screen: pygame.Surface):
        self.grid_x = x
        self.grid_y = y
        self.screen = screen
        self.surface = self.load_texture()

    def create_placeholder_texture(self) -> pygame.Surface:
        """Create placeholder player texture"""
        surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        surface.fill(RED)
        return surface

    def load_texture(self) -> pygame.Surface:
        """Load player texture"""
        surface = self.create_placeholder_texture()
        if PLAYER_TEXTURE.exists():
            try:
                img = pygame.image.load(str(PLAYER_TEXTURE)).convert_alpha()  # [web:19]
                # Scale by height, preserve aspect ratio
                ratio = TILE_SIZE / img.get_height()
                new_width = int(img.get_width() * ratio)
                img = pygame.transform.smoothscale(img, (new_width, TILE_SIZE))  # [web:13]
                surface = img
            except Exception as e:
                print(f"Failed to load player texture: {e}")
        return surface

    def move(self, dx: int, dy: int, tilemap: TileMap) -> bool:
        """Move player if valid (blocks on trees and bounds)"""
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy

        # Check bounds
        if not (0 <= new_x < tilemap.width and 0 <= new_y < tilemap.height):
            return False

        # Check collision with trees
        tile = tilemap.get_tile(new_x, new_y)
        if tile and tile.has_tree:
            return False

        # Movement is valid
        self.grid_x = new_x
        self.grid_y = new_y
        return True

    def draw(self, camera_offset: Tuple[int, int]):
        """Draw player centered on tile"""
        offset_x, offset_y = camera_offset
        center_x = self.grid_x * TILE_SIZE + TILE_SIZE // 2 + offset_x
        center_y = self.grid_y * TILE_SIZE + TILE_SIZE // 2 + offset_y
        rect = self.surface.get_rect(center=(center_x, center_y))
        self.screen.blit(self.surface, rect.topleft)


class RPGGame:
    """Main game controller for the RPG"""

    def __init__(self):
        pygame.init()  # [web:1][web:11]
        pygame.display.set_caption("Relics & Ruins - RPG Adventure")  # [web:5]
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        # Game objects
        self.tilemap = TileMap(GRID_WIDTH, GRID_HEIGHT, self.screen)
        self.player = Player(GRID_WIDTH // 2, GRID_HEIGHT // 2, self.screen)
        self.tilemap.update_loaded_chunks(self.player.grid_x, self.player.grid_y)

        # Game state
        self.frame_count = 0
        self.running = True

        # Fonts
        pygame.font.init()
        self.ui_font = pygame.font.SysFont("Arial", 18)  # [web:12][web:18]

    def handle_input(self):
        """Handle keyboard input"""
        for event in pygame.event.get():  # [web:11]
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_w:
                    self.player.move(0, -1, self.tilemap)
                elif event.key == pygame.K_s:
                    self.player.move(0, 1, self.tilemap)
                elif event.key == pygame.K_a:
                    self.player.move(-1, 0, self.tilemap)
                elif event.key == pygame.K_d:
                    self.player.move(1, 0, self.tilemap)

    def get_camera_offset(self) -> Tuple[int, int]:
        """Calculate camera offset to center on player"""
        # Desired center of the screen
        target_x = self.player.grid_x * TILE_SIZE + TILE_SIZE // 2
        target_y = self.player.grid_y * TILE_SIZE + TILE_SIZE // 2

        offset_x = WINDOW_WIDTH // 2 - target_x
        offset_y = WINDOW_HEIGHT // 2 - target_y
        return offset_x, offset_y

    def draw_ui(self):
        """Draw UI overlay: FPS, position, grid info, controls"""
        # FPS counter (simple estimate)
        fps = int(self.clock.get_fps()) if self.frame_count >= FPS else 0

        def draw_text(text: str, x: int, y: int, color=WHITE):
            surface = self.ui_font.render(text, True, color)  # [web:6][web:15]
            self.screen.blit(surface, (x, y))

        draw_text(f"FPS: {fps if fps > 0 else '...'}", 10, 10)
        draw_text(f"Pos: ({self.player.grid_x}, {self.player.grid_y})", 10, 30)
        draw_text(
            f"Grid: {self.tilemap.width}x{self.tilemap.height} | Tile: {TILE_SIZE}px",
            10,
            50,
        )
        draw_text("WASD: Move | ESC: Exit", 10, WINDOW_HEIGHT - 30, GRAY)

    def update(self):
        """Update game logic"""
        self.frame_count += 1
        self.tilemap.update_loaded_chunks(self.player.grid_x, self.player.grid_y)

    def render(self):
        """Render everything"""
        self.screen.fill(BLACK)
        camera_offset = self.get_camera_offset()
        self.tilemap.draw(camera_offset)
        self.player.draw(camera_offset)
        self.draw_ui()
        pygame.display.flip()

    def run(self):
        """Main game loop"""
        while self.running:
            self.clock.tick(FPS)
            self.handle_input()
            self.update()
            self.render()

        pygame.quit()
        sys.exit()


def run_game():
    """Entry point for the game (pygame version)"""
    game = RPGGame()
    game.run()
