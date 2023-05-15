from dataclasses import dataclass

from providers.aws import Aws
from providers.digitalocean import DigitalOcean
from constants import Providers

@dataclass(slots=True)
class ProviderFactory:
    @staticmethod
    def get_provider(provider: Providers):
        providers = {
            Providers.AWS: Aws,
            Providers.DIGITAL_OCEAN: DigitalOcean
        }
        return providers.get(provider)
