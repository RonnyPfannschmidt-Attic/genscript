def metadata_lines(metadata):
    return ['%s = %r\n'%item for item in metadata.items()]


def update_script(source, metadata):
    lines = source.splitlines(True)
    for index, line in enumerate(lines):
        line = line.lstrip()
        if line and line[0] == '#' and 'Genscript Metadata' in line:
            if not line[-1] == '\n':
                lines[index] = line + '\n'
            break
    else:
        raise ValueError('no metadata insert point found')
    lines[index+1:index] = metadata_lines(metadata)
    return ''.join(lines)

