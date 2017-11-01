def group_by_type(*args):
    groups = {}
    for arg in args:
        if type(arg) not in groups.keys():
            groups[type(arg)] = [arg]
        else:
            groups[type(arg)].append(arg)
    return groups


def create_entry_template(p):
    base = (
        '<article>'
        '   <h3>{title}</h3>'
        '   <img src="{img}"></img>'
        '   <iframe src="{video_url}"></iframe>'
        '   <p>'
        '       %s'
        '   </p>'
        '</article>'
    )

    inner = '\n<ul>\n'
    fields = vars(p).keys()
    for field in fields:
        if field not in ('title', 'img', 'video_url'):
            inner += (
                '<li> <strong>%s:</strong> {%s}</li>\n'
                % (field, field)
            )
    inner += '</ul>\n'
    template = base % inner
    return template


def create_section(key, videos):
    base = (
        '<section>'
        '   <h2>{category}</h2>'
        '   {content}'
        '</section>'
    )

    content = ''
    entry_template = create_entry_template(videos[0])
    for video in videos:
        content += entry_template.format(**vars(video)) + '\n'

    section = base.format(category, content)
    return section
