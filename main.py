import gettext


def main():
    language_translations = gettext.translation("base", localedir="locales", languages=['ru'], fallback=True)
    language_translations.install()

    _ = language_translations.gettext
    print(_("Hello world"))
    print(_(''))


if __name__ == '__main__':
    main()
