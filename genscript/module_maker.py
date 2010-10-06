import os
from genscript.utils import distribution_metadata

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


class SdistModuleMixin:

    user_options = [
        ('module', None, 'the module to enrich')
    ]


    def initialize_options(self):
        self.module = None

    def finalize_options(self):
        #XXX: read py_modules
        pass

    def run(self):
        basename =os.path.basename(self.module)
        base, ext = os.path.splitext(basename)
        new_name = '%s-%s%s'%(base, self.distribution.version, ext)
        self.distribution.dist_files.append(('sdist_module', '', new_name))
        sdist = self.distribution.get_command_obj('sdist')
        sdist.ensure_finalized()
        dist_dir = sdist.dist_dir

        infile = open(self.module)
        try:
            unprocessed_source = infile.read()
        finally:
            infile.close()
        outpath = os.path.join(dist_dir, new_name)

        metadata = distribution_metadata(self.distribution.metadata)
        processed_source = update_script(unprocessed_source, metadata)

        outfile = open(outpath, 'w')
        try:
            outfile.write(processed_source)
        finally:
            outfile.close()

