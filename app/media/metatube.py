from threading import Lock

import log
from app.media.metatubeapi import MetaTubeApi
from app.media.meta import MetaInfo
from app.utils.commons import singleton
from app.utils.types import MediaType

lock = Lock()
prefer_webp = True

@singleton
class MetaTube:
    metatubeapi = None
    message = None
    _movie_num = 20
    _tv_num = 20

    def __init__(self):
        self.init_config()

    def init_config(self):
        self.metatubeapi = MetaTubeApi()

    def search_metatube_medias(self, keyword, mtype: MediaType = None, season=None, episode=None, page=1):
        """
        根据关键字搜索MetaTube
        """
        if not keyword:
            return []
        result = self.metatubeapi.search(keyword)
        if not result:
            return []
        ret_medias = []
        for item_obj in result.get("data"):
            item = item_obj
            meta_info = MetaInfo(title=item.get("title"))
            meta_info.title = item.get("title")
            meta_info.type = MediaType.MOVIE
            meta_info.year = item.get("release_date")[0:4]
            meta_info.tmdb_id = "MT:%s" % item.get("number")
            meta_info.metatube_id = item.get("number")
            meta_info.provider = item.get("provider")
            meta_info.overview = "%s - %s" % (item.get("number"), item.get("provider"))
            meta_info.poster_path = item.get("cover_url").split('?')[0]
            meta_info.vote_average = item.get("score")
            if meta_info not in ret_medias:
                ret_medias.append(meta_info)

        return ret_medias[(page - 1) * 20:page * 20]

    def get_metatube_detail(self, metatubeid, provider, mtype=None, wait=False):
        if not provider:
            log.error("【MetaTube】需要提供provider信息才能查询详情")

        log.info("【MetaTube】正在通过API查询MetaTube详情：%s" % metatubeid)

        res = self.metatubeapi.movie_detail(metatubeid, provider)

        if not res.get("data"):
            log.warn("【MetaTube】%s %s 未找到MetaTube详细信息" % metatubeid, provider)
            return None

        metatube_info = res.get("data")
        if not metatube_info:
            log.warn("【MetaTube】%s %s 未找到MetaTube详细信息" % metatubeid, provider)
            return None

        if not metatube_info.get("title"):
            return None

        log.info("【MetaTube】查询到数据：%s" % metatube_info.get("title"))
        return metatube_info
