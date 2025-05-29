from django.shortcuts import get_object_or_404

from core.repositories import BaseRepository
from django.db import models

from api.models import Organizations


class OrganizationsRepository(BaseRepository):
    _model_cls: type[models.Model] = Organizations

    @classmethod
    def get_by_inn(cls, inn: str) -> models.Model:
        return get_object_or_404(cls._model_cls, **{'inn': inn})
