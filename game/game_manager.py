
import pygame as pg

from container.objects_container import ObjectsContainer
from screen import Window
from services import ServicesManager
from services.draw.player_drawer import PlayerDrawer
from services.force.repeller import Repeller
from services.translate.player_translater import PlayerTranslator
from utils.displayer import Displayer


class GameManager:
    def __init__(self, win: Window, 
            serviceManager: ServicesManager,
            lake: ObjectsContainer) -> None:
        self.window = win
        self.smana = serviceManager
        self.lake = lake
        
    @classmethod
    def init(cls, name: str, win_size: tuple[int, int]):
        return cls(
            Window(name, *win_size),
            ServicesManager(
                PlayerDrawer(),
                Repeller(),
                PlayerTranslator()
            ),
            ObjectsContainer()
        )

    def add(self, object_creator):
        return self.lake.add_to_me(object_creator)

    def add_displayers(self, bg_color, color, *rects, value_provider, maximum_provider=None):
        self.displayers: list[Displayer] = []
        for i, obj in enumerate(self.lake):
            if i>=len(rects) and i!=0: rect = rects[-1]
            elif len(rects) == 0: raise Exception("no rects provided, minimum one rectangle is required")
            else: 
                rect = rects[i]
            displayer = Displayer(
                        self.window, bg_color, color, rect, 
                        observable_obj=obj, 
                        max_provider=maximum_provider, 
                        value_provider=value_provider
                    )
            self.displayers.append(displayer)

    def loop(self):
        
        for p in self.lake:
            self.smana.translate(p)
            self.smana.draw(self.window, p)

        for displayer in self.displayers:
            displayer.display()
        self.lake.interaction()
        self.lake.garbage_collect()
        self.window.display()
        self.window.fill((0, 0, 0))

        # for obj in self.lake:
        #     print(obj)
        #     self.smana.translate(obj)
        #     self.smana.draw(self.window, obj)
        
        # self.lake.interaction()
        # self.lake.garbage_collect()
        # self.window.display
        # self.window.fill((0, 0, 0))

    @property
    def running(self):
        return self.window.running 
    
    def key_events(self):
        for event in self.window.events():
            if event.type == pg.KEYDOWN:
                yield event