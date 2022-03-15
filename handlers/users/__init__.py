# импорт всех хэндлеров (from users) для личой переписки с пользователем
from .start import dp
from .help import dp
from .hello import dp
from .zhopa import dp
from .menu import dp

# кнопки клавы в одном файле
from .buttons import dp

# временная клава
from .test import dp

# инлайн меню
from .imlain_menu import dp

# регистрация ползователя
from .register import dp

# если я разиещу этот импорт выше, то нижние команды не будут срабатывать!
from .error import dp


__all__ = ["dp"]
