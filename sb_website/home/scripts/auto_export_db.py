from ..models import Partner

#planned to be a generic db backup script

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

