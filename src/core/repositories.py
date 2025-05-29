from typing import Any

from django.db import models
from django.shortcuts import get_object_or_404


class BaseRepository:
    _model_cls: type[models.Model] = None

    @classmethod
    def get(cls, **kwargs: Any) -> models.Model:
        return get_object_or_404(cls._model_cls, **kwargs)

    @classmethod
    def get_by_filter(cls, **kwargs: Any) -> list[models.Model]:
        return list(cls._model_cls.objects.filter(**kwargs))

    @classmethod
    def get_with_lock(cls, model_id: int) -> models.Model:
        return cls._model_cls.objects.select_for_update().get(id=model_id)

    @classmethod
    def all(cls) -> list[models.Model]:
        return list(cls._model_cls.objects.all())

    @classmethod
    def get_or_create(cls, defaults: dict[str, Any] = None,
                      **kwargs: Any) -> tuple[models.Model, bool]:
        return cls._model_cls.objects.get_or_create(
            **kwargs, defaults=defaults
        )

    @classmethod
    def create(cls, **kwargs: Any) -> models.Model:
        return cls._model_cls.objects.create(**kwargs)

    @classmethod
    def update(cls, model_id: int, **kwargs: Any) -> models.Model:
        model = cls.get(id=model_id).delete()
        for attr, value in kwargs.items():
            setattr(model, attr, value)
        model.save()

        return model

    @classmethod
    def delete(cls, model_id: int) -> int:
        count, _ = cls.get(id=model_id).delete()
        return count
