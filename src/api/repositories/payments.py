from core.repositories import BaseRepository
from django.db import models

from api.models import Payments


class PaymentsRepository(BaseRepository):
    _model_cls: type[models.Model] = Payments
