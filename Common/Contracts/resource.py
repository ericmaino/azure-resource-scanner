from abc import ABC, abstractmethod


class Resource(ABC):

    @property
    def id(self):
        raise NotImplementedError("id not implemented")

    @property
    def account_id(self):
        raise NotImplementedError("account_id is not implemented")

    @property
    def name(self):
        raise NotImplementedError("name not implemented")

    @property
    def type(self):
        raise NotImplementedError("type not implemented")

    @property
    def location(self):
        raise NotImplementedError("location not implemented")

    @property
    def tags(self):
        raise NotImplementedError("tags not implemented")

    @tags.setter
    def tags(self, new_tags):
        raise NotImplementedError("tags setter not implemented")

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError("to_dict not implemented")

    @abstractmethod
    def to_str(self):
        raise NotImplementedError("to_str not implemented")





