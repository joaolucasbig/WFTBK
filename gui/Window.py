import pygame

class Window(object):
    background = None
    __loadedBackground = None
    __gameObjects = []
    screen = None
    name = None

    # Here will have all the stuff that needs to be updated/rendered/checked in every run of the gameLoop
    def windowScheduleFunction(self, gameLoop, event = None):
        self.setScreen(gameLoop)
        self.tick()
        self.render()

    def setScreen(self, gameLoop):
        if self.screen == None:
            self.screen = gameLoop.getScreen()

    def addGameObject(self, object):
        self.__gameObjects.append(object)

    def removeGameObject(self, object):
        self.__gameObjects.append(object)

    def tick(self):
        for object in self.__gameObjects:
            object.tick()

    #The render of all objects of the window. Including the background and the game objects
    def render(self):
        if self.__loadedBackground == None:
            self.__loadedBackground = pygame.image.load(self.background).convert_alpha()

        # It will blit the background of the screen first
        self.screen.blit(self.__loadedBackground, (0,0))

        for object in self.__gameObjects:
            sprite, pos = object.render()
            self.screen.blit(sprite, pos)

        # Draw the back buffer into the front buffer
        pygame.display.flip()

    def getMousePos(self):

        return pygame.mouse.get_pos()