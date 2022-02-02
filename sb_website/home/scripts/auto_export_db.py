# TODO: auto backup of generic model prepared for import with import-export lib
#   also export of media files

from ..models import Partner

# TODO: pass in Model from command line as arg
def run():

    instance = Partner()
    # retrieves tuple of all fields
    fields = instance._meta.get_all_field_names()
    print(fields)
    field_list = []
    for n in fields:
        value = list(n.values())
        field_list.append(value)
    print(field_list)

