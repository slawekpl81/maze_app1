from pyray import *
from save_map import save_next_map


init_window(800, 600, "APP")
set_target_fps(30)

# ========================================
GRID_WIDTH = 50
GRID_HEIGHT = 50
CELL_SIZE = 10
# ========================================


grid =[]
for i in range(GRID_WIDTH * GRID_HEIGHT):
    grid.append([Rectangle(i % GRID_WIDTH * CELL_SIZE, i // GRID_WIDTH * CELL_SIZE, CELL_SIZE, CELL_SIZE),1])


# LOOP        LOOP        LOOP        LOOP        LOOP        LOOP        LOOP
while not window_should_close():

    if is_key_pressed(KEY_S):
        save_next_map([cell[1] for cell in grid])
        print("Zapisano mapę")

    mouse_pos = get_mouse_position()
    for i in range(len(grid)):
        if check_collision_point_rec(mouse_pos, grid[i][0]):
            if is_key_down(KEY_ZERO):
                grid[i][1] = 0
            elif is_key_down(KEY_ONE):
                grid[i][1] = 1



    begin_drawing()
    clear_background(RAYWHITE)
    for i in range(len(grid)):
        if grid[i][1] == 1:
            # draw_rectangle(grid[i][0].x, grid[i][0].y, grid[i][0].width, grid[i][0].height, GREEN)
            draw_rectangle_rec(grid[i][0], GREEN)
        else:
            # draw_rectangle(grid[i][0].x, grid[i][0].y, grid[i][0].width, grid[i][0].height, GRAY)
            draw_rectangle_rec(grid[i][0], GRAY)
    end_drawing()
close_window()