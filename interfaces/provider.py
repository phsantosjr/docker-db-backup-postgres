from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ProviderInterface(ABC):
    @property
    @abstractmethod
    def secret_access_key(self):
        ...


    @property
    @abstractmethod
    def access_key_id(self):
        ...

    @property
    @abstractmethod
    def bucket_name(self):
        ...

    @property
    @abstractmethod
    def region(self):
        ...

    @property
    @abstractmethod
    def endpoint_url(self):
        ...


    @abstractmethod
    def upload(self, file):
        ...