from Print import printDebug
import os.path

class ImageSaver(object):
    def __init__(self, target_dir):
        self.target_dir_ = target_dir
        pass

    def fail_to_get(self, http_request, errstring):
        printDebug('fails to get http_request: %s, errstring: %s' % (str(http_request), errstring))

    def save(self, http_request, data):
        path = http_request.path
        file_name =  path[path.rindex('/') + 1:]
        with self._ensureOpen(file_name) as f:
            f.write(data)

    def _ensureOpen(self, file_name):
        return open(self.target_dir_ + file_name, 'wb')
