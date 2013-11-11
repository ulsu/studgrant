from django.db import models

class ApprovedAccountQuerySet(models.query.QuerySet):
    def approved(self):
        return self.filter(approved=1)

class AccountManager(models.Manager):
    use_for_related_fields = True

    def get_query_set(self):
        return ApprovedAccountQuerySet(self.model)

    def approved(self, *args, **kwargs):
        return self.get_query_set().approved(*args, **kwargs)