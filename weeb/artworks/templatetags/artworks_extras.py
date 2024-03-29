from django import template

register = template.Library()


@register.filter(name='pluralize_ru')
def pluralize_ru(value, variants):
    variants = variants.split(',')
    value = abs(int(value))

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif (
        value % 10 >= 2 and value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20)
    ):
        variant = 1
    else:
        variant = 2

    return variants[variant]


@register.filter(name='is_favored_by_user')
def is_favored_by_user(artwork, user):
    return artwork.is_favored_by_user(user)


@register.filter(name='in_collection')
def in_collection(artwork, collection):
    return artwork in [art.artwork for art in collection.artworks.all()]
