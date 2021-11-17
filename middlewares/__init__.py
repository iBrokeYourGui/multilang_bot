from loader import dp
from config import I18N_DOMAIN, LOCALES_DIR
from .multilanguage import MultiLang


if __name__ == 'middlewares':
    i18n = dp.middleware.setup(MultiLang(I18N_DOMAIN, LOCALES_DIR))
    # _ = i18n.gettext
    _ = i18n.lazy_gettext # Без этого переопределения клавиатур не работает
