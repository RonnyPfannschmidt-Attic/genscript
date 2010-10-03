
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
    elif name:
        return name
    else:
        return mail


def distribution_metadata(dist):
    metadata = dist.metadata
    author = grab_person(metadata, 'author')
    version = metadata.version
    return {
        'author': author,
        'version': version,
        'url': grab_attr(metadata, 'url'),
    }

