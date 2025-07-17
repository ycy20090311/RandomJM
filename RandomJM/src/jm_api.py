import random
import jmcomic
import logging

# 必要常量
JM_OPTION_PATH = "api_option.yml"
JM_ALBUM_ID_FILE = "album_id.txt"
JM_API_LOG_FILE = "jm_api.log"
JM_DOMAIN = "jm18c-twie.club"

# 基本对象
album_id_list: list[str] = []
option = jmcomic.create_option_by_file(JM_OPTION_PATH)
client = option.new_jm_client(impl="html")

# 本地ID列表/日志 初始化 
with open(JM_ALBUM_ID_FILE, "r") as file:
    album_id_list = file.read().split()
random.shuffle(album_id_list)

logging.basicConfig(
    filename = JM_API_LOG_FILE,
    filemode = "a",
    format = "[%(asctime)s] [%(levelname)s]: %(message)s",
    datefmt = "%m-%d %H:%M:%S",
    level = logging.INFO,
    encoding="utf-8"
)
logger = logging.getLogger("jm_api_logger")

# 获取封面url
def get_image_url(album_id: int) -> str:
    return f"https://{ JM_DOMAIN }/media/albums/{ album_id }.jpg"

# 获取本子完整url
def get_album_url(album_id: int) -> dict:
    return {
        "cn": [
            f"https://jm18c-twie.club/album/{ album_id }",
            f"https://18comic-aspa.org/album/{ album_id }",
            f"https://jmcomic-ive.cc/album/{ album_id }"

        ],
        "sea": [
            f"https://jmcomic-zzz.one/album/{ album_id }",
            f"https://jmcomic-zzz.org/album/{ album_id }"
        ],
        "int": [
            f"https://18comic.vip/album/{ album_id }",
            f"https://18comic.ink/album/{ album_id }"
        ]
    }

# 获取随机本子实体对象
def random_album() -> jmcomic.JmAlbumDetail:
    aid = random.choice(album_id_list)
    return client.get_album_detail(aid)

# 主要函数
def call() -> dict:
    try:
        album = random_album()
        logger.info(f"call_status: true album_id: { album.album_id }")

        return {
            "status": True,
            "id": album.album_id,
            "name": album.name,
            "authors": album.authors,
            "url": get_album_url(album.album_id),
            "tags": album.tags,
            "likes": album.likes,
            "views": album.views,
            "cover": get_image_url(album.album_id)
        }
    
    except Exception as e:
        logger.warning(f"call_status: false msg: {str(e)}")

        return {
            "status": False,
            "id": "",
            "name": "",
            "authors": [],
            "url":{},
            "tags": [],
            "likes": "",
            "views": "",
            "cover": ""
        }
    
