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
        '<article>\n'
        '   <h3>{title}</h3>\n'
        '   <img src="{img}"></img>\n'
        '   <iframe src="{video_url}"></iframe>\n'
        '   <p>\n'
        '       %s'
        '\n   </p>\n'
        '</article>\n'
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
        '<section>\n'
        '<h3>{category}</h3>\n'
        '   {content}'
        '\n</section>\n'
    )

    category = key.category
    content = ''
    entry_template = create_entry_template(videos[0])
    for video in videos:
        content += entry_template.format(**vars(video)) + '\n'

    section = base.format(category=category, content=content)
    return section


def create_page(*args):
    base = (
        '<html>\n'
        '<head>\n'
        '   <meta charset="utf-8">\n'
        '   <link rel="stylesheet" href="css/style.css">\n'
        '   <title>curated videos</title>\n'
        '</head>\n'
        '<body>\n'
        '{content}'
        '\n</body>\n'
        '</html>'
    )

    videos_by_type = group_by_type(*args)
    content = ''
    for key in videos_by_type:
        content += create_section(key, videos_by_type[key])

    return base.format(content=content)
