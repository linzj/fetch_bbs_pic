from Print import printDebug
import os.path

log_file = open('downloaded.log', 'a')

class ImageSaver(object):
    def __init__(self, target_dir, http_request):
        self.target_dir_ = target_dir
        self.http_request_ = http_request
        pass

    def fail_to_get(self, http_request, errstring):
        printDebug('fails to get http_request: %s, errstring: %s' % (str(http_request), errstring))

    def save(self, http_request, data):
        path = http_request.path
        file_name =  path[path.rindex('/') + 1:]
        if os.path.isfile(file_name):
            return
        with self._ensureOpen(file_name) as f:
            f.write(data)
        # write log here
        print >>log_file, "topic url:%s, file name:%s" % (str(self.http_request_), file_name)

    def _ensureOpen(self, file_name):
        return open(self.target_dir_ + file_name, 'wb')
