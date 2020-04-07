from __future__ import unicode_literals
from .responses import EC2ContainerServiceResponse

url_bases = ["https?://ecs.(.+).amazonaws.com"]

url_paths = {"{0}/$": EC2ContainerServiceResponse.dispatch}
