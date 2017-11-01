def group_by_type(*args):
    groups = {}
    for arg in args:
        if type(arg) not in groups.keys():
            groups[type(arg)] = [arg]
        else:
            groups[type(arg)].append(arg)
    return groups

def create_entry_template(p):
    with open('html_templates/entry.html', 'r') as f:
        base = f.read()
    template = '<ul>\n'
    fields = vars(p).keys()
    for field in fields:
        if field not in ('title', 'img', 'video_url'):
            template += (
                '           <li> <strong>%s:</strong> {%s}</li>\n'
                % (field, field)
            )
    template += '       </ul>'
    template = base % template
    return template
