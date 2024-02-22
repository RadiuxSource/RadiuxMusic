from RadiuxMusic.core.bot import Anony
from RadiuxMusic.core.dir import dirr
from RadiuxMusic.core.git import git
from RadiuxMusic.core.userbot import Userbot
from RadiuxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
