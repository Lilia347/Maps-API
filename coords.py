import pygame as pg

coords = [0, 0]
pg.init()
size = width, height = 400, 300
screen = pg.display.set_mode(size)
COLOR_INACTIVE = pg.Color('gray')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global coords
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, ('black'))

    def print_text(self):
        return self.text

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

def drawX(screen):
    font = pg.font.Font(None, 50)
    text = font.render("X =", True, (0, 0, 0))
    text_x = 40
    text_y = 100
    screen.blit(text, (text_x, text_y))

def drawY(screen):
    font = pg.font.Font(None, 50)
    text = font.render("Y =", True, (0, 0, 0))
    text_x = 40
    text_y = 150
    screen.blit(text, (text_x, text_y))

def main():
    clock = pg.time.Clock()
    x = InputBox(100, 100, 140, 32)
    y = InputBox(100, 150, 140, 32)
    input_boxes = [x, y]
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for i, box in enumerate(input_boxes):
            coords[i] = box.print_text()
            box.update()
        screen.fill((255, 255, 255))
        for box in input_boxes:
            box.draw(screen)
        drawX(screen)
        drawY(screen)
        pg.display.flip()
        clock.tick(30)
        with open('cordinats.txt', 'w') as cords:
            print(coords, file=cords)
