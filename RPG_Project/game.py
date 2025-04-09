'This is the main file of my RPG final project'
import characters
import races
import jobs
import sprites
import pygame as pg


pg.init()
display_info = pg.display.Info()
WINDOW_WIDTH, WINDOW_HEIGHT = display_info.current_w, display_info.current_h
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Button Practice')
clock = pg.time.Clock()
gaming = True
running = True
font = pg.font.Font()
page = 'mm'


def main_menu():
    print("main menu")
    global page, gaming
    all_sprites = pg.sprite.Group()
    buttons = pg.sprite.Group()
    menu = sprites.button('Start', font, buttons, all_sprites)
    end = sprites.button('Esc - Exit', font, buttons, all_sprites)
    end.rect.topleft = (50, 50)
    running = True
    next_page = None
    while running:
        dt = clock.tick(120) / 1000
        display_surface.fill('blue')
        buttons.draw(display_surface)
        keys = pg.key.get_pressed()
        pos = pg.mouse.get_pos()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
                gaming = False
        if keys[pg.K_ESCAPE] or end.pressed:
            running = False
            gaming = False
        if menu.pressed == True:
            running = False
            next_page = 'ow'
        pg.display.update()
        buttons.update(dt=dt)
        clock.tick(120)
    if next_page:
        for sprite in buttons:
            sprite.kill()
        page = next_page


def overworld():
    print('overworld')
    global page, gaming
    all_sprites = pg.sprite.Group()
    enemies = pg.sprite.Group()
    buttons = pg.sprite.Group()
    running = True
    next_page = None
    open = False  # Track if the menu is open
    esc_cd = (False, 0)
    esc = sprites.button('Esc - Menu', font, buttons, all_sprites)
    esc.rect.topleft = (50, 50)
    menu_button = None  # Store the menu button object

    player = sprites.Player_OW(all_sprites)
    jeff = sprites.Enemy('Jeff', 1, all_sprites, enemies)
    jeff.rect.topleft = (200, 200)
    while running:
        dt = clock.tick(120) / 1000
        display_surface.fill('lightgrey')
        keys = pg.key.get_pressed()
        pos = pg.mouse.get_pos()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
                gaming = False
        if keys[pg.K_ESCAPE] or esc.pressed:
            if esc_cd[0] and pg.time.get_ticks() >= esc_cd[1]:
                esc_cd = (True, 0)
            if not esc_cd[0]:
                open = not open
                esc_cd = (True, pg.time.get_ticks() + 400)
                if open:
                    menu_button = sprites.button(
                        'Main Menu\n(Saving WIP)', font, buttons, all_sprites)
                else:
                    buttons.empty()
                    menu_button = None

        if menu_button and menu_button.pressed:
            running = False
            next_page = 'mm'
        else:
            next_page = None

        if open:
            buttons.draw(display_surface)
            buttons.update(dt=dt)

        if player.rect.colliderect(enemies):
            print('Battle!')
            
        all_sprites.update(dt=dt)
        all_sprites.draw(display_surface)
        pg.display.update()
        clock.tick(120)

    buttons.empty()
    page = next_page


def bttl(allies: characters.Party, enemies: characters.Party):
    display_info = pg.display.Info()
    WINDOW_WIDTH, WINDOW_HEIGHT = display_info.current_w, display_info.current_h
    left = 300
    for member in allies.members:
        member.rect.bottomleft = (left, WINDOW_HEIGHT - 200)
        left += 200
    left = 400
    for member in enemies.members:
        member.rect.topleft = (left, 200)


while gaming:
    running = True
    if page:
        match page:
            case 'mm':
                main_menu()
            case 'ow':
                overworld()
            case None:
                break


# print(menu.pressed)

pg.quit()
