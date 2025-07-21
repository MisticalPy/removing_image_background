logging_config = {
    'version': 1,
    'disable_existing_loggers': False,  # Убедитесь, что это значение False
    'formatters': {
        'default': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'combining_frames_into_gif': {
            'level': 'INFO',
            'handlers': ['default'],  # Обработчик должен быть указан
            'propagate': False,  # Чтобы избежать дублирования логов
        },
        'remove_background': {
            'level': 'INFO',
            'handlers': ['default'],
            'propagate': False,
        },
        'split_gif_cadrs': {
            'level': 'INFO',
            'handlers': ['default'],
            'propagate': False,
        },
        'main': {
            'level': 'INFO',
            'handlers': ['default'],
            'propagate': False,
        }
    },
    'root': {
        'handlers': ['default'],  # Чтобы корневой логгер также использовал стандартный обработчик
        'level': 'INFO',  # Убедитесь, что уровень логирования установлен
    }
}