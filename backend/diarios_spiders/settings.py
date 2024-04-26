import pkg_resources
from decouple import config

BOT_NAME = "diarios_spiders"
SPIDER_MODULES = ["diarios_spiders.spiders"]
NEWSPIDER_MODULE = "diarios_spiders.spiders"
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    "diarios_spiders.pipelines.GazetteDateFilteringPipeline": 100,
    "diarios_spiders.pipelines.DefaultValuesPipeline": 200,
    "diarios_spiders.pipelines.QueridoDiarioFilesPipeline": 300,
    "spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 400,
    "diarios_spiders.pipelines.SQLDatabasePipeline": 500,
}
USER_AGENT = (
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
)

TEMPLATES_DIR = "templates"

DOWNLOAD_TIMEOUT = 360

FILES_STORE = config("FILES_STORE", default="data")
MEDIA_ALLOW_REDIRECTS = True

EXTENSIONS = {
    "spidermon.contrib.scrapy.extensions.Spidermon": 500,
    "diarios_spiders.extensions.StatsPersist": 600,
}
SPIDERMON_ENABLED = config("SPIDERMON_ENABLED", default=True, cast=bool)
SPIDERMON_VALIDATION_SCHEMAS = [
    pkg_resources.resource_filename("diarios_spiders", "resources/gazette_schema.json")
]

SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True
SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = True
SPIDERMON_SPIDER_CLOSE_MONITORS = ("diarios_spiders.monitors.SpiderCloseMonitorSuite",)
SPIDERMON_MAX_ERRORS = 0
SPIDERMON_MAX_ITEM_VALIDATION_ERRORS = 0

SPIDERMON_DISCORD_FAKE = config("SPIDERMON_DISCORD_FAKE", default=True, cast=bool)
SPIDERMON_DISCORD_WEBHOOK_URL = config(
    "SPIDERMON_DISCORD_WEBHOOK_URL", default="<DISCORD_WEBHOOK_URL>"
)

QUERIDODIARIO_DATABASE_URL = config(
    "QUERIDODIARIO_DATABASE_URL", default="sqlite:///querido-diario.db"
)
QUERIDODIARIO_MAX_REQUESTS_ITEMS_RATIO = 5
QUERIDODIARIO_MAX_DAYS_WITHOUT_GAZETTES = 7

# These settings are needed only when storing downloaded files
# in a S3 bucket
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", default="")
AWS_ENDPOINT_URL = config("AWS_ENDPOINT_URL", default="")
AWS_REGION_NAME = config("AWS_REGION_NAME", default="")
FILES_STORE_S3_ACL = config("FILES_STORE_S3_ACL", default="public-read")

DOWNLOADER_MIDDLEWARES = {"scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware": 610}
ZYTE_SMARTPROXY_APIKEY = "<SMARTPROXY_APIKEY>"

COMMANDS_MODULE = "diarios_spiders.commands"
