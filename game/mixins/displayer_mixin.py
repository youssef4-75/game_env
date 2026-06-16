


from game.mixins.lake_mixin import LakeMixin


class DisplayerMixin:
    def __init__(self, *__, **_) -> None:
        super().__init__(*__, **_)
        self.displayers = []

    # displayer
    def _create_disp_for_players(self, bg_color, color, *rects, value_provider, maximum_provider=None):
        
        for i, obj in enumerate(self.to_lake_mixin()):
            if i>=len(rects) and i!=0: rect = rects[-1]
            elif len(rects) == 0: raise Exception("no rects provided, minimum one rectangle is required")
            else: 
                rect = rects[i]
            displayer = PlayerDisplayer(
                self, bg_color, color, rect, 
                observable_obj=obj, 
                max_provider=maximum_provider, 
                value_provider=value_provider
                    )
            self.displayers.append(displayer)

    # displayer
    def add_displayer(self, displayer: DisplayerABC):
        self.displayers.append(displayer)

    def to_lake_mixin(self):
        assert isinstance(self, LakeMixin)
        return self.lake