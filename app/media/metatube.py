import random
from threading import Lock
from time import sleep

import zhconv

import log
from app.media.metatube import MetaTubeApi
from app.media.meta import MetaInfo
from app.utils import ExceptionUtils, StringUtils
from app.utils import RequestUtils
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
        for item_obj in result.get("items"):
            if mtype and mtype.value != item_obj.get("type_name"):
                continue
            if item_obj.get("type_name") not in (MediaType.TV.value, MediaType.MOVIE.value):
                continue
            item = item_obj.get("target")
            meta_info = MetaInfo(title=item.get("title"))
            meta_info.title = item.get("title")
            if item_obj.get("type_name") == MediaType.MOVIE.value:
                meta_info.type = MediaType.MOVIE
            else:
                meta_info.type = MediaType.TV
            if season:
                if meta_info.type != MediaType.TV:
                    continue
                if season != 1 and meta_info.begin_season != season:
                    continue
            if episode and str(episode).isdigit():
                if meta_info.type != MediaType.TV:
                    continue
                meta_info.begin_episode = int(episode)
                meta_info.title = "%s 第%s集" % (meta_info.title, episode)
            meta_info.year = item.get("year")
            meta_info.tmdb_id = "DB:%s" % item.get("id")
            meta_info.douban_id = item.get("id")
            meta_info.overview = item.get("card_subtitle") or ""
            meta_info.poster_path = item.get("cover_url").split('?')[0]
            rating = item.get("rating", {}) or {}
            meta_info.vote_average = rating.get("value")
            if meta_info not in ret_medias:
                ret_medias.append(meta_info)

        return ret_medias[(page - 1) * 20:page * 20]
