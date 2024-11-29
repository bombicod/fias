import datetime
import os
import shutil
import zipfile


class BadSource(Exception):
    pass


class SourceWrapper(object):
    source = None

    def __init__(self, source, **kwargs):
        self.source = source

    def get_date_info(self, filename):
        raise NotImplementedError()

    def get_file_list(self):
        raise NotImplementedError()

    def open(self, filename):
        raise NotImplementedError()


class DirectoryWrapper(SourceWrapper):
    is_temporary = False

    def __init__(self, source, is_temporary=False, **kwargs):
        super(DirectoryWrapper, self).__init__(source=source, **kwargs)
        self.is_temporary = is_temporary
        self.source = os.path.abspath(source)

    def get_date_info(self, filename):
        st = os.stat(os.path.join(self.source, filename))
        return datetime.datetime.fromtimestamp(st.st_mtime)

    def _list_files(self, source: str, recursive=True):
        files = [f for f in os.listdir(source) if not f.startswith('.')]
        files.sort()

        for filename in files:
            file_path = os.path.join(source, filename)

            if os.path.isfile(file_path):
                yield file_path
            elif os.path.isdir(file_path) and recursive:
                for sub_file_path in self._list_files(file_path, recursive):
                    yield sub_file_path

    def get_file_list(self, recursive=True):
        return list(self._list_files(self.source))

    def get_full_path(self, filename):
        return filename

    def open(self, filename):
        return open(self.get_full_path(filename), 'rb')

    def __del__(self):
        if self.is_temporary:
            shutil.rmtree(self.source, ignore_errors=True)


class RarArchiveWrapper(SourceWrapper):

    def __init__(self, source, **kwargs):
        super(RarArchiveWrapper, self).__init__(source=source, **kwargs)
        self.source = source

    def get_date_info(self, filename):
        info = self.source.getinfo(filename)
        return datetime.date(*info.date_time[0:3])

    def get_file_list(self):
        return self.source.namelist()

    def open(self, filename):
        return self.source.open(filename)


class ZipArchiveWrapper(SourceWrapper):
    _arc: zipfile.ZipFile

    def __init__(self, source: str, is_temporary=False, **kwargs):
        super().__init__(source=source, is_temporary=is_temporary, **kwargs)

        try:
            self._arc = zipfile.ZipFile(self.source)
        except zipfile.BadZipfile as e:
            raise BadSource(f'Can`t open archive `{self.source}`!')
        else:
            if not self._arc.filelist:
                raise BadSource(f'Archive `{self.source}` is empty!')

    def get_date_info(self, filename):
        info: zipfile.ZipInfo = self._arc.getinfo(filename)
        return datetime.datetime(*info.date_time)

    def get_file_list(self):
        info: zipfile.ZipInfo

        file_list = [info.filename for info in self._arc.filelist]
        file_list.sort()

        return file_list

    def open(self, filename):
        return self._arc.open(filename, 'r')


class SevenZipArchiveWrapper(SourceWrapper):
    pass
