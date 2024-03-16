import pygame as pg
import moderngl as mgl
import sys

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)) -> None:
        # init pygame modules
        pg.init()
        # set window size
        self.WIN_SIZE = win_size
        # opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # create an object to help track time
        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18)) # a szinek 0->255 ig normalizálva vannak 0->1 re
        # swap buffers
        pg.display.flip()
    
    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60) # framerate setting: 60 fps
    

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()