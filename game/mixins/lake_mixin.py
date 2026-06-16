


from ..container import ObjectsContainer


class LakeMixin:
    def __init__(self, *__, **_) -> None:
        super().__init__(*__, **_)
        self.lake: ObjectsContainer = ObjectsContainer()
    
    # lake
    def add(self, object_creator):
        return self.lake.add_to_me(object_creator)
