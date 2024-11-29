from .tablelist import TableList, TableListLoadingError
from .wrapper import DirectoryWrapper

__all__ = ['DirectoryTableList']


class EmptyDirError(TableListLoadingError):
    pass


class DirectoryTableList(TableList):
    wrapper_class = DirectoryWrapper

    def load_data(self, source):
        return self.wrapper_class(source=source, is_temporary=False)
