import sys, logging, open_color, arcade, os, random

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Discount Enterprise"

NUM_ENEMIES = 5
STARTING_LOCATION = (400,100)
BULLET_DAMAGE = 10
ENEMY_HP = 100
HIT_SCORE = 10
KILL_SCORE = 100
MOVEMENT_SPEED = 3

class Bullet(arcade.Sprite):
    def __init__(self, position, velocity, damage):
        ''' 
        initializes the bullet
        Parameters: position: (x,y) tuple
            velocity: (dx, dy) tuple
            damage: int (or float)
        '''
        super().__init__("assets/bullet.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):
        '''
        Moves the bullet
        '''
        self.center_x += self.dx
        self.center_y += self.dy


    
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/spaceship.png", 0.5)
        (self.center_x, self.center_y) = STARTING_LOCATION

class Enemy(arcade.Sprite):
    def __init__(self, position):
        super().__init__("assets/hjm-random_asteroids-v3/1.png", 0.5)
        self.hp = ENEMY_HP
        (self.center_x, self.center_y) = position

class Window(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.set_mouse_visible(False)
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player = Player()
        self.score = 0

        arcade.set_background_color(open_color.black)



    def setup(self):
        for i in range(NUM_ENEMIES):
            x = 120 * (i+1) + 40
            y = 500
            enemy = Enemy((x,y))
            self.enemy_list.append(enemy)     

    def update(self, delta_time):
        pass

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()




    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.player.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            x = self.player.center_x
            y = self.player.center_y + 15
            bullet = Bullet((x,y),(0,10),BULLET_DAMAGE)
            self.bullet_list.append(bullet)

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            pass

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()