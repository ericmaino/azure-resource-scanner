from abc import ABC, abstractmethod

class AccountService(ABC):

    @abstractmethod
    def get_accounts(self):
        raise NotImplementedError("get_accounts is not implemented")
