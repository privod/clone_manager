# -*- coding: UTF-8 -*-
import os
import os.path
import re

import logging

logging.basicConfig(format='%(levelname)s %(message)s', level=logging.DEBUG)

# TODO: Реализовать получение из конфига
work_path_root = u'N:\\Задачи'


def work_dir_create():
    hg_path = os.getcwd()
    logging.info(u'Текущий каталог (клон репозитория Mercurial) {0}'.format(hg_path))

    work_dir = re.search('dev-local-(\d+-\w+)', hg_path).group(1)
    if not work_dir:
        logging.error(u'Данную команду необходимо запускать из клона репозитория Mercurial')
        logging.error(u'Имя каталога клона должено соответствовать формату dev-local-<Номер задачи>-<Краткое кодовое описание задачи>')
        return

    logging.info(u'Хранилище рабочих каталогов задач: {0}'.format(work_path_root))
    if not os.path.exists(work_path_root):
        logging.error(u'Хранилище рабоих гаталогов задач не существует')
        return

    work_path = os.path.join(work_path_root, work_dir)
    if os.path.exists(work_path):
        logging.info(u'Рабоий гаталог задачи [{0}] уже создан'.format(work_path))
    else:
        os.mkdir(work_path)
        logging.info(u'Создан Рабоий гаталог задачи [{0}]'.format(work_path))
    keep_path = os.path.join(work_path, 'keep.txt')
    open(keep_path, 'a').close()
    logging.info(u'Создан файл заметок [{0}]'.format(keep_path))
