import abc

class IMailSender(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send(self, mail: Mail) -> None:
        raise NotImplementedError()
