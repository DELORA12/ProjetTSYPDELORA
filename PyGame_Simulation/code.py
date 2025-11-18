# -*- coding: utf-8 -*-
import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drone Delivery - 2 zones - plane.jpg")

# Charge ton image exacte
background = pygame.image.load(r"C:\Users\moham\OneDrive\Bureau\AZIZ\plane.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Couleurs
DRONE_COLOR = (0, 200, 255)     # Bleu cyan drone
RED   = (255, 60, 60)
YELLOW = (255, 220, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Polices
f_text = pygame.font.SysFont("Arial", 22, bold=True)
f_info = pygame.font.SysFont("Arial", 20, bold=True)
f_bat  = pygame.font.SysFont(None, 14)

# 2 dépôts seulement (gauche et droite sur ta carte)
warehouses = [
    pygame.Rect(180, 380, 50, 50),   # Zone 0 - Gauche
    pygame.Rect(1020, 380, 50, 50),  # Zone 1 - Droite
]

# Zones de génération (adaptées à ton plane.jpg)
zones = [
    (100, 580, 100, 700),   # Zone gauche
    (620, 1100, 100, 700),  # Zone droite
]

class Drone:
    def __init__(self, x, y, home_id):
        self.start_x = self.x = x
        self.start_y = self.y = y
        self.home_id = home_id
        self.battery = random.randint(70, 100)
        self.target = None
        self.speed = 4.5   # plus rapide = drone
        self.state = "idle"

    def draw(self):
        # Drone stylisé
        pygame.draw.circle(screen, DRONE_COLOR, (int(self.x), int(self.y)), 14)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 14, 3)
        # Hélices
        pygame.draw.line(screen, WHITE, (self.x-20, self.y), (self.x-10, self.y), 3)
        pygame.draw.line(screen, WHITE, (self.x+20, self.y), (self.x+10, self.y), 3)
        pygame.draw.line(screen, WHITE, (self.x, self.y-20), (self.x, self.y-10), 3)
        pygame.draw.line(screen, WHITE, (self.x, self.y+20), (self.x, self.y+10), 3)
        # Batterie
        bat = f_bat.render(str(self.battery), True, YELLOW)
        screen.blit(bat, (self.x-8, self.y-35))

    def move_to(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        dist = math.hypot(dx, dy)
        if dist > 6:
            self.x += dx/dist * self.speed
            self.y += dy/dist * self.speed
            return False
        return True

# 6 drones (3 par zone)
drones = []
for i, wh in enumerate(warehouses):
    cx, cy = wh.centerx, wh.centery
    for dx, dy in [(-60,-60), (0,-80), (60,-60)]:
        drones.append(Drone(cx + dx, cy + dy, i))

missions = []
next_pair_time = pygame.time.get_ticks() + 2000

clock = pygame.time.Clock()
running = True

while running:
    now = pygame.time.get_ticks()

    # Toutes les 2 secondes : paire Rouge + Jaune dans la même zone
    if now >= next_pair_time:
        zone_id = random.choice([0, 1])
        x_min, x_max, y_min, y_max = zones[zone_id]

        red_pos = (random.randint(x_min, x_max), random.randint(y_min, y_max))
        yellow_pos = (random.randint(x_min, x_max), random.randint(y_min, y_max))

        free = [d for d in drones if d.home_id == zone_id and d.state == "idle"]
        if free:
            drone = min(free, key=lambda d: math.hypot(d.x - red_pos[0], d.y - red_pos[1]))
            drone.state = "to_depot"
            drone.target = warehouses[zone_id].center

            missions.append({
                "drone": drone,
                "zone": zone_id,
                "red_pos": red_pos,
                "yellow_pos": yellow_pos,
                "spawn_time": now,
                "comm_end": now + 1800,
                "step": "to_depot",
                "wait_until": 0,
                "red_visible": True,
                "yellow_visible": True
            })

        next_pair_time += 2000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    # Dépôts
    for wh in warehouses:
        pygame.draw.rect(screen, BLACK, wh, border_radius=12)
        pygame.draw.rect(screen, WHITE, wh, 4, border_radius=12)

    # Gestion missions
    for m in missions[:]:
        d = m["drone"]

        if now < m["comm_end"]:
            txt = f_text.render("Package en route!", True, DRONE_COLOR)
            screen.blit(txt, (d.x - txt.get_width()//2, d.y - 90))

        elif m["step"] == "to_depot":
            if d.move_to(*warehouses[m["zone"]].center):
                m["step"] = "to_red"
                d.target = m["red_pos"]

        elif m["step"] == "to_red":
            if d.move_to(*m["red_pos"]):
                m["step"] = "waiting_red"
                m["wait_until"] = now + 1200
                m["red_visible"] = False

        elif m["step"] == "waiting_red":
            if now >= m["wait_until"]:
                m["step"] = "to_yellow"
                d.target = m["yellow_pos"]

        elif m["step"] == "to_yellow":
            if d.move_to(*m["yellow_pos"]):
                m["step"] = "waiting_yellow"
                m["wait_until"] = now + 1200
                m["yellow_visible"] = False

        elif m["step"] == "waiting_yellow":
            if now >= m["wait_until"]:
                m["step"] = "returning_home"
                d.target = (d.start_x, d.start_y)

        elif m["step"] == "returning_home":
            if d.move_to(d.start_x, d.start_y):
                d.state = "idle"
                d.target = None
                missions.remove(m)

    # Affichage Rouge + Jaune
    for m in missions:
        if m["red_visible"]:
            pygame.draw.circle(screen, RED, m["red_pos"], 22)
            pygame.draw.circle(screen, WHITE, m["red_pos"], 22, 4)
            txt = f_text.render("I have a package", True, RED)
            screen.blit(txt, (m["red_pos"][0] - txt.get_width()//2, m["red_pos"][1] - 75))

        if m["yellow_visible"]:
            pygame.draw.circle(screen, YELLOW, m["yellow_pos"], 22)
            pygame.draw.circle(screen, WHITE, m["yellow_pos"], 22, 4)
            txt = f_text.render("Deliver here!", True, YELLOW)
            screen.blit(txt, (m["yellow_pos"][0] - txt.get_width()//2, m["yellow_pos"][1] - 75))

    # Drones
    for drone in drones:
        drone.draw()
        if drone.target and "waiting" not in m.get("step", ""):
            drone.move_to(*drone.target)

    # Info
    info = f_info.render(f"Drone Delivery • 2 zones • {len(missions)} active", True, WHITE)
    screen.blit(info, (15, 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()