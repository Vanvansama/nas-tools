from functools import lru_cache

import requests
from app.utils.commons import singleton


@singleton
class MetaTubeApi(object):
    _session = requests.Session()

    _urls = {
        "actors": "/v1/actors",
        "movies": "/v1/movies",
        "search_actors": "/v1/actors/search",
        "search_movies": "/v1/movies/search",
        "primary": "/v1/images/primary",
        "thumb": "/v1/images/thumb",
        "backdrop": "/v1/images/backdrop",
        "translate": "/v1/translate",
    }

    def _call(self, action, path, params, method="GET"):
        host = "http://192.168.110.83:8085"
        url = host + action
        req = self._session.request(method, url, params, timeout=60, verify=False)
        json = req.json()
        return json

    def search(self, keyword):
        """
        搜索

        example: http://192.168.110.83:8085/v1/movies/search?q=IPX-811&provider=&fallback=True
        """
        params = {
            "q": keyword,
            "provider": '',
            "fallback": True
        }
        # return self._call(self._urls["search_movies"], params=params)
        return {
            "data": [
                {
                    "id": "1658375",
                    "number": "IPX-811",
                    "title": "媚薬で翌朝まで覚醒絶頂 キメセク相部屋NTR姦 楓カレン 「憎いほど大嫌いで別れたのに…」",
                    "provider": "ARZON",
                    "homepage": "https://www.arzon.jp/item_1658375.html",
                    "thumb_url": "https://img.arzon.jp/image/1/1658/1658375S.jpg",
                    "cover_url": "https://img.arzon.jp/image/1/1658/1658375L.jpg",
                    "score": 0,
                    "actors": [
                        "田中レモン"
                    ],
                    "release_date": "2022-02-08T00:00:00Z"
                },
                {
                    "id": "idp:IPX-811",
                    "number": "IPX-811",
                    "title": "-媚薬で翌朝まで覚醒絶頂- キメセク相部屋NTR姦 「憎いほど大嫌いで別れたのに…」 楓カレン",
                    "provider": "AVBASE",
                    "homepage": "https://www.avbase.net/works/IPX-811",
                    "thumb_url": "https://pics.dmm.co.jp/digital/video/ipx00811/ipx00811ps.jpg",
                    "cover_url": "https://pics.dmm.co.jp/digital/video/ipx00811/ipx00811pl.jpg",
                    "score": 0,
                    "actors": [
                        "楓カレン"
                    ],
                    "release_date": "2022-02-04T09:00:00+09:00"
                },
                {
                    "id": "IPX-811",
                    "number": "IPX-811",
                    "title": "-媚薬で翌朝まで覚醒絶頂- キメセク相部屋NTR姦 「憎いほど大嫌いで別れたのに…」 楓カレン",
                    "provider": "JavBus",
                    "homepage": "https://www.javbus.com/ja/IPX-811",
                    "thumb_url": "https://www.javbus.com/pics/thumb/8qy2.jpg",
                    "cover_url": "https://www.javbus.com/pics/cover/8qy2_b.jpg",
                    "score": 0,
                    "release_date": "2022-02-04T00:00:00Z"
                },
                {
                    "id": "ipx00811",
                    "number": "IPX-811",
                    "title": "-媚薬で翌朝まで覚醒絶頂- キメセク相部屋NTR姦 「憎いほど大嫌いで別れたのに…」 楓カレン",
                    "provider": "JAV321",
                    "homepage": "https://www.jav321.com/video/ipx00811",
                    "thumb_url": "http://pics.dmm.co.jp/digital/video/ipx00811/ipx00811ps.jpg",
                    "cover_url": "http://pics.dmm.co.jp//digital/video/ipx00811/ipx00811pl.jpg",
                    "score": 4.5,
                    "actors": [
                        "楓カレン"
                    ],
                    "release_date": "2022-02-08T00:00:00Z"
                },
                {
                    "id": "1675734",
                    "number": "4IPX-811",
                    "title": "媚薬で翌朝まで覚醒絶頂 キメセク相部屋NTR姦 楓カレン 「憎いほど大嫌いで別れたのに…」 レンタル版",
                    "provider": "ARZON",
                    "homepage": "https://www.arzon.jp/item_1675734.html",
                    "thumb_url": "https://img.arzon.jp/image/1/1675/1675734S.jpg",
                    "cover_url": "https://img.arzon.jp/image/1/1675/1675734L.jpg",
                    "score": 0,
                    "actors": [
                        "田中レモン"
                    ],
                    "release_date": "2022-05-24T00:00:00Z"
                },
                {
                    "id": "firststar-1622",
                    "number": "DORI-1601",
                    "title": "【配信限定】パコ撮り16時間 女子校生11名収録",
                    "provider": "DUGA",
                    "homepage": "https://duga.jp/ppv/firststar-1622/",
                    "thumb_url": "https://pic.duga.jp/unsecure/firststar/1622/noauth/jacket_240.jpg",
                    "cover_url": "https://pic.duga.jp/unsecure/firststar/1622/noauth/jacket.jpg",
                    "score": 4.5,
                    "release_date": "2022-03-12T00:00:00Z"
                },
                {
                    "id": "sekimen-0191",
                    "number": "SKMJ-192",
                    "title": "経験人数0人…澄んだ瞳、圧倒的な透明感…6人の処女美少女たちが魅せた無垢で儚い初めてのSEX…",
                    "provider": "DUGA",
                    "homepage": "https://duga.jp/ppv/sekimen-0191/",
                    "thumb_url": "https://pic.duga.jp/unsecure/sekimen/0191/noauth/jacket_240.jpg",
                    "cover_url": "https://pic.duga.jp/unsecure/sekimen/0191/noauth/jacket.jpg",
                    "score": 4,
                    "release_date": "2021-07-23T00:00:00Z"
                },
                {
                    "id": "fellatiohunter-0045",
                    "number": "ten1-4-8",
                    "title": "個撮）密着吸引！気持ち良すぎるディープスロート！【イクまで辞めない】チンポ丸のみピストンフェラ【口内発射",
                    "provider": "DUGA",
                    "homepage": "https://duga.jp/ppv/fellatiohunter-0045/",
                    "thumb_url": "https://pic.duga.jp/unsecure/fellatiohunter/0045/noauth/240x180.jpg",
                    "cover_url": "https://pic.duga.jp/unsecure/fellatiohunter/0045/noauth/240x180.jpg",
                    "score": 5,
                    "release_date": "2022-03-13T00:00:00Z"
                }
            ]
        }

    def movie_detail(self, metatubeid, provider):
        path = "/" + provider + "/" + metatubeid
        params = {
            "lazy": True
        }
        return self._call(self._urls["movies"], path, params)