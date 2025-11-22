import pygame
import sys

# --- Inisialisasi Pygame ---
pygame.init()

# --- Konstanta ---
TABLE_WIDTH = 800
TABLE_HEIGHT = 400 # Rasio 2:1
WALL_THICKNESS = 20

# --- Warna ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TABLE_FELT_COLOR = (0, 100, 0)   # Hijau Laken
RAIL_COLOR = (101, 67, 33)       # Coklat Kayu
BACKGROUND_COLOR = (50, 50, 50)  # Abu-abu Gelap (Luar meja)

# ====================================================
# 1. CLASS WALL (Dinding)
# ====================================================
class Wall:
    """
    Merepresentasikan satu segmen dinding (batas) meja.
    """
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, window):
        # Menggambar dinding (Rail)
        pygame.draw.rect(window, RAIL_COLOR, self.rect)
        # Opsional: Tambahkan garis batas agar terlihat tegas
        pygame.draw.rect(window, BLACK, self.rect, 1)

    def get_bounds(self):
        """Mengembalikan area kotak dinding untuk deteksi tabrakan (nanti)."""
        return self.rect


# ====================================================
# 2. CLASS TABLE (Meja)
# ====================================================
class Table:
    """
    Merepresentasikan meja permainan.
    Bertanggung jawab menampung dinding dan area bermain.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Area bermain (kain laken) di tengah dinding
        self.felt_rect = pygame.Rect(
            WALL_THICKNESS, WALL_THICKNESS, 
            width - (2 * WALL_THICKNESS), 
            height - (2 * WALL_THICKNESS)
        )
        
        # Inisialisasi 4 Dinding (Komposisi: Table memiliki Wall)
        self.walls = [
            Wall(0, 0, width, WALL_THICKNESS), # Atas
            Wall(0, height - WALL_THICKNESS, width, WALL_THICKNESS), # Bawah
            Wall(0, 0, WALL_THICKNESS, height), # Kiri
            Wall(width - WALL_THICKNESS, 0, WALL_THICKNESS, height) # Kanan
        ]
        
        # Catatan: Hole (Lubang) belum ditambahkan sesuai permintaan
        # untuk fokus pada struktur dasar terlebih dahulu.

    def draw(self, window):
        """Menggambar visual meja."""
        # 1. Gambar Dinding
        for wall in self.walls:
            wall.draw(window)
        
        # 2. Gambar Area Laken (Hijau)
        pygame.draw.rect(window, TABLE_FELT_COLOR, self.felt_rect)


# ====================================================
# 3. CLASS GAMEMANAGER (Pengendali Utama)
# ====================================================
class GameManager:
    """
    Kelas sentral yang mengatur Game Loop dan inisialisasi.
    """
    def __init__(self):
        # Setup Window
        self.window = pygame.display.set_mode((TABLE_WIDTH, TABLE_HEIGHT))
        pygame.display.set_caption("Simulasi Billiard - Implementasi Awal")
        
        # Inisialisasi Objek
        self.table = Table(TABLE_WIDTH, TABLE_HEIGHT)
        
        # Variabel kontrol loop
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        """
        Loop Utama Permainan (Game Loop).
        Urutan: Input -> Update -> Render.
        """
        while self.running:
            # Hitung delta time (waktu antar frame)
            delta_time = self.clock.tick(60) / 1000.0 
            
            self.process_events()
            self.update(delta_time)
            self.render()
            
        self.close()

    def process_events(self):
        """Menangani input pengguna."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Nanti: Tambahkan input mouse/keyboard di sini

    def update(self, delta_time):
        """Memperbarui logika permainan."""
        # Saat ini belum ada objek bergerak (bola) yang perlu di-update.
        # Nanti: self.ball.update(delta_time)
        pass

    def render(self):
        """Menggambar semua objek ke layar."""
        # 1. Bersihkan layar dengan warna background
        self.window.fill(BACKGROUND_COLOR)
        
        # 2. Gambar Meja
        self.table.draw(self.window)
        
        # Nanti: Gambar bola dan stik di sini
        
        # 3. Tampilkan frame
        pygame.display.flip()

    def close(self):
        """Membersihkan resource saat keluar."""
        pygame.quit()
        sys.exit()

# --- Titik Masuk Program ---
if __name__ == "__main__":
    game = GameManager()
    game.run()