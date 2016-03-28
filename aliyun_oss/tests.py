"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import unittest
from unittest import TestCase

from aliyun_oss.backends.oss import OSSStorage, OSSStorageFile


class SimpleTest(TestCase):
    def setUp(self):
        DEFAULT_FILE_STORAGE = 'aliyun_oss.backends.oss.OSSStorage'
        OSS_ACCESS_URL = 'oss-cn-qingdao-internal.aliyuncs.com'
        OSS_ACCESS_KEY_ID = '4s6p9mKWQjaFJS73'
        OSS_SECRET_ACCESS_KEY = 'YbbtIYlo1duxtB10usVviBhpst0m3o'
        OSS_STORAGE_BUCKET_NAME = 'emotion-pic'
        from aliyun_oss.backends import oss
        oss.ACCESS_ADDRESS = OSS_ACCESS_URL
        oss.ACCESS_KEY_NAME = OSS_ACCESS_KEY_ID
        oss.SECRET_KEY_NAME = OSS_SECRET_ACCESS_KEY
        oss.HEADERS = {}
        oss.DEFAULT_ACL = 'public-read'
        oss.OSS_STORAGE_BUCKET_NAME = OSS_STORAGE_BUCKET_NAME
        oss.BUCKET_PREFIX = ''
        self.storage = OSSStorage(bucket=OSS_STORAGE_BUCKET_NAME,
                                  access_key=OSS_ACCESS_KEY_ID,
                                  secret_key=OSS_SECRET_ACCESS_KEY
                                  )

    def test(self):
        fname = '3rd/jquery-2.2.1.min.6cbb321051a2.js'
        rt = self.storage.exists(fname)
        print('exists', rt)
        fd = OSSStorageFile(name=fname, storage=self.storage, mode='r')
        # fd = open('/tmp/aaa.txt', 'w')
        # fd.write(content.decode())
        # fd.close()
        content = b''
        i = 1
        while True:
            data = fd.read(1280)
            print(i, data)
            i += 1
            if not data:
                break
            # yield data
            content += data
        # content = fd.read()
        # print(content)


if __name__ == '__main__':
    unittest.main()
