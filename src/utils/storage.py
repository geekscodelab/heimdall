from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class ImageStorage(FileSystemStorage):
    """
    A custom storage class for handling image files.

    This class extends Django's FileSystemStorage to construct URLs
    for stored files by joining the base URL from settings with the file's relative URL.
    """

    def url(self, name: str) -> str:
        """
        Return the full URL for the given file name.

        Args:
            name (str): The name of the file.

        Returns:
            str: The full URL for the given file name.

        """
        return urljoin(settings.BASE_URL, super().url(name))
