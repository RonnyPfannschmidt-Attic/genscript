
def grab_attr(dist, attr):
    try:
        return getattr(dist, attr)
    except AttributeError:
        val = dist[attr]
        if val != 'UNKNOWN':
            return val

def grab_person(dist, attr):
    name = grab_attr(dist, attr)
    mail = grab_attr(dist, attr + '_email')

    if name and mail:
        return '%s <%s>' % (name, mail)
    return name or mail

def distribution_metadata(meta):
    return {
        'author': grab_person(meta, 'author'),
        'maintainer': grab_person(meta, 'maintainer'),
        'version': meta.version,
        'url': grab_attr(meta, 'url'),
    }

