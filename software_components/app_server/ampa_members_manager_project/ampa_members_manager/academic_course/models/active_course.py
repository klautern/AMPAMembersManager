from django.db import models
from django.db.models import SET_NULL

from ampa_members_manager.academic_course.models.academic_course import AcademicCourse


class ActiveCourse(models.Model):
    course = models.ForeignKey(to=AcademicCourse, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "ActiveCourse"

    def __str__(self) -> str:
        return "ActiveCourse"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(ActiveCourse, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls) -> AcademicCourse:
        established_course = cls.objects.get(pk=1)
        return established_course.course