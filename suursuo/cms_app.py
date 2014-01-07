from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

# DEPRECATED
class StablesApphook(CMSApp):
    name = _("DEPRECATED stables apphook")
    urls = []

apphook_pool.register(StablesApphook)

class CourseApphook(CMSApp):
    name = _("DEPRECATED Courses Apphook")
    urls = []

apphook_pool.register(CourseApphook)

#class HorseApphook(CMSApp):
    #name = _("DEPRECATED Horse Apphook")
    #urls = []

#apphook_pool.register(HorseApphook)

class UserApphook(CMSApp):
    name = _("DEPRECATED User Apphook")
    urls = []

apphook_pool.register(UserApphook)

class ScheduleApphook(CMSApp):
    name = _("DEPRECATED Schedule apphook")
    urls = []

apphook_pool.register(ScheduleApphook)

class BlogApphook(CMSApp):
    name = _("DEPRECATED Blog apphook")
    urls = []

apphook_pool.register(BlogApphook)
