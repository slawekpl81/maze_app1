# test.py
from raylib import *

InitWindow(800, 450, b"App")
SetTargetFPS(30)

# ========================================
GRID_WIDTH = 50
GRID_HEIGHT = 50
CELL_SIZE = 20
# ========================================

grid =[]
for _ in range(GRID_WIDTH * GRID_HEIGHT):
    grid.append(0)


# LOOP        LOOP        LOOP        LOOP        LOOP        LOOP        LOOP
while not WindowShouldClose():
    BeginDrawing()
    ClearBackground(RAYWHITE)
    DrawText(b"OK! :)", 190, 200, 40, LIGHTGRAY)
    DrawFPS(10, 10)
    EndDrawing()

CloseWindow()