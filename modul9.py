import pygame
import math
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulasi Bendera Tanpa Angle")

MERAH = (255, 0, 0)
PUTIH = (255, 255, 255)
TIANG = (100, 100, 100)
LANGIT = (135, 206, 235)
TANAH = (80, 50, 20)
PENYANGGA = (120, 120, 120)
KUNING = (255, 255, 100)
HITAM = (30, 30, 30)

partikel_angin = []
clock = pygame.time.Clock()

def gambar_bendera(x_tiang, waktu_ms):
    tinggi = 120
    lebar = 180
    t = waktu_ms / 500.0  
    for y in range(0, tinggi, 2):
        prop_y = y / tinggi
        stiffness = (1 - prop_y * 0.2)
        gelombang = math.sin((y / 20.0) + t) * 20 * stiffness
        decay = (y / tinggi) ** 0.5
        x_offset = gelombang * decay
        x1 = x_tiang
        x2 = x_tiang + lebar + x_offset
        color = MERAH if y < tinggi // 2 else PUTIH
        pygame.draw.line(screen, color, (x1, 150 + y), (x2, 150 + y), 2)

def gambar_tiang(x_tiang):
    pygame.draw.rect(screen, TIANG, (x_tiang - 5, 150, 10, 300))
    pygame.draw.rect(screen, PENYANGGA, (x_tiang - 20, 450, 40, 10))
    pygame.draw.rect(screen, TANAH, (0, 460, WIDTH, HEIGHT - 460))

def gambar_matahari(waktu_ms):
    cx, cy = 700, 100
    pygame.draw.circle(screen, KUNING, (cx, cy), 40)
    for i in range(12):
        sudut = math.radians(i * 30 + waktu_ms * 0.05)
        x1 = cx + math.cos(sudut) * 50
        y1 = cy + math.sin(sudut) * 50
        x2 = cx + math.cos(sudut) * 65
        y2 = cy + math.sin(sudut) * 65
        pygame.draw.line(screen, KUNING, (x1, y1), (x2, y2), 2)

def gambar_orang():
    x = 100
    y = 400
    pygame.draw.circle(screen, HITAM, (x, y - 60), 15)
    pygame.draw.line(screen, HITAM, (x, y - 45), (x, y - 10), 6)
    pygame.draw.line(screen, HITAM, (x, y - 40), (x - 15, y - 20), 4)
    pygame.draw.line(screen, HITAM, (x, y - 40), (x + 10, y - 60), 4)
    pygame.draw.line(screen, HITAM, (x, y - 10), (x - 10, y + 20), 4)
    pygame.draw.line(screen, HITAM, (x, y - 10), (x + 10, y + 20), 4)

def update_angin():
    while len(partikel_angin) < 30:
        partikel_angin.append([random.randint(0, WIDTH), random.randint(150, 450)])
    for p in partikel_angin:
        p[0] += 1.5
        p[1] += math.sin(p[0] * 0.05) * 0.5
        if p[0] > WIDTH:
            p[0] = 0
            p[1] = random.randint(150, 450)
        pygame.draw.circle(screen, (255, 255, 255), (int(p[0]), int(p[1])), 2)

running = True
while running:
    screen.fill(LANGIT)
    waktu_ms = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gambar_matahari(waktu_ms)
    update_angin()
    gambar_tiang(200)
    gambar_bendera(200, waktu_ms)
    gambar_orang()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
