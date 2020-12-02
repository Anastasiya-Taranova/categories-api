from django.db import models


class Category(models.Model):
    name = models.TextField(unique=True)
    parent = models.ForeignKey(
        "Category",
        related_name="children",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    @staticmethod
    def dump_data(category, parent=None):
        name = category.get("name")
        children = category.get("children")

        if parent:
            parent = Category.objects.create(name=name, parent=parent)
        else:
            parent, created = Category.objects.get_or_create(name=name)

        if children:
            for child in children:
                Category.dump_data(child, parent=parent)

    def get_last_id(self):
        if self.parent:
            return self.parent.get_last_id() + [self.parent.id]
        return []

    def get_children(self):
        return self.children.all()

    def get_parents(self):
        parents = self.get_last_id()
        return Category.objects.filter(id__in=parents)

    def get_siblings(self):
        if self.parent:
            return Category.objects.filter(parent_id=self.parent.id).exclude(id=self.id)
        return Category.objects.none()

    def __str__(self):
        return self.name
